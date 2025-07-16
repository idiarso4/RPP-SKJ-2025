import socket
import json
import threading
from datetime import datetime
from .database import Database
from .camera import Camera
from .config import SERVER_CONFIG

class ParkingServer:
    def __init__(self):
        self.host = SERVER_CONFIG['host']
        self.port = SERVER_CONFIG['port']
        self.db = Database()
        self.camera = Camera()
        self.running = True
        
    def start(self):
        """Mulai server parkir"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(5)
            print(f"Server parkir berjalan di {self.host}:{self.port}")
            
            try:
                while self.running:
                    conn, addr = s.accept()
                    print(f"Koneksi dari {addr}")
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(conn, addr)
                    )
                    client_thread.start()
            except KeyboardInterrupt:
                print("\nMenghentikan server...")
            finally:
                self.cleanup()
    
    def handle_client(self, conn, addr):
        """Menangani koneksi client"""
        try:
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                    
                try:
                    request = json.loads(data)
                    response = self.process_request(request)
                    conn.sendall(json.dumps(response).encode('utf-8'))
                except json.JSONDecodeError:
                    conn.sendall(json.dumps({
                        'status': 'error',
                        'message': 'Format request tidak valid'
                    }).encode('utf-8'))
                    
        except ConnectionResetError:
            print(f"Koneksi dengan {addr} terputus")
        finally:
            conn.close()
    
    def process_request(self, request):
        """Proses request dari client"""
        command = request.get('command')
        
        if command == 'CHECK_IN':
            return self.handle_check_in()
        elif command == 'CHECK_OUT':
            return self.handle_check_out()
        else:
            return {
                'status': 'error',
                'message': 'Perintah tidak dikenali'
            }
    
    def handle_check_in(self):
        """Proses kendaraan masuk"""
        try:
            # Ambil gambar plat nomor
            result = self.camera.capture_plate()
            if not result['success']:
                return {'status': 'error', 'message': 'Gagal mengambil gambar'}
            
            # Simpan ke database
            transaksi_id = self.db.save_vehicle_entry(result['plate_number'])
            
            # Kirim perintah ke Arduino untuk membuka gate
            self.send_to_arduino('OPEN_GATE')
            
            return {
                'status': 'success',
                'message': 'Kendaraan berhasil masuk',
                'data': {
                    'plat_nomor': result['plate_number'],
                    'waktu_masuk': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'transaksi_id': transaksi_id
                }
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Terjadi kesalahan: {str(e)}'
            }
    
    def handle_check_out(self):
        """Proses kendaraan keluar"""
        try:
            # Ambil gambar plat nomor
            result = self.camera.capture_plate()
            if not result['success']:
                return {'status': 'error', 'message': 'Gagal mengambil gambar'}
            
            # Update database
            transaksi = self.db.save_vehicle_exit(result['plate_number'])
            
            if not transaksi:
                return {'status': 'error', 'message': 'Data kendaraan tidak ditemukan'}
            
            # Kirim perintah ke Arduino untuk membuka gate
            self.send_to_arduino('OPEN_GATE')
            
            return {
                'status': 'success',
                'message': 'Kendaraan berhasil keluar',
                'data': {
                    'plat_nomor': transaksi[1],
                    'waktu_masuk': transaksi[2].strftime('%Y-%m-%d %H:%M:%S'),
                    'waktu_keluar': transaksi[3].strftime('%Y-%m-%d %H:%M:%S'),
                    'durasi': transaksi[4],
                    'biaya': float(transaksi[5]) if transaksi[5] else 0
                }
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Terjadi kesalahan: {str(e)}'
            }
    
    def send_to_arduino(self, command):
        """Mengirim perintah ke Arduino"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_CONFIG['arduino_ip'], SERVER_CONFIG['arduino_port']))
                s.sendall(command.encode('utf-8'))
        except Exception as e:
            print(f"Gagal mengirim ke Arduino: {e}")
    
    def cleanup(self):
        """Bersihkan resource"""
        self.db.close()
        self.camera.release()
        print("Server berhenti")

if __name__ == "__main__":
    server = ParkingServer()
    server.start()

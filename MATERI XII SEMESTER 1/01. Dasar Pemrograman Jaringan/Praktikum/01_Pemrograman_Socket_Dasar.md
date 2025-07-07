# 🖥️ Panduan Praktikum: Pemrograman Socket Dasar

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Membuat koneksi socket dasar
2. Mengimplementasikan client-server sederhana
3. Menangani beberapa koneksi secara bersamaan
4. Menganalisis lalu lintas jaringan

## 🛠️ Alat dan Bahan
- Python 3.8+
- Text editor (VS Code, PyCharm, dll.)
- Terminal/Command Prompt
- Wireshark (untuk analisis jaringan)
- Dua perangkat (bisa menggunakan virtual machine)

## 📋 Langkah 1: Persiapan Lingkungan

### 1.1 Instalasi Python
Pastikan Python sudah terinstal di komputer Anda:
```bash
python --version
python3 --version
```

### 1.2 Buat Direktori Proyek
```bash
mkdir -p praktikum_jaringan/{client,server}
cd praktikum_jaringan
```

## 🔌 Langkah 2: Membuat TCP Server Sederhana

### 2.1 Buat File `server/simple_server.py`
```python
import socket
import sys

def start_server(host='0.0.0.0', port=12345):
    # Buat socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind socket ke port
        server_address = (host, port)
        print(f"Memulai server di {host} port {port}")
        server_socket.bind(server_address)
        
        # Listen for incoming connections
        server_socket.listen(1)
        
        while True:
            # Tunggu koneksi
            print("Menunggu koneksi...")
            connection, client_address = server_socket.accept()
            
            try:
                print(f"Koneksi dari {client_address}")
                
                # Terima data
                while True:
                    data = connection.recv(1024)
                    print(f"Diterima: {data.decode()}")
                    
                    if data:
                        # Kirim balik data ke client
                        print("Mengirim balik ke client")
                        connection.sendall(data)
                    else:
                        print(f"Tidak ada data dari {client_address}")
                        break
                        
            finally:
                # Bersihkan koneksi
                connection.close()

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
    start_server(host, port)
```

### 2.2 Jalankan Server
```bash
python server/simple_server.py
```

## 💻 Langkah 3: Membuat TCP Client Sederhana

### 3.1 Buat File `client/simple_client.py`
```python
import socket
import sys

def start_client(host='localhost', port=12345):
    # Buat socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Hubungkan socket ke port yang dituju
        server_address = (host, port)
        print(f"Menghubungkan ke {host} port {port}")
        sock.connect(server_address)
        
        try:
            # Kirim data
            message = 'Ini pesan dari client'
            print(f'Mengirim: {message}')
            sock.sendall(message.encode())

            # Cari respon
            amount_received = 0
            amount_expected = len(message)
            
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print(f'Diterima: {data.decode()}')
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Menutup koneksi")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
    start_client(host, port)
```

### 3.2 Jalankan Client
Buka terminal baru dan jalankan:
```bash
python client/simple_client.py
```

## 🔄 Langkah 4: Multi-Threaded Server

### 4.1 Buat File `server/threaded_server.py`
```python
import socket
import threading
import time

class ThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        print(f"Server berjalan di {self.host}:{self.port}")
        
        try:
            while True:
                client, address = self.sock.accept()
                print(f"Koneksi dari {address} telah diterima.")
                
                # Mulai thread baru untuk setiap client
                client.settimeout(60)
                threading.Thread(
                    target=self.listen_to_client,
                    args=(client, address)
                ).start()
                
        except KeyboardInterrupt:
            print("\nMenghentikan server...")
        finally:
            self.sock.close()
    
    def listen_to_client(self, client, address):
        size = 1024
        
        try:
            while True:
                data = client.recv(size).decode()
                if data:
                    # Tanggapi pesan
                    response = f"Anda mengirim: {data}"
                    client.send(response.encode())
                    print(f"Dari {address}: {data}")
                else:
                    raise error('Client terputus')
                    
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            return False

if __name__ == "__main__":
    import sys
    
    host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
    
    ThreadedServer(host, port).listen()
```

### 4.2 Uji Multi-Client
1. Jalankan server:
   ```bash
   python server/threaded_server.py
   ```

2. Buka beberapa terminal dan jalankan beberapa client:
   ```bash
   # Terminal 1
   python client/simple_client.py
   
   # Terminal 2
   python client/simple_client.py
   ```

## 📊 Langkah 5: Analisis dengan Wireshark

### 5.1 Instalasi Wireshark
- Unduh dan instal Wireshark dari [https://www.wireshark.org/](https://www.wireshark.org/)

### 5.2 Capture Paket
1. Buka Wireshark
2. Pilih interface jaringan yang aktif
3. Klik tombol biru (start capture)
4. Jalankan server dan client
5. Hentikan capture setelah selesai

### 5.3 Analisis Paket
- Filter `tcp.port == 12345` untuk melihat lalu lintas aplikasi kita
- Analisis proses TCP 3-way handshake
- Perhatikan pertukaran data antara client dan server

## 📝 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum

2. **Tujuan Praktikum**
   - Tuliskan tujuan dari praktikum ini

3. **Alat dan Bahan**
   - Spesifikasi perangkat
   - Software yang digunakan
   - Library Python yang diperlukan

4. **Langkah Kerja**
   - Dokumentasikan setiap langkah praktikum
   - Sertakan screenshot hasil eksekusi
   - Tuliskan perintah yang digunakan

5. **Hasil dan Pembahasan**
   - Tampilkan hasil capture Wireshark
   - Analisis proses komunikasi client-server
   - Jawab pertanyaan:
     - Bagaimana cara kerja TCP 3-way handshake?
     - Apa perbedaan antara TCP dan UDP?
     - Mengapa perlu menggunakan multi-threading pada server?

6. **Kesimpulan**
   - Ringkasan hasil praktikum
   - Kendala yang dihadapi
   - Saran perbaikan

## 🧩 Tantangan Lanjutan
1. Modifikasi kode untuk mendukung transfer file
2. Tambahkan enkripsi menggunakan TLS/SSL
3. Buat aplikasi chat sederhana dengan antarmuka GUI
4. Implementasikan protokol FTP sederhana

## ⚠️ Troubleshooting

### Masalah: Port Sudah Digunakan
**Solusi:**
```bash
# Di Linux/Mac
sudo lsof -i :<port>
kill -9 <PID>

# Di Windows
netstat -ano | findstr :<port>
taskkill /PID <PID> /F
```

### Masalah: Koneksi Ditolak
**Solusi:**
1. Pastikan server sudah berjalan
2. Periksa alamat IP dan port
3. Nonaktifkan firewall sementara
4. Pastikan tidak ada blokir dari antivirus

## 📚 Referensi
1. [Python Socket Programming](https://realpython.com/python-sockets/)
2. [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/)
3. [Python Threading Documentation](https://docs.python.org/3/library/threading.html)

---
<div align="center">
  <p>Panduan Praktikum Pemrograman Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

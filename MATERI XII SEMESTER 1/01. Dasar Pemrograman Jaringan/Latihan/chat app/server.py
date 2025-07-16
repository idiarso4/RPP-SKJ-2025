import socket
import threading

clients = {}
lock = threading.Lock()

def broadcast(message, sender_sock=None):
    if not message:
        return
        
    message = message.strip()
    if not message:
        return
        
    with lock:
        disconnected = []
        for client_sock in list(clients.keys()):
            try:
                if client_sock != sender_sock:
                    client_sock.sendall(f"{message}\n".encode())
            except (ConnectionError, OSError):
                disconnected.append(client_sock)
        
        # Clean up disconnected clients
        for sock in disconnected:
            if sock in clients:
                print(f"[INFO] Membersihkan koneksi dari {clients[sock]}")
                sock.close()
                del clients[sock]

def is_http_request(data):
    try:
        # Check if the data looks like an HTTP request
        first_line = data.decode().split('\r\n')[0]
        return first_line.startswith(('GET ', 'POST ', 'PUT ', 'DELETE ', 'HEAD ', 'OPTIONS '))
    except:
        return False

def handle_client(client_sock, addr):
    name = "Unknown"
    client_ip = addr[0]
    
    try:
        # Set timeout for the initial handshake
        client_sock.settimeout(10.0)
        
        # Send welcome message and get name
        client_sock.sendall("Masukkan nama Anda: ".encode())
        name_data = client_sock.recv(1024)
        if not name_data:
            print(f"[INFO] Koneksi ditutup oleh {addr} sebelum mengirim nama")
            return
            
        name = name_data.decode().strip()
        if not name:
            name = f"Anon-{client_ip}"
            
        print(f"[INFO] {name} ({client_ip}) terhubung")
        
        # Add to clients list
        with lock:
            clients[client_sock] = name
            
        # Broadcast join message
        broadcast(f"[INFO] {name} bergabung ke chat.", client_sock)
        
        # Reset timeout to None (blocking)
        client_sock.settimeout(None)
        
        # Main message loop
        while True:
            try:
                data = client_sock.recv(1024)
                if not data:
                    print(f"[INFO] {name} memutuskan koneksi")
                    break
                    
                msg = data.decode().strip()
                if msg:  # Only broadcast non-empty messages
                    print(f"[CHAT] {name}: {msg}")
                    broadcast(f"{name}: {msg}", client_sock)
                    
            except socket.timeout:
                print(f"[WARN] Timeout dari {name}")
                break
            except ConnectionResetError:
                print(f"[INFO] {name} terputus tiba-tiba")
                break
                
    except Exception as e:
        print(f"[ERROR] Error dengan {name}: {e}")
        
    finally:
        # Clean up
        with lock:
            if client_sock in clients:
                del clients[client_sock]
                
        try:
            broadcast(f"[INFO] {name} keluar dari chat.")
            client_sock.close()
        except:
            pass

def main():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 9009
    
    print(f"Memulai server chat...")
    print(f"Tekan Ctrl+C untuk menghentikan server\n")
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_sock.bind((host, port))
        server_sock.listen(5)
        print(f"[SERVER] Berjalan di {host}:{port}")
        print("Menunggu koneksi...")
        
        while True:
            try:
                client_sock, addr = server_sock.accept()
                client_sock.settimeout(5)  # Initial handshake timeout
                print(f"\n[INFO] Koneksi baru dari {addr[0]}")
                
                # Start new thread for the client
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(client_sock, addr),
                    daemon=True
                )
                client_thread.start()
                
                # Print active connections
                with lock:
                    print(f"[INFO] Klien terhubung: {len(clients)}")
                    
            except KeyboardInterrupt:
                print("\nMenghentikan server...")
                break
            except Exception as e:
                print(f"[ERROR] Error menerima koneksi: {e}")
                
    except Exception as e:
        print(f"[ERROR] Server error: {e}")
        
    finally:
        print("\nMenutup semua koneksi...")
        with lock:
            for sock in list(clients.keys()):
                try:
                    sock.close()
                except:
                    pass
        server_sock.close()
        print("Server berhenti.")

if __name__ == "__main__":
    main()
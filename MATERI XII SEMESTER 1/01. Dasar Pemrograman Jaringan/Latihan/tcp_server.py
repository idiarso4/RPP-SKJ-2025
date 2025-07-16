import socket

def start_server():
    # Buat socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind ke alamat dan port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    
    # Listen untuk koneksi masuk
    server_socket.listen(1)
    print(f"Server TCP berjalan di {server_address[0]}:{server_address[1]}")
    
    try:
        while True:
            # Terima koneksi
            print("Menunggu koneksi...")
            connection, client_address = server_socket.accept()
            print(f"Terhubung dengan {client_address}")
            
            try:
                while True:
                    # Terima data
                    data = connection.recv(1024)
                    if not data:
                        break
                    
                    # Tampilkan pesan dari client
                    print(f"Diterima: {data.decode()}")
                    
                    # Kirim balasan
                    response = f"Server menerima: {data.decode()}"
                    connection.sendall(response.encode())
                    
            finally:
                # Tutup koneksi
                connection.close()
                print(f"Koneksi dengan {client_address} ditutup")
                
    except KeyboardInterrupt:
        print("\nMenghentikan server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()

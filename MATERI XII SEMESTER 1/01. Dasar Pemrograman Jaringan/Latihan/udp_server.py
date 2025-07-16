import socket

def start_udp_server():
    # Buat socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind ke alamat dan port
    server_address = ('localhost', 12346)
    server_socket.bind(server_address)
    
    print(f"Server UDP berjalan di {server_address[0]}:{server_address[1]}")
    print("Tekan Ctrl+C untuk menghentikan server\n")
    
    try:
        while True:
            print("\nMenunggu pesan...")
            
            # Terima data
            data, client_address = server_socket.recvfrom(1024)
            print(f"Menerima pesan dari {client_address}")
            
            # Tampilkan pesan
            message = data.decode()
            print(f"Pesan: {message}")
            
            # Kirim balasan
            response = f"Server UDP menerima: {message}"
            server_socket.sendto(response.encode(), client_address)
            
    except KeyboardInterrupt:
        print("\nMenghentikan server...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Server dihentikan")

if __name__ == "__main__":
    start_udp_server()

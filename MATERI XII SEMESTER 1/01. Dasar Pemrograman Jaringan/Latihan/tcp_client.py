import socket

def start_client():
    # Buat socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Tentukan alamat server dan port
    server_address = ('localhost', 12345)
    
    try:
        # Hubungkan ke server
        print(f"Menghubungkan ke {server_address[0]}:{server_address[1]}")
        client_socket.connect(server_address)
        print("Terhubung ke server!")
        print("Ketik 'exit' untuk keluar")
        
        while True:
            # Input pesan dari pengguna
            message = input("Pesan Anda: ")
            
            # Keluar jika pengguna mengetik 'exit'
            if message.lower() == 'exit':
                break
                
            # Kirim pesan ke server
            client_socket.sendall(message.encode())
            
            # Terima balasan dari server
            response = client_socket.recv(1024)
            print(f"Dari Server: {response.decode()}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Tutup koneksi
        client_socket.close()
        print("Koneksi ditutup")

if __name__ == "__main__":
    start_client()

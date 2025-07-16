import socket

def start_udp_client():
    # Buat socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Tentukan alamat server dan port
    server_address = ('localhost', 12346)
    
    print("=== UDP Client ===")
    print("Ketik pesan untuk dikirim ke server")
    print("Ketik 'exit' untuk keluar\n")
    
    try:
        while True:
            # Input pesan dari pengguna
            message = input("Pesan Anda: ")
            
            # Keluar jika pengguna mengetik 'exit'
            if message.lower() == 'exit':
                break
                
            # Kirim pesan ke server
            print(f"Mengirim: {message}")
            client_socket.sendto(message.encode(), server_address)
            
            # Terima balasan dari server
            data, server = client_socket.recvfrom(1024)
            print(f"Dari Server: {data.decode()}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("\nKlien dihentikan")

if __name__ == "__main__":
    start_udp_client()

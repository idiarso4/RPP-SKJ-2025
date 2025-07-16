import socket
import threading
import sys

def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[INFO] Koneksi ke server terputus.")
                break
            print(f"\n{data.decode()}")
            print("Pesan Anda: ", end='', flush=True)
        except ConnectionResetError:
            print("\n[ERROR] Koneksi ke server terputus secara tiba-tiba.")
            break
        except Exception as e:
            print(f"\n[ERROR] Terjadi kesalahan: {e}")
            break

def main():
    host = input("Masukkan alamat server [default: localhost]: ") or "localhost"
    port_input = input("Masukkan port server [default: 9009]: ")
    port = int(port_input) if port_input.strip() else 9009

    print(f"\n[INFO] Mencoba terhubung ke {host}:{port}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        print("[INFO] Terhubung ke server. Ketik pesan Anda di bawah ini:")
    except Exception as e:
        print(f"[ERROR] Gagal terhubung ke server: {e}")
        print("Pastikan server sudah berjalan dan alamat/port benar.")
        return

    threading.Thread(target=receive, args=(sock,), daemon=True).start()

    try:
        while True:
            try:
                msg = input("Pesan Anda: ")
                if msg.lower() == "/quit":
                    print("Keluar dari chat...")
                    break
                sock.sendall((msg + '\n').encode())
            except (ConnectionResetError, BrokenPipeError):
                print("\n[ERROR] Koneksi ke server terputus.")
                break
            except KeyboardInterrupt:
                print("\nMengakhiri koneksi...")
                break
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
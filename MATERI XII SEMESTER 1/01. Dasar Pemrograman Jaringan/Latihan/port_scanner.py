import socket
import concurrent.futures
import time

def scan_port(host, port):
    """
    Mencoba melakukan koneksi ke port tertentu pada host
    """
    try:
        # Buat socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout 1 detik
        
        # Coba terhubung ke port
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            return port, "TERBUKA"
        else:
            return port, "TERTUTUP"
    except:
        return port, "ERROR"

def main():
    print("=== PORT SCANNER SEDERHANA ===\n")
    
    # Input dari pengguna
    target = input("Masukkan alamat target (contoh: localhost atau 192.168.1.1): ").strip()
    start_port = int(input("Masukkan port awal (1-65535): ").strip() or "1")
    end_port = int(input(f"Masukkan port akhir ({start_port}-65535): ").strip() or str(start_port + 100))
    
    # Validasi input
    if start_port < 1 or start_port > 65535 or end_port < 1 or end_port > 65535:
        print("Error: Port harus berada di antara 1 dan 65535")
        return
    if start_port > end_port:
        start_port, end_port = end_port, start_port  # Swap jika port awal lebih besar
    
    print(f"\nMemindai {target} dari port {start_port} ke {end_port}...\n")
    
    start_time = time.time()
    open_ports = []
    
    # Gunakan ThreadPoolExecutor untuk pemindaian lebih cepat
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {
            executor.submit(scan_port, target, port): port 
            for port in range(start_port, end_port + 1)
        }
        
        for future in concurrent.futures.as_completed(future_to_port):
            port, status = future.result()
            if status == "TERBUKA":
                open_ports.append(port)
                print(f"Port {port}: {status}")
    
    # Tampilkan hasil
    print("\n=== HASIL PEMINDAIAN ===")
    print(f"Host: {target}")
    print(f"Port yang dipindai: {start_port}-{end_port}")
    print(f"Port terbuka: {', '.join(map(str, sorted(open_ports))) or 'Tidak ada'}")
    print(f"Waktu pemindaian: {time.time() - start_time:.2f} detik")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPemindaian dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
    input("\nTekan Enter untuk keluar...")

# 📚 Referensi Cepat - Pemrograman Jaringan dengan Python

## 📋 Daftar Isi
1. [Modul Socket Dasar](#-modul-socket-dasar)
2. [Konstanta Socket](#-konstanta-socket)
3. [Method Socket](#-method-socket)
4. [Error Handling](#-error-handling)
5. [Contoh Kode](#-contoh-kode)
6. [Alat Bantu](#-alat-bantu)
7. [Referensi Eksternal](#-referensi-eksternal)

---

## 🔌 Modul Socket Dasar

### `socket` - Modul Utama
```python
import socket
```

### `select` - I/O Multiplexing
```python
import select
```

### `threading` - Threading
```python
import threading
```

### `socketserver` - Framework Server
```python
import socketserver
```

---

## 🔢 Konstanta Socket

### Address Families
- `socket.AF_INET` - IPv4
- `socket.AF_INET6` - IPv6
- `socket.AF_UNIX` - Unix domain socket

### Socket Types
- `socket.SOCK_STREAM` - TCP
- `socket.SOCK_DGRAM` - UDP
- `socket.SOCK_RAW` - Raw socket

### Socket Options
- `socket.SO_REUSEADDR` - Izinkan penggunaan ulang alamat
- `socket.SOL_SOCKET` - Level socket
- `socket.IPPROTO_TCP` - Protokol TCP

### Flags
- `socket.MSG_WAITALL` - Tunggu sampai semua data diterima
- `socket.MSG_DONTWAIT` - Non-blocking mode

---

## 🛠️ Method Socket

### Membuat Socket
```python
# IPv4 TCP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IPv6 TCP Socket
sock_v6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# UDP Socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### Server Methods
```python
# Bind ke alamat dan port
sock.bind((host, port))

# Listen untuk koneksi masuk
sock.listen(backlog)

# Terima koneksi
connection, client_address = sock.accept()
```

### Client Methods
```python
# Hubungkan ke server
sock.connect((host, port))

# Kirim data
sock.sendall(data)

# Terima data
data = sock.recv(buffer_size)
```

### Utility Methods
```python
# Dapatkan nama host
hostname = socket.gethostname()

# Dapatkan alamat IP
ip_address = socket.gethostbyname(hostname)

# Dapatkan informasi layanan
service = socket.getservbyname('http')
```

---

## 🚨 Error Handling

### Exception Handling
```python
try:
    # Kode socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    
except socket.error as e:
    print(f"Error socket: {e}")
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    # Pastikan socket ditutup
    if 'sock' in locals():
        sock.close()
```

### Timeout
```python
# Set timeout (dalam detik)
sock.settimeout(5.0)

try:
    data = sock.recv(1024)
except socket.timeout:
    print("Waktu tunggu habis")
```

---

## 📝 Contoh Kode

### 1. TCP Echo Server
```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Terhubung dengan', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

### 2. TCP Echo Client
```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Menerima', repr(data))
```

### 3. UDP Echo Server
```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        print('Menerima dari', addr)
        s.sendto(data, addr)
```

### 4. UDP Echo Client
```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello, world', (HOST, PORT))
    data, addr = s.recvfrom(1024)

print('Menerima', repr(data), 'dari', addr)
```

---

## 🛠️ Alat Bantu

### 1. Netcat (nc)
```bash
# Dengarkan pada port
nc -l -p 1234

# Hubungkan ke port
nc localhost 1234
```

### 2. Telnet
```bash
# Hubungkan ke server
telnet localhost 1234
```

### 3. Nmap
```bash
# Pindai port terbuka
nmap -sS -p 1-1024 localhost
```

### 4. Wireshark
- Alat analisis protokol jaringan
- Dapat menangkap dan menganalisis lalu lintas jaringan

### 5. Postman
- Berguna untuk menguji API HTTP/HTTPS

---

## 📚 Referensi Eksternal

### Dokumentasi Resmi
- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
- [Python Select Module](https://docs.python.org/3/library/select.html)
- [Python Threading](https://docs.python.org/3/library/threading.html)

### Tutorial
- [Real Python - Socket Programming](https://realpython.com/python-sockets/)
- [GeeksforGeeks - Socket Programming](https://www.geeksforgeeks.org/socket-programming-python/)
- [Python Official HOWTO](https://docs.python.org/3/howto/sockets.html)

### Buku
- "Black Hat Python" by Justin Seitz
- "Violent Python" by TJ O'Connor
- "Foundations of Python Network Programming" by Brandon Rhodes

### Video
- [Network Programming with Python](https://www.youtube.com/playlist?list=PL1A2CSdiySGIPxpSlgzsZiWDavYTAx61d)
- [Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)

---
<div align="center">
  <p>Dokumen Referensi - Dasar Pemrograman Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

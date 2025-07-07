# 📚 Latihan Soal - Dasar Pemrograman Jaringan

## 🎯 Tujuan Latihan
- Memahami konsep dasar pemrograman jaringan
- Menerapkan socket programming dengan Python
- Menganalisis masalah jaringan
- Mengembangkan keterampilan pemecahan masalah

## 📝 Soal Teori

### Soal 1: Konsep Dasar
1. Jelaskan perbedaan antara TCP dan UDP dalam hal:
   - Keandalan (reliability)
   - Pengurutan paket (ordering)
   - Kecepatan
   - Penggunaan bandwidth

2. Apa yang dimaksud dengan port dalam konteks jaringan? Sebutkan 5 well-known port beserta layanannya!

3. Jelaskan proses TCP three-way handshake dan mengapa proses ini penting!

### Soal 2: Socket Programming
4. Jelaskan perbedaan antara `socket.bind()`, `socket.listen()`, dan `socket.accept()` dalam konteks server socket!

5. Mengapa penting untuk menggunakan `try-finally` atau `with` statement saat bekerja dengan socket di Python?

6. Jelaskan apa yang dilakukan oleh kode berikut:
   ```python
   import socket
   
   def check_port(host, port):
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.settimeout(1)
       result = sock.connect_ex((host, port))
       sock.close()
       return result == 0
   ```

## 💻 Soal Praktik

### Latihan 1: Port Scanner Sederhana
Buatlah program Python sederhana yang dapat memindai port-port yang terbuka pada sebuah host. Program harus:
- Menerima input alamat IP/hostname
- Menerima range port (awal dan akhir)
- Memeriksa status setiap port dalam range tersebut
- Menampilkan port-port yang terbuka

**Contoh Output:**
```
Masukkan alamat target: localhost
Port awal: 75
Port akhir: 85

Memindai localhost...
Port 80/tcp terbuka
Port 443/tcp terbuka

Pemindaian selesai!
```

### Latihan 2: Server HTTP Sederhana
Buatlah server HTTP sederhana yang dapat:
- Merespon permintaan GET dengan halaman HTML sederhana
- Menampilkan informasi client (IP, User-Agent)
- Mencatat setiap permintaan ke dalam file log

**Contoh Output:**
```
[INFO] Server berjalan di port 8000
[INFO] Permintaan dari 127.0.0.1 - GET / - Mozilla/5.0...
```

### Latihan 3: Chat Room Sederhana
Buatlah aplikasi chat sederhana yang terdiri dari:
1. **Server:**
   - Menerima koneksi dari beberapa client
   - Meneruskan pesan dari satu client ke client lainnya
   - Menangani client yang terputus dengan baik

2. **Client:**
   - Dapat terhubung ke server
   - Dapat mengirim dan menerima pesan secara real-time
   - Menampilkan nama pengirim pesan

## 🧩 Tantangan Lanjutan

### Tantangan 1: Proxy Server
Buatlah proxy server sederhana yang dapat:
- Menerima permintaan HTTP dari client
- Meneruskan permintaan ke server tujuan
- Meneruskan respon kembali ke client
- Mencatat lalu lintas ke dalam file log

### Tantangan 2: File Transfer
Buatlah program untuk mengirim file antara client dan server dengan fitur:
- Daftar file yang tersedia di server
- Upload file ke server
- Download file dari server
- Progress bar untuk transfer file

## 📝 Jawaban

### Kunci Jawaban Soal Teori

#### Soal 1:
1. Perbedaan TCP dan UDP:
   - **Keandalan:** TCP handal (menggunakan acknowledgment), UDP tidak
   - **Pengurutan:** TCP menjamin pengurutan paket, UDP tidak
   - **Kecepatan:** UDP lebih cepat karena tidak ada overhead
   - **Bandwidth:** TCP menggunakan lebih banyak bandwidth karena header yang lebih besar

2. Port adalah endpoint logis dalam sistem operasi yang digunakan oleh protokol TCP/UDP untuk mengidentifikasi aplikasi. Contoh:
   - 80: HTTP
   - 443: HTTPS
   - 22: SSH
   - 21: FTP
   - 25: SMTP

3. Three-way handshake adalah proses pembentukan koneksi TCP:
   1. Client mengirim SYN
   2. Server merespon dengan SYN-ACK
   3. Client mengirim ACK
   Penting untuk memastikan koneksi yang andal sebelum pertukaran data.

#### Soal 2:
4. Perbedaan:
   - `bind()`: Mengaitkan socket dengan alamat IP dan port
   - `listen()`: Mengaktifkan server untuk menerima koneksi
   - `accept()`: Menerima koneksi dari client

5. Penting untuk memastikan socket ditutup dengan benar meskipun terjadi error, untuk menghindari kebocoran sumber daya.

6. Kode tersebut memeriksa apakah suatu port pada host tertentu terbuka dengan mencoba membuat koneksi TCP.

## 📚 Referensi
1. [Python Socket Programming](https://realpython.com/python-sockets/)
2. [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/)
3. [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)

---
<div align="center">
  <p>Dokumen Latihan - Dasar Pemrograman Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

# Panduan Praktikum Pemrograman Jaringan TCP

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Struktur Program](#struktur-program)
3. [Cara Menjalankan](#cara-menjalankan)
4. [Penjelasan Kode](#penjelasan-kode)
5. [Latihan](#latihan)
6. [Troubleshooting](#troubleshooting)

## Pendahuluan
Dokumen ini menjelaskan tentang contoh program jaringan menggunakan protokol TCP. TCP (Transmission Control Protocol) adalah protokol yang handal untuk komunikasi antara dua perangkat dalam jaringan.

## Struktur Program
```
Latihan/
├── tcp_server.py     # Program server TCP
├── tcp_client.py     # Program client TCP
└── PANDUAN_TCP.md    # Dokumen ini
```

## Cara Menjalankan

### 1. Menjalankan Server
Buka terminal dan jalankan:
```bash
py tcp_server.py
```
Server akan berjalan di `localhost:12345`

### 2. Menjalankan Client
Buka terminal baru dan jalankan:
```bash
py tcp_client.py
```

### 3. Menggunakan Aplikasi
- Di client, ketik pesan dan tekan Enter
- Server akan merespon dengan mengulang pesan
- Ketik 'exit' untuk keluar

## Penjelasan Kode

### tcp_server.py
- Membuat socket TCP dengan `socket.AF_INET` dan `socket.SOCK_STREAM`
- Mengikat socket ke alamat dan port dengan `bind()`
- Mendengarkan koneksi masuk dengan `listen()`
- Menerima koneksi dengan `accept()`
- Menerima dan mengirim data dengan `recv()` dan `sendall()`

### tcp_client.py
- Membuat socket TCP
- Menghubungkan ke server dengan `connect()`
- Mengirim pesan ke server
- Menerima balasan dari server

## Latihan

### Latihan 1: Modifikasi Pesan
Ubah server untuk mengubah pesan menjadi huruf besar sebelum mengirim balasan.

### Latihan 2: Multi-Client
Modifikasi server untuk bisa menangani beberapa client sekaligus menggunakan thread.

### Latihan 3: Protokol Sederhana
Buat protokol sederhana di mana client bisa mengirim perintah:
- `TIME` - Server mengirim waktu saat ini
- `UPPER <teks>` - Server mengembalikan teks dalam huruf besar
- `LOWER <teks>` - Server mengembalikan teks dalam huruf kecil

## Troubleshooting

### 1. Port Sudah Digunakan
```
OSError: [Errno 98] Address already in use
```
Tunggu beberapa saat atau ganti port di kode.

### 2. Koneksi Ditolak
```
ConnectionRefusedError: [Errno 111] Connection refused
```
Pastikan server sudah berjalan sebelum menjalankan client.

### 3. Port Tidak Tersedia
```
PermissionError: [Errno 13] Permission denied
```
Port di bawah 1024 membutuhkan hak akses administrator. Gunakan port di atas 1024.

## Referensi
1. [Python Socket Programming](https://realpython.com/python-sockets/)
2. [Python Documentation - socket](https://docs.python.org/3/library/socket.html)
3. [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/)

---
<div align="center">
  <p>Dokumen Panduan - Praktikum Jaringan Komputer</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

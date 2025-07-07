# 📋 Tugas Praktik - Aplikasi Client-Server Sederhana

## 🎯 Tujuan
Menguji kemampuan peserta didik dalam mengimplementasikan pemrograman jaringan dengan membuat aplikasi client-server sederhana menggunakan socket programming.

## 📝 Deskripsi Tugas
Buatlah sebuah aplikasi client-server dengan spesifikasi sebagai berikut:

### 1. Server
- Menerima koneksi dari beberapa client secara bersamaan
- Mencatat semua pesan yang masuk ke dalam file log
- Mampu mengirim daftar perintah yang tersedia ke client
- Mampu membalas pesan dari client dengan format tertentu
- Menangani error dengan baik (misalnya client terputus)

### 2. Client
- Dapat terhubung ke server dengan alamat dan port tertentu
- Menampilkan menu interaktif untuk pengguna
- Mampu mengirim perintah ke server
- Menampilkan respon dari server dengan rapi
- Memiliki opsi untuk keluar dari aplikasi

## 🛠️ Spesifikasi Teknis

### Persyaratan Server
1. **Fitur Wajib:**
   - Menerima koneksi pada port 23456
   - Mencatat semua aktivitas ke file `server.log`
   - Menyediakan perintah-perintah berikut:
     - `TIME` - Mengembalikan waktu server saat ini
     - `LIST` - Menampilkan daftar client yang terhubung
     - `ECHO <pesan>` - Mengembalikan pesan yang sama
     - `QUIT` - Memutus koneksi
   - Multi-threaded untuk menangani banyak client

2. **Contoh Output Server:**
   ```
   [INFO] Server berjalan di 0.0.0.0:23456
   [INFO] Client terhubung dari 127.0.0.1:54321
   [CLIENT 127.0.0.1] TIME
   [CLIENT 127.0.0.1] QUIT
   [INFO] Koneksi dari 127.0.0.1 ditutup
   ```

### Persyaratan Client
1. **Fitur Wajib:**
   - Dapat terhubung ke alamat IP dan port tertentu
   - Menampilkan menu interaktif
   - Validasi input pengguna
   - Menampilkan respon dari server dengan rapi
   - Handle koneksi terputus dengan baik

2. **Contoh Tampilan Client:**
   ```
   Selamat datang di Client Aplikasi
   ===============================
   Masukkan alamat server [localhost]: 
   Masukkan port [23456]:
   
   Terhubung ke localhost:23456
   
   Menu:
   1. Lihat waktu server
   2. Kirim pesan
   3. Lihat daftar perintah
   4. Keluar
   
   Pilihan [1-4]: 
   ```

## 📋 Ketentuan Penilaian

### Kriteria Penilaian (100 poin)
1. **Fungsionalitas (40 poin)**
   - Server dapat menerima koneksi (10 poin)
   - Multi-client support (10 poin)
   - Semua perintah berfungsi (10 poin)
   - Logging berfungsi (10 poin)

2. **Kode (30 poin)**
   - Struktur kode rapi dan terorganisir (10 poin)
   - Komentar yang jelas (10 poin)
   - Error handling yang baik (10 poin)

3. **Dokumentasi (20 poin)**
   - README.md yang jelas (10 poin)
   - Komentar dalam kode (5 poin)
   - Panduan instalasi dan eksekusi (5 poin)

4. **Tambahan (10 poin)**
   - Fitur tambahan yang bermanfaat (5 poin)
   - Antarmuka pengguna yang baik (5 poin)

## 📅 Tenggat Waktu
- **Pengumpulan:** 1 minggu dari tanggal pemberian tugas
- **Presentasi:** Minggu berikutnya (jika diperlukan)

## 📤 Pengumpulan
1. Buat folder dengan format: `NIM_Nama_Kelas`
2. Masukkan semua file yang diperlukan ke dalam folder
3. Zip folder tersebut
4. Upload ke Google Classroom

## 📚 Referensi
1. [Python Socket Programming](https://realpython.com/python-sockets/)
2. [Python Threading](https://docs.python.org/3/library/threading.html)
3. [Python Logging](https://docs.python.org/3/howto/logging.html)

---
<div align="center">
  <p>Dokumen Tugas - Dasar Pemrograman Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

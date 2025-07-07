# 📝 Soal Pilihan Ganda - Dasar Pemrograman Jaringan

## Instruksi
Pilihlah jawaban yang paling tepat dengan memberikan tanda (X) pada pilihan yang tersedia.

---

### 1. Manakah pernyataan yang BENAR tentang socket dalam pemrograman jaringan?
- [ ] a. Socket hanya dapat digunakan untuk komunikasi dalam satu komputer
- [X] b. Socket adalah endpoint dari komunikasi dua arah antara dua program yang berjalan di jaringan
- [ ] c. Socket hanya mendukung protokol TCP
- [ ] d. Socket tidak bisa digunakan untuk komunikasi real-time

**Pembahasan:** Socket adalah endpoint dari komunikasi dua arah antara dua program yang berjalan di jaringan, bisa dalam satu komputer atau komputer yang berbeda.

---

### 2. Port manakah yang TIDAK termasuk well-known port?
- [ ] a. 80 (HTTP)
- [ ] b. 21 (FTP)
- [ ] c. 22 (SSH)
- [X] d. 54321

**Pembahasan:** Port well-known adalah port 0-1023 yang telah ditetapkan untuk layanan tertentu. Port 54321 bukan termasuk well-known port.

---

### 3. Apa fungsi dari method `bind()` pada socket programming?
- [ ] a. Mendengarkan koneksi masuk
- [ ] b. Menerima koneksi dari client
- [X] c. Mengaitkan socket dengan alamat IP dan port tertentu
- [ ] d. Mengirim data ke client

**Pembahasan:** Method `bind()` digunakan untuk mengaitkan socket dengan alamat IP dan port tertentu di mana server akan mendengarkan koneksi masuk.

---

### 4. Manakah yang BUKAN keuntungan menggunakan TCP dibanding UDP?
- [ ] a. Handal (reliable)
- [ ] b. Pengiriman data berurutan (in-order)
- [X] c. Lebih cepat karena tidak ada overhead koneksi
- [ ] d. Memiliki mekanisme flow control

**Pembahasan:** TCP memiliki overhead yang lebih besar karena proses three-way handshake dan mekanisme keandalan, sehingga tidak lebih cepat dibanding UDP.

---

### 5. Apa yang terjadi jika dua program mencoba menggunakan port yang sama?
- [ ] a. Kedua program akan berjalan dengan normal
- [ ] b. Sistem operasi akan secara otomatis mengalokasikan port lain
- [X] c. Akan terjadi error "Address already in use"
- [ ] d. Kedua program akan berbagi port yang sama

**Pembahasan:** Jika dua program mencoba menggunakan port yang sama, akan terjadi error "Address already in use" karena satu port hanya dapat digunakan oleh satu aplikasi dalam satu waktu.

---

### 6. Manakah pernyataan yang BENAR tentang multi-threading pada server?
- [ ] a. Multi-threading membuat server lebih lambat
- [ ] b. Setiap thread berbagi memori yang sama dengan thread lainnya
- [X] c. Multi-threading memungkinkan server menangani beberapa koneksi secara bersamaan
- [ ] d. Python tidak mendukung multi-threading

**Pembahasan:** Multi-threading memungkinkan server menangani beberapa koneksi secara bersamaan dengan membuat thread terpisah untuk setiap koneksi.

---

### 7. Manakah fungsi yang digunakan untuk mengubah string menjadi bytes sebelum dikirim melalui socket?
- [ ] a. `str()`
- [X] b. `encode()`
- [ ] c. `decode()`
- [ ] d. `convert()`

**Pembahasan:** Method `encode()` digunakan untuk mengubah string menjadi bytes sebelum dikirim melalui socket.

---

### 8. Apa yang dilakukan oleh method `listen()` pada socket server?
- [ ] a. Menerima koneksi dari client
- [ ] b. Mengirim data ke client
- [X] c. Mengaktifkan server untuk menerima koneksi
- [ ] d. Menutup koneksi socket

**Pembahasan:** Method `listen()` mengaktifkan server untuk menerima koneksi dari client.

---

### 9. Manakah yang BUKAN tahapan dalam komunikasi TCP?
- [ ] a. Three-way handshake
- [ ] b. Transfer data
- [ ] c. Connection termination
- [X] d. Broadcast message

**Pembahasan:** Broadcast message bukan bagian dari tahapan komunikasi TCP. TCP menggunakan koneksi point-to-point yang terarah.

---

### 10. Mengapa penting untuk menutup koneksi socket setelah selesai digunakan?
- [ ] a. Untuk menghemat listrik
- [X] b. Untuk membebaskan sumber daya sistem
- [ ] c. Karena diwajibkan oleh Python
- [ ] d. Agar bisa digunakan oleh program lain

**Pembahasan:** Menutup koneksi socket penting untuk membebaskan sumber daya sistem seperti port dan memori yang digunakan oleh koneksi tersebut.

---

## Kunci Jawaban
1. b
2. d
3. c
4. c
5. c
6. c
7. b
8. c
9. d
10. b

---
<div align="center">
  <p>Dokumen Soal - Dasar Pemrograman Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

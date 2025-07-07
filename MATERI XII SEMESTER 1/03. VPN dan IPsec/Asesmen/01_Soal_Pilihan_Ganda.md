# 📝 Soal Pilihan Ganda - VPN dan IPsec

## Instruksi
Pilih jawaban yang paling tepat dengan memberikan tanda (X) pada pilihan yang tersedia.

---

### 1. Manakah yang BUKAN termasuk keuntungan menggunakan VPN?
- [ ] a. Enkripsi data
- [ ] b. Akses jarak jauh yang aman
- [X] c. Meningkatkan kecepatan internet
- [ ] d. Menyembunyikan alamat IP asli

**Pembahasan:** VPN umumnya tidak meningkatkan kecepatan internet, bahkan bisa menurunkan karena overhead enkripsi.

---

### 2. Protokol manakah yang menggunakan port 500/UDP secara default?
- [ ] a. OpenVPN
- [X] b. IKEv1/IKEv2
- [ ] c. PPTP
- [ ] d. L2TP

**Pembahasan:** IKE (Internet Key Exchange) menggunakan port 500/UDP untuk negosiasi kunci.

---

### 3. Manakah yang BUKAN merupakan mode operasi IPsec?
- [ ] a. Transport Mode
- [X] b. Bridge Mode
- [ ] c. Tunnel Mode
- [ ] d. Semua jawaban benar

**Pembahasan:** IPsec memiliki dua mode utama: Transport Mode dan Tunnel Mode.

---

### 4. Protokol manakah yang TIDAK direkomendasikan karena kerentanan keamanannya?
- [ ] a. IKEv2
- [ ] b. OpenVPN
- [X] c. PPTP
- [ ] d. WireGuard

**Pembahasan:** PPTP memiliki kerentanan keamanan yang serius dan tidak lagi direkomendasikan.

---

### 5. Apa fungsi dari Security Association (SA) dalam IPsec?
- [ ] a. Mengenkripsi data
- [ ] b. Mengautentikasi pengguna
- [X] c. Menyimpan parameter keamanan untuk koneksi
- [ ] d. Melakukan routing paket

**Pembahasan:** SA menyimpan parameter keamanan seperti kunci enkripsi dan algoritma untuk koneksi tertentu.

---

### 6. Manakah yang BUKAN komponen dari IPsec?
- [ ] a. AH (Authentication Header)
- [ ] b. ESP (Encapsulating Security Payload)
- [X] c. SSL (Secure Sockets Layer)
- [ ] d. IKE (Internet Key Exchange)

**Pembahasan:** SSL bukan bagian dari IPsec, melainkan protokol yang berbeda untuk keamanan lapisan aplikasi.

---

### 7. Apa perbedaan utama antara mode Transport dan Tunnel pada IPsec?
- [ ] a. Transport Mode lebih aman dari Tunnel Mode
- [X] b. Transport Mode hanya mengenkripsi payload, sedangkan Tunnel Mode mengenkripsi seluruh paket
- [ ] c. Tunnel Mode hanya untuk IPv4, Transport Mode untuk IPv6
- [ ] d. Tidak ada perbedaan signifikan

**Pembahasan:** Transport Mode mengenkripsi payload asli, sementara Tunnel Mode mengenkripsi seluruh paket IP asli dan menambahkan header baru.

---

### 8. Protokol manakah yang menggunakan port 1194/UDP secara default?
- [ ] a. L2TP
- [ ] b. IKEv2
- [X] c. OpenVPN
- [ ] d. PPTP

**Pembahasan:** OpenVPN menggunakan port 1194/UDP secara default.

---

### 9. Manakah yang BUKAN merupakan kelebihan IKEv2 dibandingkan IKEv1?
- [ ] a. Dukungan MOBIKE
- [ ] b. Perlindungan DoS yang lebih baik
- [X] c. Kompatibilitas yang lebih luas dengan perangkat lama
- [ ] d. Proses negosiasi yang lebih cepat

**Pembahasan:** IKEv2 justru memiliki kompatibilitas yang lebih terbatas dengan perangkat lama dibandingkan IKEv1.

---

### 10. Apa yang dimaksud dengan "Perfect Forward Secrecy" dalam konteks VPN?
- [ ] a. Kemampuan untuk meneruskan koneksi tanpa batas
- [X] b. Setiap sesi menggunakan kunci enkripsi yang unik
- [ ] c. Kemampuan untuk memulihkan koneksi yang terputus
- [ ] d. Fitur untuk mempercepat koneksi VPN

**Pembahasan:** Perfect Forward Secrecy memastikan bahwa setiap sesi menggunakan kunci enkripsi yang unik, sehingga jika satu kunci terkompromikan, kunci sesi lainnya tetap aman.

## Kunci Jawaban
1. c
2. b
3. b
4. c
5. c
6. c
7. b
8. c
9. c
10. b

---
<div align="center">
  <p>Dokumen Soal - VPN dan IPsec</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

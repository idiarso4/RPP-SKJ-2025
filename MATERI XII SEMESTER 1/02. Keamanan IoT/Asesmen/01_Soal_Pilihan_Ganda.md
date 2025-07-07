# 📝 Soal Pilihan Ganda - Keamanan IoT

## Instruksi
Pilihlah jawaban yang paling tepat dengan memberikan tanda (X) pada pilihan yang tersedia.

---

### 1. Manakah yang BUKAN termasuk dalam OWASP IoT Top 10?
- [ ] a. Weak, Guessable, or Hardcoded Passwords
- [ ] b. Insecure Network Services
- [ ] c. Lack of Secure Update Mechanism
- [X] d. SQL Injection

**Pembahasan:** SQL Injection termasuk dalam OWASP Top 10 untuk aplikasi web, bukan khusus IoT.

---

### 2. Protokol manakah yang TIDAK direkomendasikan untuk perangkat IoT karena tidak memiliki enkripsi bawaan?
- [ ] a. MQTT dengan TLS
- [ ] b. CoAP dengan DTLS
- [X] c. MQTT tanpa enkripsi
- [ ] d. HTTPS

**Pembahasan:** MQTT tanpa enkripsi mengirimkan data dalam bentuk plaintext yang mudah disadap.

---

### 3. Apa tujuan dari secure boot pada perangkat IoT?
- [ ] a. Mempercepat proses booting
- [X] b. Memastikan hanya kode yang terpercaya yang dijalankan saat boot
- [ ] c. Mengenkripsi semua data yang disimpan
- [ ] d. Menonaktifkan port USB

**Pembahasan:** Secure boot memverifikasi tanda tangan digital pada firmware sebelum dijalankan.

---

### 4. Manakah yang BUKAN merupakan ancaman umum pada perangkat IoT?
- [ ] a. Default credentials
- [ ] b. Firmware yang tidak diupdate
- [X] c. Buffer overflow pada aplikasi desktop
- [ ] d. Komunikasi tidak terenkripsi

**Pembahasan:** Buffer overflow pada aplikasi desktop bukan ancaman khusus IoT.

---

### 5. Apa yang dimaksud dengan "bricking" dalam konteks keamanan IoT?
- [ ] a. Perangkat diubah menjadi router
- [X] b. Perangkat menjadi tidak dapat digunakan akibat update yang gagal
- [ ] c. Perangkat digunakan untuk mining cryptocurrency
- [ ] d. Perangkat terhubung ke botnet

**Pembahasan:** Bricking terjadi ketika perangkat menjadi tidak berfungsi seperti batu bata (brick).

---

### 6. Manakah yang BUKAN termasuk dalam prinsip "Security by Design" untuk IoT?
- [ ] a. Least privilege
- [ ] b. Defense in depth
- [X] c. Backdoor untuk akses mudah
- [ ] d. Secure defaults

**Pembahasan:** Backdoor bertentangan dengan prinsip keamanan.

---

### 7. Apa tujuan dari penggunaan TPM (Trusted Platform Module) pada perangkat IoT?
- [ ] a. Meningkatkan kecepatan pemrosesan
- [X] b. Menyimpan kriptografi dengan aman
- [ ] c. Mengurangi konsumsi daya
- [ ] d. Meningkatkan jangkauan WiFi

**Pembahasan:** TPM digunakan untuk menyimpan kunci kriptografi dengan aman.

---

### 8. Manakah yang BUKAN merupakan contoh serangan pada lapisan fisik perangkat IoT?
- [ ] a. Side-channel attacks
- [ ] b. Chip decapping
- [X] c. SQL injection
- [ ] d. JTAG debugging

**Pembahasan:** SQL injection adalah serangan pada lapisan aplikasi, bukan fisik.

---

### 9. Mengapa perangkat IoT sering menjadi target serangan DDoS?
- [ ] a. Karena harganya mahal
- [X] b. Karena sering memiliki keamanan yang lemah dan terhubung ke internet
- [ ] c. Karena memiliki daya komputasi yang tinggi
- [ ] d. Karena menggunakan enkripsi yang kuat

**Pembahasan:** Keamanan yang lemah dan koneksi internet membuatnya mudah direkrut ke botnet.

---

### 10. Apa yang dimaksud dengan "fuzzing" dalam pengujian keamanan IoT?
- [ ] a. Mengenkripsi data dengan algoritma acak
- [X] b. Mengirim input acak atau tidak terduga ke perangkat
- [ ] c. Menyembunyikan data dalam gambar
- [ ] d. Membuat salinan cadangan firmware

**Pembahasan:** Fuzzing adalah teknik pengujian dengan mengirim input tak terduga untuk menemukan kerentanan.

## Kunci Jawaban
1. d
2. c
3. b
4. c
5. b
6. c
7. b
8. c
9. b
10. b

---
<div align="center">
  <p>Dokumen Soal - Keamanan IoT</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

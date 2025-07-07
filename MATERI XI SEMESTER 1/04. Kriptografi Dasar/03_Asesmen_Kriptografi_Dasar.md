# 📝 Asesmen: Kriptografi Dasar

## 🎯 Kompetensi Dasar
3.9 Menerapkan konsep kriptografi dasar
3.10 Menganalisis algoritma kriptografi
3.11 Mengimplementasikan enkripsi dan dekripsi

## 📝 Soal Pilihan Ganda

### 1. Manakah yang BUKAN termasuk tujuan kriptografi?
   a) Kerahasiaan  
   b) Ketersediaan  
   c) Integritas  
   d) Otentikasi  
   
   **Jawaban: b) Ketersediaan**  
   *Pembahasan: Tujuan utama kriptografi adalah kerahasiaan, integritas, otentikasi, dan non-repudiasi. Ketersediaan adalah aspek keamanan informasi yang dijamin oleh mekanisme lain seperti backup dan redundansi.*

### 2. Algoritma manakah yang menggunakan kunci yang sama untuk enkripsi dan dekripsi?
   a) RSA  
   b) AES  
   c) ECC  
   d) Diffie-Hellman  
   
   **Jawaban: b) AES**  
   *Pembahasan: AES adalah algoritma kriptografi simetris yang menggunakan kunci yang sama untuk enkripsi dan dekripsi. RSA, ECC, dan Diffie-Hellman adalah algoritma asimetris yang menggunakan pasangan kunci publik-privat.*

### 3. Manakah yang BUKAN merupakan fungsi hash kriptografis?
   a) MD5  
   b) SHA-256  
   c) AES  
   d) SHA-3  
   
   **Jawaban: c) AES**  
   *Pembahasan: AES adalah algoritma enkripsi simetris, bukan fungsi hash. MD5, SHA-256, dan SHA-3 adalah contoh fungsi hash kriptografis.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara kriptografi simetris dan asimetris, serta berikan contoh penggunaan masing-masing dalam keamanan jaringan!

**Jawaban:**
**Kriptografi Simetris:**
- Menggunakan kunci yang sama untuk enkripsi dan dekripsi
- Lebih cepat dan efisien untuk data dalam jumlah besar
- Contoh algoritma: AES, DES, ChaCha20
- Penggunaan dalam jaringan:
  - Enkripsi data dalam VPN (AES)
  - Enkripsi disk (BitLocker, FileVault)
  - Enkripsi komunikasi real-time (video call, streaming)

**Kriptografi Asimetris:**
- Menggunakan pasangan kunci (publik dan privat)
- Lebih lambat tetapi menyelesaikan masalah pertukaran kunci
- Contoh algoritma: RSA, ECC, ElGamal
- Penggunaan dalam jaringan:
  - Pertukaran kunci rahasia (Diffie-Hellman)
  - Tanda tangan digital (RSA, ECDSA)
  - Sertifikat digital (X.509, SSL/TLS)

### 2. Jelaskan apa yang dimaksud dengan "man-in-the-middle attack" dan bagaimana kriptografi dapat mencegah serangan tersebut!

**Jawaban:**
**Man-in-the-Middle (MITM) Attack** adalah serangan di mana penyerang menyisipkan diri di tengah komunikasi antara dua pihak, sehingga dapat menyadap dan memodifikasi pesan yang dikirimkan.

**Cara Kerja MITM:**
1. Penyerang berada di antara korban dan server/tujuan
2. Korban mengira berkomunikasi langsung dengan server
3. Server mengira berkomunikasi langsung dengan korban
4. Penyerang dapat membaca, menyisipkan, atau memodifikasi pesan

**Pencegahan dengan Kriptografi:**
1. **Enkripsi Ujung-ke-Ujung**
   - Hanya pengirim dan penerima yang memiliki kunci untuk membaca pesan
   - Contoh: Signal, WhatsApp (end-to-end encryption)

2. **Pertukaran Kunci yang Aman**
   - Menggunakan protokol seperti Diffie-Hellman
   - Mencegah penyerang mengetahui kunci rahasia

3. **Otentikasi**
   - Menggunakan sertifikat digital untuk memverifikasi identitas
   - Mencegah penyerang berpura-pura sebagai salah satu pihak
   - Contoh: Sertifikat SSL/TLS di website

4. **Perfect Forward Secrecy**
   - Setiap sesi menggunakan kunci rahasia yang berbeda
   - Jika satu kunci terkompromi, sesi lain tetap aman

## 📝 Studi Kasus

### Kasus: Keamanan Aplikasi Perbankan

**Deskripsi:**
Sebuah bank ingin mengamankan aplikasi mobile banking mereka. Aplikasi ini memungkinkan nasabah untuk melakukan transfer uang, pembayaran, dan melihat riwayat transaksi. Bank tersebut khawatir akan ancaman keamanan seperti:
1. Penyadapan komunikasi
2. Pemalsuan identitas
3. Perubahan data transaksi
4. Penyangkalan transaksi

**Pertanyaan:**
1. Teknik kriptografi apa saja yang sebaiknya diimplementasikan untuk mengamankan aplikasi mobile banking tersebut?
2. Bagaimana cara mengamankan koneksi antara aplikasi mobile dan server bank?
3. Bagaimana cara memastikan integritas dan keaslian data transaksi?
4. Bagaimana cara melindungi data sensitif yang disimpan di perangkat mobile?

**Jawaban Contoh:**

1. **Teknik Kriptografi yang Diperlukan:**
   - **Enkripsi Simetris (AES-256)**: Untuk mengenkripsi data yang disimpan di perangkat
   - **Enkripsi Asimetris (RSA 2048-bit/ECC)**: Untuk pertukaran kunci dan tanda tangan digital
   - **Fungsi Hash (SHA-384/SHA-3)**: Untuk memastikan integritas data
   - **Tanda Tangan Digital (ECDSA)**: Untuk otentikasi dan non-repudiasi
   - **HMAC**: Untuk memverifikasi keaslian pesan

2. **Mengamankan Koneksi:**
   - Gunakan TLS 1.3 dengan cipher suite yang kuat (contoh: TLS_AES_256_GCM_SHA384)
   - Terapkan Certificate Pinning untuk mencegah serangan MITM
   - Gunakan HSTS (HTTP Strict Transport Security)
   - Implementasikan Perfect Forward Secrecy

3. **Menjaga Integritas dan Keaslian Data:**
   - Setiap transaksi ditandatangani secara digital oleh nasabah
   - Gunakan timestamp dan nomor acak (nonce) untuk mencegah replay attack
   - Terapkan mekanisme sequence number untuk transaksi
   - Simpan log transaksi yang diamankan dengan hash berantai

4. **Melindungi Data di Perangkat:**
   - Gunakan Android Keystore/iOS Keychain untuk menyimpan kunci enkripsi
   - Enkripsi database lokal dengan SQLCipher
   - Gunakan teknik white-box cryptography untuk melindungi kunci di aplikasi
   - Terapkan aplikasi tambahan seperti mobile app shielding

## 📝 Tugas Praktik

### Instruksi:
1. Buat program Python yang mengimplementasikan enkripsi hybrid (gabungan simetris dan asimetris)
2. Program harus dapat:
   - Membangkitkan pasangan kunci RSA
   - Melakukan enkripsi file dengan kunci sesi acak (AES)
   - Mengenkripsi kunci sesi dengan kunci publik RSA
   - Menyimpan kunci sesi terenkripsi bersama file terenkripsi
   - Melakukan dekripsi file dengan kunci privat RSA

### Contoh Output:
```
$ python hybrid_encrypt.py encrypt rahasia.txt rahasia.enc
File berhasil dienkripsi: rahasia.enc
Kunci sesi tersimpan di: rahasia.enc.key

$ python hybrid_encrypt.py decrypt rahasia.enc rahasia_dekripsi.txt rahasia.enc.key
File berhasil didekripsi: rahasia_dekripsi.txt
```

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kebenaran Logika | 30% | Program berfungsi sesuai spesifikasi |
| Keamanan | 25% | Implementasi kriptografi yang aman |
| Penanganan Error | 20% | Menangani kasus kesalahan dengan baik |
| Dokumentasi | 15% | Komentar dan dokumentasi yang jelas |
| Kemudahan Penggunaan | 10% | Antarmuka pengguna yang intuitif |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. b) Ketersediaan
2. b) AES
3. c) AES

### Pedoman Penskoran Esai
1. **Kelengkapan Jawaban** (40%): Semua poin penting tercakup
2. **Ketepatan Konsep** (30%): Penjelasan konsep yang akurat
3. **Contoh Relevan** (20%): Contoh yang diberikan sesuai konteks
4. **Struktur Jawaban** (10%): Sistematika penyampaian yang baik

## 📚 Referensi
1. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of Applied Cryptography*. CRC Press.
2. Paar, C., & Pelzl, J. (2009). *Understanding Cryptography: A Textbook for Students and Practitioners*. Springer.
3. NIST FIPS 197: Advanced Encryption Standard (AES)
4. RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
5. OWASP Mobile Security Testing Guide

---
<div align="center">
  <p>Dokumen Asesmen - Kriptografi Dasar</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

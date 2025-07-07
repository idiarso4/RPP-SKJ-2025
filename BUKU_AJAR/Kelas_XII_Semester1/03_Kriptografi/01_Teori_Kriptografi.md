# Modul 3: Kriptografi

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Konsep Dasar Kriptografi](#konsep-dasar)
3. [Sejarah Perkembangan Kriptografi](#sejarah)
4. [Jenis-Jenis Algoritma Kriptografi](#jenis-algoritma)
5. [Infrastruktur Kunci Publik (PKI)](#pki)
6. [Standar dan Protokol Kriptografi](#standar-protokol)
7. [Implementasi Kriptografi Modern](#implementasi-modern)
8. [Studi Kasus](#studi-kasus)
9. [Tantangan dan Ancaman](#tantangan-dan-ancaman)
10. [Latihan dan Tugas](#latihan-dan-tugas)
11. [Referensi](#referensi)

## 1. Pendahuluan
Kriptografi adalah ilmu dan seni mengamankan pesan dengan cara membuatnya tidak dapat dibaca oleh pihak yang tidak berwenang. Modul ini membahas konsep dasar, algoritma, dan implementasi kriptografi modern dalam keamanan informasi.

## 2. Konsep Dasar Kriptografi
### 2.1 Tujuan Kriptografi
- **Kerahasiaan (Confidentiality)**: Memastikan informasi hanya dapat diakses oleh yang berwenang
- **Integritas (Integrity)**: Menjaga keakuratan dan kelengkapan informasi
- **Otentikasi (Authentication)**: Memverifikasi identitas pengirim/penerima
- **Non-repudiasi (Non-repudiation)**: Mencegah penyangkalan pengiriman/penerimaan pesan

### 2.2 Istilah Penting
- Plaintext: Pesan asli
- Ciphertext: Pesan terenkripsi
- Enkripsi: Proses mengubah plaintext menjadi ciphertext
- Dekripsi: Proses mengembalikan ciphertext ke plaintext
- Kunci: Data yang digunakan untuk enkripsi/dekripsi

## 3. Sejarah Perkembangan Kriptografi
### 3.1 Kriptografi Klasik
- Caesar Cipher
- Vigenère Cipher
- Enigma Machine (Perang Dunia II)

### 3.2 Era Modern
- Kriptografi simetris (DES, AES)
- Kriptografi asimetris (RSA, ECC)
- Kriptografi kuantum

## 4. Jenis-Jenis Algoritma Kriptografi
### 4.1 Kriptografi Simetris
- **AES (Advanced Encryption Standard)**
  - Ukuran kunci: 128, 192, atau 256 bit
  - Digunakan untuk enkripsi data dalam skala besar
  - Contoh implementasi: enkripsi disk (BitLocker, FileVault)

- **ChaCha20**
  - Alternatif AES yang lebih cepat di perangkat mobile
  - Digunakan dalam protokol TLS 1.3

### 4.2 Kriptografi Asimetris
- **RSA (Rivest-Shamir-Adleman)**
  - Berbasis faktorisasi bilangan prima besar
  - Digunakan untuk pertukaran kunci dan tanda tangan digital

- **ECC (Elliptic Curve Cryptography)**
  - Menawarkan keamanan setara dengan kunci yang lebih pendek
  - Efisien untuk perangkat dengan sumber daya terbatas

### 4.3 Fungsi Hash Kriptografis
- **SHA-3 (Keccak)**
  - Standar terbaru dari keluarga SHA
  - Tahan terhadap serangan tabrakan (collision attack)

- **BLAKE3**
  - Fungsi hash yang sangat cepat
  - Cocok untuk verifikasi data dalam jumlah besar

## 5. Infrastruktur Kunci Publik (PKI)
### 5.1 Komponen PKI
- Otoritas Sertifikat (CA)
- Daftar Pencabutan Sertifikat (CRL)
- Protokol OCSP (Online Certificate Status Protocol)

### 5.2 Sertifikat Digital
- X.509 v3
- Extended Validation (EV) Certificates
- Sertifikat Domain (DV) dan Organisasi (OV)

## 6. Standar dan Protokol Kriptografi
### 6.1 Standar Enkripsi
- **TLS 1.3**
  - Versi terbaru protokol keamanan lapisan transport
  - Peningkatan keamanan dan performa

- **Signal Protocol**
  - Digunakan oleh WhatsApp, Signal, dll.
  - Mengimplementasikan pertukaran kunci Double Ratchet

### 6.2 Protokol Kriptografi
- **DNSSEC**
  - Keamanan ekstensi untuk DNS
  - Mencegah serangan cache poisoning

- **PGP/GPG**
  - Standar enkripsi email dan file
  - Menggabungkan kriptografi simetris dan asimetris

## 7. Implementasi Kriptografi Modern
### 7.1 Kriptografi Post-Quantum
- Algoritma tahan kuantum
- Standarisasi NIST PQC (Post-Quantum Cryptography)

### 7.2 Homomorphic Encryption
- Memungkinkan komputasi pada data terenkripsi
- Aplikasi dalam komputasi awan yang aman

### 7.3 Zero-Knowledge Proofs
- Membuktikan pengetahuan rahasia tanpa mengungkapkannya
- Digunakan dalam protokol privasi seperti zk-SNARKs

## 8. Studi Kasus
### 8.1 Implementasi TLS di Layanan Perbankan Online
- Analisis penggunaan kriptografi dalam transaksi perbankan
- Perlindungan terhadap serangan man-in-the-middle

### 8.2 Kriptografi dalam Blockchain
- Mekanisme konsensus Proof of Work/Stake
- Tanda tangan digital untuk transaksi kripto

## 9. Tantangan dan Ancaman
### 9.1 Ancaman Terkini
- Serangan terhadap implementasi kriptografi
- Komputasi kuantum dan ancaman terhadap kriptografi asimetris
- Side-channel attacks

### 9.2 Praktik Terbaik
- Penggunaan algoritma yang kuat dan terbaru
- Manajemen kunci yang aman
- Pembaruan berkala terhadap standar kriptografi

## 10. Latihan dan Tugas
### Latihan Individu
1. Enkripsi dan dekripsi file menggunakan GPG
2. Analisis sertifikat SSL/TLS dari situs web populer
3. Implementasi sederhana algoritma kriptografi klasik

### Tugas Kelompok
1. Presentasi tentang perkembangan terbaru kriptografi post-quantum
2. Analisis keamanan implementasi kriptografi pada aplikasi populer
3. Simulasi pertukaran kunci aman menggunakan protokol Diffie-Hellman

## 11. Referensi
### Buku Teks
1. "Cryptography and Network Security" by William Stallings
2. "Serious Cryptography" by Jean-Philippe Aumasson
3. "Real-World Cryptography" by David Wong

### Standar dan Dokumen Resmi
1. **NIST FIPS 140-3**: Security Requirements for Cryptographic Modules
2. **RFC 8446**: The Transport Layer Security (TLS) Protocol Version 1.3
3. **NIST SP 800-175B**: Guideline for Using Cryptographic Standards in the Federal Government

### Sumber Online
1. **NIST Cryptographic Standards**: https://csrc.nist.gov/projects/cryptographic-standards
2. **Let's Encrypt**: https://letsencrypt.org/
3. **Crypto 101**: https://www.crypto101.io/

### Regulasi Indonesia
1. Peraturan BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi
2. Peraturan Menteri Kominfo tentang Standar Keamanan Informasi
3. Undang-Undang Informasi dan Transaksi Elektronik (UU ITE)

**Catatan Versi**:
- Versi Dokumen: 1.0
- Terakhir Diperbarui: 7 Juli 2025
- Penulis: Tim Pengembang Kurikulum Keamanan Jaringan

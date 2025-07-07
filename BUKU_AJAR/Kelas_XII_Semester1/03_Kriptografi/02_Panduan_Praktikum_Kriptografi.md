# Panduan Praktikum Kriptografi

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Persiapan Lingkungan Praktikum](#persiapan-lingkungan)
3. [Praktikum 1: Enkripsi Simetris dengan OpenSSL](#praktikum-1)
4. [Praktikum 2: Kriptografi Asimetris dengan GPG](#praktikum-2)
5. [Praktikum 3: Analisis Sertifikat Digital](#praktikum-3)
6. [Praktikum 4: Implementasi Fungsi Hash](#praktikum-4)
7. [Praktikum 5: Keamanan Koneksi dengan Wireshark](#praktikum-5)
8. [Penyusunan Laporan](#penyusunan-laporan)
9. [Referensi](#referensi)

## 1. Pendahuluan
Panduan praktikum ini dirancang untuk memberikan pengalaman langsung dalam mengimplementasikan berbagai teknik kriptografi. Praktikum ini mencakup enkripsi simetris, asimetris, analisis sertifikat, fungsi hash, dan analisis keamanan protokol.

## 2. Persiapan Lingkungan Praktikum
### 2.1 Perangkat Keras yang Dibutuhkan
- Komputer dengan spesifikasi minimal:
  - Prosesor: Intel Core i3 atau setara
  - RAM: 4GB (disarankan 8GB)
  - Penyimpanan: 100GB ruang kosong
  - Koneksi internet

### 2.2 Perangkat Lunak yang Dibutuhkan
- Sistem Operasi: Windows 10/11 atau Linux
- OpenSSL (command line)
- GnuPG (GPG)
- Wireshark
- Python 3.x dengan library cryptography
- Visual Studio Code atau teks editor lainnya

### 2.3 Instalasi Perangkat Lunak
1. **Windows**:
   - Unduh dan instal Git Bash
   - Instal OpenSSL dari [slproweb](https://slproweb.com/products/Win32OpenSSL.html)
   - Instal Gpg4win dari [gpg4win.org](https://gpg4win.org/)
   - Instal Wireshark dari [wireshark.org](https://www.wireshark.org/)

2. **Linux (Debian/Ubuntu)**:
   ```bash
   sudo apt update
   sudo apt install openssl gnupg2 wireshark python3-pip
   pip3 install cryptography
   ```

## 3. Praktikum 1: Enkripsi Simetris dengan OpenSSL
### 3.1 Tujuan
- Memahami konsep enkripsi simetris
- Mampu menggunakan OpenSSL untuk enkripsi/dekripsi file
- Menganalisis perbedaan mode operasi cipher

### 3.2 Langkah Kerja
1. Buat file teks berisi pesan rahasia
2. Enkripsi file menggunakan AES-256-CBC:
   ```bash
   openssl enc -aes-256-cbc -salt -in pesan.txt -out pesan.enc
   ```
3. Dekripsi file:
   ```bash
   openssl enc -d -aes-256-cbc -in pesan.enc -out pesan_decrypted.txt
   ```
4. Bandingkan file asli dan hasil dekripsi

### 3.3 Analisis
- Bandingkan ukuran file asli dan terenkripsi
- Uji dengan mode operasi berbeda (ECB, CBC, GCM)
- Catat waktu yang dibutuhkan untuk enkripsi/dekripsi

## 4. Praktikum 2: Kriptografi Asimetris dengan GPG
### 4.1 Tujuan
- Memahami konsep kriptografi asimetris
- Mampu membuat dan mengelola kunci GPG
- Melakukan enkripsi dan tanda tangan digital

### 4.2 Langkah Kerja
1. Buat pasangan kunci GPG:
   ```bash
   gpg --full-generate-key
   ```
2. Ekspor kunci publik:
   ```bash
   gpg --export -a "Nama Anda" > public.key
   ```
3. Enkripsi file untuk penerima:
   ```bash
   gpg --encrypt --recipient email@penerima.com pesan.txt
   ```
4. Buat tanda tangan digital:
   ```bash
   gpg --sign pesan.txt
   ```

## 5. Praktikum 3: Analisis Sertifikat Digital
### 5.1 Tujuan
- Memahami struktur sertifikat digital
- Menganalisis sertifikat SSL/TLS
- Memverifikasi rantai kepercayaan

### 5.2 Langkah Kerja
1. Dapatkan sertifikat dari website:
   ```bash
   openssl s_client -connect google.com:443 -showcerts </dev/null | openssl x509 -text -noout
   ```
2. Analisis informasi sertifikat:
   - Penerbit (Issuer)
   - Masa berlaku
   - Algoritma tanda tangan
   - Ekstensi sertifikat

## 6. Praktikum 4: Implementasi Fungsi Hash
### 6.1 Tujuan
- Memahami konsep fungsi hash kriptografis
- Menerapkan fungsi hash menggunakan Python
- Menganalisis properti hash

### 6.2 Langkah Kerja
1. Buat skrip Python untuk menghitung hash:
   ```python
   from cryptography.hazmat.primitives import hashes
   
   def calculate_hash(data, algorithm=hashes.SHA256()):
       digest = hashes.Hash(algorithm)
       digest.update(data.encode())
       return digest.finalize().hex()
   
   # Contoh penggunaan
   print("SHA-256:", calculate_hash("Hello, World!"))
   ```
2. Uji dengan input yang berbeda
3. Amati perubahan kecil pada input

## 7. Praktikum 5: Analisis Keamanan Protokol dengan Wireshark
### 7.1 Tujuan
- Menganalisis lalu lintas jaringan terenkripsi
- Memahami implementasi TLS
- Mengidentifikasi potensi kerentanan

### 7.2 Langkah Kerja
1. Mulai capture paket dengan Wireshark
2. Akses website HTTPS
3. Hentikan capture dan filter dengan `ssl`
4. Analisis handshake TLS
5. Identifikasi cipher suite yang digunakan

## 8. Penyusunan Laporan
### 8.1 Format Laporan
1. Halaman Judul
2. Daftar Isi
3. Pendahuluan
4. Metodologi
5. Hasil dan Analisis
6. Kesimpulan
7. Lampiran (screenshot, kode, dll)

### 8.2 Poin Penting
- Jelaskan setiap langkah dengan jelas
- Sertakan screenshot yang relevan
- Analisis hasil yang diperoleh
- Berikan kesimpulan dari praktikum

## 9. Referensi
1. **Buku**
   - "Cryptography Engineering" by Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno
   - "Applied Cryptography" by Bruce Schneier
   - "Understanding Cryptography" by Christof Paar and Jan Pelzl

2. **Sumber Online**
   - OpenSSL Documentation: https://www.openssl.org/docs/
   - GnuPG Documentation: https://gnupg.org/documentation/
   - Let's Encrypt Documentation: https://letsencrypt.org/docs/

3. **Alat**
   - OpenSSL: https://www.openssl.org/
   - GnuPG: https://gnupg.org/
   - Wireshark: https://www.wireshark.org/

**Catatan**:
- Selalu backup data penting sebelum melakukan praktikum
- Gunakan perangkat dalam lingkungan yang aman dan legal
- Dokumentasikan semua langkah yang dilakukan dengan baik

**Versi Dokumen**: 1.0  
**Terakhir Diperbarui**: 7 Juli 2025  
**Penulis**: Tim Pengembang Kurikulum Keamanan Jaringan

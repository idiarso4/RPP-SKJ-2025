# Panduan Praktikum Keamanan Cloud

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Persiapan Lingkungan Praktikum](#persiapan-lingkungan)
3. [Praktikum 1: Membuat Akun Cloud Gratis](#praktikum-1)
4. [Praktikum 2: Mengamankan Akun Cloud](#praktikum-2)
5. [Praktikum 3: Mengamankan Penyimpanan Cloud](#praktikum-3)
6. [Praktikum 4: Monitoring dan Logging](#praktikum-4)
7. [Praktikum 5: Analisis Keamanan Cloud](#praktikum-5)
8. [Penyusunan Laporan](#penyusunan-laporan)
9. [Referensi](#referensi)

## 1. Pendahuluan
Panduan praktikum ini dirancang untuk memberikan pengalaman langsung dalam mengamankan lingkungan cloud. Praktikum ini mencakup konfigurasi keamanan dasar, manajemen identitas, pengamanan penyimpanan, dan monitoring di lingkungan cloud.

## 2. Persiapan Lingkungan Praktikum
### 2.1 Persyaratan Sistem
- Komputer dengan koneksi internet
- Browser web terbaru (Chrome, Firefox, atau Edge)
- Akun email yang valid

### 2.2 Akun Cloud yang Dibutuhkan
1. **AWS Free Tier** (https://aws.amazon.com/free/)
2. **Google Cloud Free Tier** (https://cloud.google.com/free)
3. **Microsoft Azure Free Account** (https://azure.microsoft.com/en-us/free/)

> **Catatan**: Beberapa layanan mungkin memerlukan kartu kredit untuk verifikasi, tetapi akan menggunakan layanan yang termasuk dalam tier gratis.

## 3. Praktikum 1: Membuat Akun Cloud Gratis
### 3.1 Tujuan
- Memahami proses pendaftaran akun cloud
- Mengenal antarmuka dashboard cloud provider
- Mengaktifkan fitur keamanan dasar

### 3.2 Langkah Kerja (AWS Contoh)
1. Kunjungi https://aws.amazon.com/free/
2. Klik "Create a Free Account"
3. Ikuti proses pendaftaran dengan:
   - Masukkan informasi akun
   - Verifikasi nomor telepon
   - Masukkan detail pembayaran (tidak akan dikenakan biaya untuk layanan gratis)
   - Verifikasi identitas
   Pilih "Basic Support - Free"
4. Masuk ke AWS Management Console

### 3.3 Tugas
1. Jelaskan langkah-langkah yang Anda lakukan
2. Screenshot halaman dashboard AWS
3. Identifikasi layanan keamanan yang tersedia

## 4. Praktikum 2: Mengamankan Akun Cloud
### 4.1 Tujuan
- Mengaktifkan MFA (Multi-Factor Authentication)
- Mengonfigurasi IAM (Identity and Access Management)
- Menerapkan prinsip least privilege

### 4.2 Langkah Kerja (AWS IAM)
1. Buka layanan IAM
2. Aktifkan MFA untuk akun root:
   - Klik pada nama akun Anda (kanan atas)
   - Pilih "Security Credentials"
   - Aktifkan MFA
   - Ikuti petunjuk untuk menyiapkan MFA
3. Buat pengguna IAM baru:
   - Buka IAM > Users > Add user
   - Beri nama pengguna
   - Pilih "Programmatic access" dan "AWS Management Console access"
   - Setel permission "Attach existing policies directly" > "ReadOnlyAccess"
   - Tambahkan tag opsional
   - Tinjau dan buat pengguna
   - Unduh kredensial (.csv)

### 4.3 Tugas
1. Jelaskan mengapa MFA penting untuk keamanan cloud
2. Buat laporan tentang kebijakan IAM yang Anda buat
3. Jelaskan prinsip least privilege dan penerapannya

## 5. Praktikum 3: Mengamankan Penyimpanan Cloud
### 5.1 Tujuan
- Mengonfigurasi bucket S3 yang aman
- Menerapkan enkripsi
- Mengatur kebijakan akses

### 5.2 Langkah Kerja (AWS S3)
1. Buka layanan S3
2. Buat bucket baru:
   - Klik "Create bucket"
   - Beri nama unik
   - Pilih region terdekat
   - Nonaktifkan "Block all public access" (untuk keperluan praktikum)
   - Aktifkan enkripsi default (AES-256)
   - Buat bucket
3. Unggah file contoh
4. Konfigurasi bucket policy

### 5.3 Tugas
1. Uji akses ke file yang diunggah
2. Analisis pengaturan keamanan bucket
3. Jelaskan pentingnya enkripsi data di cloud

## 6. Praktikum 4: Monitoring dan Logging
### 6.1 Tujuan
- Mengaktifkan CloudTrail
- Menganalisis log aktivitas
- Menyiapkan alarm keamanan

### 6.2 Langkah Kerja (AWS CloudTrail)
1. Buka layanan CloudTrail
2. Buat trail baru:
   - Klik "Create trail"
   - Beri nama
   - Pilih "Apply trail to all regions"
   - Buat bucket S3 baru untuk log
   - Aktifkan log file validation
   - Buat trail
3. Lihat event history

### 6.3 Tugas
1. Jelaskan aktivitas yang terekam di CloudTrail
2. Buat alarm sederhana untuk aktivitas mencurigakan
3. Analisis pentingnya logging di cloud

## 7. Praktikum 5: Analisis Keamanan Cloud
### 7.1 Tujuan
- Menggunakan alat analisis keamanan
- Mengidentifikasi konfigurasi yang tidak aman
- Menerapkan perbaikan

### 7.2 Langkah Kerja (AWS Security Hub)
1. Buka AWS Security Hub
2. Aktifkan Security Hub (jika belum aktif)
3. Tinjau temuan keamanan
4. Analisis rekomendasi

### 7.3 Tugas
1. Identifikasi 3 temuan keamanan kritis
2. Jelaskan risiko dari temuan tersebut
3. Rekomendasikan langkah perbaikan

## 8. Penyusunan Laporan
### 8.1 Format Laporan
1. Halaman Judul
2. Daftar Isi
3. Pendahuluan
4. Metodologi
5. Hasil dan Analisis
6. Kesimpulan
7. Lampiran (screenshot, konfigurasi, dll)

### 8.2 Aspek yang Dinilai
- Kelengkapan laporan
- Kedalaman analisis
- Kesesuaian dengan praktik terbaik
- Kualitas dokumentasi

## 9. Referensi
### Dokumen Resmi
1. **AWS Well-Architected Framework**
   https://aws.amazon.com/architecture/well-architected/

2. **Google Cloud Security Best Practices**
   https://cloud.google.com/security/best-practices

3. **Microsoft Azure Security Documentation**
   https://docs.microsoft.com/en-us/azure/security/

### Alat Bantu
1. **CloudSploit** - Pemindai konfigurasi cloud
   https://cloudsploit.com/

2. **Prowler** - Tool CLI untuk keamanan AWS
   https://github.com/toniblyx/prowler

3. **Scout Suite** - Alat audit keamanan multi-cloud
   https://github.com/nccgroup/ScoutSuite

### Sumber Belajar
1. **Cloud Security Alliance (CSA)**
   https://cloudsecurityalliance.org/

2. **OWASP Cloud Security**
   https://owasp.org/www-project-cloud-security/

3. **NIST Cloud Computing Security Reference Architecture**
   https://www.nist.gov/publications/nist-cloud-computing-security-reference-architecture

**Catatan**:
- Selalu ikuti praktik keamanan terbaik saat bekerja dengan layanan cloud
- Pastikan untuk menghapus sumber daya yang tidak digunakan untuk menghindari biaya tak terduga
- Dokumentasikan semua perubahan konfigurasi dengan baik

**Versi Dokumen**: 1.0  
**Terakhir Diperbarui**: 8 Juli 2025  
**Penulis**: Tim Pengembang Kurikulum Keamanan Jaringan

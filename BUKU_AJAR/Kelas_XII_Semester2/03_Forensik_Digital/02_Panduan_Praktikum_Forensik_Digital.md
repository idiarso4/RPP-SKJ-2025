# Panduan Praktikum Forensik Digital

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Persiapan Lingkungan Praktikum](#persiapan-lingkungan)
3. [Praktikum 1: Akuisisi Bukti Digital](#praktikum-1)
4. [Praktikum 2: Analisis File System](#praktikum-2)
5. [Praktikum 3: Analisis Memori](#praktikum-3)
6. [Praktikum 4: Analisis Jaringan](#praktikum-4)
7. [Praktikum 5: Mobile Forensik Dasar](#praktikum-5)
8. [Penyusunan Laporan](#penyusunan-laporan)
9. [Referensi](#referensi)

## 1. Pendahuluan
Panduan praktikum ini dirancang untuk memberikan pengalaman langsung dalam melakukan investigasi forensik digital. Praktikum ini meliputi akuisisi bukti digital, analisis file system, analisis memori, analisis jaringan, dan dasar-dasar mobile forensik.

## 2. Persiapan Lingkungan Praktikum
### 2.1 Perangkat Keras yang Dibutuhkan
- Komputer dengan spesifikasi minimal:
  - Prosesor: Intel Core i5 atau setara
  - RAM: 8GB (disarankan 16GB)
  - Penyimpanan: SSD 256GB + HDD 1TB (untuk penyimpanan bukti)
  - Port USB 3.0
- Write blocker hardware
- Perangkat mobile (opsional)
- Flashdisk/HDD eksternal

### 2.2 Perangkat Lunak yang Dibutuhkan
- Sistem Operasi: Windows 10/11 dan Linux (disarankan menggunakan Kali Linux atau SIFT Workstation)
- VirtualBox/VMware Workstation
- Alat forensik digital:
  - FTK Imager
  - Autopsy
  - Wireshark
  - Volatility
  - Cellebrite Reader (versi gratis)

### 2.3 Persiapan Awal
1. Instal VirtualBox/VMware Workstation
2. Unduh dan instal SIFT Workstation
3. Siapkan direktori kerja untuk penyimpanan bukti
4. Siapkan perangkat write blocker

## 3. Praktikum 1: Akuisisi Bukti Digital
### 3.1 Tujuan
- Memahami prinsip akuisisi bukti digital
- Mampu menggunakan FTK Imager untuk membuat image disk
- Memvalidasi integritas image yang dibuat

### 3.2 Alat yang Digunakan
- FTK Imager
- HashCalc

### 3.3 Langkah Kerja
1. Hubungkan media penyimpanan target ke komputer melalui write blocker
2. Buka FTK Imager
3. Buat image disk dari media target
4. Hitung hash MD5/SHA-1 dari image yang dihasilkan
5. Bandingkan hash sebelum dan sesudah akuisisi
6. Dokumentasikan seluruh proses

### 3.4 Evaluasi
- Bandingkan hasil hash
- Analisis perbedaan jika ada
- Buat laporan singkat

## 4. Praktikum 2: Analisis File System
### 4.1 Tujuan
- Menganalisis file system menggunakan Autopsy
- Mengidentifikasi file-file penting
- Memulihkan file yang terhapus

### 4.2 Alat yang Digunakan
- Autopsy
- PhotoRec (opsional)

### 4.3 Langkah Kerja
1. Buka Autopsy
2. Buat kasus baru atau buka kasus yang ada
3. Tambahkan image disk yang telah dibuat sebelumnya
4. Lakukan analisis otomatis
5. Identifikasi file-file mencurigakan
6. Coba pulihkan file yang terhapus
7. Ekspor hasil analisis

## 5. Praktikum 3: Analisis Memori
### 5.1 Tujuan
- Menganalisis memory dump
- Mengidentifikasi proses yang mencurigakan
- Mengekstrak informasi penting dari memori

### 5.2 Alat yang Digunakan
- Volatility Framework
- Redline (opsional)

### 5.3 Langkah Kerja
1. Dapatkan sampel memory dump
2. Identifikasi profil sistem menggunakan Volatility
3. Analisis proses yang berjalan
4. Identifikasi koneksi jaringan
5. Cari artifact seperti password atau kredensial
6. Ekspor hasil analisis

## 6. Praktikum 4: Analisis Jaringan
### 6.1 Tujuan
- Menganalisis lalu lintas jaringan
- Mengidentifikasi serangan jaringan
- Mengekstrak file dari lalu lintas jaringan

### 6.2 Alat yang Digunakan
- Wireshark
- NetworkMiner

### 6.3 Langkah Kerja
1. Tangkap lalu lintas jaringan menggunakan Wireshark
2. Analisis protokol yang digunakan
3. Identifikasi paket mencurigakan
4. Ekstrak file dari lalu lintas jaringan
5. Analisis file yang diekstrak

## 7. Praktikum 5: Mobile Forensik Dasar
### 7.1 Tujuan
- Memahami dasar-dasar mobile forensik
- Mengekstrak data dari perangkat mobile
- Menganalisis data yang diekstrak

### 7.2 Alat yang Digunakan
- Cellebrite Reader
- ADB (Android Debug Bridge)
- SQLite Browser

### 7.3 Langkah Kerja
1. Hubungkan perangkat mobile ke komputer
2. Backup data menggunakan ADB
3. Analisis backup menggunakan Cellebrite Reader
4. Ekspor data kontak, pesan, dan log panggilan
5. Analisis database SQLite

## 8. Penyusunan Laporan
### 8.1 Format Laporan
1. Halaman Judul
2. Daftar Isi
3. Pendahuluan
4. Metodologi
5. Hasil dan Analisis
6. Kesimpulan
7. Lampiran

### 8.2 Poin Penting
- Gunakan bahasa yang jelas dan objektif
- Sertakan bukti pendukung (screenshot, log, dll)
- Jelaskan langkah-langkah yang dilakukan
- Analisis temuan dengan kritis

## 9. Referensi
1. **Buku**
   - "Practical Forensic Imaging" by Bruce Nikkel
   - "Windows Forensic Analysis Toolkit" by Harlan Carvey
   - "Android Forensics" by Andrew Hoog

2. **Sumber Online**
   - SANS Digital Forensics and Incident Response: https://www.sans.org/digital-forensics-incident-response/
   - DFIR Training & Resources: https://www.dfir.training/
   - Forensics Wiki: https://forensicswiki.xyz/

3. **Dokumen Resmi**
   - NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response
   - ACPO Good Practice Guide for Digital Evidence
   - ISO/IEC 27037: Guidelines for identification, collection, acquisition, and preservation of digital evidence

**Catatan**:
- Pastikan untuk selalu mematuhi hukum dan etika yang berlaku
- Dapatkan izin tertulis sebelum melakukan analisis pada sistem yang bukan milik Anda
- Dokumentasikan semua langkah yang dilakukan dengan baik

**Versi Dokumen**: 1.0  
**Terakhir Diperbarui**: 7 Juli 2025  
**Penulis**: Tim Pengembang Kurikulum Keamanan Jaringan

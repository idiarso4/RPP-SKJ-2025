# 📝 Asesmen: Keamanan Sistem Operasi

## 🎯 Kompetensi Dasar
3.12 Menerapkan prinsip keamanan sistem operasi
3.13 Melakukan hardening pada sistem operasi
3.14 Menganalisis keamanan sistem operasi

## 📝 Soal Pilihan Ganda

### 1. Manakah yang BUKAN termasuk dalam prinsip hardening sistem operasi?
   a) Menonaktifkan layanan yang tidak diperlukan  
   b) Mengupdate sistem secara berkala  
   c) Menggunakan akun root untuk semua aktivitas  
   d) Menerapkan prinsip least privilege  
   
   **Jawaban: c) Menggunakan akun root untuk semua aktivitas**  
   *Pembahasan: Menggunakan akun root untuk semua aktivitas adalah praktik yang buruk karena meningkatkan risiko keamanan. Sebaiknya gunakan akun biasa untuk aktivitas sehari-hari dan gunakan sudo/runas untuk tugas administratif.*

### 2. Manakah pernyataan yang BENAR tentang SELinux?
   a) SELinux adalah antivirus untuk Linux  
   b) SELinux mengontrol akses proses ke file dan port  
   c) SELinux hanya tersedia di Windows  
   d) SELinux memperlambat sistem secara signifikan  
   
   **Jawaban: b) SELinux mengontrol akses proses ke file dan port**  
   *Pembahasan: SELinux (Security-Enhanced Linux) adalah modul keamanan kernel Linux yang menyediakan mekanisme untuk mendukung kebijakan kontrol akses keamanan, termasuk kontrol akses wajib (MAC).*

### 3. Manakah yang BUKAN termasuk dalam komponen keamanan Windows?
   a) Windows Defender  
   b) BitLocker  
   c) AppArmor  
   d) User Account Control (UAC)  
   
   **Jawaban: c) AppArmor**  
   *Pembahasan: AppArmor adalah sistem kontrol akses wajib (MAC) yang digunakan di Linux, bukan di Windows. Windows memiliki komponen keamanan seperti Windows Defender, BitLocker, dan UAC.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara autentikasi dan otorisasi dalam konteks keamanan sistem operasi, serta berikan contoh implementasinya!

**Jawaban:**
**Autentikasi** adalah proses verifikasi identitas pengguna atau sistem yang mencoba mengakses sumber daya. Sedangkan **Otorisasi** adalah proses menentukan hak akses apa yang dimiliki oleh identitas yang sudah terautentikasi.

**Contoh Implementasi Autentikasi:**
1. **Linux**:
   - Autentikasi berbasis password di `/etc/shadow`
   - Autentikasi berbasis kunci SSH di `~/.ssh/authorized_keys`
   - PAM (Pluggable Authentication Modules) untuk autentikasi terintegrasi

2. **Windows**:
   - Autentikasi domain dengan Active Directory
   - Windows Hello untuk biometrik
   - Smart card authentication

**Contoh Implementasi Otorisasi:**
1. **Linux**:
   - Izin file dan direktori (rwx)
   - ACL (Access Control Lists) untuk izin yang lebih granular
   - Capabilities untuk memberikan hak spesifik ke proses

2. **Windows**:
   - NTFS permissions
   - Share permissions
   - Group Policy untuk mengatur hak akses terpusat

### 2. Jelaskan apa yang dimaksud dengan "prinsip defense in depth" dalam konteks keamanan sistem operasi, dan berikan contoh implementasinya!

**Jawaban:**
**Prinsip Defense in Depth** adalah pendekatan keamanan berlapis yang mengimplementasikan berbagai mekanisme pertahanan untuk melindungi sistem. Jika satu lapisan pertahanan ditembus, lapisan berikutnya akan memberikan perlindungan tambahan.

**Contoh Implementasi Defense in Depth di Sistem Operasi:**

1. **Lapisan Fisik**
   - BIOS/UEFI password
   - Full disk encryption (BitLocker, LUKS)
   - Secure boot

2. **Lapisan Sistem Operasi**
   - Patch management yang ketat
   - Least privilege principle
   - User Account Control (Windows) / sudo (Linux)

3. **Lapasan Aplikasi**
   - Application whitelisting
   - Software restriction policies
   - AppArmor/SELinux (Linux)

4. **Lapasan Data**
   - Enkripsi file sensitif
   - Data Loss Prevention (DLP)
   - Backup dan recovery

5. **Lapasan Monitoring**
   - Audit logging
   - Intrusion Detection System (IDS)
   - Security Information and Event Management (SIEM)

## 📝 Studi Kasus

### Kasus: Keamanan Server Web Perusahaan

**Latar Belakang:**
Sebuah perusahaan e-commerce ingin mengamankan server web mereka yang berjalan di Ubuntu Server 22.04 LTS. Server ini menyimpan data pelanggan dan transaksi yang sensitif. Sebagai administrator sistem, Anda diminta untuk melakukan hardening pada server tersebut.

**Spesifikasi Server:**
- OS: Ubuntu Server 22.04 LTS
- Layanan: Nginx, MySQL, PHP-FPM
- Aplikasi: Aplikasi e-commerce berbasis PHP
- Jaringan: Terhubung ke internet melalui firewall

**Pertanyaan:**
1. Langkah-langkah apa saja yang akan Anda lakukan untuk mengamankan server ini?
2. Bagaimana cara mengamankan layanan web (Nginx, PHP-FPM, MySQL)?
3. Apa yang akan Anda lakukan untuk memonitor dan mendeteksi serangan?
4. Bagaimana strategi backup yang akan Anda terapkan?

**Jawaban Contoh:**

1. **Langkah Hardening Dasar:**
   - Update sistem dan paket ke versi terbaru
   - Konfigurasi firewall (UFW) untuk hanya mengizinkan port yang diperlukan (22, 80, 443)
   - Nonaktifkan root login via SSH
   - Aktifkan fail2ban untuk mencegah brute force
   - Konfigurasi automatic security updates
   - Pasang dan konfigurasi auditd untuk logging

2. **Pengamanan Layanan:**
   **Nginx:**
   - Hapus header server version
   - Aktifkan HTTPS dengan konfigurasi TLS yang aman
   - Batasi metode HTTP yang diizinkan (GET, POST, HEAD)
   - Aktifkan mod_security atau NAXSI WAF
   
   **PHP-FPM:**
   - Gunakan versi PHP terbaru
   - Nonaktifkan fungsi-fungsi berbahaya di php.ini
   - Aktifkan open_basedir
   - Atur upload_max_filesize dan post_max_size yang wajar
   
   **MySQL:**
   - Jalankan mysql_secure_installation
   - Hapus database dan user default
   - Batasi akses MySQL hanya dari localhost
   - Aktifkan binary logging untuk audit

3. **Monitoring dan Deteksi:**
   - Pasang dan konfigurasi OSSEC HIDS
   - Aktifkan log monitoring dengan logwatch atau logrotate
   - Setup alert untuk aktivitas mencurigakan
   - Gunakan fail2ban untuk memblokir IP yang mencurigakan
   - Monitor resource usage (CPU, memory, disk, network)

4. **Strategi Backup 3-2-1:**
   - **3** salinan data (1 utama, 2 backup)
   - **2** media penyimpanan berbeda (contoh: hard drive dan cloud)
   - **1** backup disimpan offsite
   
   **Implementasi:**
   - Backup harian database dengan mysqldump
   - Backup mingguan full system dengan BorgBackup
   - Enkripsi backup sebelum dikirim ke penyimpanan cloud
   - Simpan backup di lokasi fisik yang berbeda
   - Uji proses restore secara berkala

## 📝 Tugas Praktik

### Instruksi:
1. Lakukan audit keamanan pada sistem Linux menggunakan Lynis
2. Analisis hasil audit dan buat laporan yang berisi:
   - Ringkasan temuan
   - Tingkat keparahan setiap temuan
   - Rekomendasi perbaikan
   - Langkah-langkah mitigasi

### Langkah Kerja:
```bash
# Install Lynis
sudo apt update
sudo apt install lynis -y

# Jalankan audit keamanan
sudo lynis audit system --cronjob

# Hasil audit akan tersimpan di /var/log/lynis.log
# Laporan detail ada di /var/log/lynis-report.dat
```

### Format Laporan:
1. **Informasi Sistem**
   - Nama host
   - Versi OS
   - Waktu audit

2. **Ringkasan Temuan**
   | No | Kategori | Jumlah Temuan | Tingkat Keparahan |
   |----|----------|---------------|-------------------|
   | 1  | Authentication | 3 | Medium |
   | 2  | Network | 5 | High |
   | 3  | Storage | 2 | Low |

3. **Detail Temuan Penting**
   ```
   [ID] WEAK-123: Deskripsi masalah
   - Tingkat: High
   - Dampak: Penjelasan dampak keamanan
   - Rekomendasi: Langkah perbaikan
   - Referensi: Link atau dokumen pendukung
   ```

4. **Rekomendasi Keseluruhan**
   - Prioritas tinggi yang harus segera ditangani
   - Perbaikan jangka menengah
   - Saran peningkatan keamanan

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kelengkapan Audit | 25% | Semua aspek penting tercakup |
| Analisis Temuan | 30% | Kedalaman analisis setiap temuan |
| Rekomendasi | 25% | Kualitas dan relevansi rekomendasi |
| Dokumentasi | 20% | Kerapian dan kejelasan laporan |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. c) Menggunakan akun root untuk semua aktivitas
2. b) SELinux mengontrol akses proses ke file dan port
3. c) AppArmor

### Pedoman Penskoran Esai
1. **Kelengkapan Jawaban** (40%): Semua poin penting tercakup
2. **Ketepatan Konsep** (30%): Penjelasan konsep yang akurat
3. **Contoh Implementasi** (20%): Contoh yang diberikan relevan dan aplikatif
4. **Struktur Jawaban** (10%): Sistematika penyampaian yang baik

## 📚 Referensi
1. CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
2. NIST SP 800-123: Guide to General Server Security
3. Ubuntu Security Documentation: https://ubuntu.com/security
4. Lynis Documentation: https://cisofy.com/lynis/
5. OWASP Secure Configuration Guide

---
<div align="center">
  <p>Dokumen Asesmen - Keamanan Sistem Operasi</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

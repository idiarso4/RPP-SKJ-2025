# Panduan Praktikum Etika Hacking

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Persiapan Lingkungan Praktikum](#persiapan-lingkungan)
3. [Praktikum 1: Pengenalan Kali Linux](#praktikum-1)
4. [Praktikum 2: Footprinting dan Reconnaissance](#praktikum-2)
5. [Praktikum 3: Scanning Jaringan](#praktikum-3)
6. [Praktikum 4: Vulnerability Assessment](#praktikum-4)
7. [Praktikum 5: Pelaporan Keamanan](#praktikum-5)
8. [Penyusunan Laporan](#penyusunan-laporan)
9. [Referensi](#referensi)

## 1. Pendahuluan
Panduan praktikum ini dirancang untuk memberikan pengalaman langsung dalam melakukan aktivitas ethical hacking yang legal dan bertanggung jawab. Praktikum ini mencakup pengumpulan informasi, analisis kerentanan, dan pelaporan temuan keamanan.

## 2. Persiapan Lingkungan Praktikum
### 2.1 Persyaratan Sistem
- Komputer dengan spesifikasi minimal:
  - Prosesor 64-bit
  - 8GB RAM (disarankan 16GB)
  - 100GB ruang disk bebas
  - Koneksi internet

### 2.2 Instalasi Virtualisasi
1. Unduh dan instal **VirtualBox** terbaru:
   https://www.virtualbox.org/

2. Unduh image **Kali Linux** resmi:
   https://www.kali.org/get-kali/

3. Buat mesin virtual baru di VirtualBox:
   - Alokasikan minimal 4GB RAM
   - Buat virtual disk minimal 40GB
   - Pasang image Kali Linux

### 2.3 Lingkungan Target
Kami akan menggunakan **Metasploitable 2** sebagai lingkungan target yang aman untuk latihan:
1. Unduh Metasploitable 2:
   https://sourceforge.net/projects/metasploitable/
2. Ekstrak dan impor ke VirtualBox
3. Konfigurasi jaringan ke mode "Host-only"

## 3. Praktikum 1: Pengenalan Kali Linux
### 3.1 Tujuan
- Mengenal antarmuka Kali Linux
- Memahami tools dasar keamanan
- Menggunakan terminal Linux

### 3.2 Langkah Kerja
1. Boot mesin virtual Kali Linux
2. Login dengan kredensial default (kali/kali)
3. Buka terminal dan coba perintah dasar:
   ```bash
   # Update sistem
   sudo apt update && sudo apt upgrade -y
   
   # Periksa alamat IP
   ip a
   
   # Periksa koneksi jaringan
   ping google.com
   ```
4. Eksplorasi direktori penting:
   - /usr/share/wordlists/
   - /usr/share/nmap/scripts/
   - /usr/share/metasploit-framework/modules/

### 3.3 Tugas
1. Buat direktori kerja baru dengan nama "ethical_hacking"
2. Dokumentasikan 10 perintah Linux yang berguna untuk ethical hacking
3. Screenshot antarmuka Kali Linux Anda

## 4. Praktikum 2: Footprinting dan Reconnaissance
### 4.1 Tujuan
- Mengumpulkan informasi target
- Menggunakan tools pasif untuk reconnaissance
- Menganalisis hasil pengumpulan informasi

### 4.2 Langkah Kerja
1. Gunakan **whois** untuk informasi domain:
   ```bash
   whois example.com
   ```

2. Gunakan **theHarvester** untuk mengumpulkan email dan subdomain:
   ```bash
   theharvester -d example.com -b google
   ```

3. Gunakan **nmap** untuk deteksi OS dan layanan:
   ```bash
   nmap -sS -sV -O target-ip
   ```

### 4.3 Tugas
1. Kumpulkan informasi tentang domain yang ditentukan
2. Identifikasi layanan yang berjalan di target
3. Buat peta jaringan target

## 5. Praktikum 3: Scanning Jaringan
### 5.1 Tujuan
- Mengidentifikasi host aktif
- Memindai port dan layanan
- Menganalisis hasil pemindaian

### 5.2 Langkah Kerja
1. Gunakan **nmap** untuk pemindaian dasar:
   ```bash
   # Pemindaian cepat
   nmap -T4 -F target-ip
   
   # Pemindaian menyeluruh
   nmap -sS -sV -sC -A -p- target-ip
   ```

2. Gunakan **netcat** untuk koneksi manual ke layanan:
   ```bash
   nc -nv target-ip 80
   GET / HTTP/1.1
   Host: target-ip
   ```

### 5.3 Tugas
1. Identifikasi port terbuka di target
2. Analisis versi layanan yang rentan
3. Dokumentasikan temuan Anda

## 6. Praktikum 4: Vulnerability Assessment
### 6.1 Tujuan
- Mengidentifikasi kerentanan
- Mengeksploitasi kerentanan yang diketahui
- Mendokumentasikan temuan

### 6.2 Langkah Kerja
1. Gunakan **Nessus** atau **OpenVAS** untuk pemindaian kerentanan
2. Analisis hasil pemindaian
3. Verifikasi kerentanan dengan **Metasploit Framework**:
   ```bash
   msfconsole
   search [nama_kerentanan]
   use [exploit_path]
   set RHOSTS target-ip
   exploit
   ```

### 6.3 Tugas
1. Identifikasi 3 kerentanan kritis
2. Verifikasi kerentanan dengan aman
3. Dokumentasikan langkah-langkah reproduksi

## 7. Praktikum 5: Pelaporan Keamanan
### 7.1 Tujuan
- Membuat laporan keamanan yang jelas
- Memberikan rekomendasi perbaikan
- Berkomunikasi temuan dengan baik

### 7.2 Langkah Kerja
1. Kumpulkan semua bukti:
   - Screenshot
   - Log
   - Output perintah

2. Analisis dampak:
   - Tingkat keparahan
   - Potensi eksploitasi
   - Dampak bisnis

3. Buat rekomendasi perbaikan

### 7.3 Tugas
Buat laporan keamanan yang mencakup:
1. Ringkasan Eksekutif
2. Metodologi
3. Temuan Detail
4. Bukti
5. Rekomendasi
6. Kesimpulan

## 8. Penyusunan Laporan
### 8.1 Format Laporan
1. Halaman Judul
2. Daftar Isi
3. Pendahuluan
4. Metodologi
5. Temuan dan Analisis
6. Rekomendasi
7. Lampiran (screenshot, log, dll.)

### 8.2 Aspek yang Dinilai
- Kelengkapan laporan
- Kedalaman analisis
- Kejelasan rekomendasi
- Kualitas dokumentasi

## 9. Referensi
### Buku Teks
1. "The Web Application Hacker's Handbook"
2. "Penetration Testing: A Hands-On Introduction to Hacking"
3. "The Hacker Playbook" series

### Sumber Online
1. **Hack The Box Academy**
   https://academy.hackthebox.com/

2. **TryHackMe**
   https://tryhackme.com/

3. **PortSwigger Web Security Academy**
   https://portswigger.net/web-security

### Tools yang Digunakan
1. **Kali Linux**
   https://www.kali.org/

2. **Metasploitable 2**
   https://sourceforge.net/projects/metasploitable/

3. **OWASP ZAP**
   https://www.zaproxy.org/

### Regulasi dan Etika
1. **Code of Ethics (EC-Council)**
   https://www.eccouncil.org/code-ethics/

2. **Responsible Disclosure Guidelines**
   https://www.cert.org/vulnerability-analysis/vul-disclosure.cfm

**Peringatan Penting**:
- Lakukan praktikum HANYA pada lingkungan yang Anda miliki atau memiliki izin
- Selalu dapatkan persetujuan tertulis sebelum melakukan pengujian
- Dokumentasikan SEMUA aktivitas yang dilakukan
- Laporkan kerentanan yang ditemukan dengan bertanggung jawab

**Versi Dokumen**: 1.0  
**Terakhir Diperbarui**: 8 Juli 2025  
**Penulis**: Tim Pengembang Kurikulum Keamanan Jaringan

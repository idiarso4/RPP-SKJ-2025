# Modul 1: Pengantar Keamanan Jaringan

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Mengapa Keamanan Jaringan Penting?](#mengapa-keamanan-jaringan-penting)
3. [Konsep Dasar Keamanan Jaringan](#konsep-dasar-keamanan-jaringan)
4. [Ancaman Keamanan Jaringan](#ancaman-keamanan-jaringan)
5. [Alat Dasar Keamanan Jaringan](#alat-dasar-keamanan-jaringan)
6. [Studi Kasus Sederhana](#studi-kasus-sederhana)
7. [Ringkasan](#ringkasan)
8. [Latihan dan Tugas](#latihan-dan-tugas)
9. [Referensi](#referensi)

## 1. Pendahuluan
Selamat datang di modul Pengantar Keamanan Jaringan! Di modul ini, kita akan mempelajari dasar-dasar keamanan jaringan yang sangat penting di era digital seperti sekarang.

## 2. Mengapa Keamanan Jaringan Penting?
- Perlindungan data pribadi dan bisnis
- Mencegah serangan siber
- Memastikan ketersediaan layanan
- Mematuhi peraturan yang berlaku

## 3. Konsep Dasar Keamanan Jaringan
### 3.1 CIA Triad
- **Kerahasiaan (Confidentiality)**: Memastikan informasi hanya dapat diakses oleh yang berwenang
- **Integritas (Integrity)**: Menjaga keakuratan dan konsistensi data
- **Ketersediaan (Availability)**: Memastikan data dan sistem dapat diakses saat dibutuhkan

### 3.2 Autentikasi dan Otorisasi
- Perbedaan antara autentikasi dan otorisasi
- Contoh sederhana dalam kehidupan sehari-hari

## 4. Ancaman Keamanan Jaringan
### 4.1 Jenis Ancaman
- Malware (Virus, Worm, Trojan)
- Phishing
- Serangan Denial of Service (DoS)
- Man-in-the-Middle (MitM)

### 4.2 Contoh Kasus Terkini (2023-2025)
1. **Kebocoran Data BPJS Kesehatan 2023**
   - 279 juta data warga Indonesia diduga bocor
   - Jenis data: NIK, nomor BPJS, alamat, dll.
   - Sumber: Kerentanan pada API
   
2. **Serangan Ransomware pada BUMN 2024**
   - Perusahaan pelayaran nasional menjadi korban
   - Dampak: Gangguan operasional selama 3 hari
   - Tebusan diminta dalam bentuk kripto senilai 1,5 juta USD

3. **Statistik Serangan Siber di Indonesia (BSSN 2024)**
   - Rata-rata 1,2 miliar ancaman siber per hari
   - 65% serangan menyasar sektor pemerintahan
   - Kenaikan 47% serangan ransomware dibanding tahun sebelumnya

## 5. Alat Dasar Keamanan Jaringan
### 5.1 Firewall
- **Definisi**: Sistem keamanan yang memantau dan mengontrol lalu lintas jaringan
- **Cara Kerja**:
  - Memfilter paket data berdasarkan aturan keamanan
  - Mencegah akses tidak sah ke/dari jaringan privat
- **Contoh Implementasi**:
  - **pfSense**: Firewall open source berbasis FreeBSD
  - **UFW (Uncomplicated Firewall)**: Untuk sistem berbasis Linux
  - **Windows Defender Firewall**: Bawaan sistem operasi Windows

### 5.2 Software Antivirus/Antimalware
- **Cara Kerja**:
  - Pemindaian berbasis signature
  - Analisis perilaku (behavioral analysis)
  - Perlindungan real-time
- **Contoh Solusi**:
  - **ClamAV**: Antivirus open source
  - **Malwarebytes**: Untuk deteksi dan penghapusan malware
  - **Windows Defender**: Bawaan Windows 10/11

### 5.3 Alat Pemantauan Jaringan
- **Wireshark 4.0.6**: Analisis protokol jaringan
- **Nmap 7.94**: Pemindaian port dan jaringan
- **Nagios**: Pemantauan infrastruktur TI

### 5.4 Alat Keamanan Tambahan
- **OpenVAS**: Pemindai kerentanan open source
- **Snort**: Sistem deteksi intrusi (IDS)
- **Metasploit Framework**: Pengujian penetrasi
- Tips memilih antivirus yang baik

## 6. Studi Kasus Sederhana
### Kasus: Serangan Ransomware pada Sekolah
- Kronologi kejadian
- Analisis penyebab
- Langkah pencegahan

## 7. Ringkasan
- Poin-poin penting yang telah dipelajari
- Kaitan dengan modul selanjutnya

## 8. Latihan dan Tugas
### Latihan Individu
1. Identifikasi perangkat keamanan jaringan di sekitar Anda
2. Buat daftar 5 ancaman keamanan jaringan yang pernah Anda dengar
3. Jelaskan perbedaan antara virus, worm, dan trojan

### Tugas Kelompok
1. Buat presentasi tentang salah satu ancaman keamanan jaringan
2. Lakukan wawancara dengan tenaga IT di sekolah tentang praktik keamanan jaringan
3. Buat poster tentang tips keamanan berinternet

## 9. Referensi
1. **Dokumen Resmi**
   - BSSN. (2024). Laporan Tahunan Keamanan Siber Indonesia 2023
   - Kementerian Kominfo. (2023). Panduan Keamanan Siber untuk Pendidikan Vokasi
   - Peraturan BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi

2. **Sumber Internasional**
   - Cisco. (2024). Cybersecurity Threat Trends Report
   - NIST. (2023). Cybersecurity Framework (CSF) 2.0
   - ISO/IEC 27001:2022 - Information security management systems

3. **Sumber Pembelajaran**
   - Cisco Networking Academy. (2024). Introduction to Cybersecurity
   - TryHackMe. (2024). Introduction to Cybersecurity
   - BSSN. (2024). Panduan Praktis Keamanan Jaringan untuk Pemula

4. **Sumber Online**
   - BSSN: https://bssn.go.id
   - ID-SIRTII: https://idsirtii.or.id
   - CISA Alerts: https://www.cisa.gov/uscert/ncas/alerts

**Catatan Versi**:
- Versi Dokumen: 1.1
- Terakhir Diperbarui: 7 Juli 2025
- Penulis: Tim Pengembang Kurikulum Keamanan Jaringan

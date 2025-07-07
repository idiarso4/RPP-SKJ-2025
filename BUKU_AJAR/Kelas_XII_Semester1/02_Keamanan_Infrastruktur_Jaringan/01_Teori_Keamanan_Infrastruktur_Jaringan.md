# Modul 2: Keamanan Infrastruktur Jaringan

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Konsep Dasar Infrastruktur Jaringan](#konsep-dasar)
3. [Komponen Kritis Infrastruktur Jaringan](#komponen-kritis)
4. [Ancaman dan Kerentanan](#ancaman-dan-kerentanan)
5. [Strategi Pengamanan](#strategi-pengamanan)
6. [Alat dan Teknologi](#alat-dan-teknologi)
7. [Studi Kasus](#studi-kasus)
8. [Best Practices](#best-practices)
9. [Latihan dan Tugas](#latihan-dan-tugas)
10. [Referensi](#referensi)

## 1. Pendahuluan
Infrastruktur jaringan adalah tulang punggung operasional organisasi modern. Modul ini membahas prinsip, ancaman, dan praktik terbaik dalam mengamankan infrastruktur jaringan untuk memastikan ketersediaan, integritas, dan kerahasiaan layanan TI.

## 2. Konsep Dasar Infrastruktur Jaringan
### 2.1 Arsitektur Jaringan Modern
- Arsitektur tradisional vs. perbatasan yang kabur (blurred perimeter)
- Konsep Zero Trust Architecture (ZTA)
- Software-Defined Networking (SDN) dan keamanannya

### 2.2 Komponen Utama
- Perangkat jaringan (router, switch, firewall)
- Sistem operasi jaringan
- Protokol dan layanan jaringan
- Infrastruktur kunci publik (PKI)

## 3. Komponen Kritis Infrastruktur Jaringan
### 3.1 Perimeter Jaringan
- Firewall generasi terbaru (NGFW)
- Sistem Pencegahan/Deteksi Intrusi (IPS/IDS)
- Gerbang Keamanan Web (Secure Web Gateway)

### 3.2 Jaringan Inti
- Segmentasi jaringan (mikrosegmentasi)
- Virtualisasi fungsi jaringan (NFV)
- Jaringan overlay dan underlay

### 3.3 Akses Jaringan
- Network Access Control (NAC)
- 802.1X Authentication
- Zero Trust Network Access (ZTNA)

## 4. Ancaman dan Kerentanan
### 4.1 Ancaman Umum
- Serangan DDoS (Distributed Denial of Service)
- Man-in-the-Middle (MitM) attacks
- Eksploitasi kerentanan perangkat
- Serangan terhadap protokol routing

### 4.2 Kerentanan Khusus
- Konfigurasi yang tidak aman
- Perangkat dengan kredensial default
- Protokol jaringan yang tidak terenkripsi
- Perangkat IoT yang rentan

## 5. Strategi Pengamanan
### 5.1 Pertahanan Berlapis
- Defense in Depth (DiD)
- Pemisahan tugas dan privilege
- Pemantauan dan logging terpusat

### 5.2 Hardening Jaringan
- Konfigurasi aman untuk perangkat jaringan
- Pemutakhiran dan patch keamanan
- Penonaktifan layanan yang tidak perlu

## 6. Alat dan Teknologi
### 6.1 Alat Pemantauan
- Wireshark untuk analisis lalu lintas
- SolarWinds Network Performance Monitor
- PRTG Network Monitor

### 6.2 Alat Keamanan
- Snort (IDS/IPS open source)
- Nmap untuk pemindaian jaringan
- OpenVAS untuk pemindaian kerentanan

## 7. Studi Kasus
### 7.1 Serangan pada Penyedia Layanan Kesehatan (2024)
- **Gambaran**: Serangan ransomware mengganggu layanan rumah sakit
- **Analisis**: Eksploitasi VPN yang tidak dipatch
- **Dampak**: Gangguan layanan selama 72 jam
- **Pelajaran**: Pentingnya patch keamanan dan rencana pemulihan bencana

### 7.2 Kebocoran Data melalui Perangkat IoT (2023)
- **Gambaran**: Perangkat keamanan IoT yang tidak aman menjadi pintu masuk peretas
- **Analisis**: Kredensial default dan firmware usang
- **Dampak**: Kebocoran data sensitif pelanggan
- **Pelajaran**: Keamanan perangkat IoT dan segmentasi jaringan

## 8. Best Practices
### 8.1 Manajemen Konfigurasi
- Dokumentasi konfigurasi
- Pengendalian perubahan (change management)
- Backup konfigurasi rutin

### 8.2 Pemantauan dan Respons
- SIEM (Security Information and Event Management)
- Analisis perilaku jaringan (Network Behavior Analysis)
- Rencana respons insiden

## 9. Latihan dan Tugas
### Latihan Individu
1. Lakukan pemindaian jaringan menggunakan Nmap
2. Analisis log firewall untuk aktivitas mencurigakan
3. Buat dokumentasi konfigurasi perangkat jaringan

### Tugas Kelompok
1. Rancang arsitektur jaringan yang aman untuk sekolah menengah
2. Lakukan penilaian risiko untuk infrastruktur jaringan yang ada
3. Presentasikan temuan dan rekomendasi peningkatan keamanan

## 10. Referensi
### Standar dan Kerangka Kerja
1. **NIST SP 800-53** - Security and Privacy Controls for Information Systems and Organizations
2. **ISO/IEC 27033** - IT Security Techniques - Network Security
3. **CIS Controls** - Critical Security Controls for Effective Cyber Defense

### Regulasi Indonesia
1. Peraturan BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi
2. Peraturan Menteri Kominfo No. 20 Tahun 2021 tentang Penyelenggara Sistem Elektronik
3. Standar SNI ISO/IEC 27001:2022 - Sistem Manajemen Keamanan Informasi

### Sumber Pembelajaran
1. **Buku**
   - "Network Security Essentials" by William Stallings
   - "Zero Trust Networks" by Evan Gilman and Doug Barth
   - "CISSP All-in-One Exam Guide" by Shon Harris

2. **Kursus Online**
   - [Cisco Networking Academy] Cybersecurity Essentials
   - [Pluralsight] Network Security Architecture
   - [BSSN] Pelatihan Keamanan Jaringan Tingkat Lanjut

**Catatan Versi**:
- Versi Dokumen: 1.0
- Terakhir Diperbarui: 7 Juli 2025
- Penulis: Tim Pengembang Kurikulum Keamanan Jaringan

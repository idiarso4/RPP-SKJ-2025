# Modul 1: Keamanan Aplikasi Web

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Konsep Dasar Keamanan Aplikasi Web](#konsep-dasar-keamanan-aplikasi-web)
3. [Kerentanan Umum Aplikasi Web](#kerentanan-umum-aplikasi-web)
4. [Teknik Pengujian Keamanan](#teknik-pengujian-keamanan)
5. [Praktik Pengembangan yang Aman](#praktik-pengembangan-yang-aman)
6. [Studi Kasus](#studi-kasus)
7. [Ringkasan](#ringkasan)
8. [Latihan dan Tugas](#latihan-dan-tugas)
9. [Referensi](#referensi)

## 1. Pendahuluan
Keamanan aplikasi web adalah aspek kritis dalam pengembangan perangkat lunak modern. Modul ini akan membahas konsep dasar, kerentanan umum, dan praktik terbaik dalam pengembangan aplikasi web yang aman.

## 2. Konsep Dasar Keamanan Aplikasi Web
- Prinsip dasar keamanan informasi (CIA Triad)
  - Kerahasiaan (Confidentiality)
  - Integritas (Integrity)
  - Ketersediaan (Availability)
- Model ancaman terkini:
  - STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)
  - DREAD (Damage, Reproducibility, Exploitability, Affected Users, Discoverability)
- Siklus hidup pengembangan perangkat lunak aman (Secure SDLC)
- OWASP Top 10:2021 (Perubahan dari versi 2017)
- Regulasi terkait di Indonesia:
  - UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi
  - Peraturan Menteri Kominfo No. 20 Tahun 2016 tentang Perlindungan Data Pribadi

## 3. Kerentanan Umum Aplikasi Web
### 3.1 Injeksi (Injection)
- SQL Injection
- Command Injection
- LDAP Injection

### 3.2 Autentikasi yang Rusak
- Serangan brute force
- Manajemen sesi yang tidak aman
- Masalah kredensial default

### 3.3 Cross-Site Scripting (XSS)
- Reflected XSS
- Stored XSS
- DOM-based XSS

## 4. Teknik Pengujian Keamanan
### 4.1 Pengujian Keamanan Aplikasi Web
- Pengujian penetrasi
- Pemindaian kerentanan
- Code review keamanan

### 4.2 Alat Bantu Keamanan Aplikasi Web
1. **OWASP ZAP (Zed Attack Proxy) 2.12.0**
   - Alat open source untuk pengujian keamanan aplikasi web
   - Fitur: Automated scanner, Intercepting proxy, Fuzzer
   - Situs resmi: [owasp.org/zap](https://www.zaproxy.org/)

2. **Burp Suite Community Edition**
   - Alat pengujian keamanan aplikasi web yang komprehensif
   - Fitur: Web vulnerability scanner, Intruder, Repeater
   - Situs resmi: [portswigger.net](https://portswigger.net/burp/communitydownload)

3. **Nmap 7.92**
   - Alat pemindaian jaringan sumber terbuka
   - Berguna untuk enumerasi dan pengujian keamanan
   - Situs resmi: [nmap.org](https://nmap.org/)

4. **Alternatif Lain**
   - **Nikto**: Pemindai keamanan web otomatis
   - **SQLMap**: Alat otomatis untuk mendeteksi dan mengeksploitasi kerentanan SQL injection
   - **WPScan**: Pemindai keamanan khusus WordPress

## 5. Praktik Pengembangan yang Aman
### 5.1 Input Validation
- Whitelist vs Blacklist
- Sanitasi input
- Output encoding

### 5.2 Manajemen Sesi yang Aman
- Pembuatan token CSRF
- Cookie security flags
- Session timeout

## 6. Studi Kasus
### 6.1 Kasus Kebocoran Data
- Analisis penyebab
- Dampak yang ditimbulkan
- Pelajaran yang didapat

## 7. Ringkasan
- Poin-poin penting yang telah dipelajari
- Keterkaitan dengan modul lainnya
- Persiapan untuk modul selanjutnya

## 8. Latihan dan Tugas
### Latihan Individu
1. Identifikasi kerentanan pada kode yang diberikan
2. Lakukan pengujian keamanan dasar pada aplikasi web sederhana
3. Analisis laporan keamanan aplikasi web terbuka

### Tugas Kelompok
1. Buat aplikasi web sederhana dengan menerapkan prinsip keamanan yang telah dipelajari
2. Lakukan pengujian keamanan pada aplikasi web yang dibuat
3. Buat laporan hasil pengujian dan rekomendasi perbaikan

## 9. Referensi
1. **Standar Internasional**
   - OWASP Foundation. (2021). OWASP Top 10:2021. [Link](https://owasp.org/Top10/)
   - NIST. (2021). Secure Software Development Framework (SSDF) Version 1.1. [Link](https://csrc.nist.gov/Projects/ssdf)
   - ISO/IEC 27034-1:2011 - Information technology — Security techniques — Application security

2. **Regulasi Indonesia**
   - Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi
   - Peraturan Menteri Kominfo No. 20 Tahun 2016 tentang Perlindungan Data Pribadi
   - Peraturan BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi

3. **Sumber Tambahan**
   - Web Application Security Consortium (WASC) Threat Classification
   - BSSN. (2023). Panduan Keamanan Aplikasi Web untuk Instansi Pemerintah
   - ID-SIRTII. (2023). Laporan Ancaman Siber Kuartal I 2023

4. **Alat dan Sumber Daya**
   - OWASP ZAP: https://www.zaproxy.org/
   - NIST National Vulnerability Database: https://nvd.nist.gov/
   - CVE Details: https://www.cvedetails.com/

**Catatan Versi**:
- Versi Dokumen: 1.0
- Terakhir Diperbarui: 7 Juli 2025
- Penulis: Tim Pengembang Kurikulum Keamanan Jaringan

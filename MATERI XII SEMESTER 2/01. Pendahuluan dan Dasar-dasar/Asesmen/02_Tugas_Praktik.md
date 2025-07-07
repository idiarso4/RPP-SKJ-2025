# 📋 Tugas Praktik - Analisis Keamanan Jaringan Dasar

## 🎯 Tujuan
Menguji kemampuan peserta didik dalam menerapkan konsep keamanan siber dasar menggunakan tools yang telah dipelajari.

## 📝 Deskripsi Tugas
Anda ditugaskan untuk melakukan analisis keamanan jaringan sederhana menggunakan tools yang telah dipelajari. Tugas ini mencakup pemindaian jaringan, analisis traffic, dan pelaporan temuan.

### 1. Lingkup Pekerjaan

#### 1.1 Target Analisis
- Jaringan lokal (milik sendiri atau yang diizinkan)
- Website demo/test (jika tersedia)
- Perangkat virtual (opsional)

#### 1.2 Tools yang Digunakan
1. Nmap
2. Wireshark
3. Tools tambahan (opsional):
   - Netcat
   - Tcpdump
   - Ping/Traceroute

### 2. Langkah Pengerjaan

#### 2.1 Pemetaan Jaringan (30%)
1. Lakukan pemindaian jaringan untuk mengidentifikasi perangkat yang terhubung
2. Identifikasi sistem operasi dan layanan yang berjalan
3. Buat peta jaringan sederhana

#### 2.2 Analisis Traffic (30%)
1. Capture traffic jaringan menggunakan Wireshark
2. Analisis protokol yang digunakan
3. Identifikasi potensi kerentanan

#### 2.3 Dokumentasi (40%)
1. Buat laporan lengkap
2. Sertakan bukti screenshot
3. Berikan rekomendasi pengamanan

### 3. Format Laporan

#### 3.1 Halaman Judul
- Nama Lengkap
- Kelas
- Tanggal Pengerjaan
- Nama Tugas

#### 3.2 Pendahuluan
- Latar belakang
- Tujuan
- Ruang lingkup

#### 3.3 Metodologi
- Tools yang digunakan
- Langkah-langkah kerja
- Parameter yang digunakan

#### 3.4 Hasil dan Analisis
1. **Pemetaan Jaringan**
   - Daftar perangkat yang ditemukan
   - Port dan layanan yang terbuka
   - Analisis keamanan

2. **Analisis Traffic**
   - Protokol yang terdeteksi
   - Potensi ancaman
   - Rekomendasi

#### 3.5 Kesimpulan dan Saran
- Ringkasan temuan
- Rekomendasi peningkatan keamanan
- Refleksi pembelajaran

### 4. Kriteria Penilaian

#### 4.1 Kualitas Analisis (40%)
- Kedalaman analisis
- Ketepatan identifikasi
- Relevansi temuan

#### 4.2 Dokumentasi (30%)
- Kelengkapan laporan
- Kejelasan penyajian
- Kualitas bukti

#### 4.3 Kreativitas (20%)
- Pendekatan analisis
- Solusi yang ditawarkan
- Inovasi dalam penyelesaian masalah

#### 4.4 Kepatuhan Waktu (10%)
- Ketepatan pengumpulan
- Kesesuaian dengan tenggat waktu

### 5. Contoh Tugas

#### 5.1 Contoh Perintah Nmap
```bash
# Scan jaringan dasar
nmap -sV 192.168.1.0/24

# Deteksi sistem operasi
nmap -O 192.168.1.1

# Scan port spesifik
nmap -p 80,443,22,3389 192.168.1.1
```

#### 5.2 Contoh Analisis Wireshark
1. Filter HTTP traffic: `http`
2. Filter DNS queries: `dns`
3. Filter by IP: `ip.addr == 192.168.1.1`

### 6. Panduan Pengumpulan
1. Format file: PDF
2. Nama file: `Tugas1_KeamananJaringan_Nama_Kelas.pdf`
3. Dikumpulkan melalui LMS
4. Batas waktu: 1 minggu

### 7. Referensi
1. Nmap Documentation: https://nmap.org/docs.html
2. Wireshark User Guide: https://www.wireshark.org/docs/
3. Diktat Keamanan Jaringan SMK

## 📌 Catatan Penting
1. Hanya lakukan pengujian pada jaringan yang Anda miliki atau yang telah diizinkan
2. Jangan melakukan aktivitas yang mengganggu layanan
3. Laporkan temuan dengan bertanggung jawab
4. Jaga kerahasiaan informasi sensitif

---
<div align="center">
  <p>Dokumen Tugas - Analisis Keamanan Jaringan Dasar</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

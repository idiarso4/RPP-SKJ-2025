# Network Address Translation (NAT)

## Pendahuluan

Network Address Translation (NAT) adalah teknik yang memungkinkan beberapa perangkat dalam jaringan lokal berbagi satu alamat IP publik untuk mengakses internet. Modul ini akan membahas konsep, jenis, dan implementasi NAT dalam jaringan komputer.

## Tujuan Pembelajaran

Setelah mempelajari materi ini, peserta didik diharapkan mampu:
1. Memahami konsep dan fungsi NAT
2. Mengenal berbagai tipe NAT
3. Mengkonfigurasi NAT pada perangkat jaringan
4. Menganalisis keuntungan dan keterbatasan NAT
5. Menerapkan NAT untuk keamanan jaringan

## Materi Pembelajaran

### 1. Konsep Dasar NAT
- Pengertian dan latar belakang NAT
- Keterbatasan alamat IPv4
- Cara kerja NAT
- Komponen NAT (Inside Local, Inside Global, Outside Local, Outside Global)

### 2. Jenis-jenis NAT
- **Static NAT**
  - One-to-One Mapping
  - Penggunaan untuk server yang dapat diakses dari internet

- **Dynamic NAT**
  - Pool of Public IPs
  - Many-to-Many Mapping

- **Port Address Translation (PAT) / NAT Overload**
  - Many-to-One Mapping
  - Port Multiplexing

- **Port Forwarding**
  - Penerusan port tertentu ke server internal
  - Konfigurasi untuk layanan seperti web server, game server, dll.

### 3. Keuntungan dan Kerugian NAT
**Keuntungan:**
- Penghematan alamat IP publik
- Peningkatan keamanan (menyembunyikan topologi jaringan internal)
- Fleksibilitas dalam pengelolaan jaringan

**Kerugian:**
- Kompleksitas dalam troubleshooting
- Beberapa protokol tidak kompatibel dengan NAT
- Potensi bottleneck kinerja
- Menyulitkan koneksi peer-to-peer

### 4. NAT dan Keamanan Jaringan
- NAT sebagai firewall dasar
- Kelemahan keamanan NAT
- Praktik terbaik pengamanan NAT

### 5. Implementasi NAT di Berbagai Perangkat
- NAT di Router MikroTik
- NAT di Cisco Router
- NAT di pfSense
- NAT di Windows Server

## Praktikum

### Praktikum 6.1: Konfigurasi NAT Dasar di MikroTik
1. Siapkan topologi jaringan sederhana
2. Konfigurasi NAT Overload (masquerade)
3. Uji koneksi internet dari jaringan lokal
4. Analisis lalu lintas jaringan

### Praktikum 6.2: Port Forwarding
1. Buat aturan port forwarding untuk web server
2. Uji akses dari jaringan eksternal
3. Analisis keamanan konfigurasi

## Latihan Soal

1. Jelaskan perbedaan antara Static NAT dan Dynamic NAT!
2. Mengapa NAT Overload (PAT) lebih efisien dibandingkan Dynamic NAT biasa?
3. Apa yang dimaksud dengan "port exhaustion" dalam konteks PAT?
4. Sebutkan 3 protokol yang mungkin bermasalah dengan NAT dan jelaskan alasannya!
5. Bagaimana cara mengkonfigurasi port forwarding untuk mengizinkan akses remote desktop ke komputer di belakang NAT?

## Referensi

1. Cisco. (2023). Configuring NAT on Cisco Devices.
2. MikroTik. (2023). NAT Documentation.
3. Comer, D. E. (2014). Computer Networks and Internets. Pearson Education.

## Tugas

Buatlah laporan praktikum yang mencakup:
1. Topologi jaringan yang digunakan
2. Langkah-langkah konfigurasi NAT
3. Screenshot konfigurasi dan pengujian
4. Analisis hasil pengujian
5. Kesimpulan dan saran perbaikan

Kumpulkan dalam format PDF maksimal 10 halaman.

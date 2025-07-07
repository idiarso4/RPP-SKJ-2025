# Firewall dan Keamanan Jaringan

## Pendahuluan

Firewall merupakan komponen penting dalam sistem keamanan jaringan yang berfungsi sebagai garis pertahanan pertama terhadap ancaman dari luar. Modul ini akan membahas konsep, jenis, dan implementasi firewall dalam keamanan jaringan.

## Tujuan Pembelajaran

Setelah mempelajari materi ini, peserta didik diharapkan mampu:
1. Memahami konsep dan fungsi firewall
2. Mengenal berbagai jenis firewall
3. Mengkonfigurasi firewall dasar
4. Menerapkan aturan firewall untuk mengamankan jaringan

## Materi Pembelajaran

### 1. Konsep Dasar Firewall
- Pengertian dan tujuan firewall
- Prinsip kerja firewall
- Keuntungan dan keterbatasan firewall
- Arsitektur firewall

### 2. Jenis-jenis Firewall
- **Berdasarkan Lapisan Kerja**
  - Packet Filtering Firewall
  - Stateful Inspection Firewall
  - Application-Level Gateway (Proxy)
  - Next-Generation Firewall (NGFW)

- **Berdasarkan Implementasi**
  - Hardware Firewall
  - Software Firewall
  - Cloud-based Firewall

### 3. Komponen Firewall
- Access Control Lists (ACLs)
- Network Address Translation (NAT)
- Port Forwarding
- Virtual Private Network (VPN)
- Intrusion Prevention System (IPS)

### 4. Aturan Firewall
- Default Policy
- Inbound Rules
- Outbound Rules
- Connection Tracking
- Logging dan Monitoring

### 5. Best Practices Konfigurasi Firewall
- Prinsip Least Privilege
- Default Deny Policy
- Regular Updates dan Patching
- Segmentasi Jaringan
- Audit dan Monitoring

## Praktikum

### Praktikum 5.1: Konfigurasi Windows Firewall
1. Aktifkan Windows Firewall
2. Buat aturan inbound dan outbound
3. Uji aturan yang telah dibuat
4. Analisis log firewall

### Praktikum 5.2: Implementasi Firewall dengan pfSense
1. Instalasi pfSense
2. Konfigurasi antarmuka jaringan
3. Buat aturan firewall dasar
4. Uji konektivitas dan keamanan

## Latihan Soal

1. Jelaskan perbedaan antara stateful dan stateless firewall!
2. Mengapa firewall tidak cukup untuk melindungi jaringan secara keseluruhan?
3. Apa yang dimaksud dengan default deny policy?
4. Sebutkan 3 parameter yang dapat digunakan dalam aturan firewall paket filtering!
5. Bagaimana cara kerja application-level gateway?

## Referensi

1. Zwicky, E. D., Cooper, S., & Chapman, D. B. (2000). Building Internet Firewalls. O'Reilly Media.
2. pfSense Documentation. (2023). https://docs.netgate.com/pfsense/en/latest/
3. Microsoft. (2023). Windows Firewall documentation.

## Tugas

Buatlah laporan yang berisi:
1. Analisis kebutuhan firewall untuk jaringan sekolah
2. Desain arsitektur firewall yang sesuai
3. Konfigurasi aturan firewall yang direkomendasikan
4. Prosedur pemantauan dan pemeliharaan
5. Rencana tanggap darurat jika terjadi pelanggaran keamanan

Kumpulkan dalam format PDF maksimal 15 halaman.

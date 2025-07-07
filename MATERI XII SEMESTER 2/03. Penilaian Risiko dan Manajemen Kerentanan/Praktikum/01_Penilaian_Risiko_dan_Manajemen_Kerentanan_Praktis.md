# 🛠️ Praktikum: Penilaian Risiko dan Manajemen Kerentanan Praktis

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Melakukan penilaian risiko keamanan informasi
2. Mengidentifikasi dan menilai kerentanan sistem
3. Menggunakan alat analisis risiko
4. Mengembangkan rencana mitigasi risiko
5. Membuat laporan penilaian risiko

## 📋 Persiapan

### 1. Persyaratan Sistem
- Sistem Operasi: Windows 10/11 atau Linux (disarankan Kali Linux)
- Tools: OpenVAS, Nmap, OWASP ZAP, Microsoft Excel/LibreOffice Calc
- Akses internet untuk mengunduh tools dan dokumentasi

### 2. Tools yang Digunakan
1. **OpenVAS** - Pemindaian kerentanan
2. **OWASP ZAP** - Pengujian keamanan aplikasi web
3. **Nmap** - Pemindaian jaringan dan port
4. **Dradis Community** - Dokumentasi pengujian keamanan
5. **Risk Assessment Matrix Template** - Template Excel untuk analisis risiko

## 📝 Langkah Kerja

### 1. Persiapan Lingkungan

#### 1.1 Instalasi OpenVAS (Kali Linux)
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Instal OpenVAS
sudo apt install gvm -y

# Inisialisasi OpenVAS
sudo gvm-setup

# Jalankan OpenVAS
sudo gvm-start

# Dapatkan kredensial login
sudo gvm-check-setup
```

#### 1.2 Konfigurasi Target
Buat daftar aset yang akan dinilai:
```
# Contoh daftar aset
1. Web Server (192.168.1.10)
   - IP: 192.168.1.10
   - OS: Ubuntu Server 20.04
   - Layanan: Apache, MySQL, PHP
   - Pemilik: Tim IT
   - Nilai: Tinggi

2. Database Server (192.168.1.20)
   - IP: 192.168.1.20
   - OS: Windows Server 2019
   - Layanan: Microsoft SQL Server
   - Pemilik: Tim Database
   - Nilai: Sangat Tinggi
```

### 2. Identifikasi Aset dan Ancaman

#### 2.1 Pemindaian Jaringan dengan Nmap
```bash
# Identifikasi host aktif
nmap -sn 192.168.1.0/24 -oN host_discovery.txt

# Pemindaian layanan
nmap -sV -sC -O -p- -T4 192.168.1.10 -oN web_scan.txt

# Deteksi kerentanan
nmap --script vuln 192.168.1.10 -oN vulnerability_scan.txt
```

#### 2.2 Analisis Hasil Pemindaian
Buat daftar temuan:
```markdown
## Hasil Pemindaian Web Server (192.168.1.10)

### Port Terbuka:
- 80/tcp  - HTTP (Apache 2.4.41)
- 22/tcp  - SSH (OpenSSH 8.2p1)
- 3306/tcp - MySQL 8.0.27

### Masalah Keamanan:
1. Apache 2.4.41 - Beberapa kerentanan yang diketahui
2. OpenSSH 8.2p1 - Perlu pembaruan keamanan
3. MySQL 8.0.27 - Konfigurasi default yang tidak aman
```

### 3. Penilaian Risiko

#### 3.1 Matriks Risiko
Buat matriks risiko di Excel/Calc:

| ID | Aset | Ancaman | Kemungkinan | Dampak | Risiko | Status |
|----|------|---------|-------------|--------|--------|--------|
| 1 | Web Server | Serangan DDoS | 3 | 4 | 12 | Open |
| 2 | Database | Kebocoran Data | 2 | 5 | 10 | Open |
| 3 | Aplikasi Web | SQL Injection | 4 | 5 | 20 | Open |

**Keterangan:**
- **Kemungkinan**: 1 (Sangat Rendah) - 5 (Sangat Tinggi)
- **Dampak**: 1 (Minim) - 5 (Kritis)
- **Risiko** = Kemungkinan × Dampak

#### 3.2 Analisis Dampak Bisnis (BIA)
```markdown
## Analisis Dampak Bisnis

### Aset: Web Server E-commerce
- **Fungsi Utama**: Menangani transaksi online
- **Waktu Pemulihan Maksimum (RTO)**: 4 jam
- **Titik Pemulihan Maksimum (RPO)**: 15 menit
- **Dampak Keuangan**: $10,000/jam downtime
- **Dampak Reputasi**: Tinggi
- **Dampak Hukum**: Kepatuhan PCI DSS
```

### 4. Mitigasi Risiko

#### 4.1 Rencana Mitigasi
Buat tabel rencana mitigasi:

| ID Risiko | Deskripsi | Tindakan Mitigasi | Tanggung Jawab | Tenggat Waktu | Status |
|-----------|-----------|-------------------|----------------|---------------|--------|
| 1 | Serangan DDoS | - Implementasi WAF<br>- Konfigurasi rate limiting | Tim Jaringan | 2 Minggu | On Progress |
| 2 | Kebocoran Data | - Enkripsi data sensitif<br>- Penerapan DLP | Tim Keamanan | 1 Bulan | Belum Dimulai |
| 3 | SQL Injection | - Pembersihan input<br>- Prepared statements | Tim Pengembang | 1 Minggu | Selesai |

#### 4.2 Implementasi Kontrol Keamanan
```bash
# Contoh: Mengamankan SSH
sudo nano /etc/ssh/sshd_config

# Nonaktifkan login root
PermitRootLogin no

# Aktifkan autentikasi berbasis kunci
PasswordAuthentication no

# Batas percobaan login
MaxAuthTries 3

# Restart layanan SSH
sudo systemctl restart sshd
```

### 5. Dokumentasi dan Pelaporan

#### 5.1 Template Laporan Penilaian Risiko
```markdown
# LAPORAN PENILAIAN RISIKO KEAMANAN INFORMASI

## 1. Ringkasan Eksekutif
- Tanggal Penilaian: [Tanggal]
- Lingkup: [Deskripsi Lingkup]
- Tim Penilai: [Nama Anggota Tim]
- Ringkasan Temuan: [Jumlah temuan berdasarkan tingkat keparahan]

## 2. Metodologi
- Standar yang Digunakan: [ISO 27005, NIST SP 800-30, dll.]
- Tools: [Daftar Tools]
- Pendekatan: [Kualitatif/Kuantitatif/Campuran]

## 3. Temuan Utama
### 3.1 Ringkasan Risiko
| Tingkat Risiko | Jumlah |
|----------------|--------|
| Tinggi         | 5      |
| Sedang         | 12     |
| Rendah         | 8      |

### 3.2 Risiko Kritis
1. **ID: R-001** - [Nama Risiko]
   - **Deskripsi**: [Penjelasan singkat]
   - **Dampak**: [Tinggi/Sedang/Rendah]
   - **Kemungkinan**: [Tinggi/Sedang/Rendah]
   - **Rekomendasi**: [Tindakan yang disarankan]
   - **Pemilik**: [Penanggung Jawab]
   - **Tenggat Waktu**: [Batas Waktu]

## 4. Lampiran
- Hasil Pemindaian
- Bukti Temuan
- Dokumen Pendukung
```

## 📌 Tugas Praktikum

### Tugas 1: Pemindaian Kerentanan
1. Lakukan pemindaian terhadap sistem target menggunakan OpenVAS
2. Identifikasi 5 kerentanan kritis
3. Buat laporan singkat tentang temuan

### Tugas 2: Analisis Risiko
1. Pilih 3 aset kritis di lingkungan sekolah
2. Lakukan penilaian risiko menggunakan matriks 5x5
3. Buat rencana mitigasi untuk risiko tertinggi

### Tugas 3: Presentasi Temuan
1. Buat presentasi 10 slide tentang temuan penilaian risiko
2. Sertakan rekomendasi perbaikan
3. Presentasikan di depan kelas

## ⚠️ Etika dan Legalitas
- Hanya lakukan pengujian pada sistem yang diizinkan
- Dapatkan persetujuan tertulis sebelum pengujian
- Patuhi kebijakan keamanan organisasi
- Jaga kerahasiaan temuan

## 📚 Referensi
1. NIST SP 800-30 - Guide for Conducting Risk Assessments
2. ISO/IEC 27005 - Information security risk management
3. OWASP Risk Rating Methodology
4. PTES Technical Guidelines

---
<div align="center">
  <p>Panduan Praktikum - Penilaian Risiko dan Manajemen Kerentanan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

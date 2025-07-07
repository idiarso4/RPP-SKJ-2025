# 🛠️ Praktikum: Penerapan Standar Keamanan dan Metodologi Pengujian

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menerapkan kerangka kerja keamanan NIST
2. Melakukan asesmen risiko sederhana
3. Menggunakan metodologi pengujian keamanan
4. Membuat laporan temuan keamanan
5. Menerapkan kontrol keamanan dasar

## 📋 Persiapan

### 1. Persyaratan Sistem
- Sistem Operasi: Windows/Linux dengan akses admin
- Tools: Nmap, OpenVAS, OWASP ZAP, Microsoft Excel/LibreOffice Calc
- Koneksi internet untuk mengunduh tools dan dokumentasi

### 2. Tools yang Akan Digunakan
1. **Nmap** - Pemindaian jaringan
2. **OpenVAS** - Pemindaian kerentanan
3. **OWASP ZAP** - Pengujian keamanan aplikasi web
4. **Lynis** - Audit keamanan sistem Linux
5. **Microsoft Excel/LibreOffice Calc** - Analisis risiko

## 📝 Langkah Kerja

### 1. Penerapan NIST Cybersecurity Framework

#### 1.1 Identifikasi Aset
```bash
# Gunakan Nmap untuk mengidentifikasi perangkat dalam jaringan
nmap -sn 192.168.1.0/24 -oN inventaris_jaringan.txt

# Identifikasi layanan yang berjalan
nmap -sV -sC -O 192.168.1.1-254 -oG layanan_aktif.txt
```

#### 1.2 Kategorikan Aset
Buat tabel inventaris aset:

| No | Alamat IP | Nama Host | Sistem Operasi | Layanan | Kategori Data | Pemilik |
|----|-----------|-----------|----------------|---------|---------------|---------|
| 1  | 192.168.1.1 | router | Linux 3.4 | HTTP, SSH | Konfigurasi Jaringan | IT Dept |
| 2  | 192.168.1.100 | pc-01 | Windows 10 | SMB, RDP | Data Pribadi | HRD |

### 2. Asesmen Risiko Sederhana

#### 2.1 Identifikasi Ancaman
Gunakan template berikut untuk menilai risiko:

```
Aset: [Nama Aset]
Nilai: [Rendah/Sedang/Tinggi]
Ancaman: [Jenis Ancaman]
Tingkat Ancaman: [1-5]
Tingkat Dampak: [1-5]
Tingkat Risiko = Ancaman x Dampak
```

#### 2.2 Matriks Risiko
Buat matriks risiko menggunakan Excel/Calc:

| Risiko | Kemungkinan | Dampak | Tingkat Risiko | Tindakan |
|--------|-------------|--------|----------------|----------|
| Serangan DDoS | 3 | 4 | 12 | Mitigasi DDoS |
| Kebocoran Data | 2 | 5 | 10 | Enkripsi Data |
| Malware | 4 | 3 | 12 | Antivirus Update |

### 3. Penerapan Metodologi Pengujian

#### 3.1 Menggunakan OWASP ZAP
1. **Konfigurasi Dasar**
   - Atur browser untuk menggunakan proxy ZAP (localhost:8080)
   - Aktifkan mode pengujian pasif

2. **Pemindaian Dasar**
   ```
   1. Masukkan URL target
   2. Klik 'Attack' > 'Active Scan'
   3. Pilih policy pengujian
   4. Mulai pemindaian
   ```

3. **Analisis Hasil**
   - Identifikasi temuan kritis
   - Verifikasi false positive
   - Dokumentasikan temuan

#### 3.2 Audit Keamanan dengan Lynis (Linux)
```bash
# Instalasi Lynis
sudo apt update
sudo apt install lynis -y

# Jalankan audit sistem
sudo lynis audit system

# Hasil akan disimpan di /var/log/lynis.log
```

### 4. Implementasi Kontrol Keamanan

#### 4.1 Hardening SSH
Edit file konfigurasi SSH:
```bash
sudo nano /etc/ssh/sshd_config

# Konfigurasi yang direkomendasikan:
PermitRootLogin no
PasswordAuthentication no
X11Forwarding no
MaxAuthTries 3
ClientAliveInterval 300
```

#### 4.2 Konfigurasi Firewall Dasar
```bash
# Untuk Linux (UFW)
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable

# Untuk Windows
# Gunakan Windows Defender Firewall dengan Advanced Security
```

## 📊 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum
   - Nama Praktikum

2. **Ringkasan Eksekutif**
   - Tujuan praktikum
   - Lingkup pengujian
   - Temuan utama

3. **Metodologi**
   - Tools yang digunakan
   - Prosedur pengujian
   - Batasan pengujian

4. **Temuan**
   - Daftar temuan kerentanan
   - Tingkat keparahan
   - Bukti temuan (screenshot/log)

5. **Rekomendasi**
   - Tindakan perbaikan
   - Referensi standar
   - Timeline perbaikan

6. **Lampiran**
   - Output lengkap tools
   - Referensi
   - Catatan tambahan

## 📌 Tugas Tambahan
1. Lakukan asesmen risiko untuk jaringan sekolah
2. Buat matriks risiko dengan minimal 10 aset
3. Lakukan pengujian keamanan dasar pada website sekolah
4. Buat laporan profesional dari hasil pengujian

## ⚠️ Etika dan Legalitas
- Hanya lakukan pengujian pada sistem yang diizinkan
- Dapatkan persetujuan tertulis sebelum pengujian
- Patuhi kebijakan keamanan organisasi
- Jaga kerahasiaan temuan

## 📚 Referensi
1. NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
2. OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
3. PTES Technical Guidelines: http://www.pentest-standard.org/
4. CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/

---
<div align="center">
  <p>Panduan Praktikum - Penerapan Standar Keamanan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

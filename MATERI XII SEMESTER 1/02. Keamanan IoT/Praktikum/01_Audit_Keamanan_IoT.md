# 🛠️ Panduan Praktikum: Audit Keamanan Perangkat IoT

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Melakukan pemindaian keamanan pada perangkat IoT
2. Mengidentifikasi kerentanan umum pada perangkat IoT
3. Menerapkan langkah-langkah pengamanan dasar
4. Menganalisis lalu lintas jaringan IoT

## 🛠️ Alat dan Bahan
- Raspberry Pi / Perangkat IoT
- Komputer dengan Kali Linux
- Router jaringan
- Kabel Ethernet
- Perangkat IoT untuk pengujian (contoh: kamera IP, smart plug)
- Tools: Nmap, Wireshark, RouterSploit, Shodan

## 📋 Langkah 1: Persiapan Lingkungan

### 1.1 Instalasi Tools
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install tools keamanan
sudo apt install -y nmap wireshark tcpdump

# Install RouterSploit
git clone https://github.com/threat9/routersploit
cd routersploit
pip install -r requirements.txt

# Install Shodan CLI
pip install shodan
shodan init YOUR_API_KEY
```

### 1.2 Persiapan Jaringan
1. Siapkan jaringan terisolasi untuk pengujian
2. Hubungkan perangkat IoT ke jaringan
3. Catat alamat IP perangkat

## 🔍 Langkah 2: Pemindaian Jaringan

### 2.1 Pemindaian dengan Nmap
```bash
# Pemindaian dasar
nmap -sV -sC -O <target_ip>

# Deteksi OS dan versi
nmap -A -T4 <target_ip>

# Deteksi kerentanan umum
nmap --script vuln <target_ip>
```

### 2.2 Analisis Port Terbuka
1. Identifikasi port terbuka
2. Catat layanan yang berjalan
3. Periksa versi layanan untuk kerentanan yang diketahui

## 🕵️ Langkah 3: Analisis Lalu Lintas Jaringan

### 3.1 Capture Paket dengan Wireshark
```bash
# Mulai capture
sudo wireshark &

# Atau gunakan tcpdump
sudo tcpdump -i eth0 -w iot_traffic.pcap
```

### 3.2 Analisis Protokol
1. Filter protokol umum IoT:
   - MQTT (port 1883/8883)
   - CoAP (port 5683/5684)
   - HTTP/HTTPS (80/443)
   - Telnet (23)
   - SSH (22)

2. Cari kredensial dalam plaintext
3. Identifikasi data sensitif yang tidak terenkripsi

## 🔓 Langkah 4: Pengujian Otentikasi

### 4.1 Uji Kredensial Default
```bash
# Contoh dengan hydra
hydra -l admin -P /usr/share/wordlists/rockyou.txt <target_ip> http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid"
```

### 4.2 Uji Kekuatan Kata Sandi
1. Gunakan wordlist umum
2. Uji serangan brute force
3. Periksa kebijakan penguncian akun

## 🛡️ Langkah 5: Pengujian Aplikasi Web

### 5.1 OWASP ZAP
```bash
# Jalankan ZAP
zap-webswing.sh
```

### 5.2 Langkah Pengujian
1. Spider aplikasi web
2. Scan aktif untuk kerentanan
3. Analisis hasil scan
4. Dokumentasikan temuan

## 📝 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum

2. **Pendahuluan**
   - Latar belakang
   - Tujuan praktikum

3. **Alat dan Bahan**
   - Daftar peralatan
   - Spesifikasi perangkat

4. **Langkah Kerja**
   - Dokumentasikan setiap langkah
   - Sertakan screenshot
   - Tuliskan perintah yang digunakan

5. **Hasil dan Pembahasan**
   - Hasil pemindaian
   - Analisis kerentanan
   - Rekomendasi perbaikan

6. **Kesimpulan**
   - Ringkasan temuan
   - Kendala yang dihadapi
   - Saran perbaikan

### Template Laporan
```markdown
# Laporan Praktikum Keamanan IoT

## 1. Informasi Umum
- Nama: ______________________
- Kelas: _____________________
- Tanggal: ___________________
- Perangkat Uji: _____________
- Alamat IP: _________________

## 2. Hasil Pemindaian

### 2.1 Nmap Scan
```
[Salin hasil scan Nmap di sini]
```

### 2.2 Analisis Kerentanan
| No | Kerentanan | Tingkat Risiko | Keterangan |
|----|------------|----------------|------------|
| 1  |            |                |            |
| 2  |            |                |            |

## 3. Rekomendasi
1. ________________________________________________
2. ________________________________________________
3. ________________________________________________
```

## 🧩 Tantangan Lanjutan
1. Lakukan pengujian keamanan fisik pada perangkat IoT
2. Coba eksploitasi kerentanan yang ditemukan (dengan izin)
3. Buat laporan profesional dengan Executive Summary

## ⚠️ Etika dan Legalitas
- Hanya lakukan pengujian pada perangkat yang Anda miliki
- Dapatkan izin tertulis sebelum menguji perangkat milik orang lain
- Patuhi hukum dan peraturan yang berlaku
- Gunakan pengetahuan ini untuk tujuan yang baik

## 📚 Referensi
1. OWASP IoT Testing Guide
2. NIST IoT Security Guidelines
3. ENISA IoT Security Recommendations

---
<div align="center">
  <p>Panduan Praktikum - Keamanan IoT</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

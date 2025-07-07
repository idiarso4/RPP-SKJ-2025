# 🛠️ Praktikum: Pengenalan Tools Keamanan Siber Dasar

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengenal berbagai tools dasar keamanan siber
2. Melakukan instalasi dan konfigurasi dasar tools
3. Memahami fungsi dasar setiap tool
4. Menerapkan etika penggunaan tools keamanan

## 📋 Persiapan

### 1. Persyaratan Sistem
- Sistem Operasi: Windows 10/11 atau Linux (disarankan Kali Linux)
- RAM: Minimal 4GB (disarankan 8GB)
- Ruang Penyimpanan: Minimal 20GB ruang kosong
- Koneksi Internet

### 2. Tools yang Akan Digunakan
1. Nmap
2. Wireshark
3. Metasploit Framework
4. Burp Suite Community
5. OWASP ZAP

## 📝 Langkah Kerja

### 1. Instalasi Tools

#### 1.1 Nmap (Network Mapper)
```bash
# Untuk Linux (Debian/Ubuntu/Kali)
sudo apt update
sudo apt install nmap -y

# Untuk Windows
# Unduh dari https://nmap.org/download.html
```

**Verifikasi Instalasi:**
```bash
nmap --version
```

#### 1.2 Wireshark
```bash
# Untuk Linux
sudo apt install wireshark -y

# Untuk Windows
# Unduh dari https://www.wireshark.org/download.html
```

**Verifikasi Instalasi:**
```bash
wireshark --version
```

#### 1.3 Metasploit Framework
```bash
# Untuk Linux (Kali Linux sudah include)
sudo apt install metasploit-framework -y

# Untuk Windows
# Instal melalui Kali Linux WSL atau gunakan versi Windows
```

**Verifikasi Instalasi:**
```bash
msfconsole --version
```

### 2. Pengenalan Dasar Tools

#### 2.1 Nmap Dasar
```bash
# Scan host tunggal
nmap -sV 192.168.1.1

# Scan jaringan
nmap -sn 192.168.1.0/24

# Scan port spesifik
nmap -p 80,443,22,21 192.168.1.1
```

#### 2.2 Wireshark Dasar
1. Buka Wireshark
2. Pilih interface jaringan (contoh: Wi-Fi, Ethernet)
3. Klik tombol start untuk memulai capture
4. Gunakan filter untuk melihat traffic tertentu:
   - `http` - Hanya tampilkan traffic HTTP
   - `tcp.port == 80` - Filter berdasarkan port
   - `ip.addr == 192.168.1.1` - Filter berdasarkan IP

#### 2.3 Metasploit Dasar
```bash
# Jalankan msfconsole
msfconsole

# Cari modul exploit
search eternalblue

# Gunakan modul
use exploit/windows/smb/ms17_010_eternalblue

# Lihat opsi yang tersedia
show options
```

### 3. Praktik Dasar

#### 3.1 Analisis Jaringan dengan Nmap
1. Lakukan scan terhadap perangkat di jaringan lokal
2. Identifikasi layanan yang berjalan
3. Catat hasil scan dalam format tabel:

| IP Address | Port Terbuka | Layanan | Versi |
|------------|--------------|---------|-------|
| 192.168.1.1 | 80, 443 | http, https | Apache 2.4.41 |

#### 3.2 Analisis Traffic dengan Wireshark
1. Mulai capture traffic
2. Buka website menggunakan browser
3. Hentikan capture dan analisis paket HTTP/HTTPS
4. Identifikasi:
   - Alamat IP sumber dan tujuan
   - Protokol yang digunakan
   - Header HTTP

#### 3.3 Penggunaan Burp Suite Community
1. Buka Burp Suite Community
2. Konfigurasi browser untuk menggunakan proxy Burp (127.0.0.1:8080)
3. Aktifkan intercept
4. Kunjungi website HTTP (bukan HTTPS)
5. Analisis request dan response

## 📊 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum
   - Nama Praktikum

2. **Tujuan**
   - Tuliskan tujuan praktikum

3. **Alat dan Bahan**
   - Daftar tools yang digunakan
   - Spesifikasi perangkat

4. **Langkah Kerja**
   - Dokumentasikan setiap langkah dengan screenshot
   - Beri penjelasan singkat

5. **Hasil dan Pembahasan**
   - Tampilkan hasil scan/analisis
   - Beri analisis dari hasil yang didapat

6. **Kesimpulan**
   - Ringkasan hasil praktikum
   - Kendala yang dihadapi
   - Solusi dari kendala

## 📌 Tugas Tambahan
1. Lakukan scan terhadap website sekolah menggunakan Nmap
2. Analisis traffic saat login ke website (gunakan HTTP, jangan HTTPS)
3. Buat laporan singkat tentang temuan Anda

## ⚠️ Etika dan Legalitas
- Hanya lakukan praktikum pada sistem yang Anda miliki atau yang sudah mendapat izin
- Jangan lakukan scanning terhadap sistem/organisasi tanpa izin tertulis
- Patuhi peraturan yang berlaku di lingkungan praktikum

## 📚 Referensi
1. Nmap Documentation: https://nmap.org/docs.html
2. Wireshark User's Guide: https://www.wireshark.org/docs/wsug_html/
3. Metasploit Unleashed: https://www.offensive-security.com/metasploit-unleashed/
4. Burp Suite Documentation: https://portswigger.net/burp/documentation

---
<div align="center">
  <p>Panduan Praktikum - Pengenalan Tools Keamanan Siber</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

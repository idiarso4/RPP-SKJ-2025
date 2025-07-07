# 🔧 Praktikum: Konfigurasi Keamanan Jaringan Dasar

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengkonfigurasi firewall dasar menggunakan Windows Firewall dan UFW
2. Menganalisis lalu lintas jaringan dengan Wireshark
3. Mengamankan koneksi SSH
4. Menerapkan kebijakan kata sandi yang kuat
5. Melakukan pemindaian keamanan jaringan

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- Komputer dengan Windows 10/11 dan Linux (dual boot atau virtual machine)
- VirtualBox/VMware Workstation
- Kali Linux (virtual machine)
- Windows 10/11 (virtual machine atau host)
- Koneksi jaringan yang stabil

### 2. Perangkat Lunak yang Diperlukan
- Wireshark
- Nmap
- OpenSSH Server (di Linux)
- Windows Terminal/PowerShell
- Notepad++ (opsional)

## 📝 Langkah Kerja

### 1. Konfigurasi Windows Firewall

#### 1.1 Membuat Aturan Firewall Masuk (Inbound)
```powershell
# Buka PowerShell sebagai Administrator
# Membuat aturan untuk memblokir ping (ICMP)
New-NetFirewallRule -DisplayName "Block ICMPv4" -Direction Inbound -Protocol ICMPv4 -IcmpType 8 -Action Block

# Memeriksa aturan yang telah dibuat
Get-NetFirewallRule -DisplayName "Block ICMPv4" | Select-Object DisplayName, Enabled, Action, Direction
```

#### 1.2 Membuat Aturan Firewall Keluar (Outbound)
```powershell
# Membuat aturan untuk memblokir akses ke DNS (port 53)
New-NetFirewallRule -DisplayName "Block Outbound DNS" -Direction Outbound -Protocol UDP -RemotePort 53 -Action Block

# Verifikasi aturan
Get-NetFirewallRule -DisplayName "Block Outbound DNS" | Select-Object DisplayName, Enabled, Action, Direction
```

### 2. Konfigurasi UFW di Linux

#### 2.1 Instalasi dan Aktivasi UFW
```bash
# Update package list
sudo apt update

# Install UFW jika belum terinstall
sudo apt install ufw -y

# Aktifkan UFW
sudo ufw enable

# Periksa status
sudo ufw status verbose
```

#### 2.2 Konfigurasi Aturan Dasar
```bash
# Izinkan SSH
sudo ufw allow 22/tcp

# Izinkan HTTP dan HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Tolak ping (ICMP)
sudo ufw deny proto icmp

# Aktifkan logging
sudo ufw logging on

# Periksa aturan yang berlaku
sudo ufw status numbered
```

### 3. Analisis Lalu Lintas Jaringan dengan Wireshark

#### 3.1 Menangkap dan Menganalisis Paket
1. Buka Wireshark
2. Pilih antarmuka jaringan yang aktif
3. Mulai penangkapan paket
4. Lakukan aktivitas berikut:
   - Buka browser dan kunjungi sebuah website
   - Lakukan ping ke alamat IP publik (contoh: 8.8.8.8)
   - Akses layanan SSH jika tersedia
5. Hentikan penangkapan dan simpan file capture

#### 3.2 Filter Paket untuk Analisis Keamanan
```
# Hanya tampilkan paket HTTP
http

# Tampilkan percobaan login SSH yang gagal
ssh.message_code == 51

# Tampilkan paket ICMP (ping)
icmp

# Tampilkan traffic DNS
dns
```

### 4. Mengamankan Layanan SSH

#### 4.1 Konfigurasi SSH Server
```bash
# Edit file konfigurasi SSH
sudo nano /etc/ssh/sshd_config
```

Ubah konfigurasi berikut:
```ini
Port 2222  # Ubah port default
PermitRootLogin no
PasswordAuthentication no  # Hanya mengizinkan autentikasi dengan kunci
X11Forwarding no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
```

#### 4.2 Membuat Kunci SSH
```bash
# Generate kunci SSH (di client)
ssh-keygen -t ed25519 -C "email@example.com"

# Salin kunci publik ke server
ssh-copy-id -p 2222 username@server_ip

# Restart layanan SSH
sudo systemctl restart sshd
```

### 5. Pemindaian Keamanan dengan Nmap

#### 5.1 Pemindaian Port Dasar
```bash
# Pemindaian port TCP
nmap -sS -T4 -A -v target_ip

# Pemindaian UDP (memerlukan hak akses root)
sudo nmap -sU -T4 target_ip

# Deteksi sistem operasi
sudo nmap -O target_ip

# Deteksi versi layanan
nmap -sV target_ip
```

#### 5.2 Pemindaian Kerentanan Dasar
```bash
# Gunakan script NSE untuk mendeteksi kerentanan umum
nmap --script vuln target_ip

# Deteksi kerentanan Heartbleed
nmap -p 443 --script ssl-heartbleed target_ip

# Deteksi kerentanan SMB
nmap --script smb-vuln-ms17-010 target_ip
```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum konfigurasi keamanan jaringan.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Hasil Konfigurasi Firewall
```
# Tempelkan hasil perintah Get-NetFirewallRule dan ufw status
```

#### 4.2 Analisis Wireshark
Sertakan screenshot analisis paket yang menarik.

#### 4.3 Hasil Pemindaian Nmap
```
# Tempelkan hasil pemindaian Nmap
```

### 5. Analisis
1. Apa perbedaan antara firewall stateful dan stateless?
2. Mengapa penting untuk mengubah port default SSH?
3. Jenis serangan apa yang dapat dideteksi dengan menganalisis log UFW?
4. Bagaimana cara mengamankan layanan web selain menggunakan firewall?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Coba konfigurasi IDS (Intrusion Detection System) dasar menggunakan Snort
2. Implementasikan fail2ban untuk memblokir upaya brute force
3. Buat skrip otomatisasi untuk memantau perubahan aturan firewall

## ⚠️ Etika dan Keamanan
1. Hanya lakukan praktikum di lingkungan lab yang diizinkan
2. Dapatkan izin tertulis sebelum memindai jaringan yang bukan milik Anda
3. Dokumentasikan semua perubahan konfigurasi
4. Selalu backup konfigurasi sebelum melakukan perubahan

## 📚 Referensi
1. NIST Special Publication 800-41: Guidelines on Firewalls and Firewall Policy
2. Wireshark User's Guide
3. Nmap Network Scanning (2023) - Gordon Lyon
4. OpenSSH Documentation

---
<div align="center">
  <p>Lembar Kerja Praktikum - Konfigurasi Keamanan Jaringan Dasar</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

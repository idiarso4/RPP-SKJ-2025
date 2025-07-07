# 🛠️ Praktikum: Keamanan Jaringan Lanjutan

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengimplementasikan IDS/IPS menggunakan Snort
2. Membangun VPN server dengan OpenVPN
3. Menganalisis keamanan infrastruktur cloud
4. Melakukan penanganan insiden keamanan
5. Menerapkan segmentasi jaringan mikro

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- 2+ komputer dengan OS Linux (disarankan Ubuntu Server)
- 1 komputer dengan OS Windows (opsional, untuk pengujian klien)
- Koneksi jaringan yang stabil
- Akses internet untuk mengunduh paket
- Virtualisasi (VMware/VirtualBox) jika menggunakan lingkungan virtual

### 2. Software yang Diperlukan
- Snort (IDS/IPS)
- OpenVPN
- Wireshark
- Nmap
- Docker (untuk simulasi cloud)
- Python 3.x

## 📝 Langkah Kerja

### 1. Implementasi Snort sebagai NIDS

#### 1.1 Instalasi Snort
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install dependensi
sudo apt install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex zlib1g-dev

# Download dan ekstrak Snort
wget https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz
tar -xvzf snort-2.9.20.tar.gz
cd snort-2.9.20

# Konfigurasi dan instalasi
./configure --enable-sourcefire --disable-open-appid
make -j$(nproc)
sudo make install

# Buat direktori konfigurasi
sudo mkdir -p /etc/snort/rules
sudo mkdir /var/log/snort

# Salin file konfigurasi
sudo cp etc/*.conf* /etc/snort/
sudo cp etc/*.map /etc/snort/
```

#### 1.2 Konfigurasi Dasar Snort
```bash
# Edit konfigurasi utama
sudo nano /etc/snort/snort.conf

# Sesuaikan variabel berikut:
ipvar HOME_NET 192.168.1.0/24
ipvar EXTERNAL_NET !$HOME_NET
var RULE_PATH /etc/snort/rules
var SO_RULE_PATH /etc/snort/so_rules
var PREPROC_RULE_PATH /etc/snort/preproc_rules

# Download aturan terbaru
sudo wget https://www.snort.org/rules/snortrules-snapshot-2990.tar.gz -O /tmp/snort-rules.tar.gz
sudo tar -xzvf /tmp/snort-rules.tar.gz -C /etc/snort/

# Jalankan Snort dalam mode IDS
sudo snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i eth0
```

### 2. Membangun VPN Server dengan OpenVPN

#### 2.1 Instalasi dan Konfigurasi Awal
```bash
# Install OpenVPN dan Easy-RSA
sudo apt update
sudo apt install -y openvpn easy-rsa

# Setup direktori PKI
make-cadir ~/openvpn-ca
cd ~/openvpn-ca

# Edit variabel
nano vars
# Sesuaikan:
# export KEY_COUNTRY="US"
# export KEY_PROVINCE="CA"
# export KEY_CITY="SanFrancisco"
# export KEY_ORG="Fort-Funston"
# export KEY_EMAIL="mail@hostname.com"
# export KEY_OU="MyOrganizationalUnit"
# export KEY_NAME="server"

# Inisialisasi PKI
source vars
./clean-all
./build-ca
```

#### 2.2 Generate Sertifikat Server dan Kunci
```bash
# Generate key dan sertifikat server
./build-key-server server

# Generate Diffie-Hellman parameters
./build-dh

# Generate TLS-Auth key
openvpn --genkey --secret keys/ta.key

# Salin file yang dibutuhkan
cd ~/openvpn-ca/keys
sudo cp ca.crt server.crt server.key ta.key dh2048.pem /etc/openvpn/
```

#### 2.3 Konfigurasi Server OpenVPN
```bash
# Salin konfigurasi contoh
sudo cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz /etc/openvpn/
sudo gzip -d /etc/openvpn/server.conf.gz

# Edit konfigurasi
sudo nano /etc/openvpn/server.conf

# Sesuaikan dengan konfigurasi:
tls-auth ta.key 0
key-direction 0
cipher AES-256-CBC
auth SHA256
user nobody
group nogroup
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"
```

#### 2.4 Konfigurasi Klien
```bash
# Buat direktori konfigurasi klien
mkdir -p ~/client-configs/files
chmod 700 ~/client-configs/files

# Buat konfigurasi dasar klien
nano ~/client-configs/base.conf

# Isi dengan:
client
dev tun
proto udp
remote your_server_ip 1194
resolv-retry infinite
nobind
user nobody
group nogroup
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
auth SHA256
key-direction 1
verb 3
```

### 3. Analisis Keamanan Infrastruktur Cloud dengan Docker

#### 3.1 Setup Lingkungan Docker
```bash
# Install Docker
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce

# Jalankan container yang rentan
sudo docker run -d --name vuln-app -p 80:80 vulnerables/web-dvwa
```

#### 3.2 Analisis Keamanan
```bash
# Pindai port dengan Nmap
nmap -sV -sC -p- 172.17.0.2

# Analisis layanan web
nikto -h http://localhost

# Periksa konfigurasi Docker
docker inspect vuln-app
docker ps --no-trunc
docker history vulnerables/web-dvwa
```

### 4. Simulasi Penanganan Insiden Keamanan

#### 4.1 Deteksi Anomali
```bash
# Monitor log sistem
sudo tail -f /var/log/auth.log

# Periksa koneksi jaringan
sudo netstat -tulnp

# Analisis proses yang berjalan
top
ps aux | grep -i "suspicious"
```

#### 4.2 Isolasi dan Analisis
```bash
# Isolasi sistem yang terinfeksi
sudo iptables -A INPUT -s IP_PENYERANG -j DROP

# Dump memori untuk analisis
sudo apt install -y volatility
sudo python -m pip install distorm3
sudo python -m pip install yara-python

# Ambil snapshot memori
sudo python vol.py -f memory.dump --profile=LinuxUbuntu_5_4_0-42-generic_profilex64 linux_pslist
```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum keamanan jaringan lanjutan.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Implementasi Snort
```
# Tampilkan konfigurasi Snort
# Tampilkan contoh alert yang dihasilkan
```

#### 4.2 Konfigurasi OpenVPN
```
# Tampilkan konfigurasi server dan klien
# Tampilkan hasil koneksi VPN
```

#### 4.3 Analisis Keamanan Cloud
```
# Tampilkan hasil pemindaian keamanan
# Identifikasi kerentanan yang ditemukan
```

### 5. Analisis
1. Apa tantangan utama dalam mengimplementasikan IDS/IPS?
2. Bagaimana cara meningkatkan keamanan koneksi VPN?
3. Apa saja temuan keamanan pada lingkungan cloud yang diuji?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Implementasikan Snort dalam mode IPS menggunakan iptables
2. Buat sistem otomatisasi untuk memantau dan merespons ancaman
3. Lakukan hardening pada server VPN berdasarkan standar industri

## ⚠️ Keamanan dan Etika
1. Hanya lakukan pengujian pada lingkungan yang Anda miliki atau memiliki izin
2. Dokumentasikan semua temuan dengan baik
3. Laporkan kerentanan ke pemilik sistem dengan bertanggung jawab
4. Patuhi hukum dan etika yang berlaku

## 📚 Referensi
1. Snort User Manual: https://www.snort.org/documents
2. OpenVPN Documentation: https://openvpn.net/community-resources/
3. Docker Security: https://docs.docker.com/engine/security/
4. NIST SP 800-61: Computer Security Incident Handling Guide

---
<div align="center">
  <p>Lembar Kerja Praktikum - Keamanan Jaringan Lanjutan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

# 🔒 Panduan Praktikum: Implementasi OpenVPN

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menginstal dan mengkonfigurasi OpenVPN server
2. Membuat sertifikat dan kunci
3. Mengkonfigurasi klien VPN
4. Mengamankan komunikasi VPN

## 🖥️ Spesifikasi Sistem

### Server
- OS: Ubuntu Server 22.04 LTS
- CPU: 2 core (minimal)
- RAM: 2GB (minimal)
- Storage: 10GB
- IP Publik: 203.0.113.1 (contoh)

### Klien
- OS: Windows/Linux/macOS
- Koneksi internet stabil

## 📥 Langkah 1: Instalasi OpenVPN Server

### 1.1 Update Sistem
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Instal OpenVPN dan Easy-RSA
```bash
# Instal paket yang diperlukan
sudo apt install -y openvpn easy-rsa

# Buat direktori konfigurasi
mkdir -p ~/openvpn-ca/{certs,keys,configs}
```

## 🔐 Langkah 2: Setup PKI (Public Key Infrastructure)

### 2.1 Siapkan Direktori Easy-RSA
```bash
# Salin template easy-rsa
cp -r /usr/share/easy-rsa/* ~/openvpn-ca/

# Masuk ke direktori
cd ~/openvpn-ca

# Inisialisasi PKI
./easyrsa init-pki

# Build CA (Certificate Authority)
./easyrsa build-ca nopass

# Buat server certificate
./easyrsa gen-req server nopass
./easyrsa sign-req server server

# Buat Diffie-Hellman parameters
./easyrsa gen-dh

# Buat TLS-Auth key
openvpn --genkey secret ta.key
```

### 2.2 Generate Client Certificate
```bash
# Buat client certificate
./easyrsa gen-req client1 nopass
./easyrsa sign-req client client1
```

## ⚙️ Langkah 3: Konfigurasi Server

### 3.1 Salin File yang Diperlukan
```bash
# Salin file ke direktori OpenVPN
sudo cp ~/openvpn-ca/pki/ca.crt /etc/openvpn/server/
sudo cp ~/openvpn-ca/pki/issued/server.crt /etc/openvpn/server/
sudo cp ~/openvpn-ca/pki/private/server.key /etc/openvpn/server/
sudo cp ~/openvpn-ca/ta.key /etc/openvpn/server/
sudo cp ~/openvpn-ca/pki/dh.pem /etc/openvpn/server/
```

### 3.2 Buat Konfigurasi Server
```bash
sudo nano /etc/openvpn/server/server.conf
```

Isi dengan konfigurasi berikut:
```
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh.pem
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist /var/log/openvpn/ipp.txt
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"
keepalive 10 120
tls-auth ta.key 0
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status /var/log/openvpn/openvpn-status.log
verb 3
explicit-exit-notify 1
```

### 3.3 Aktifkan IP Forwarding
```bash
# Edit sysctl.conf
sudo nano /etc/sysctl.conf

# Uncomment atau tambahkan baris berikut:
net.ipv4.ip_forward=1

# Terapkan perubahan
sudo sysctl -p
```

### 3.4 Konfigurasi Firewall
```bash
# Install UFW jika belum ada
sudo apt install -y ufw

# Atur kebijakan default
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Izinkan SSH dan OpenVPN
sudo ufw allow 22/tcp
sudo ufw allow 1194/udp

# Aktifkan NAT
sudo nano /etc/ufw/before.rules
```

Tambahkan di atas "# don't delete" line:
```
# START OPENVPN RULES
# NAT table rules
*nat
:POSTROUTING ACCEPT [0:0]
# Allow traffic from OpenVPN client to eth0
-A POSTROUTING -s 10.8.0.0/8 -o eth0 -j MASQUERADE
# END OPENVPN RULES
```

### 3.5 Mulai dan Aktifkan OpenVPN
```bash
# Restart UFW
sudo ufw disable
sudo ufw enable

# Start OpenVPN
sudo systemctl start openvpn@server
sudo systemctl enable openvpn@server

# Periksa status
sudo systemctl status openvpn@server
```

## 💻 Langkah 4: Konfigurasi Klien

### 4.1 Buat File Konfigurasi Klien
```bash
mkdir -p ~/client-configs/files
nano ~/client-configs/base.conf
```

Isi dengan:
```
client
dev tun
proto udp
remote 203.0.113.1 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
verb 3
<ca>
[isi dengan isi file ca.crt]
</ca>
<cert>
[isi dengan isi file client1.crt]
</cert>
<key>
[isi dengan isi file client1.key]
</key>
<tls-auth>
[isi dengan isi file ta.key]
</tls-auth>
key-direction 1
```

### 4.2 Generate File Konfigurasi Klien
```bash
# Salin file yang diperlukan
cp ~/openvpn-ca/pki/ca.crt ~/client-configs/files/
cp ~/openvpn-ca/pki/issued/client1.crt ~/client-configs/files/
cp ~/openvpn-ca/pki/private/client1.key ~/client-configs/files/
cp ~/openvpn-ca/ta.key ~/client-configs/files/

# Gabungkan konfigurasi
cd ~/client-configs
cat base.conf \
    <(echo -e '<ca>') \
    files/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    files/client1.crt \
    <(echo -e '</cert>\n<key>') \
    files/client1.key \
    <(echo -e '</key>\n<tls-auth>') \
    files/ta.key \
    <(echo -e '</tls-auth>') \
    > client1.ovpn
```

## 📱 Langkah 5: Uji Koneksi VPN

### 5.1 Di Server
```bash
# Periksa log
sudo tail -f /var/log/syslog | grep -i vpn

# Periksa interface tun0
ip addr show tun0
```

### 5.2 Di Klien
1. Instal OpenVPN Client
   - Windows: https://openvpn.net/community-downloads/
   - Linux: `sudo apt install openvpn`
   - macOS: `brew install openvpn`

2. Impor file `client1.ovpn`
3. Sambungkan ke VPN
4. Verifikasi koneksi:
   ```bash
   # Di terminal Linux/macOS
   curl ifconfig.me
   # Seharusnya menampilkan IP server VPN
   ```

## 📝 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum

2. **Tujuan Praktikum**
   - Tuliskan tujuan praktikum

3. **Alat dan Bahan**
   - Spesifikasi perangkat
   - Software yang digunakan

4. **Langkah Kerja**
   - Dokumentasikan setiap langkah
   - Sertakan screenshot
   - Tuliskan perintah yang digunakan

5. **Hasil dan Pembahasan**
   - Tampilkan hasil konfigurasi
   - Analisis koneksi VPN
   - Jawab pertanyaan:
     - Bagaimana cara kerja enkripsi pada OpenVPN?
     - Apa keuntungan menggunakan VPN?

6. **Kesimpulan**
   - Ringkasan hasil
   - Kendala yang dihadapi
   - Saran perbaikan

## 🧩 Tantangan Lanjutan
1. Implementasikan autentikasi dua faktor
2. Buat skrip otomatisasi untuk membuat user baru
3. Konfigurasi load balancing dengan beberapa server VPN

## ⚠️ Troubleshooting

### Masalah: Koneksi Gagal
**Solusi:**
1. Periksa log server:
   ```bash
   sudo journalctl -u openvpn@server -f
   ```
2. Verifikasi port terbuka:
   ```bash
   sudo ufw status
   ```
3. Periksa koneksi klien ke server:
   ```bash
   nc -vzu 203.0.113.1 1194
   ```

### Masalah: Tidak Bisa Akses Internet
**Solusi:**
1. Pastikan IP forwarding aktif:
   ```bash
   cat /proc/sys/net/ipv4/ip_forward
   ```
2. Periksa NAT rules:
   ```bash
   sudo iptables -t nat -L -n -v
   ```
3. Verifikasi DNS di klien

## 📚 Referensi
1. [OpenVPN Documentation](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-4/)
2. [DigitalOcean OpenVPN Guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-20-04)
3. [OpenVPN Hardening](https://community.openvpn.net/openvpn/wiki/Hardening)

---
<div align="center">
  <p>Panduan Praktikum OpenVPN - SMKN 1 Punggelan</p>
  <p>© 2025 Tim Pengajar Keamanan Jaringan</p>
</div>

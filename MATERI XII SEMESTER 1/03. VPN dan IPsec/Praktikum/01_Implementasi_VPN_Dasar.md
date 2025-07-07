# 🛠️ Panduan Praktikum: Implementasi VPN Dasar

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengkonfigurasi server dan klien VPN
2. Menerapkan IPsec untuk koneksi aman
3. Menguji konektivitas dan keamanan VPN
4. Memecahkan masalah konfigurasi dasar

## 🛠️ Alat dan Bahan
- 2+ komputer dengan Ubuntu Server 20.04/22.04
- Koneksi jaringan yang stabil
- Akses root/sudo
- VirtualBox/VMware (opsional untuk simulasi)

## 📋 Langkah 1: Persiapan Lingkungan

### 1.1 Update Sistem
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Instal Paket yang Diperlukan
```bash
sudo apt install -y strongswan strongswan-pki libcharon-extra-plugins \
libcharon-extauth-plugins libstrongswan-extra-plugins
```

## 🔧 Langkah 2: Konfigurasi IPsec VPN (IKEv2)

### 2.1 Generate Sertifikat
```bash
# Buat direktori untuk sertifikat
mkdir -p ~/pki/{cacerts,certs,private}
chmod 700 ~/pki

# Generate CA
ipsec pki --gen --type rsa --size 4096 --outform pem > ~/pki/private/ca-key.pem
ipsec pki --self --ca --lifetime 3650 --in ~/pki/private/ca-key.pem \
    --type rsa --digest sha256 --dn "CN=VPN CA" --outform pem > ~/pki/cacerts/ca-cert.pem

# Generate server certificate
ipsec pki --gen --type rsa --size 4096 --outform pem > ~/pki/private/server-key.pem
ipsec pki --pub --in ~/pki/private/server-key.pem | ipsec pki --issue \
    --lifetime 1825 --cacert ~/pki/cacerts/ca-cert.pem --cakey ~/pki/private/ca-key.pem \
    --dn "CN=vpn.example.com" --san vpn.example.com --flag serverAuth --flag ikeIntermediate \
    --outform pem > ~/pki/certs/server-cert.pem
```

### 2.2 Konfigurasi StrongSwan
```bash
# Salin sertifikat
sudo cp -r ~/pki/* /etc/ipsec.d/

# Buat konfigurasi IPsec
sudo nano /etc/ipsec.conf
```

Isi dengan konfigurasi berikut:
```
config setup
    charondebug="ike 1, knl 1, cfg 0"
    uniqueids=no

conn ikev2-vpn
    auto=add
    compress=no
    type=tunnel
    keyexchange=ikev2
    fragmentation=yes
    forceencaps=yes
    ike=aes256-sha256-modp1024,3des-sha1-modp1024,aes256-sha1-modp1024!
    esp=aes256-sha256,3des-sha1,aes256-sha1!
    dpdaction=clear
    dpddelay=300s
    rekey=no
    left=%any
    leftid=@vpn.example.com
    leftcert=server-cert.pem
    leftsendcert=always
    leftsubnet=0.0.0.0/0
    right=%any
    rightid=%any
    rightauth=eap-mschapv2
    rightsourceip=10.10.10.0/24
    rightdns=8.8.8.8,8.8.4.4
    rightsendcert=never
    eap_identity=%identity
```

### 2.3 Konfigurasi Autentikasi
```bash
sudo nano /etc/ipsec.secrets
```

Tambahkan:
```
: RSA server-key.pem
username : EAP "password"
```

### 2.4 Aktifkan IP Forwarding
```bash
sudo nano /etc/sysctl.conf
```

Uncomment atau tambahkan:
```
net.ipv4.ip_forward = 1
net.ipv4.ip_no_pmtu_disc = 1
```

Terapkan perubahan:
```bash
sudo sysctl -p
```

### 2.5 Konfigurasi Firewall (UFW)
```bash
sudo ufw allow OpenSSH
sudo ufw allow 500/udp
sudo ufw allow 4500/udp
sudo ufw enable
```

## 🔍 Langkah 3: Konfigurasi Klien

### 3.1 Windows
1. Buka Settings > Network & Internet > VPN
2. Klik "Add a VPN connection"
3. Isi detail:
   - VPN Provider: Windows (built-in)
   - Connection name: Nama VPN Anda
   - Server name or address: alamat-ip-server
   - VPN type: IKEv2
   - Type of sign-in info: Username and password
   - Username: username
   - Password: password

### 3.2 Android/iOS
1. Buka Settings > Network & Internet > VPN
2. Ketuk "+" atau "Add VPN"
3. Pilih tipe IKEv2/IPsec
4. Isi detail server dan kredensial

## 🧪 Langkah 4: Pengujian

### 4.1 Mulai Layanan
```bash
sudo systemctl start strongswan-starter
sudo systemctl enable strongswan-starter
```

### 4.2 Periksa Status
```bash
sudo ipsec statusall
```

### 4.3 Uji Konektivitas
```bash
# Dari klien
ping 10.10.10.1

# Periksa rute
ip route
```

## 🐛 Troubleshooting

### 4.1 Log IPsec
```bash
sudo ipsec stroke loglevel ike 2
sudo ipsec stroke loglevel cfg 2
sudo ipsec restart
sudo journalctl -f -u strongswan-starter
```

### 4.2 Masalah Umum
1. **Koneksi Gagal**
   - Periksa port 500/4500 UDP terbuka
   - Verifikasi sertifikat dan kunci
   - Periksa log untuk pesan error

2. **Tidak Bisa Akses Internet**
   - Pastikan IP forwarding aktif
   - Periksa aturan NAT
   - Verifikasi DNS

## 📝 Laporan Praktikum

### Format Laporan
1. **Pendahuluan**
   - Tujuan praktikum
   - Alat dan bahan

2. **Langkah Kerja**
   - Dokumentasi setiap langkah
   - Screenshot konfigurasi
   - Output perintah penting

3. **Hasil dan Pembahasan**
   - Hasil pengujian
   - Analisis masalah
   - Solusi yang diterapkan

4. **Kesimpulan**
   - Pencapaian tujuan
   - Kendala yang dihadapi
   - Saran perbaikan

### Template Laporan
```markdown
# Laporan Praktikum Implementasi VPN

## 1. Informasi Umum
- Nama: ______________________
- Kelas: _____________________
- Tanggal: ___________________
- Perangkat: _________________
- Alamat IP Server: _________

## 2. Hasil Konfigurasi

### 2.1 Konfigurasi Server
```
[Salin konfigurasi penting di sini]
```

### 2.2 Hasil Pengujian
| No | Pengujian | Hasil | Keterangan |
|----|-----------|-------|------------|
| 1  | Ping ke server | [✓/×] |            |
| 2  | Koneksi internet | [✓/×] |            |
| 3  | Kecepatan koneksi | [nilai] |           |

## 3. Analisis Masalah
[Deskripsi masalah dan solusi]

## 4. Kesimpulan
[Ringkasan hasil dan pembelajaran]
```

## 🧩 Tantangan Lanjutan
1. Implementasikan autentikasi berbasis sertifikat
2. Konfigurasikan VPN site-to-site antara dua server
3. Tambahkan fitur kill switch
4. Implementasikan load balancing untuk koneksi VPN

## 📚 Referensi
1. [StrongSwan Documentation](https://wiki.strongswan.org/)
2. [IKEv2 VPN Setup Guide](https://help.ubuntu.com/community/StrongSwan)
3. [IPsec VPN Best Practices](https://www.nist.gov/)

---
<div align="center">
  <p>Panduan Praktikum - VPN dan IPsec</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

# 📚 Referensi Cepat - VPN dan IPsec

## 📋 Daftar Isi
1. [Perintah Dasar](#-perintah-dasar)
2. [Port dan Protokol](#-port-dan-protokol)
3. [Algoritma Kriptografi](#-algoritma-kriptografi)
4. [File Konfigurasi](#-file-konfigurasi)
5. [Troubleshooting](#-troubleshooting)
6. [Best Practices](#-best-practices)
7. [Sumber Daya](#-sumber-daya)

---

## 💻 Perintah Dasar

### Manajemen Layanan
```bash
# Restart layanan StrongSwan
sudo systemctl restart strongswan-starter

# Periksa status
sudo ipsec status
sudo ipsec statusall

# Mulai/menghentikan koneksi
sudo ipsec up <connection_name>
sudo ipsec down <connection_name>
```

### Pemantauan
```bash
# Log real-time
sudo journalctl -f -u strongswan-starter

# Statistik koneksi
sudo ipsec status

# Cek SA (Security Associations)
sudo ipsec statusall
```

### Manajemen Sertifikat
```bash
# Generate CA
ipsec pki --gen --type rsa --size 4096 --outform pem > ca-key.pem
ipsec pki --self --ca --lifetime 3650 --in ca-key.pem \
    --type rsa --digest sha256 --dn "CN=VPN CA" --outform pem > ca-cert.pem

# Generate sertifikat server
ipsec pki --gen --type rsa --size 4096 --outform pem > server-key.pem
ipsec pki --pub --in server-key.pem | ipsec pki --issue \
    --lifetime 1825 --cacert ca-cert.pem --cakey ca-key.pem \
    --dn "CN=vpn.example.com" --san vpn.example.com \
    --flag serverAuth --flag ikeIntermediate --outform pem > server-cert.pem
```

---

## 🔌 Port dan Protokol

### Port Umum
| Port | Protokol | Keterangan |
|------|----------|------------|
| 500/udp | IKE | Internet Key Exchange (IKE) |
| 4500/udp | IKE/NAT-T | IKE melalui NAT |
| 1701/udp | L2TP | Layer 2 Tunneling Protocol |
| 1194/udp | OpenVPN | OpenVPN default |
| 1723/tcp | PPTP | Point-to-Point Tunneling |

### Protokol VPN
- **IPsec**: Layanan keamanan lapisan jaringan
- **IKEv1/IKEv2**: Protokol pertukaran kunci
- **L2TP**: Sering dipasangkan dengan IPsec
- **OpenVPN**: Solusi open source yang fleksibel
- **WireGuard**: Protokol modern yang ringan

---

## 🔒 Algoritma Kriptografi

### Enkripsi
| Algoritma | Kekuatan | Keterangan |
|-----------|----------|------------|
| AES-256 | Sangat Kuat | Standar industri |
| AES-128 | Kuat | Lebih cepat dari 256-bit |
| ChaCha20 | Kuat | Alternatif AES yang efisien |
| 3DES | Lemah | Tidak direkomendasikan |

### Integritas
| Algoritma | Keterangan |
|-----------|------------|
| SHA-256 | Direkomendasikan |
| SHA-1 | Tidak aman, hindari |
| MD5 | Sangat tidak aman |

### Pertukaran Kunci
| DH Group | Kekuatan |
|----------|----------|
| 14 | 2048-bit (direkomendasikan) |
| 19 | 256-bit ECDH |
| 20 | 384-bit ECDH |
| 5 | 1536-bit (tidak aman) |

---

## 📁 File Konfigurasi

### StrongSwan
- `/etc/ipsec.conf` - Konfigurasi utama
- `/etc/ipsec.secrets` - Rahasia dan kunci pribadi
- `/etc/ipsec.d/` - Direktori sertifikat
- `/etc/strongswan.conf` - Konfigurasi lanjutan

### OpenVPN
- `/etc/openvpn/server.conf` - Konfigurasi server
- `/etc/openvpn/client/` - Konfigurasi klien
- `/etc/openvpn/easy-rsa/` - Sertifikat dan kunci

### WireGuard
- `/etc/wireguard/wg0.conf` - Konfigurasi interface
- `/etc/wireguard/keys/` - Direktori kunci

---

## 🐛 Troubleshooting

### Masalah Umum
1. **Koneksi Gagal**
   ```bash
   # Periksa log
   sudo journalctl -u strongswan-starter -n 50
   
   # Debug IKE
   sudo ipsec stroke loglevel ike 2
   sudo ipsec restart
   ```

2. **Masalah NAT**
   ```bash
   # Aktifkan NAT-T
   nat_traversal=yes
   
   # Periksa kebijakan NAT
   sudo iptables -t nat -L -n -v
   ```

3. **Masalah DNS**
   ```bash
   # Periksa resolusi DNS
   nslookup example.com
   dig example.com
   
   # Cek konfigurasi DNS
   cat /etc/resolv.conf
   ```

---

## 🛡️ Best Practices

### Keamanan
1. Gunakan IKEv2 bukan IKEv1
2. Aktifkan Perfect Forward Secrecy (PFS)
3. Nonaktifkan protokol yang tidak aman (IKEv1, 3DES, MD5)
4. Gunakan autentikasi berbasis sertifikat
5. Terapkan pembaruan keamanan secara berkala

### Kinerja
1. Gunakan AES-NI untuk akselerasi perangkat keras
2. Sesuaikan parameter MTU untuk menghindari fragmentasi
3. Gunakan kompresi untuk lalu lintas yang dapat dikompresi
4. Pertimbangkan UDP daripada TCP untuk VPN

---

## 📚 Sumber Daya

### Dokumentasi
- [StrongSwan Wiki](https://wiki.strongswan.org/)
- [OpenVPN Documentation](https://openvpn.net/community-resources/)
- [WireGuard Documentation](https://www.wireguard.com/)
- [RFC 7296 - IKEv2](https://tools.ietf.org/html/rfc7296)

### Alat Online
- [IPsec Analyzer](https://www.ipsec.pl/)
- [VPN Comparison](https://thatoneprivacysite.net/vpn-comparison-chart/)
- [Cipher Suite Search](https://ciphersuite.info/)

### Buku dan Tutorial
- "VPNs Illustrated" by Jon C. Snader
- "Network Security with OpenSSL" by John Viega
- "Bulletproof SSL and TLS" by Ivan Ristić

---

## 📖 Glosarium

| Istilah | Deskripsi |
|---------|-----------|
| **IPsec** | Protokol keamanan lapisan jaringan |
| **IKE** | Internet Key Exchange - protokol negosiasi kunci |
| **ESP** | Encapsulating Security Payload - enkripsi IPsec |
| **AH** | Authentication Header - autentikasi IPsec |
| **SA** | Security Association - parameter keamanan koneksi |
| **PFS** | Perfect Forward Secrecy - keamanan maju sempurna |
| **NAT-T** | NAT Traversal - mekanisme melewati NAT |
| **DPD** | Dead Peer Detection - deteksi koneksi putus |

---
<div align="center">
  <p>Dokumen Referensi - VPN dan IPsec</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

# 📚 Latihan Soal - VPN dan IPsec

## 🎯 Tujuan Latihan
- Memahami konsep dasar VPN dan IPsec
- Menganalisis konfigurasi VPN
- Memecahkan masalah koneksi VPN
- Menerapkan praktik keamanan terbaik

## 📝 Soal Teori

### Soal 1: Konsep Dasar
1. Jelaskan perbedaan antara mode Transport dan Tunnel pada IPsec!
2. Mengapa autentikasi berbasis sertifikat lebih aman dibandingkan username/password?
3. Apa yang dimaksud dengan Perfect Forward Secrecy (PFS) dan mengapa penting?

### Soal 2: Analisis Kasus
4. Sebuah perusahaan memiliki kantor cabang di 3 lokasi berbeda. Setiap kantor memiliki:
   - 20-30 pengguna
   - Layanan file sharing internal
   - Aplikasi berbasis web
   
   Rancang solusi VPN yang sesuai dengan kebutuhan tersebut!

5. Analisis konfigurasi IPsec berikut:
   ```
   conn myvpn
       left=192.168.1.1
       leftsubnet=10.0.1.0/24
       right=203.0.113.2
       rightsubnet=10.0.2.0/24
       ike=aes256-sha2_256-modp2048
       esp=aes256-sha2_256
       keyexchange=ikev2
       auto=start
   ```
   a. Apa fungsi dari setiap parameter?
   b. Identifikasi potensi masalah keamanan!
   c. Berikan rekomendasi perbaikan!

## 💻 Soal Praktik

### Latihan 1: Analisis Lalu Lintas VPN
1. Capture lalu lintas VPN menggunakan Wireshark
2. Identifikasi protokol yang digunakan
3. Analisis proses handshake IKEv2
4. Verifikasi enkripsi yang digunakan

**Contoh Output:**
```
1. Protokol Teridentifikasi:
   - IKEv2 (UDP/500, UDP/4500)
   - ESP (IP Protocol 50)

2. Proses Handshake:
   - IKE_SA_INIT
   - IKE_AUTH
   - CREATE_CHILD_SA

3. Parameter Kriptografi:
   - Enkripsi: AES-256
   - Integritas: SHA-256
   - DH Group: 14 (2048-bit)
```

### Latihan 2: Konfigurasi Dasar
Buat konfigurasi IPsec untuk skenario berikut:
- Site A: 192.168.1.0/24
- Site B: 192.168.2.0/24
- Menggunakan IKEv2 dengan sertifikat
- Enkripsi AES-256, SHA-256
- Perfect Forward Secrecy dengan DH Group 14

### Latihan 3: Troubleshooting
Diberikan skenario:
- Koneksi VPN terputus setiap 5 menit
- Kecepatan transfer lambat
- Beberapa aplikasi tidak bisa terkoneksi

Langkah pemecahan masalah:
1. Analisis log
2. Periksa konfigurasi timeout
3. Verifikasi MTU
4. Periksa kebijakan firewall

## 🧩 Tantangan Lanjutan

### Tantangan 1: Load Balancing VPN
Implementasikan load balancing untuk koneksi VPN dengan:
- 2+ server VPN
- Failover otomatis
- Pembagian beban seimbang

### Tantangan 2: VPN over Tor
Buat konfigurasi untuk:
- Mengarahkan lalu lintas VPN melalui Tor
- Mempertahankan anonimitas
- Mengatasi tantangan performa

## 📝 Jawaban

### Kunci Jawaban Soal Teori

#### Soal 1:
1. **Perbedaan Mode Transport dan Tunnel**:
   - **Transport Mode**: Hanya mengenkripsi payload, header asli tetap, cocok untuk host-to-host
   - **Tunnel Mode**: Mengenkripsi seluruh paket, menambahkan header baru, cocok untuk gateway-to-gateway

2. **Autentikasi Sertifikat vs Username/Password**:
   - Sertifikat menggunakan kriptografi asimetris
   - Tidak ada rahasia bersama yang dikirim melalui jaringan
   - Perlindungan terhadap serangan phishing
   - Dapat dicabut (revocation)

3. **Perfect Forward Secrecy**:
   - Setiap sesi menggunakan kunci unik
   - Jika satu kunci terkompromikan, sesi lain tetap aman
   - Mencegah decrypt massal lalu lintas yang terekam

#### Soal 2:
4. **Solusi VPN Perusahaan**:
   - Site-to-site IPsec antara kantor
   - Remote access VPN untuk pekerja jarak jauh
   - QoS untuk prioritas lalu lintas penting
   - Redundansi koneksi

5. **Analisis Konfigurasi**:
   a. **Fungsi Parameter**:
      - `left`: Alamat IP lokal
      - `leftsubnet`: Subnet yang dilindungi lokal
      - `right`: Alamat IP remote
      - `rightsubnet`: Subnet remote yang diakses
      - `ike/esp`: Algoritma enkripsi dan integritas
      
   b. **Masalah Keamanan**:
      - Tidak ada konfigurasi lifetime
      - Tidak ada PFS (Perfect Forward Secrecy)
      - Tidak ada konfigurasi DPD (Dead Peer Detection)
      
   c. **Rekomendasi**:
      ```
      conn myvpn
          ...
          ike=aes256-sha2_256-modp2048
          esp=aes256-sha2_256
          keyexchange=ikev2
          keyingtries=%forever
          ikelifetime=24h
          lifetime=1h
          rekey=yes
          reauth=no
          dpddelay=30s
          dpdtimeout=150s
          dpdaction=restart
          closeaction=restart
          leftauth=pubkey
          rightauth=pubkey
          leftcert=server-cert.pem
          rightcert=client-cert.pem
          auto=start
      ```

## 📚 Referensi
1. [StrongSwan Documentation](https://wiki.strongswan.org/)
2. [RFC 7296 - IKEv2 Protocol](https://tools.ietf.org/html/rfc7296)
3. [NIST SP 800-77 - Guide to IPsec VPNs](https://csrc.nist.gov/)
4. [OpenVPN Documentation](https://openvpn.net/community-resources/)

---
<div align="center">
  <p>Dokumen Latihan - VPN dan IPsec</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

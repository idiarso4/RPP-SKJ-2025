# 📚 Referensi Cepat - Keamanan IoT

## 📋 Daftar Isi
1. [Tools Penting](#-tools-penting)
2. [Perintah Dasar](#-perintah-dasar)
3. [Kerentanan Umum](#-kerentanan-umum)
4. [Best Practices](#-best-practices)
5. [Sumber Daya](#-sumber-daya)
6. [Glosarium](#-glosarium)

---

## 🛠️ Tools Penting

### 1. Pemindaian Jaringan
- **Nmap** - Pemindai port dan layanan
- **Masscan** - Pemindai port cepat
- **ZMap** - Pemetaan jaringan internet

### 2. Analisis Keamanan
- **Wireshark** - Analisis protokol jaringan
- **TShark** - Versi CLI dari Wireshark
- **Burp Suite** - Testing keamanan aplikasi web

### 3. Pengujian Keamanan IoT
- **RouterSploit** - Framework eksploitasi perangkat IoT
- **Firmware Analysis Toolkit** - Analisis firmware
- **Binwalk** - Ekstraksi firmware

### 4. Pemantauan Jaringan
- **Zeek** - Analisis lalu lintas jaringan
- **Snort** - Sistem deteksi intrusi
- **Suricata** - IDS/IPS open source

---

## 💻 Perintah Dasar

### Nmap
```bash
# Pemindaian dasar
nmap -sV -sC <target_ip>

# Deteksi OS dan versi
nmap -A -T4 <target_ip>

# Pemindaian UDP
nmap -sU -p 1-1000 <target_ip>

# Deteksi kerentanan
nmap --script vuln <target_ip>
```

### Wireshark/TShark
```bash
# Capture ke file
sudo tshark -i eth0 -w capture.pcap

# Filter protokol IoT
tshark -r capture.pcap -Y "mqtt || coap || http"

# Ekstrak kredensial
tshark -r capture.pcap -Y "http.authbasic" -T fields -e http.authorization
```

### RouterSploit
```bash
# Menjalankan RouterSploit
./rsf.py

# Mencari eksploit untuk perangkat tertentu
use scanners/autopwn
set target <target_ip>
run
```

---

## 🚨 Kerentanan Umum

### 1. Kredensial Default
- **Deskripsi**: Penggunaan kredensial default
- **Dampak**: Akses tidak sah ke perangkat
- **Contoh**: admin:admin, root:root

### 2. Layanan yang Tidak Aman
- **Port Umum**: 23/tcp (Telnet), 80/tcp (HTTP), 554/tcp (RTSP)
- **Risiko**: Ekspos layanan ke internet

### 3. Firmware yang Tidak Diupdate
- **Masalah**: Bug keamanan yang tidak terpatch
- **Solusi**: Update berkala

### 4. Komunikasi Tidak Terenkripsi
- **Protokol Tidak Aman**: HTTP, Telnet, FTP
- **Protokol Aman**: HTTPS, SSH, SFTP

---

## 🛡️ Best Practices

### 1. Keamanan Perangkat
- Ubah kredensial default
- Nonaktifkan layanan yang tidak diperlukan
- Update firmware secara berkala
- Gunakan autentikasi dua faktor

### 2. Keamanan Jaringan
- Segmentasi jaringan IoT
- Gunakan VLAN terpisah
- Terapkan firewall
- Pantau lalu lintas jaringan

### 3. Pengembangan yang Aman
- Security by design
- Input validation
- Secure coding practices
- Code review

### 4. Respon Insiden
- Buat rencana respons insiden
- Backup data secara berkala
- Dokumentasi kejadian keamanan
- Pelajari dari insiden

---

## 📚 Sumber Daya

### Dokumentasi
- [OWASP IoT Project](https://owasp.org/www-project-internet-of-things/)
- [NIST IoT Security Guidelines](https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program)
- [ENISA IoT Security](https://www.enisa.europa.eu/topics/iot-and-smart-infrastructures/iot)

### Alat Online
- [Shodan](https://www.shodan.io/) - Mesin pencari perangkat IoT
- [Censys](https://censys.io/) - Pencarian aset internet
- [VirusTotal](https://www.virustotal.com/) - Analisis file mencurigakan

### Pelatihan
- [IoT Security Training - PentesterLab](https://pentesterlab.com/)
- [IoT Hacking - HackTheBox](https://academy.hackthebox.com/)
- [Cybrary IoT Security](https://www.cybrary.it/catalog/)

---

## 📖 Glosarium

| Istilah | Deskripsi |
|---------|-----------|
| **IoT** | Internet of Things - Jaringan perangkat fisik yang terhubung |
| **DDoS** | Distributed Denial of Service - Serangan untuk melumpuhkan layanan |
| **Firmware** | Perangkat lunak yang disematkan dalam perangkat keras |
| **OT** | Operational Technology - Teknologi untuk mengelola sistem industri |
| **IIoT** | Industrial IoT - Penerapan IoT di industri |
| **MQTT** | Protokol pesan ringan untuk IoT |
| **CoAP** | Protokol aplikasi terbatas untuk perangkat IoT |
| **Zigbee** | Protokol nirkabel untuk jaringan area pribadi |
| **LoRaWAN** | Protokol jaringan area luas untuk IoT |
| **Zero Trust** | Model keamanan yang memverifikasi setiap permintaan |

---
<div align="center">
  <p>Dokumen Referensi - Keamanan IoT</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

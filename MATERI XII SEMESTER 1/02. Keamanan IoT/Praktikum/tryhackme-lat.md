echo "# 🛡️ Latihan Keamanan IoT - TryHackMe Style

## 🎯 Tujuan Pembelajaran
- Menerapkan teknik keamanan IoT secara praktis
- Menganalisis kerentanan pada perangkat IoT
- Menerapkan prinsip keamanan berbasis OWASP IoT Top 10
- Melakukan pengujian penetrasi dasar pada perangkat IoT

## 📋 Prasyarat
- VirtualBox/VMware
- Kali Linux (atau distro security lainnya)
- Perangkat IoT (Raspberry Pi/ESP32/Arduino)
- Tools: Nmap, Wireshark, Burp Suite, Shodan

---

## 🔍 Modul 1: Analisis Jaringan IoT

### 🎯 Tujuan
Menganalisis lalu lintas jaringan perangkat IoT dan mengidentifikasi kerentanan

### 🛠️ Alat yang Dibutuhkan
- Wireshark
- Nmap
- Router dengan akses admin

### 📋 Langkah-langkah
1. **Pemetaan Jaringan**
   ```bash
   nmap -sP 192.168.1.0/24
   ```
   Identifikasi alamat IP perangkat IoT di jaringan lokal

2. **Pemindaian Port**
   ```bash
   nmap -sV -sC -p- <IP_TARGET> -oN scan_results.txt
   ```
   Analisis port dan layanan yang terbuka

3. **Analisis Lalu Lintas**
   - Buka Wireshark
   - Tangkap paket dari antarmuka jaringan
   - Filter dengan `ip.addr == <IP_TARGET>`
   - Analisis protokol yang digunakan (HTTP/MQTT/CoAP)

### ❓ Pertanyaan
1. Port apa saja yang terbuka pada perangkat target?
2. Protokol komunikasi apa yang digunakan perangkat?
3. Apakah ditemukan kredensial yang dikirim secara plaintext?

---

## 🛡️ Modul 2: Eksploitasi Web Interface

### 🎯 Tujuan
Mengidentifikasi dan mengeksploitasi kerentanan pada antarmuka web perangkat IoT

### 🛠️ Alat yang Dibutuhkan
- Burp Suite
- Browser web
- Dirb/Dirbuster

### 📋 Langkah-langkah
1. **Enumeration**
   ```bash
   dirb http://<IP_TARGET> /usr/share/wordlists/dirb/common.txt -o dirb_scan.txt
   ```

2. **Analisis Form Login**
   - Gunakan Burp Suite untuk intercept request login
   - Coba kredensial default (admin:admin, admin:password, dll)
   - Uji SQL Injection:
     ```
     Username: admin' OR '1'='1
     Password: anything
     ```

3. **XSS Testing**
   ```html
   <script>alert('XSS')</script>
   ```
   Uji pada form input yang tersedia

### ❓ Pertanyaan
1. Halaman web apa saja yang ditemukan?
2. Apakah kredensial default berhasil digunakan?
3. Apakah ditemukan kerentanan XSS atau SQL Injection?

---

## 📡 Modul 3: Keamanan Nirkabel IoT

### 🎯 Tujuan
Menganalisis keamanan koneksi nirkabel perangkat IoT

### 🛠️ Alat yang Dibutuhkan
- Aircrack-ng suite
- Wireshark
- Adapter WiFi yang mendukung monitor mode

### 📋 Langkah-langkah
1. **Monitor Mode**
   ```bash
   airmon-ng start wlan0
   ```

2. **Capture Handshake**
   ```bash
   airodump-ng -c <channel> --bssid <BSSID> -w capture wlan0mon
   ```

3. **Deauthentication Attack**
   ```bash
   aireplay-ng --deauth 10 -a <BSSID> wlan0mon
   ```

4. **Crack Password**
   ```bash
   aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
   ```

### ❓ Pertanyaan
1. Protokol keamanan apa yang digunakan jaringan?
2. Berapa lama waktu yang dibutuhkan untuk mendapatkan handshake?
3. Seberapa kuat password yang digunakan?

---

## 🧩 Modul 4: Firmware Analysis

### 🎯 Tujuan
Menganalisis firmware perangkat IoT untuk menemukan kerentanan

### 🛠️ Alat yang Dibutuhkan
- Binwalk
- Firmware Analysis Toolkit (FAT)
- Ghidra/IDA Pro

### 📋 Langkah-langkah
1. **Ekstrak Firmware**
   ```bash
   binwalk -Me firmware.bin
   ```

2. **Analisis File System**
   ```bash
   cd _firmware.bin.extracted
   find . -type f -exec file {} \;
   ```

3. **Cari Kredensial**
   ```bash
   grep -r "password\\|passwd\\|pwd\\|user\\|admin" .
   ```

### ❓ Pertanyaan
1. File system apa yang digunakan?
2. Apakah ditemukan kredensial hardcoded?
3. Komponen apa saja yang rentan berdasarkan versinya?

---

## 🏆 Tantangan Akhir: CTF IoT

### 🎯 Tujuan
Menerapkan semua teknik yang telah dipelajari untuk menyelesaikan tantangan CTF

### 🎯 Target
Perangkat IoT yang telah disiapkan dengan beberapa flag tersembunyi

### 📋 Tantangan
1. Dapatkan akses shell pada perangkat
2. Temukan file flag.txt
3. Dapatkan akses root
4. Analisis lalu lintas jaringan untuk menemukan flag tersembunyi

### 💡 Petunjuk
- Gunakan teknik enumerasi yang tepat
- Periksa layanan yang berjalan pada port tidak biasa
- Analisis kredensial default

---

## 📝 Laporan Praktikum
1. Dokumentasikan setiap langkah yang dilakukan
2. Screenshot penting sebagai bukti
3. Analisis temuan kerentanan
4. Rekomendasi perbaikan

## 🔗 Referensi
1. [OWASP IoT Top 10](https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf)
2. [IoT Pentesting Guide](https://www.hackers-arise.com/iot)
3. [TryHackMe IoT Rooms](https://tryhackme.com/hacktivities?tab=search&search=iot)

---

<div align="center">
  <p>Latihan Keamanan IoT - Praktikum</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>" > "C:\Users\IDTek\Desktop\Materi\RPP-SKJ-2025\MATERI XII SEMESTER 1\02. Keamanan IoT\Praktikum\tryhackme-lat.md"
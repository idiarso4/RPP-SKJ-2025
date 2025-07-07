# 📝 Asesmen: Keamanan Jaringan Nirkabel dan IoT

## 🎯 Kompetensi Dasar
3.18 Menganalisis keamanan jaringan nirkabel
3.19 Menerapkan pengujian keamanan perangkat IoT
3.20 Melakukan pengamanan jaringan nirkabel dan perangkat IoT

## 📝 Soal Pilihan Ganda

### 1. Manakah yang BUKAN termasuk protokol keamanan Wi-Fi?
   a) WEP  
   b) WPA  
   c) WPS  
   d) WPA3  
   
   **Jawaban: c) WPS**  
   *Pembahasan: WPS (Wi-Fi Protected Setup) adalah fitur keamanan, bukan protokol enkripsi. Protokol keamanan Wi-Fi meliputi WEP, WPA, WPA2, dan WPA3.*

### 2. Manakah pernyataan yang BENAR tentang serangan Evil Twin?
   a) Hanya membutuhkan perangkat dengan mode monitor  
   b) Menciptakan jaringan Wi-Fi palsu dengan SSID yang sama  
   c) Tidak dapat dideteksi oleh pengguna biasa  
   d) Hanya bekerja pada jaringan terbuka  
   
   **Jawaban: b) Menciptakan jaringan Wi-Fi palsu dengan SSID yang sama**  
   *Pembahasan: Serangan Evil Twin melibatkan pembuatan titik akses palsu dengan SSID yang sama dengan jaringan asli untuk menipu pengguna agar terhubung.*

### 3. Manakah yang BUKAN termasuk kerentanan umum pada perangkat IoT?
   a) Kredensial default  
   b) Pembaruan keamanan otomatis  
   c) Komunikasi tidak terenkripsi  
   d) Port terbuka yang tidak perlu  
   
   **Jawaban: b) Pembaruan keamanan otomatis**  
   *Pembahasan: Pembaruan keamanan otomatis adalah fitur keamanan, bukan kerentanan. Kebanyakan perangkat IoT justru tidak memiliki mekanisme pembaruan yang memadai.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara WPA2 dan WPA3, serta mengapa WPA3 dianggap lebih aman?

**Jawaban:**

**Perbedaan Utama WPA2 vs WPA3:**

| Aspek | WPA2 | WPA3 |
|-------|------|------|
| **Enkripsi** | AES-CCMP | AES-256-GCM |
| **Handshake** | 4-way handshake (rentan KRACK) | SAE (Simultaneous Authentication of Equals) |
| **Keamanan Jaringan Terbuka** | Tidak ada enkripsi | Opportunistic Wireless Encryption (OWE) |
| **Forward Secrecy** | Tidak ada | Ada |
| **Perlindungan Brute Force** | Rentan terhadap serangan kamus | Proteksi terhadap serangan kamus offline |

**Alasan WPA3 Lebih Aman:**

1. **Proteksi terhadap Serangan Offline**
   - WPA3 menggunakan SAE yang mencegah penyerang melakukan serangan kamus offline
   - Setiap upaya autentikasi memerlukan interaksi dengan jaringan

2. **Enkripsi yang Lebih Kuat**
   - Menggunakan AES-256-GCM yang lebih aman dibanding AES-CCMP
   - Menerapkan enkripsi 192-bit untuk penggunaan enterprise

3. **Perlindungan Jaringan Terbuka**
   - OWE menyediakan enkripsi bahkan untuk jaringan terbuka
   - Mencegah serangan eavesdropping di tempat umum

4. **Forward Secrecy**
   - Jika kunci utama berhasil dicuri, komunikasi masa lalu tetap aman
   - Setiap sesi memiliki kunci enkripsi unik

5. **Proteksi Konfigurasi**
   - Meningkatkan keamanan untuk perangkat IoT yang sulit dikonfigurasi
   - Mengurangi risiko konfigurasi yang tidak aman

### 2. Jelaskan apa yang dimaksud dengan serangan "Man-in-the-Middle" (MITM) pada jaringan nirkabel, bagaimana cara mendeteksinya, dan langkah-langkah pencegahannya!

**Jawaban:**

**Pengertian Serangan MITM:**
Serangan Man-in-the-Middle (MITM) adalah teknik di mana penyerang menyisipkan diri di antara dua pihak yang berkomunikasi, memungkinkan mereka memantau, mengubah, atau mencuri data yang dikirimkan.

**Cara Kerja di Jaringan Nirkabel:**
1. **ARP Spoofing/Poisoning**
   - Penyerang mengirim balasan ARP palsu ke korban dan router
   - Lalu lintas korban dialihkan melalui perangkat penyerang

2. **Evil Twin**
   - Membuat titik akses palsu dengan SSID yang sama
   - Pengguna terhubung ke jaringan penyerang tanpa menyadarinya

3. **DNS Spoofing**
   - Mengalihkan lalu lintas DNS ke server palsu
   - Pengguna diarahkan ke situs web palsu

**Cara Mendeteksi Serangan MITM:**

1. **Analisis Jaringan**
   ```bash
   # Periksa tabel ARP untuk entri ganda
   arp -a
   
   # Gunakan Wireshark untuk mendeteksi ARP spoofing
   # Filter: arp.duplicate-address-detected
   ```

2. **Pemantauan Sinyal**
   ```bash
   # Deteksi perubahan BSSID atau kekuatan sinyal
   sudo airodump-ng wlan0mon
   ```

3. **Alat Khusus**
   ```bash
   # Gunakan arpwatch untuk memantau perubahan ARP
   sudo arpwatch -i eth0
   
   # Atau bettercap untuk deteksi lanjutan
   sudo bettercap -iface eth0 -caplet hstshijack/hstshijack
   ```

**Langkah Pencegahan:**

1. **Gunakan Koneksi Aman**
   ```bash
   # Selalu gunakan VPN
   sudo openvpn --config client.ovpn
   ```

2. **Aktifkan Perlindungan ARP**
   ```bash
   # Di Linux
   echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
   echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce
   ```

3. **Gunakan HTTPS dan HSTS**
   ```bash
   # Di server web
   add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
   ```

4. **Konfigurasi Keamanan Router**
   ```bash
   # Nonaktifkan fitur yang tidak perlu
   uci set wireless.@wifi-iface[0].wps_pushbutton='0'
   uci set wireless.@wifi-iface[0].isolate='1'
   uci commit
   ```

5. **Monitor Jaringan**
   ```bash
   # Gunakan IDS/IPS
   sudo snort -i eth0 -c /etc/snort/snort.conf
   ```

## 📝 Studi Kasus: Keamanan Jaringan Nirkabel Perusahaan

**Latar Belakang:**
Sebuah perusahaan menengah dengan 100 karyawan memiliki jaringan nirkabel dengan konfigurasi sebagai berikut:
- SSID: CorpNet
- Keamanan: WPA2-Personal
- Password: company123
- Jangkauan: Seluruh area kantor
- Perangkat: 5 access point dengan konfigurasi identik

Beberapa hari terakhir, kecepatan jaringan menurun drastis dan beberapa karyawan mengeluhkan masalah koneksi yang tidak stabil.

**Pertanyaan:**
1. Analisis potensi masalah keamanan pada konfigurasi jaringan tersebut!
2. Jelaskan langkah-langkah yang akan Anda lakukan untuk mengamankan jaringan tersebut!
3. Buat rekomendasi kebijakan keamanan nirkabel untuk perusahaan!

**Jawaban Contoh:**

### 1. Analisis Masalah Keamanan

**Kerentanan Utama:**
1. **Password Lemah**
   - Password "company123" sangat mudah ditebak
   - Tidak ada kompleksitas karakter
   
2. **Menggunakan WPA2-Personal**
   - Rentan terhadap serangan offline
   - Tidak ada autentikasi individual
   
3. **Konfigurasi Identik**
   Semua access point menggunakan konfigurasi yang sama, meningkatkan risiko jika salah satu berhasil dibobol

4. **Tidak Ada Segmentasi Jaringan**
   Semua perangkat berada dalam jaringan yang sama
   
5. **Tidak Ada Monitoring**
   Tidak terdeteksinya aktivitas mencurigakan

### 2. Langkah Pengamanan

**Segera (Hari Ini):**
```bash
# 1. Ganti password menjadi yang lebih kuat
for ap in ap1 ap2 ap3 ap4 ap5; do
    ssh admin@$ap "configure terminal\nwpa-passphrase CorpNet 'N3w$tr0ngP@ss!2025'\nwrite memory\nexit"
done

# 2. Nonaktifkan WPS
for ap in ap1 ap2 ap3 ap4 ap5; do
    ssh admin@$ap "configure terminal\nno wps enable\nwrite memory\nexit"
done
```

**Jangka Pendek (Minggu Ini):**
1. **Implementasikan WPA3-Enterprise**
   ```bash
   # Contoh konfigurasi RADIUS
   apt install freeradius freeradius-mysql
   mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql
   ```

2. **Segmentasi Jaringan**
   ```bash
   # Buat VLAN terpisah
   vlan 10
    name Staff
    exit
   vlan 20
    name Guest
    exit
   ```

3. **Aktifkan Fitur Keamanan Tambahan**
   ```bash
   # Contoh di Cisco
   wlan CorpNet_Staff
    security wpa akm dot1x
    security wpa dot1x cipher aes
    security ft over-the-ds
    no security wpa wpa2 ciphers tkip
    exit
   ```

**Jangka Panjang (Bulan Ini):**
1. **Deploy Sistem Monitoring**
   ```bash
   # Install Security Onion
   sudo apt-add-repository -y ppa:securityonion/stable
   sudo apt update
   sudo apt install securityonion-all
   ```

2. **Audit dan Pelatihan**
   - Audit keamanan berkala
   - Pelatihan kesadaran keamanan untuk karyawan

### 3. Rekomendasi Kebijakan Keamanan

**Kebijakan Akses Nirkabel:**
1. **Autentikasi**
   - Wajib menggunakan WPA3-Enterprise
   - Multi-Factor Authentication untuk akses administratif
   - Sertifikat digital untuk perangkat perusahaan

2. **Enkripsi**
   - WPA3 dengan AES-256-GCM
   - Wajib HTTPS untuk semua layanan internal
   - VPN untuk akses jarak jauh

3. **Segmentasi Jaringan**
   - VLAN terpisah untuk departemen
   - Jaringan tamu yang terisolasi
   - Zona keamanan untuk perangkat IoT

4. **Monitoring dan Respon**
   - Sistem deteksi intrusi (IDS/IPS)
   - Logging terpusat
   - Respons insiden yang terdefinisi

5. **Pembaruan dan Pemeliharaan**
   - Patch keamanan rutin
   - Audit keamanan berkala
   - Backup konfigurasi terenkripsi

## 📝 Tugas Praktik: Audit Keamanan Nirkabel

### Instruksi:
1. Lakukan audit keamanan pada jaringan nirkabel yang telah ditentukan
2. Identifikasi kerentanan menggunakan tools yang tersedia
3. Buat laporan temuan beserta rekomendasi perbaikan

### Format Laporan:

1. **Informasi Umum**
   - Nama Jaringan
   - Lokasi
   - Tanggal Audit
   - Tim Auditor

2. **Metodologi**
   - Tools yang Digunakan
   - Lingkungan Pengujian
   - Ruang Lingkup

3. **Temuan**
   ```
   ### 1. [Nama Kerentanan]
   - **Tingkat Keparahan**: [High/Medium/Low]
   - **Deskripsi**: [Jelaskan kerentanan]
   - **Dampak**: [Jelaskan dampak potensial]
   - **Rekomendasi**: [Berikan rekomendasi perbaikan]
   - **Referensi**: [OWASP, CVE, dll.]
   ```

4. **Kesimpulan dan Rekomendasi**
   - Ringkasan temuan
   - Rekomendasi prioritas tinggi
   - Rencana tindak lanjut

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kelengkapan Audit | 25% | Semua aspek penting tercakup |
| Kedalaman Analisis | 30% | Kedalaman analisis setiap temuan |
| Rekomendasi | 25% | Kualitas dan relevansi rekomendasi |
| Dokumentasi | 20% | Kerapian dan kejelasan laporan |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. c) WPS
2. b) Menciptakan jaringan Wi-Fi palsu dengan SSID yang sama
3. b) Pembaruan keamanan otomatis

### Pedoman Penskoran Esai
1. **Kelengkapan Jawaban** (40%): Semua poin penting tercakup
2. **Ketepatan Konsep** (30%): Penjelasan konsep yang akurat
3. **Contoh Implementasi** (20%): Contoh yang diberikan relevan dan aplikatif
4. **Struktur Jawaban** (10%): Sistematika penyampaian yang baik

## 📚 Referensi
1. OWASP Wireless Security Guide: https://owasp.org/www-project-wireless-security/
2. NIST Guidelines for Securing Wireless Networks: https://csrc.nist.gov/
3. Wi-Fi Alliance Security: https://www.wi-fi.org/security
4. ENISA IoT Security Guidelines: https://www.enisa.europa.eu/

---
<div align="center">
  <p>Dokumen Asesmen - Keamanan Jaringan Nirkabel dan IoT</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

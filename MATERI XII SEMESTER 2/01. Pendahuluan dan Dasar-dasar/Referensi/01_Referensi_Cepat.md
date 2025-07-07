# 📚 Referensi Cepat - Keamanan Siber Dasar

## 🔑 Konsep Dasar

### 1. CIA Triad
```
Confidentiality (Kerahasiaan)
├─ Enkripsi data
├─ Kontrol akses
└─ Otentikasi kuat

Integrity (Integritas)
├─ Checksum
├─ Digital signature
└─ Hash functions

Availability (Ketersediaan)
├─ Redundansi
├─ Backup
└─ Proteksi DDoS
```

### 2. Jenis-jenis Hacker
| Tipe | Deskripsi | Contoh Aktivitas |
|------|-----------|------------------|
| 🤍 White Hat | Ethical, legal | Penetration testing |
| 🖤 Black Hat | Kriminal | Pencurian data |
| 💜 Grey Hat | Di antaranya | Report vuln tanpa izin |
| 💙 Blue Hat | Testing keamanan | Bug bounty |
| 🧒 Script Kiddie | Pemula | Pakai tools orang |

## 🛠️ Tools Penting

### 1. Nmap
```bash
# Scan dasar
nmap -sV <target>

# Scan OS
nmap -O <target>

# Scan cepat
nmap -T4 -F <target>

# Simpan hasil
nmap -oN hasil.txt <target>
```

### 2. Wireshark
```
Filter Umum:
- http          : HTTP traffic
- tcp.port==80  : Port spesifik
- ip.addr==x.x.x.x : IP tertentu
- dns           : DNS queries
- tcp.flags.syn==1 : Koneksi baru
```

### 3. Metasploit Framework
```bash
# Cari modul
search <keyword>

# Gunakan modul
use exploit/...

# Lihat opsi
show options

# Set parameter
set RHOSTS x.x.x.x

# Jalankan
exploit
```

## 📜 Etika & Hukum

### 1. Prinsip Etis
- Dapatkan izin tertulis
- Tetap dalam ruang lingkup yang disepakati
- Laporkan temuan dengan bertanggung jawab
- Jaga kerahasiaan informasi sensitif

### 2. Regulasi Penting
- UU ITE (Pasal 30-37)
- UU PDP (Perlindungan Data Pribadi)
- ISO/IEC 27001
- Permenkominfo 4/2016 (PSE)

## 📚 Sumber Belajar

### 1. Online
- [OWASP](https://owasp.org/)
- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)
- [Cybrary](https://www.cybrary.it/)

### 2. Buku
- "The Web Application Hacker's Handbook"
- "Metasploit: The Penetration Tester's Guide"
- "Hacking: The Art of Exploitation"

## 🔍 Cheat Sheet

### 1. HTTP Response Codes
- 200 OK
- 301 Moved Permanently
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

### 2. Port Umum
```
20/21 - FTP
22    - SSH
23    - Telnet
25    - SMTP
53    - DNS
80    - HTTP
443   - HTTPS
3306  - MySQL
3389  - RDP
```

## 🚨 Pelaporan Kerentanan
```markdown
Judul: [Tingkat Keparahan] Deskripsi Singkat

## Detail
- URL/Lokasi: 
- Deskripsi: 
- Langkah Reproduksi: 
1. Langkah 1
2. Langkah 2
3. ...

## Dampak
- [ ] Kerahasiaan
- [ ] Integritas
- [ ] Ketersediaan

## Bukti
[URL/Screenshot]

## Rekomendasi
- Saran perbaikan
- Referensi
```

## 📅 Timeline Respons
```
Hari 1: Laporan diterima
Hari 2-3: Investigasi
Hari 4-5: Perbaikan
Hari 6: Verifikasi
Hari 7: Rilis patch
```

---
<div align="center">
  <p>Dokumen Referensi - Keamanan Siber Dasar</p>
  <p>© 2025 SMKN 1 Punggelan</p>
  <p>Update Terakhir: 07/07/2025</p>
</div>

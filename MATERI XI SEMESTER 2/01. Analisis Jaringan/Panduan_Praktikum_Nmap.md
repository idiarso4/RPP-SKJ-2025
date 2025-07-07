# 🛠️ Panduan Praktikum Nmap

## Pendahuluan
Panduan ini akan membantu Anda memahami dan menggunakan Nmap (Network Mapper) untuk melakukan analisis jaringan. Nmap adalah alat open-source yang digunakan untuk penemuan jaringan dan audit keamanan.

## Persyaratan
- Komputer dengan OS Linux/Windows
- Nmap terinstal
- Akses ke jaringan yang diizinkan untuk di-scan
- Izin dari administrator jaringan

## Instalasi Nmap

### Windows
1. Unduh installer dari [nmap.org](https://nmap.org/download.html)
2. Jalankan installer dan ikuti petunjuk
3. Verifikasi instalasi dengan membuka Command Prompt dan ketik:
   ```
   nmap --version
   ```

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install nmap
```

## Dasar-dasar Nmap

### 1. Scanning Host Tunggal
```bash
nmap <target_ip>
```
Contoh:
```bash
nmap 192.168.1.1
```

### 2. Scanning Multiple Hosts
```bash
nmap 192.168.1.1 192.168.1.2 192.168.1.3
# Atau menggunakan range
nmap 192.168.1.1-10
# Atau subnet
nmap 192.168.1.0/24
```

### 3. Jenis-jenis Scan

#### TCP Connect Scan
```bash
nmap -sT <target>
```
- Melakukan koneksi TCP penuh
- Mudah terdeteksi
- Tidak membutuhkan hak akses root

#### SYN Stealth Scan
```bash
nmap -sS <target>
```
- Hanya mengirim paket SYN
- Lebih cepat dan lebih tersembunyi
- Membutuhkan hak akses root

#### UDP Scan
```bash
nmap -sU <target>
```
- Untuk menemukan layanan UDP
- Lebih lambat dari TCP scan

### 4. Deteksi Versi Layanan
```bash
nmap -sV <target>
```
- Mengidentifikasi versi layanan yang berjalan
- Berguna untuk menemukan kerentanan

### 5. Output ke File
```bash
nmap -oN hasil_scan.txt <target>        # Format normal
nmap -oX hasil_scan.xml <target>        # Format XML
nmap -oG hasil_scan.gnmap <target>      # Format greppable
```

## Teknik Lanjutan

### 1. Scripting Engine (NSE)
```bash
nmap --script=<script> <target>
```
Contoh:
```bash
nmap --script=http-title <target>        # Mendapatkan judul halaman web
nmap --script=vuln <target>              # Scan kerentanan dasar
nmap --script=smb-os-discovery <target>  # Mendeteksi OS via SMB
```

### 2. Timing dan Performa
```
-T0 (Paranoid)   : Sangat lambat, menghindari IDS
-T1 (Sneaky)     : Sangat lambat
-T2 (Polite)     : Lambat, mengurangi beban jaringan
-T3 (Normal)     : Default, seimbang
-T4 (Aggressive) : Cepat, untuk jaringan cepat
-T5 (Insane)     : Sangat cepat, mungkin tidak akurat
```

### 3. Firewall/IDS Evasion
```bash
nmap -f <target>                        # Fragmentasi paket
nmap --mtu 16 <target>                  # Mengatur ukuran MTU
nmap -D RND:5 <target>                  # Decoy scan
nmap --source-port 53 <target>          # Spoofing port sumber
nmap --data-length 200 <target>         # Menambahkan data acak
```

## Praktikum

### Latihan 1: Pemetaan Jaringan Dasar
1. Lakukan scanning terhadap jaringan lokal Anda
2. Identifikasi perangkat yang aktif
3. Catat alamat IP dan layanan yang berjalan

### Latihan 2: Analisis Layanan
1. Pilih satu target dari hasil scan sebelumnya
2. Lakukan version detection
3. Identifikasi versi OS dan layanan yang berjalan
4. Analisis potensi kerentanan

### Latihan 3: Penggunaan NSE
1. Gunakan script NSE untuk memeriksa kerentanan umum
2. Dokumentasikan temuan Anda
3. Berikan rekomendasi pengamanan

## Keamanan dan Etika
1. **Selalu dapatkan izin** sebelum melakukan scanning
2. Hanya scan jaringan yang menjadi tanggung jawab Anda
3. Patuhi kebijakan keamanan organisasi
4. Dokumentasikan setiap aktivitas scanning

## Troubleshooting

### Nmap tidak terdeteksi
- Pastikan Nmap terinstal dengan benar
- Periksa PATH environment variable
- Restart terminal/command prompt

### Scan terlalu lambat
- Gunakan parameter timing yang lebih agresif (-T4)
- Kurangi jumlah port yang di-scan (-p)
- Pastikan koneksi jaringan stabil

## Referensi
1. [Nmap Official Documentation](https://nmap.org/docs.html)
2. [Nmap Network Scanning](https://nmap.org/book/)
3. [Nmap Cheat Sheet](https://www.stationx.net/nmap-cheat-sheet/)

---

<div align="center">
  <p>Dokumen ini merupakan bagian dari materi praktikum Analisis Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - All Rights Reserved</p>
</div>

# 📚 Panduan Praktikum Nmap

## 🎯 Tujuan Praktikum
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menginstal dan mengkonfigurasi Nmap
2. Melakukan scanning jaringan dasar
3. Menganalisis hasil scanning
4. Mendokumentasikan temuan

## 🛠️ Alat dan Bahan
1. Komputer dengan OS Windows/Linux
2. Koneksi jaringan
3. VirtualBox/VMware (opsional)
4. Target mesin untuk di-scan (dapat menggunakan localhost)

## 📋 Langkah Kerja

### A. Instalasi Nmap

#### Untuk Windows:
1. Unduh installer Nmap dari [situs resmi](https://nmap.org/download.html)
2. Jalankan installer dan ikuti petunjuk
3. Verifikasi instalasi dengan membuka Command Prompt dan ketik:
   ```bash
   nmap --version
   ```

#### Untuk Linux (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install nmap
```

### B. Dasar-Dasar Nmap

#### 1. Scan Host Tunggal
```bash
nmap [target]
Contoh: nmap 192.168.1.1
```

#### 2. Scan Multiple Hosts
```bash
nmap [target1] [target2] [target3]
Contoh: nmap 192.168.1.1 192.168.1.2 192.168.1.3
```

#### 3. Scan Range IP
```bash
nmap [range-ip]
Contoh: nmap 192.168.1.1-100
```

#### 4. Scan Subnet
```bash
nmap [subnet]
Contoh: nmap 192.168.1.0/24
```

### C. Teknik Scanning

#### 1. TCP SYN Scan (Stealth Scan)
```bash
nmap -sS [target]
```

#### 2. TCP Connect Scan
```bash
nmap -sT [target]
```

#### 3. UDP Scan
```bash
nmap -sU [target]
```

#### 4. OS Detection
```bash
nmap -O [target]
```

#### 5. Service Version Detection
```bash
nmap -sV [target]
```

### D. Output dan Dokumentasi

#### 1. Simpan Hasil ke File Teks
```bash
nmap -oN hasil_scan.txt [target]
```

#### 2. Format XML
```bash
nmap -oX hasil_scan.xml [target]
```

### E. Praktik Terkendali

#### Latihan 1: Pemetaan Jaringan
1. Lakukan scanning terhadap jaringan lokal Anda
2. Identifikasi perangkat yang aktif
3. Catat alamat IP dan layanan yang berjalan

#### Latihan 2: Analisis Layanan
1. Pilih satu alamat IP dari hasil scanning
2. Lakukan deteksi versi layanan
3. Identifikasi potensi kerentanan

## 📝 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum
   - Judul Praktikum

2. **Tujuan Praktikum**
   - Tuliskan tujuan praktikum

3. **Alat dan Bahan**
   - Daftar peralatan yang digunakan

4. **Langkah Kerja**
   - Dokumentasikan langkah-langkah yang dilakukan
   - Sertakan screenshot setiap tahapan

5. **Hasil dan Pembahasan**
   - Tampilkan hasil scanning
   - Analisis hasil yang diperoleh
   - Diskusikan temuan menarik

6. **Kesimpulan**
   - Ringkasan hasil praktikum
   - Kendala yang dihadapi
   - Saran perbaikan

## 🔍 Evaluasi

### Kriteria Penilaian
| No | Aspek | Bobot |
|----|-------|-------|
| 1 | Ketepatan prosedur | 30% |
| 2 | Kelengkapan laporan | 25% |
| 3 | Analisis hasil | 25% |
| 4 | Ketepatan waktu | 20% |

### Soal Evaluasi
1. Jelaskan perbedaan antara TCP SYN Scan dan TCP Connect Scan!
2. Mengapa OS Detection membutuhkan hak akses root/administrator?
3. Bagaimana cara mengidentifikasi port terbuka yang tidak seharusnya terbuka?

## ⚠️ Etika dan Keamanan
1. Hanya lakukan scanning pada jaringan yang Anda miliki atau telah mendapatkan izin
2. Jangan melakukan scanning terhadap jaringan publik tanpa izin
3. Patuhi kebijakan keamanan organisasi
4. Laporkan temuan kerentanan kepada pemilik sistem

## 📚 Referensi
1. Nmap Network Scanning - Gordon Lyon
2. Dokumentasi Resmi Nmap: https://nmap.org/book/
3. Nmap Cheat Sheet: https://www.stationx.net/nmap-cheat-sheet/

## 💡 Tips
- Gunakan parameter `-v` untuk output yang lebih detail
- Gabungkan beberapa opsi untuk hasil yang lebih lengkap
- Selalu dokumentasikan perintah yang digunakan
- Backup hasil scanning untuk referensi mendatang

---
<div align="center">
  <p>Panduan Praktikum Nmap - SMKN 1 Punggelan</p>
  <p>© 2025 Tim Pengajar Keamanan Jaringan</p>
</div>

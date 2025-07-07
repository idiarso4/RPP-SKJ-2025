# 📚 Modul Pelatihan CTF Dasar

## 🎯 Tujuan Pembelajaran
Setelah mengikuti pelatihan ini, peserta mampu:
1. Memahami konsep dasar Capture The Flag (CTF)
2. Menggunakan tools dasar keamanan siber
3. Memecahkan challenge keamanan dasar
4. Bekerja sama dalam tim untuk menyelesaikan tantangan

## 🧩 Jenis Challenge CTF

### 1. Web Exploitation
**Tools yang Digunakan**:
- Burp Suite
- OWASP ZAP
- Browser DevTools

**Contoh Challenge**:
```
Temukan flag yang tersembunyi di halaman web:
http://ctf.smkn1punggelan.sch.id/challenge1
```

**Langkah Penyelesaian**:
1. Inspeksi elemen halaman
2. Periksa source code
3. Analisis request/response
4. Eksploitasi kerentanan yang ditemukan

### 2. Forensik Dasar
**Tools yang Digunakan**:
- Wireshark
- Binwalk
- ExifTool

**Contoh File**:
- capture.pcapng
- gambar_tersembunyi.jpg
- log_terenkripsi.txt

**Teknik Analisis**:
1. Ekstraksi metadata
2. Analisis header file
3. Pencarian string tersembunyi
4. Rekayasa balik sederhana

### 3. Kriptografi Dasar
**Konsep yang Diajarkan**:
- Caesar cipher
- Base64 encoding
- XOR encryption
- Hash functions

**Challenge Contoh**:
```
Dekripsi pesan berikut:
Gur frperg zrffntr vf rapelcgrq
```

### 4. Steganografi
**Tools**:
- Steghide
- Binwalk
- Foremost

**Langkah-langkah**:
1. Identifikasi tipe file
2. Ekstraksi data tersembunyi
3. Analisis bit dan byte
4. Rekayasa balik jika diperlukan

## 🛠️ Panduan Setup Lingkungan

### 1. Virtual Machine
```bash
# Install VirtualBox
sudo apt install virtualbox

# Download Kali Linux
wget https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-netinst-amd64.iso
```

### 2. Tools Penting
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install tools dasar
sudo apt install -y \
  wireshark \
  binwalk \
  steghide \
  john \
  hashcat
```

## 📋 Daftar Challenge Latihan

| No | Kategori | Level | Deskripsi | Flag Format |
|----|----------|-------|-----------|-------------|
| 1 | Web | Mudah | Temukan flag di komentar HTML | CTF{contoh_flag} |
| 2 | Forensik | Menengah | Ekstrak file tersembunyi | CTF{hidden_file} |
| 3 | Kripto | Mudah | Dekripsi pesan Caesar | CTF{pesan_rahasia} |
| 4 | Stegano | Menengah | Temukan pesan dalam gambar | CTF{stego123} |

## 🏆 Sistem Poin
- Challenge mudah: 100 poin
- Challenge menengah: 250 poin
- Challenge sulit: 500 poin
- Challenge ekstrem: 1000 poin

## 📅 Jadwal Pelatihan

### Minggu 1: Pengenalan
- Konsep dasar CTF
- Pengenalan tools
- Challenge dasar

### Minggu 2: Web & Kripto
- Teknik web exploitation
- Dasar kriptografi
- Latihan terstruktur

### Minggu 3: Forensik & Stegano
- Analisis file
- Steganografi dasar
- Pemecahan kasus

### Minggu 4: Kompetisi Mini
- CTF internal
- Pembahasan solusi
- Evaluasi hasil

## 📝 Penilaian
1. Partisipasi (20%)
2. Penyelesaian challenge (50%)
3. Laporan teknikal (30%)

## 📚 Referensi
1. CTF Field Guide
2. OverTheWire Wargames
3. Hack The Box Academy
4. PicoCTF Resources

---
<div align="center">
  <p>Modul Pelatihan CTF Dasar - SMKN 1 Punggelan</p>
  <p>© 2025 Tim Keamanan Siber</p>
</div>

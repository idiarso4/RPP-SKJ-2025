# 📚 Latihan Soal dan Kasus - Konsep Dasar Keamanan Siber

## 🎯 Tujuan
Melatih pemahaman dan kemampuan analisis peserta didik melalui latihan soal dan studi kasus nyata.

## 📝 Latihan Teori

### A. Pilihan Ganda Kompleks

1. **Kerahasiaan Data**
   Seorang administrator sistem menemukan bahwa data karyawan dapat diakses oleh semua pengguna dalam jaringan internal. Prinsip keamanan apa yang dilanggar?
   - [ ] a. Availability
   - [ ] b. Integrity
   - [X] c. Confidentiality
   - [ ] d. Authentication

   **Pembahasan:** Kerahasiaan (Confidentiality) dilanggar karena data yang seharusnya bersifat rahasia dapat diakses oleh pihak yang tidak berwenang.

2. **Etika Hacking**
   Seorang siswa menemukan kerentanan di website sekolah. Tindakan yang TIDAK etis adalah:
   - [ ] a. Melaporkan ke guru/administrator IT
   - [ ] b. Mendokumentasikan temuan dengan detail
   - [X] c. Mengeksploitasi kerentanan untuk membuktikan temuannya
   - [ ] d. Menjaga kerahasiaan temuan

   **Pembahasan:** Mengeksploitasi kerentanan tanpa izin adalah tindakan yang tidak etis dan bisa melanggar hukum.

### B. Analisis Kasus

#### Kasus 1: Insiden Keamanan Sekolah
**Latar Belakang:**
Sekolah XYZ mengalami kebocoran data siswa yang berisi informasi pribadi seperti nama, alamat, dan nilai akademik. Data tersebut ditemukan tersebar di internet.

**Pertanyaan:**
1. Prinsip keamanan apa yang dilanggar?
2. Siapa saja yang mungkin menjadi pihak yang bertanggung jawab?
3. Langkah-langkah apa yang harus diambil untuk mencegah terulangnya kejadian serupa?

**Jawaban Contoh:**
1. Prinsip kerahasiaan (confidentiality) dan privasi data.
2. Tim IT sekolah, penyedia layanan hosting, dan administrator sistem.
3. Enkripsi data, audit keamanan berkala, pelatihan kesadaran keamanan, dan penerapan kebijakan akses yang ketat.

## 🔍 Latihan Praktik

### Latihan 1: Analisis Jaringan Dasar

**Tujuan:** Mengidentifikasi perangkat dalam jaringan lokal

**Alat:** Nmap

**Langkah Kerja:**
1. Buka terminal/command prompt
2. Ketik perintah berikut:
   ```bash
   # Scan jaringan lokal
   nmap -sn 192.168.1.0/24
   
   # Identifikasi layanan pada perangkat target
   nmap -sV [IP_TARGET]
   ```
3. Catat hasil scan dalam format:
   ```
   IP Address    Status    MAC Address       Vendor
   ----------    ------    -----------       ------
   192.168.1.1   up        00:11:22:33:44:55  TP-Link
   ```

### Latihan 2: Analisis Traffic Jaringan

**Tujuan:** Menganalisis protokol jaringan

**Alat:** Wireshark

**Langkah Kerja:**
1. Buka Wireshark dan mulai capture
2. Akses website HTTP (bukan HTTPS)
3. Hentikan capture setelah beberapa detik
4. Gunakan filter `http`
5. Identifikasi:
   - Request dan response HTTP
   - Header yang dikirim
   - Informasi sensitif yang terlihat

## 🧩 Tantangan

### Tantangan 1: Pemetaan Jaringan
Buatlah peta jaringan sederhana yang menunjukkan:
1. Perangkat yang terhubung
2. Jenis koneksi
3. Titik-titik kerentanan potensial

### Tantangan 2: Analisis Keamanan Website
Kunjungi website sekolah/kampus Anda (dengan izin) dan lakukan:
1. Analisis header HTTP
2. Identifikasi teknologi yang digunakan
3. Cari informasi sensitif yang mungkin terpapar

## 📋 Format Laporan Latihan

### 1. Identitas
- Nama:
- Kelas:
- Tanggal:

### 2. Hasil Latihan
#### 2.1 Analisis Jaringan
```
[Tempel hasil scan Nmap]
```

#### 2.2 Analisis Traffic
```
[Deskripsi temuan dari Wireshark]
```

### 3. Temuan Menarik
- [ ] Kerentanan yang ditemukan
- [ ] Perilaku jaringan yang tidak biasa
- [ ] Rekomendasi perbaikan

### 4. Refleksi
- Kesulitan yang dihadapi:
- Pelajaran yang didapat:
- Ingin mempelajari lebih lanjut tentang:

## 📚 Referensi Tambahan
1. [OWASP Top 10](https://owasp.org/www-project-top-ten/)
2. [Nmap Network Scanning](https://nmap.org/book/)
3. [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/)

---
<div align="center">
  <p>Dokumen Latihan - Konsep Dasar Keamanan Siber</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

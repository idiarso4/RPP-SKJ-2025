# 📋 Tugas Praktik - Audit Keamanan Aplikasi Web

## 🎯 Tujuan
Menguji kemampuan peserta didik dalam mengidentifikasi, menganalisis, dan melaporkan kerentanan keamanan pada aplikasi web menggunakan metodologi yang tepat.

## 📝 Deskripsi Tugas
Anda ditugaskan untuk melakukan audit keamanan terhadap aplikasi web yang telah disediakan. Tugas ini mencakup identifikasi kerentanan, analisis dampak, dan rekomendasi perbaikan.

### 1. Lingkup Pekerjaan

#### 1.1 Target Aplikasi
- Aplikasi web yang rentan (contoh: OWASP Juice Shop, DVWA, atau aplikasi yang disediakan)
- Lingkungan pengujian yang telah disiapkan

#### 1.2 Alat yang Direkomendasikan
- OWASP ZAP
- Burp Suite Community
- Nmap
- Browser Developer Tools
- Wireshark (opsional)

### 2. Langkah Pengerjaan

#### 2.1 Pengenalan (10%)
1. Pemetaan aplikasi
2. Identifikasi teknologi yang digunakan
3. Analisis alur kerja aplikasi

#### 2.2 Pengujian Keamanan (50%)
1. Identifikasi kerentanan OWASP Top 10
2. Uji autentikasi dan otorisasi
3. Uji manajemen sesi
4. Uji validasi input
5. Uji konfigurasi keamanan

#### 2.3 Analisis (20%)
1. Klasifikasi kerentanan
2. Analisis dampak
3. Proof of Concept (PoC)
4. Rekomendasi perbaikan

#### 2.4 Dokumentasi (20%)
1. Laporan teknis
2. Presentasi temuan
3. Kode eksploit (jika ada)

### 3. Format Laporan

#### 3.1 Halaman Judul
- Judul laporan
- Nama dan NIM
- Tanggal pengujian
- Lingkup pengujian

#### 3.2 Ringkasan Eksekutif
- Ikhtisar temuan
- Tingkat risiko keseluruhan
- Rekomendasi utama

#### 3.3 Metodologi
- Pendekatan pengujian
- Tools yang digunakan
- Lingkungan pengujian

#### 3.4 Temuan
Untuk setiap kerentanan:
- Deskripsi
- Tingkat risiko
- Dampak potensial
- Bukti (screenshot, log, dll.)
- Rekomendasi perbaikan

## 📅 Tenggat Waktu
- **Pengumpulan:** 2 minggu dari tanggal pemberian tugas
- **Presentasi:** 1 minggu setelah pengumpulan

## 📤 Ketentuan Pengumpulan
1. Format file: PDF untuk laporan, PPT untuk presentasi
2. Kode eksploit dalam format teks terpisah
3. Screenshot bukti kerentanan
4. Upload ke LMS sebelum tenggat waktu

## 🏆 Kriteria Penilaian

### 1. Kualitas Temuan (40%)
- Validitas kerentanan
- Tingkat keparahan
- Bukti yang meyakinkan

### 2. Kedalaman Analisis (30%)
- Pemahaman kerentanan
- Dampak bisnis
- Rekomendasi yang relevan

### 3. Dokumentasi (20%)
- Kejelasan penulisan
- Kelengkapan laporan
- Presentasi yang efektif

### 4. Etika (10%)
- Bertanggung jawab dalam pengujian
- Menghormati ruang lingkup
- Pelaporan yang bertanggung jawab

## 📚 Sumber Daya
1. [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
2. [PortSwigger Web Security Academy](https://portswigger.net/web-security)
3. [HackTricks](https://book.hacktricks.xyz/)
4. [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)

## 📝 Template Laporan

```markdown
# Laporan Audit Keamanan Aplikasi Web

## 1. Informasi Umum
- Nama: ______________________
- NIM: _______________________
- Tanggal Pengujian: _________
- Target Aplikasi: ___________
- Lingkup Pengujian: _________

## 2. Ringkasan Eksekutif
[Ringkasan temuan dan rekomendasi utama]

## 3. Metodologi
### 3.1 Pendekatan
[Deskripsi pendekatan pengujian]

### 3.2 Tools
- OWASP ZAP vX.X
- Nmap vX.XX
- [Lainnya]

## 4. Temuan

### 4.1 [Nama Kerentanan]
- **Risiko**: [Tinggi/Sedang/Rendah]
- **Lokasi**: [URL/Endpoint]
- **Deskripsi**: 
  [Penjelasan rinci tentang kerentanan]
  
- **Dampak**:
  [Dampak potensial terhadap aplikasi]
  
- **Bukti**:
  ```
  [Permintaan HTTP]
  ```
  ```
  [Respons HTTP]
  ```
  
- **Rekomendasi**:
  1. [Rekomendasi 1]
  2. [Rekomendasi 2]
  3. [Dst.]

## 5. Kesimpulan
[Ringkasan temuan dan rekomendasi keseluruhan]

## 6. Lampiran
- Screenshot
- Log pengujian
- Kode eksploit (jika ada)
```

## ❓ Pertanyaan yang Sering Diajukan

### 1. Apakah saya perlu menguji semua kerentanan OWASP Top 10?
Tidak perlu semua, fokuslah pada kerentanan yang relevan dengan aplikasi target.

### 2. Berapa banyak kerentanan yang harus saya temukan?
Kualitas lebih penting daripada kuantitas. Lebih baik menemukan beberapa kerentanan kritis daripada banyak kerentanan rendah.

### 3. Apakah saya perlu membuat kode eksploit?
Tidak wajib, tetapi akan menjadi nilai tambah jika Anda bisa menunjukkan proof of concept.

## 📞 Bantuan
Untuk pertanyaan lebih lanjut, hubungi:
- Email: [dummy@smkn1pgl.sch.id](mailto:dummy@smkn1pgl.sch.id)
- WhatsApp: +62 812-3456-7890
- Jam kerja: Senin-Jumat, 08.00-15.00 WIB

---
<div align="center">
  <p>Dokumen Tugas - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

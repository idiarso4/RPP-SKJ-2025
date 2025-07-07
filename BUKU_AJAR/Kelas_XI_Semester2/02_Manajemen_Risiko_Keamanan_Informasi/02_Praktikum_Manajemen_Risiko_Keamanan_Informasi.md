# Praktikum Manajemen Risiko Keamanan Informasi

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Tujuan Praktikum](#tujuan-praktikum)
3. [Alat dan Bahan](#alat-dan-bahan)
4. [Langkah Kerja](#langkah-kerja)
5. [Lembar Kerja](#lembar-kerja)
6. [Tugas dan Laporan](#tugas-dan-laporan)
7. [Evaluasi](#evaluasi)
8. [Referensi](#referensi)

## 1. Pendahuluan
Praktikum ini dirancang untuk memberikan pengalaman langsung dalam menerapkan konsep manajemen risiko keamanan informasi. Peserta akan belajar mengidentifikasi, menganalisis, dan mengevaluasi risiko keamanan informasi dalam skenario yang disimulasikan.

## 2. Tujuan Praktikum
Setelah menyelesaikan praktikum ini, peserta diharapkan mampu:
1. Mengidentifikasi aset informasi dan ancamannya
2. Melakukan analisis risiko menggunakan metode kualitatif
3. Mengembangkan rencana penanganan risiko
4. Menerapkan kontrol keamanan yang sesuai
5. Mendokumentasikan proses manajemen risiko

## 3. Alat dan Bahan
### Perangkat Keras
- Komputer dengan spesifikasi minimal:
  - Prosesor: Intel Core i3 atau setara
  - RAM: 4GB
  - Penyimpanan: 100MB ruang kosong
  - Koneksi internet

### Perangkat Lunak
#### 3.2.1 Dasar
- Microsoft Excel atau Google Sheets
- Peramban web terbaru (Chrome, Firefox, atau Edge)

#### 3.2.2 Alat Sumber Terbuka
1. **OWASP Threat Dragon**
   - *Platform*: Web, Desktop (Windows/macOS/Linux)
   - *Link*: [https://owasp.org/www-project-threat-dragon/](https://owasp.org/www-project-threat-dragon/)
   - *Kegunaan*: Pemodelan ancaman dan analisis risiko
   
2. **SimpleRisk**
   - *Platform*: Web (PHP/MySQL)
   - *Link*: [https://www.simplerisk.com/](https://www.simplerisk.com/)
   - *Kegunaan*: Manajemen risiko terintegrasi
   
3. **Dradis Framework**
   - *Platform*: Cross-platform
   - *Link*: [https://dradisframework.com/](https://dradisframework.com/)
   - *Kegunaan*: Dokumentasi dan kolaborasi keamanan

#### 3.2.3 Panduan Instalasi Cepat OWASP Threat Dragon
1. **Persyaratan Sistem**
   - Node.js (versi 14.x atau lebih baru)
   - npm (versi 6.x atau lebih baru)
   
2. **Langkah Instalasi**
   ```bash
   # Instal secara global
   npm install -g owasp-threat-dragon
   
   # Jalankan aplikasi
   owasp-threat-dragon
   ```
   
3. **Alternatif**: Gunakan versi web di [https://threatdragon.org/](https://threatdragon.org/)

### Bahan
#### 3.3.1 Template dan Dokumen
1. **Template Penilaian Risiko** ([unduh](https://example.com/template_risiko.xlsx))
   - Matriks risiko
   - Lembar kerja analisis dampak
   
2. **Daftar Periksa Keamanan**
   - Berdasarkan ISO 27002:2022
   - Daftar periksa keamanan jaringan
   
#### 3.3.2 Skenario Praktikum
1. **Sektor Pendidikan**
   - Sekolah: SMK Negeri 1 Punggelan
   - Aset: Data siswa, sistem e-learning, infrastruktur TI
   
2. **UMKM Lokal**
   - Bisnis: Toko Online "Batik Jaya"
   - Aset: Data pelanggan, sistem pembayaran, katalog produk
   
3. **Layanan Kesehatan**
   - Klinik: Klinik Sehat Bersama
   - Aset: Rekam medis, data pasien, sistem janji temu

## 4. Langkah Kerja
### Praktikum 1: Identifikasi Aset dan Ancaman
1. **Persiapan**
   - Bentuk kelompok yang terdiri dari 3-4 orang
   - Pilih salah satu skenario organisasi yang disediakan
   - Unduh template penilaian risiko

2. **Identifikasi Aset**
   - Buat daftar aset informasi organisasi
   - Klasifikasikan aset berdasarkan kriteria:
     - Kepemilikan (organisasi, pihak ketiga)
     - Sensitivitas (sangat rahasia, rahasia, terbatas, umum)
     - Nilai (tinggi, sedang, rendah)

3. **Identifikasi Ancaman dan Kerentanan**
   - Gunakan daftar periksa ancaman umum (misal: OWASP Top 10, SANS Top 20)
   - Identifikasi kerentanan yang mungkin dieksploitasi
   - Dokumentasikan skenario ancaman

### Praktikum 2: Analisis dan Evaluasi Risiko
1. **Penilaian Dampak**
   - Tentukan dampak potensial untuk setiap ancaman yang teridentifikasi
   - Gunakan skala 1-5 (1 = sangat rendah, 5 = sangat tinggi)
   
2. **Penilaian Kemungkinan**
   - Perkirakan kemungkinan terjadinya setiap ancaman
   - Gunakan skala 1-5 (1 = sangat tidak mungkin, 5 = hampir pasti)

3. **Perhitungan Tingkat Risiko**
   - Hitung tingkat risiko = Dampak × Kemungkinan
   - Plot hasil pada matriks risiko
   - Tentukan risiko yang memerlukan penanganan segera

### Praktikum 3: Pengendalian Risiko
1. **Pengembangan Rencana Penanganan**
   - Untuk setiap risiko tinggi dan sedang, tentukan strategi:
     - Menghindari
     - Mengurangi
     - Memindahkan
     - Menerima
   - Pilih kontrol keamanan yang sesuai dari ISO 27002

2. **Implementasi Kontrol**
   - Buat rencana aksi untuk menerapkan kontrol terpilih
   - Tentukan pemilik, tenggat waktu, dan sumber daya yang dibutuhkan

## 5. Lembar Kerja
### Lembar Kerja 1: Daftar Aset Informasi
| No | Nama Aset | Deskripsi | Klasifikasi | Kepemilikan | Nilai |
|----|-----------|-----------|-------------|-------------|-------|
| 1  |           |           |             |             |       |

### Lembar Kerja 2: Identifikasi Ancaman
| No | Aset | Ancaman | Kemungkinan | Dampak | Tingkat Risiko |
|----|------|---------|-------------|--------|----------------|
| 1  |      |         |             |        |                |

### Lembar Kerja 3: Rencana Penanganan Risiko
| No | Risiko | Strategi | Tindakan | Pemilik | Tenggat Waktu | Status |
|----|--------|----------|----------|---------|---------------|--------|
| 1  |        |          |          |         |               |        |

## 6. Tugas dan Laporan
### Tugas Individu
1. Buat analisis risiko untuk aset pribadi Anda
2. Dokumentasikan proses dan temuan dalam format laporan
3. Presentasikan hasil analisis dalam 5 menit

### Tugas Kelompok
1. Lengkapi semua lembar kerja untuk organisasi simulasi
2. Buat laporan manajemen risiko yang mencakup:
   - Ringkasan eksekutif
   - Metodologi yang digunakan
   - Temuan utama
   - Rekomendasi
   - Rencana aksi
3. Presentasikan hasil kepada kelas (15 menit)

## 7. Evaluasi
### 7.1 Kriteria Penilaian
#### 7.1.1 Aspek Teknis (60%)
1. **Kelengkapan Dokumen** (15%)
   - Semua template terisi lengkap
   - Lampiran pendukung lengkap
   
2. **Ketepatan Analisis** (25%)
   - Metodologi yang digunakan tepat
   - Perhitungan risiko akurat
   
3. **Kualitas Rekomendasi** (20%)
   - Relevansi dengan risiko yang diidentifikasi
   - Kelayakan implementasi

#### 7.1.2 Aspek Non-Teknis (40%)
1. **Kerja Sama Tim** (15%)
   - Pembagian tugas yang seimbang
   - Kolaborasi efektif
   
2. **Presentasi** (15%)
   - Kejelasan penyampaian
   - Penggunaan media pendukung
   
3. **Ketepatan Waktu** (10%)
   - Penyelesaian sesuai jadwal
   - Pengumpulan laporan tepat waktu

### 7.2 Rubrik Penilaian Terperinci
| Aspek | Indikator | Skor | Keterangan |
|-------|-----------|------|------------|
| **Kelengkapan** | - Semua bagian terisi<br>- Dokumen pendukung lengkap | 90-100 | Sangat lengkap |
|  | - Hampir semua terisi<br>- Beberapa dokumen kurang | 80-89 | Cukup lengkap |
|  | - Banyak bagian kosong<br>- Kurang bukti pendukung | <80 | Perlu perbaikan |
| **Ketepatan Analisis** | - Metodologi tepat<br>- Perhitungan akurat | 90-100 | Sangat akurat |
|  | - Metodologi cukup tepat<br>- Ada sedikit kesalahan | 80-89 | Cukup akurat |
|  | - Banyak kesalahan metodologi<br>- Perhitungan tidak akurat | <80 | Kurang akurat |
| **Kualitas Rekomendasi** | - Solusi inovatif<br>- Sangat layak diimplementasikan | 90-100 | Sangat baik |
|  | - Solusi standar<br>- Cukup layak diimplementasikan | 80-89 | Baik |
|  | - Solusi kurang relevan<br>- Sulit diimplementasikan | <80 | Perlu perbaikan |

### 7.3 Contoh Jawaban
#### Studi Kasus: SMK Negeri 1 Punggelan
**Risiko Utama**:
1. Kebocoran data pribadi siswa
   - *Dampak*: Tinggi (4)
   - *Kemungkinan*: Sedang (3)
   - *Tingkat Risiko*: 12 (Tinggi)
   
**Rekomendasi**:
1. Implementasi enkripsi data
2. Pelatihan kesadaran keamanan
3. Audit keamanan berkala

## 8. Referensi
1. ISO/IEC 27005:2022 - Information security risk management
2. NIST SP 800-30 Rev. 1 - Guide for Conducting Risk Assessments
3. OCTAVE Allegro: Improving the Information Security Risk Assessment Process
4. FAIR (Factor Analysis of Information Risk) Framework
5. OWASP Risk Rating Methodology

---
*Dokumen ini merupakan bagian dari Buku Ajar Sistem Keamanan Jaringan Kelas XI Semester 2. Hak Cipta © 2025 SMK Negeri 1 Punggelan.*

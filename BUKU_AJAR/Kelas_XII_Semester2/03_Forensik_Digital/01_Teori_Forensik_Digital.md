# Modul 3: Forensik Digital

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Konsep Dasar Forensik Digital](#konsep-dasar)
3. [Prinsip dan Etika](#prinsip-dan-etika)
4. [Alur Investigasi Forensik](#alur-investigasi)
5. [Alat dan Teknologi](#alat-dan-teknologi)
6. [Studi Kasus](#studi-kasus)
7. [Tantangan dan Solusi](#tantangan-dan-solusi)
8. [Praktik Terbaik](#praktik-terbaik)
9. [Latihan dan Tugas](#latihan-dan-tugas)
10. [Referensi](#referensi)

## 1. Pendahuluan
Forensik digital adalah proses pengumpulan, analisis, dan pelaporan data digital dengan cara yang dapat diterima secara hukum. Modul ini membahas prinsip, metodologi, dan praktik terbaik dalam investigasi forensik digital.

## 2. Konsep Dasar Forensik Digital
### 2.1 Definisi dan Ruang Lingkup
- Pengertian forensik digital
- Perbedaan dengan disiplin ilmu terkait (keamanan informasi, investigasi digital)
- Bidang-bidang forensik digital (komputer, jaringan, mobile, cloud)

### 2.2 Konsep Kunci
- Bukti digital (digital evidence)
- Rantai kustodian (chain of custody)
- Integritas data
- Bukti yang dapat diterima di pengadilan

## 3. Prinsip dan Etika
### 3.1 Prinsip Dasar
1. Jangan mengubah data asli
2. Dokumentasikan semua tindakan
3. Ikuti prosedur yang dapat dipertanggungjawabkan
4. Patuhi hukum yang berlaku

### 3.2 Aspek Hukum dan Etika
- Undang-Undang ITE dan perubahannya
- Undang-Undang Keterbukaan Informasi Publik
- Kode etik profesi forensik digital
- Perlindungan data pribadi dalam investigasi

## 4. Alur Investigasi Forensik
### 4.1 Tahap Persiapan
- Perencanaan investigasi
- Penyiapan peralatan dan perizinan
- Pembuatan rencana respons insiden

### 4.2 Pengumpulan Bukti
- Identifikasi sumber bukti digital
- Teknik akuisisi data
- Pencatatan dan dokumentasi
- Pembuatan hash untuk validasi integritas

### 4.3 Analisis Bukti
- Pemulihan data terhapus
- Analisis log sistem
- Pencarian bukti pada file system
- Analisis memori (RAM)

### 4.4 Pelaporan
- Penyusunan laporan forensik
- Presentasi temuan
- Kesaksian ahli di pengadilan

## 5. Alat dan Teknologi
### 5.1 Alat Akuisisi
- **FTK Imager**: Untuk pembuatan image disk
- **dd**: Command line tool untuk akuisisi data
- **Guymager**: Alat akuisisi open source

### 5.2 Alat Analisis
- **Autopsy**: Platform analisis forensik open source
- **Wireshark**: Analisis lalu lintas jaringan
- **Volatility**: Analisis memori (RAM)
- **SIFT Workstation**: Distribusi Linux untuk forensik

### 5.3 Alat Mobile Forensik
- **Cellebrite UFED**: Untuk ekstraksi data perangkat mobile
- **Mobiledit Forensic Express**: Analisis perangkat mobile
- **Oxygen Forensic Detective**: Solusi forensik mobile

## 6. Studi Kasus
### 6.1 Kasus Penipuan Online (2024)
- **Gambaran**: Penipuan investasi online mengorbankan ribuan korban
- **Metode Investigasi**:
  - Analisis log server
  - Pelacakan transaksi kripto
  - Pemetaan jaringan pelaku
- **Tantangan**: Penggunaan teknologi enkripsi dan dark web
- **Hasil**: Pengungkapan sindikat dan pengembalian sebagian dana korban

### 6.2 Kasus Peretasan Situs Pemerintah (2023)
- **Gambaran**: Deface dan kebocoran data situs pemerintah
- **Metode Investigasi**:
  - Analisis log web server
  - Pemindaian kerentanan
  - Pemulihan file yang dimodifikasi
- **Tantangan**: Penghapusan log oleh peretas
- **Hasil**: Identifikasi kerentanan dan peningkatan keamanan

## 7. Tantangan dan Solusi
### 7.1 Tantangan Umum
- Enkripsi end-to-end
- Penyimpanan cloud
- Perangkat IoT
- Volume data yang besar

### 7.2 Solusi dan Pendekatan
- Penggunaan teknik live forensik
- Kolaborasi dengan penyedia layanan cloud
- Pemanfaatan machine learning untuk analisis data besar
- Pengembangan standar dan prosedur baru

## 8. Praktik Terbaik
### 8.1 Persiapan
- Siapkan toolkit forensik yang lengkap
- Buat image kerja untuk analisis
- Dokumentasikan semua langkah dengan baik

### 8.2 Selama Investigasi
- Jaga integritas bukti asli
- Gunakan write blocker
- Catat semua perubahan yang dibuat

### 8.3 Setelah Investigasi
- Simpan bukti dengan aman
- Buat laporan yang komprehensif
- Siapkan diri untuk memberikan kesaksian

## 9. Latihan dan Tugas
### Latihan Individu
1. Lakukan akuisisi image dari flashdisk menggunakan FTK Imager
2. Analisis file log menggunakan alat forensik
3. Buat laporan investigasi sederhana

### Tugas Kelompok
1. Lakukan simulasi investigasi insiden keamanan
2. Analisis bukti digital yang diberikan
3. Presentasikan temuan dan rekomendasi

## 10. Referensi
### Buku Teks
1. "Digital Forensics with Open Source Tools" by Cory Altheide & Harlan Carvey
2. "The Art of Memory Forensics" by Michael Hale Ligh et al.
3. "Practical Mobile Forensics" by Rohit Tamma et al.

### Standar dan Panduan
1. **NIST SP 800-86**: Guide to Integrating Forensic Techniques into Incident Response
2. **ISO/IEC 27037**: Guidelines for identification, collection, acquisition, and preservation of digital evidence
3. **ACPO Guidelines**: Good Practice Guide for Digital Evidence

### Sumber Online
1. **SANS Digital Forensics and Incident Response**: https://www.sans.org/digital-forensics-incident-response/
2. **DFIR Training & Resources**: https://www.dfir.training/
3. **Forensic Focus**: https://www.forensicfocus.com/

### Regulasi Indonesia
1. Undang-Undang No. 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik (UU ITE)
2. Peraturan Kepala BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi
3. Peraturan Menteri Kominfo tentang Penyelenggaraan Sistem Elektronik

**Catatan Versi**:
- Versi Dokumen: 1.0
- Terakhir Diperbarui: 7 Juli 2025
- Penulis: Tim Pengembang Kurikulum Keamanan Jaringan

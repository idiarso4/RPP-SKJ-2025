# 📝 Bank Soal Sistem Autentikasi Terpusat

## Daftar Isi
1. [Pilihan Ganda](#-pilihan-ganda)
2. [Essay](#-essay)
3. [Praktik](#-praktik)
4. [Studi Kasus](#-studi-kasus)
5. [Kunci Jawaban](#-kunci-jawaban)

## 🔘 Pilihan Ganda

### Konsep Dasar
1. Berikut ini yang BUKAN komponen dari kerangka kerja AAA adalah...
   a. Authentication
   b. Authorization
   c. Accounting
   d. Availability

2. Protokol yang digunakan untuk autentikasi terpusat adalah...
   a. HTTP
   b. RADIUS
   c. FTP
   d. SMTP

### Konfigurasi
3. File konfigurasi utama FreeRADIUS di Linux biasanya berada di...
   a. /etc/radius/
   b. /etc/freeradius/3.0/
   c. /var/lib/radius/
   d. /usr/local/radius/

4. Perintah untuk menguji konfigurasi FreeRADIUS tanpa menjalankan service adalah...
   a. radiusd -X
   b. freeradius -t
   c. radius-test
   d. test-radius

## 📝 Essay

### Teori
1. Jelaskan perbedaan antara autentikasi dan otorisasi dalam konteks keamanan jaringan!
   **Jawaban:**
   - Autentikasi: Proses verifikasi identitas pengguna
   - Otorisasi: Proses menentukan hak akses pengguna
   - Contoh: Usaha masuk (autentikasi) vs. akses file (otorisasi)

2. Mengapa RADIUS menggunakan UDP bukan TCP?
   **Jawaban:**
   - UDP lebih ringan dan cepat
   - Tidak memerlukan koneksi yang berkelanjutan
   - Cocok untuk lingkungan dengan latensi tinggi
   - Dapat menangani timeout dengan lebih baik

## 🛠️ Praktik

### Tugas 1: Konfigurasi Dasar FreeRADIUS
**Instruksi:**
1. Install FreeRADIUS pada sistem Linux
2. Buat 3 user dengan level akses berbeda
3. Konfigurasi client jaringan lokal
4. Lakukan testing menggunakan radtest

**Rubrik Penilaian:**
| Kriteria | Skor |
|----------|------|
| Keberhasilan instalasi | 25 |
| Kebenaran konfigurasi | 25 |
| Hasil testing | 25 |
| Dokumentasi | 25 |

### Tugas 2: Integrasi dengan MikroTik
**Instruksi:**
1. Konfigurasi MikroTik sebagai NAS
2. Integrasikan dengan FreeRADIUS
3. Uji koneksi PPPoE
4. Buat laporan hasil

## 📚 Studi Kasus

### Kasus: Implementasi RADIUS di Perusahaan
**Deskripsi:**
Sebuah perusahaan dengan 50 karyawan ingin mengimplementasikan sistem autentikasi terpusat. Setiap departemen memiliki kebijakan akses yang berbeda-beda.

**Tugas:**
1. Rancang arsitektur yang sesuai
2. Buat konfigurasi dasar FreeRADIUS
3. Implementasikan kebijakan akses per departemen
4. Buat dokumentasi teknis

**Rubrik Penilaian:**
| Kriteria | Maks. Skor |
|----------|------------|
| Kelayakan solusi | 30 |
| Kelengkapan konfigurasi | 30 |
| Kejelasan dokumentasi | 20 |
| Presentasi solusi | 20 |

## ✅ Kunci Jawaban

### Pilihan Ganda
1. d
2. b
3. b
4. b

### Essay (Contoh Jawaban)
1. **Autentikasi vs Otorisasi**
   - Autentikasi: Siapa Anda? (verifikasi identitas)
   - Otorisasi: Apa yang boleh Anda akses? (hak akses)
   - Contoh: Login (autentikasi) vs. akses folder (otorisasi)

2. **RADIUS Menggunakan UDP**
   - Ringan dan cepat
   - Tidak perlu koneksi berkelanjutan
   - Cocok untuk autentikasi yang membutuhkan respons cepat
   - Dapat menangani packet loss dengan mekanisme timeout

## 📊 Format Penilaian

### Penilaian Kognitif (40%)
- Kuis: 20%
- UTS: 30%
- UAS: 50%

### Penilaian Psikomotorik (40%)
- Praktikum: 60%
- Proyek: 40%

### Penilaian Afektif (20%)
- Kedisiplinan: 40%
- Kerjasama: 30%
- Tanggung Jawab: 30%

## 📅 Jadwal Penilaian
1. Kuis 1: Minggu ke-3
2. Praktikum 1: Minggu ke-4
3. UTS: Minggu ke-8
4. Proyek: Minggu ke-12
5. UAS: Minggu ke-16

---
<div align="center">
  <p>Bank Soal Sistem Autentikasi Terpusat</p>
  <p>© 2025 SMKN 1 Punggelan - Tim Pengajar</p>
</div>

# 📋 Tugas Praktik - Analisis Keamanan Perangkat IoT

## 🎯 Tujuan
Menguji kemampuan peserta didik dalam menganalisis dan meningkatkan keamanan perangkat IoT melalui pendekatan praktis.

## 📝 Deskripsi Tugas
Anda ditugaskan untuk menganalisis keamanan sebuah perangkat IoT (misalnya: router, kamera IP, atau smart plug) dan membuat laporan keamanan yang komprehensif.

### 1. Lingkup Pekerjaan

#### 1.1 Pemetaan Sistem
- Identifikasi perangkat target
- Buat diagram arsitektur
- Daftar komponen dan layanan

#### 1.2 Analisis Keamanan
- Pemindaian port dan layanan
- Analisis kerentanan
- Uji kekuatan autentikasi
- Analisis lalu lintas jaringan

#### 1.3 Dokumentasi Temuan
- Daftar kerentanan
- Tingkat keparahan
- Bukti temuan
- Rekomendasi perbaikan

### 2. Tools yang Direkomendasikan
- Nmap
- Wireshark
- Metasploit
- RouterSploit
- OWASP ZAP
- Shodan

### 3. Format Laporan

#### 3.1 Halaman Judul
- Judul Proyek
- Nama dan NIM
- Kelas
- Tanggal

#### 3.2 Executive Summary
- Ringkasan temuan
- Tingkat risiko keseluruhan
- Rekomendasi utama

#### 3.3 Metodologi
- Lingkup pengujian
- Tools yang digunakan
- Teknik pengujian

#### 3.4 Temuan Utama
- Daftar kerentanan
- Tingkat keparahan (Kritis, Tinggi, Sedang, Rendah)
- Dampak potensial

#### 3.5 Rekomendasi
- Perbaikan teknis
- Perubahan konfigurasi
- Praktik terbaik

#### 3.6 Lampiran
- Screenshot
- Log pengujian
- Referensi

## 📅 Tenggat Waktu
- **Pengumpulan:** 2 minggu dari tanggal pemberian tugas
- **Presentasi:** Minggu berikutnya setelah pengumpulan

## 📤 Ketentuan Pengumpulan
1. Format file: PDF
2. Maksimal 20 halaman (tidak termasuk lampiran)
3. Kode sumber (jika ada) dalam format .zip terpisah
4. Upload ke LMS sebelum tenggat waktu

## 🏆 Kriteria Penilaian

### 1. Kelengkapan (30%)
- Semua bagian laporan terisi
- Dokumentasi yang lengkap
- Lampiran yang relevan

### 2. Kedalaman Analisis (30%)
- Kualitas temuan
- Analisis dampak
- Rekomendasi yang relevan

### 3. Kualitas Teknis (25%)
- Ketepatan penggunaan tools
- Metodologi yang tepat
- Validasi temuan

### 4. Presentasi (15%)
- Struktur laporan
- Kejelasan penulisan
- Visualisasi data

## 📚 Sumber Daya
1. OWASP IoT Testing Guide
2. NIST IoT Security Guidelines
3. ENISA Baseline Security Recommendations
4. IoT Security Foundation Best Practices

## 📝 Contoh Format Temuan

### ID: IoT-001
**Judul:** Default Credentials pada Antarmuka Web
**Tingkat Risiko:** Tinggi
**Deskripsi:** Perangkat menggunakan kredensial default admin:admin
**Dampak:** Pelaku ancaman dapat mengakses kontrol penuh perangkat
**Rekomendasi:**
1. Ubah kredensial default
2. Terapkan kebijakan kata sandi yang kuat
3. Aktifkan autentikasi dua faktor
**Referensi:** OWASP IoT Top 10 #1

## ❓ Pertanyaan yang Sering Diajukan

### 1. Apakah saya perlu membeli perangkat khusus?
Tidak perlu. Anda bisa menggunakan perangkat yang tersedia di lab atau meminjam dari sekolah.

### 2. Apakah saya perlu izin untuk melakukan pengujian?
Ya, pastikan Anda mendapatkan izin tertulis sebelum menguji perangkat yang bukan milik Anda.

### 3. Bagaimana jika saya tidak menemukan kerentanan?
Tidak masalah. Laporkan saja temuan Anda secara jujur. Tidak menemukan kerentanan yang kritis juga merupakan hasil yang valid.

## 📞 Bantuan
Untuk pertanyaan lebih lanjut, hubungi:
- Email: [dummy@smkn1pgl.sch.id](mailto:dummy@smkn1pgl.sch.id)
- WhatsApp: +62 812-3456-7890
- Jam kerja: Senin-Jumat, 08.00-15.00 WIB

---
<div align="center">
  <p>Dokumen Tugas - Keamanan IoT</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

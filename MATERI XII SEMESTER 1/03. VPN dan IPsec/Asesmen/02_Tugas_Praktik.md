# 📋 Tugas Praktik - Implementasi dan Analisis VPN

## 🎯 Tujuan
Menguji kemampuan peserta didik dalam mengimplementasikan, mengkonfigurasi, dan menganalisis solusi VPN menggunakan berbagai protokol dan teknologi.

## 📝 Deskripsi Tugas
Anda ditugaskan untuk membuat dan mengkonfigurasi solusi VPN yang aman untuk skenario perusahaan. Tugas ini mencakup implementasi, pengujian, dan analisis keamanan.

### 1. Spesifikasi Teknis

#### 1.1 Lingkungan
- 2+ server Ubuntu 22.04 LTS
- 1+ klien (Windows/Linux)
- Koneksi jaringan yang stabil

#### 1.2 Persyaratan
- Implementasikan VPN site-to-site antara dua server
- Konfigurasikan VPN remote access untuk klien
- Terapkan kebijakan keamanan yang sesuai
- Dokumentasikan seluruh proses

### 2. Langkah Pengerjaan

#### 2.1 Persiapan (20%)
1. Rancang arsitektur jaringan
2. Siapkan lingkungan pengujian
3. Instal paket yang diperlukan

#### 2.2 Implementasi (40%)
1. Konfigurasi server VPN (IKEv2/IPsec)
2. Setel autentikasi berbasis sertifikat
3. Konfigurasi klien
4. Uji konektivitas dasar

#### 2.3 Pengujian (20%)
1. Uji kecepatan dan latensi
2. Verifikasi enkripsi
3. Uji failover (jika ada)
4. Periksa kebocoran DNS/IP

#### 2.4 Dokumentasi (20%)
1. Buat panduan instalasi
2. Dokumentasikan konfigurasi
3. Analisis keamanan
4. Rekomendasi perbaikan

### 3. Tools yang Direkomendasikan
- **VPN Server**: StrongSwan, OpenVPN, WireGuard
- **Analisis Jaringan**: Wireshark, tcpdump
- **Pengujian Keamanan**: Nmap, OpenSSL
- **Monitoring**: iftop, bmon

## 📅 Tenggat Waktu
- **Pengumpulan:** 2 minggu dari tanggal pemberian tugas
- **Presentasi:** 1 minggu setelah pengumpulan

## 📤 Ketentuan Pengumpulan
1. Format laporan: PDF
2. Kode konfigurasi dalam format teks terpisah
3. Screenshot hasil pengujian
4. Video demonstrasi (opsional, nilai tambah)
5. Upload ke LMS sebelum tenggat waktu

## 🏆 Kriteria Penilaian

### 1. Fungsionalitas (40%)
- Koneksi berhasil dibuat
- Keamanan terimplementasi dengan baik
- Performa yang memadai

### 2. Dokumentasi (30%)
- Kelengkapan dokumentasi
- Kejelasan penjelasan
- Kualitas analisis

### 3. Inovasi (20%)
- Fitur tambahan
- Optimasi performa
- Solusi kreatif

### 4. Presentasi (10%)
- Kejelasan presentasi
- Kemampuan menjawab pertanyaan
- Penguasaan materi

## 📚 Sumber Daya
1. [StrongSwan Documentation](https://wiki.strongswan.org/)
2. [OpenVPN Documentation](https://openvpn.net/community-resources/)
3. [WireGuard Documentation](https://www.wireguard.com/)
4. [NIST Guidelines for IPsec VPNs](https://csrc.nist.gov/)

## 📝 Contoh Format Laporan

### 1. Ringkasan Eksekutif
- Tujuan proyek
- Lingkup pekerjaan
- Hasil utama

### 2. Arsitektur Jaringan
- Diagram jaringan
- Spesifikasi perangkat
- Alamat IP yang digunakan

### 3. Implementasi
- Langkah-langkah konfigurasi
- File konfigurasi penting
- Screenshot konfigurasi

### 4. Pengujian
- Metodologi pengujian
- Hasil pengujian
- Analisis hasil

### 5. Keamanan
- Analisis keamanan
- Kerentanan yang ditemukan
- Rekomendasi perbaikan

### 6. Kesimpulan
- Pencapaian
- Kendala
- Pelajaran yang didapat

## ❓ Pertanyaan yang Sering Diajukan

### 1. Apakah boleh menggunakan layanan VPN pihak ketiga?
Tidak, tugas ini mengharuskan implementasi VPN server sendiri.

### 2. Berapa banyak klien yang harus didukung?
Minimal 2 klien secara bersamaan.

### 3. Apakah perlu mengimplementasikan semua protokol VPN?
Tidak, pilih satu protokol utama (IKEv2/IPsec, OpenVPN, atau WireGuard) dan satu protokol cadangan.

## 📞 Bantuan
Untuk pertanyaan lebih lanjut, hubungi:
- Email: [dummy@smkn1pgl.sch.id](mailto:dummy@smkn1pgl.sch.id)
- WhatsApp: +62 812-3456-7890
- Jam kerja: Senin-Jumat, 08.00-15.00 WIB

---
<div align="center">
  <p>Dokumen Tugas - VPN dan IPsec</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

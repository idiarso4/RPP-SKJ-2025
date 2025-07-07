# 🎯 Asesmen Kompetensi: Penetration Tester

## 📋 Informasi Umum
- **Mata Pelajaran**: Pengujian Keamanan Jaringan
- **Kelas**: XII
- **Semester**: 2
- **Waktu**: 120 menit
- **Bobot Nilai**: 30% dari total nilai akhir

## 🔍 Bagian 1: Pemahaman Konsep (30%)

### Soal 1: Multiple Choice (Pilih jawaban yang paling tepat)
1. Tools manakah yang PALING TEPAT digunakan untuk melakukan pemindaian port secara stealth?
   a) `nmap -sS`  
   b) `nmap -sT`  
   c) `nmap -sU`  
   d) `nmap -sP`

2. Apa yang dimaksud dengan "false positive" dalam konteks pengujian keamanan?
   a) Kerentanan yang tidak terdeteksi  
   b) Laporan kerentanan yang tidak valid  
   c) Serangan yang berhasil dieksploitasi  
   d) Hasil positif yang salah

### Soal 2: Studi Kasus Singkat
**Skenario**:
Sebuah situs web e-commerce memiliki form login dengan parameter berikut:
```
POST /login.php
username=admin&password=secret123
```

**Pertanyaan**:
1. Identifikasi 3 (tiga) kerentanan keamanan potensial pada form tersebut
2. Jelaskan bagaimana cara menguji setiap kerentanan tersebut
3. Berikan rekomendasi perbaikan untuk setiap kerentanan

## 🛠️ Bagian 2: Praktik (50%)

### Tugas 1: Pemindaian Jaringan (20%)
Lakukan pemindaian terhadap target yang disediakan dan jawab pertanyaan berikut:

1. Berapa jumlah port terbuka yang ditemukan?
2. Layanan apa saja yang berjalan di port tersebut?
3. Identifikasi 3 (tiga) kerentanan potensial berdasarkan hasil pemindaian

**Command yang harus digunakan**:
```bash
nmap -sV -sC -p- -T4 [TARGET_IP] -oN scan_results.txt
```

### Tugas 2: Eksploitasi Terkendali (30%)
Diberikan mesin dengan IP `192.168.1.100` yang memiliki layanan web rentan. Tugas Anda:

1. Identifikasi kerentanan pada aplikasi web
2. Eksploitasi kerentanan tersebut untuk mendapatkan akses shell
3. Dapatkan flag yang tersimpan di direktori `/root/`
4. Dokumentasikan setiap langkah yang dilakukan

**Kriteria Penilaian**:
- Ketepatan identifikasi kerentanan (10%)
- Keberhasilan eksploitasi (10%)
- Kualitas dokumentasi (5%)
- Keamanan dalam melakukan tes (5%)

## 📝 Bagian 3: Pelaporan (20%)
Buat laporan profesional yang mencakup:

### 1. Ringkasan Eksekutif (5%)
- Tujuan pengujian
- Metodologi
- Temuan utama
- Rekomendasi singkat

### 2. Temuan Rinci (10%)
Untuk setiap temuan, sertakan:
- Deskripsi kerentanan
- Tingkat keparahan (CVSS Score)
- Dampak potensial
- Bukti (screenshot/command)
- Rekomendasi perbaikan

### 3. Lampiran (5%)
- Log lengkap pengujian
- Referensi terkait
- Dokumentasi tambahan

## 📊 Rubrik Penilaian

### Kategori: Pemahaman Konsep (30%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Ketepatan jawaban pilihan ganda | 10% | Minimal 80% benar |
| Analisis studi kasus | 20% | Kedalaman analisis dan kelengkapan jawaban |

### Kategori: Praktik (50%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Keakuratan pemindaian | 10% | Kelengkapan dan ketepatan hasil scan |
| Keberhasilan eksploitasi | 15% | Kemampuan mendapatkan akses |
| Dokumentasi langkah | 15% | Kejelasan dan kelengkapan dokumentasi |
| Keamanan pengujian | 10% | Tidak merusak sistem target |

### Kategori: Pelaporan (20%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Struktur laporan | 5% | Kelengkapan bagian laporan |
| Kualitas temuan | 10% | Kedalaman analisis temuan |
| Rekomendasi | 5% | Kualitas dan kelayakan rekomendasi |

## ⚠️ Ketentuan Umum
1. Dilarang bekerja sama selama ujian
2. Semua aktivitas harus didokumentasikan
3. Hanya lakukan pengujian pada target yang diizinkan
4. Laporkan setiap temuan secara bertanggung jawab

## 🏆 Kriteria Kelulusan
- Nilai minimal 70 untuk lulus
- Waktu pengerjaan maksimal 120 menit
- Dilarang menggunakan perangkat elektronik tambahan

## 📚 Referensi
1. OWASP Testing Guide v4.2
2. NIST SP 800-115
3. PTES Technical Guidelines
4. CEH Practical Guide

---
<div align="center">
  <p>Dokumen Asesmen - Kompetensi Penetration Tester</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

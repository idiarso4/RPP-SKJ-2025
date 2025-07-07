# 🎯 Asesmen Kompetensi: Keamanan Aplikasi Web

## 📋 Informasi Umum
- **Mata Pelajaran**: Keamanan Aplikasi Web
- **Kelas**: XII
- **Semester**: 2
- **Waktu**: 120 menit
- **Bobot Nilai**: 30% dari total nilai akhir

## 🔍 Bagian 1: Pemahaman Konsep (30%)

### Soal 1: Multiple Choice (Pilih jawaban yang paling tepat)
1. Manakah dari berikut ini yang BUKAN termasuk dalam OWASP Top 10 2024?
   a) Broken Access Control  
   b) Cryptographic Failures  
   c) Buffer Overflow  
   d) Injection

2. Teknik apa yang PALING EFEKTIF untuk mencegah SQL Injection?
   a) Memfilter karakter khusus  
   b) Menggunakan parameterized queries  
   c) Mengenkripsi input pengguna  
   d) Menonaktifkan JavaScript

### Soal 2: Studi Kasus
**Skenario**:
Sebuah situs e-commerce memiliki kerentanan XSS yang memungkinkan penyerang mencuri cookie sesi pengguna. Cookie tersebut tidak memiliki flag HttpOnly dan Secure.

**Pertanyaan**:
1. Jelaskan langkah-langkah yang akan dilakukan penyerang untuk mengeksploitasi kerentanan ini
2. Bagaimana cara mencegah serangan tersebut?
3. Apa dampak potensial dari serangan ini terhadap pengguna dan bisnis?

## 🛠️ Bagian 2: Praktik (50%)

### Tugas 1: Analisis Kode (20%)
Diberikan potongan kode berikut:

```javascript
// server.js
const express = require('express');
const app = express();
const db = require('./db');

app.get('/user/:id', (req, res) => {
    const userId = req.params.id;
    const query = `SELECT * FROM users WHERE id = ${userId}`;
    
    db.query(query, (err, result) => {
        if (err) throw err;
        res.json(result);
    });
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
    
    db.query(query, (err, result) => {
        if (err) throw err;
        if (result.length > 0) {
            res.cookie('session', 'valid', { httpOnly: false });
            res.redirect('/dashboard');
        } else {
            res.send('Login gagal');
        }
    });
});
```

**Pertanyaan**:
1. Identifikasi minimal 3 kerentanan keamanan dalam kode di atas
2. Perbaiki kode tersebut untuk mengatasi kerentanan yang ditemukan
3. Jelaskan mengapa perbaikan yang Anda lakukan dapat meningkatkan keamanan aplikasi

### Tugas 2: Pengujian Keamanan (30%)
Anda diberikan akses ke aplikasi web yang rentan di http://vulnerable-webapp.local

**Langkah Kerja**:
1. Lakukan pengujian keamanan menggunakan OWASP ZAP
2. Identifikasi minimal 5 kerentanan berbeda
3. Dokumentasikan temuan Anda dalam format laporan keamanan singkat

**Alat yang Diperbolehkan**:
- OWASP ZAP
- Browser dengan developer tools
- Nmap
- SQLmap (hanya untuk pengujian SQL Injection)

**Format Laporan**:
```markdown
# LAPORAN TEMUAN KEAMANAN

## Ringkasan Eksekutif
[Ringkasan singkat temuan]

## Daftar Kerentanan
### 1. [Nama Kerentanan]
- **Tingkat Keparahan**: [Kritis/Tinggi/Sedang/Rendah]
- **Lokasi**: [URL/Endpoint]
- **Deskripsi**: 
- **Dampak**: 
- **Bukti**: [Screenshot/Command]
- **Rekomendasi**:

## Kesimpulan dan Rekomendasi Umum
```

## 📝 Bagian 3: Analisis Kasus (20%)

### Studi Kasus: Kebocoran Data Pelanggan
Sebuah perusahaan e-commerce melaporkan bahwa data pribadi 10.000 pelanggan mereka bocor ke publik. Setelah investigasi, ditemukan bahwa:
- API endpoint `/api/v1/users` dapat diakses tanpa otentikasi
- Tidak ada mekanisme rate limiting yang diterapkan
- Logging yang tidak memadai

**Pertanyaan**:
1. Apa akar masalah dari insiden ini?
2. Bagaimana seharusnya API tersebut diamankan?
3. Langkah-langkah apa yang harus diambil setelah insiden terjadi?
4. Bagaimana mencegah kejadian serupa di masa depan?

## 📊 Rubrik Penilaian

### Kategori: Pemahaman Konsep (30%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Ketepatan jawaban pilihan ganda | 10% | Minimal 80% benar |
| Analisis studi kasus | 20% | Kedalaman analisis dan kelengkapan jawaban |

### Kategori: Praktik (50%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Identifikasi kerentanan kode | 10% | Kelengkapan dan ketepatan identifikasi |
| Perbaikan kode | 10% | Kualitas dan kelayakan perbaikan |
| Pengujian keamanan | 20% | Jumlah dan kualitas temuan kerentanan |
| Kualitas laporan | 10% | Struktur dan kelengkapan laporan |

### Kategori: Analisis Kasus (20%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Analisis akar masalah | 5% | Ketepatan identifikasi akar masalah |
| Solusi teknis | 10% | Kesesuaian dan kelayakan solusi |
| Rekomendasi pencegahan | 5% | Kelayakan dan kelengkapan rekomendasi |

## ⚠️ Ketentuan Umum
1. Dilarang bekerja sama selama ujian
2. Semua jawaban harus didokumentasikan dengan baik
3. Waktu pengerjaan maksimal 120 menit
4. Jawaban diserahkan dalam format PDF

## 🏆 Kriteria Kelulusan
- Nilai minimal 70 untuk lulus
- Waktu pengerjaan maksimal 120 menit
- Dilarang menggunakan perangkat elektronik tambahan

## 📚 Referensi
1. OWASP Top 10 2024
2. OWASP Testing Guide v4.2
3. NIST SP 800-115: Technical Guide to Information Security Testing
4. Web Application Security Testing Cheat Sheet

---
<div align="center">
  <p>Dokumen Asesmen - Kompetensi Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

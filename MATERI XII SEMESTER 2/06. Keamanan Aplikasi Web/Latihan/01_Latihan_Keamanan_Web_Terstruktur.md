# 🏋️ Latihan Terstruktur: Keamanan Aplikasi Web

## 🎯 Tujuan Pembelajaran
Melalui serangkaian latihan ini, peserta didik akan mengembangkan kemampuan:
1. Mengidentifikasi kerentanan umum aplikasi web
2. Melakukan pengujian keamanan aplikasi web
3. Menerapkan praktik pengembangan yang aman
4. Menganalisis dan mengeksploitasi kerentanan
5. Mendokumentasikan temuan keamanan

## 🔍 Latihan 1: Identifikasi Kerentanan Kode

### Tujuan
Mengidentifikasi kerentanan keamanan dalam kode aplikasi web

### Langkah Kerja
Analisis potongan kode berikut dan identifikasi kerentanan keamanannya:

```javascript
// app.js - Backend Node.js/Express
const express = require('express');
const app = express();
const db = require('./db');

// Kerentanan 1: SQL Injection
app.get('/products', (req, res) => {
    const category = req.query.category;
    db.query(`SELECT * FROM products WHERE category = '${category}'`, (err, result) => {
        if (err) throw err;
        res.json(result);
    });
});

// Kerentanan 2: XSS
app.get('/search', (req, res) => {
    const query = req.query.q;
    res.send(`<h1>Hasil Pencarian: ${query}</h1>`);
});

// Kerentanan 3: Hardcoded Credentials
const ADMIN_USERNAME = 'admin';
const ADMIN_PASSWORD = 'admin123';

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (username === ADMIN_USERNAME && password === ADMIN_PASSWORD) {
        res.cookie('isAdmin', 'true');
        res.redirect('/admin');
    } else {
        res.send('Login gagal');
    }
});
```

### Pertanyaan
1. Identifikasi minimal 3 kerentanan keamanan dalam kode di atas
2. Jelaskan dampak potensial dari setiap kerentanan
3. Perbaiki kode tersebut untuk mengatasi kerentanan yang ditemukan

## 🛡️ Latihan 2: Pengujian Keamanan dengan OWASP ZAP

### Tujuan
Melakukan pengujian keamanan aplikasi web menggunakan OWASP ZAP

### Langkah Kerja
1. Instal OWASP ZAP di mesin Anda
2. Konfigurasi browser untuk menggunakan ZAP sebagai proxy (localhost:8080)
3. Uji aplikasi web target (misalnya: http://testphp.vulnweb.com/)
4. Lakukan:
   - Spidering untuk memetakan aplikasi
   - Pemindaian aktif untuk menemukan kerentanan
   - Analisis manual terhadap parameter yang rentan

### Tugas
1. Dokumentasikan minimal 5 kerentanan yang ditemukan
2. Untuk setiap kerentanan, sertakan:
   - Nama kerentanan
   - URL/Endpoint yang terpengaruh
   - Tingkat keparahan
   - Langkah reproduksi
   - Rekomendasi perbaikan

## ⚔️ Latihan 3: Eksploitasi SQL Injection

### Tujuan
Memahami dan mengeksploitasi kerentanan SQL Injection

### Langkah Kerja
Gunakan aplikasi web yang rentan (contoh: OWASP Juice Shop)

1. Temukan form yang rentan SQL Injection
2. Gunakan teknik-teknik berikut:
   ```sql
   ' OR '1'='1
   ' UNION SELECT username, password FROM users--
   '; DROP TABLE users--
   ```

### Tugas
1. Dokumentasikan payload yang berhasil
2. Jelaskan cara kerja setiap payload
3. Bagaimana cara mencegah serangan SQL Injection?

## 🔒 Latihan 4: Pengamanan Aplikasi Web

### Tujuan
Menerapkan praktik pengembangan yang aman

### Langkah Kerja
Buat aplikasi web sederhana dengan fitur:
1. Form login yang aman
2. Halaman profil pengguna
3. Fitur pencarian yang aman

### Persyaratan Keamanan:
- Gunakan prepared statements untuk query database
- Terapkan validasi input di sisi server
- Implementasikan proteksi terhadap XSS
- Gunakan cookie dengan flag HttpOnly dan Secure
- Terapkan CSRF protection

### Kode Contoh (Node.js/Express)
```javascript
const express = require('express');
const { body, validationResult } = require('express-validator');
const bcrypt = require('bcrypt');
const cookieParser = require('cookie-parser');
const csrf = require('csurf');

const app = express();
app.use(express.json());
app.use(cookieParser());
app.use(csrf({ cookie: true }));

// Middleware untuk validasi input
const validateInput = [
    body('username').trim().isLength({ min: 3 }).escape(),
    body('password').isLength({ min: 8 })
];

// Route login yang aman
app.post('/login', validateInput, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { username, password } = req.body;
    
    try {
        // Contoh query dengan parameterized query
        const user = await db.query('SELECT * FROM users WHERE username = ?', [username]);
        
        if (user && await bcrypt.compare(password, user.password)) {
            const token = generateAuthToken(user.id);
            
            // Set cookie yang aman
            res.cookie('session', token, {
                httpOnly: true,
                secure: process.env.NODE_ENV === 'production',
                sameSite: 'strict',
                maxAge: 24 * 60 * 60 * 1000 // 1 hari
            });
            
            res.json({ message: 'Login berhasil' });
        } else {
            res.status(401).json({ message: 'Kredensial tidak valid' });
        }
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ message: 'Terjadi kesalahan server' });
    }
});
```

## 📝 Latihan 5: Pembuatan Laporan Keamanan

### Tujuan
Membuat laporan keamanan yang profesional

### Langkah Kerja
Berdasarkan temuan dari latihan sebelumnya, buat laporan keamanan yang mencakup:

1. **Ringkasan Eksekutif**
   - Deskripsi singkat pengujian
   - Temuan utama
   - Rekomendasi umum

2. **Detail Temuan**
   Untuk setiap kerentanan:
   - Deskripsi
   - Tingkat keparahan
   - Dampak potensial
   - Langkah reproduksi
   - Rekomendasi perbaikan
   - Referensi (CVE, OWASP, dll)

3. **Lampiran**
   - Screenshot bukti
   - Log pengujian
   - Kode contoh perbaikan

### Template Laporan
```markdown
# LAPORAN PENGUJIAN KEAMANAN APLIKASI WEB

## 1. Informasi Umum
- Nama Aplikasi: 
- URL: 
- Tanggal Pengujian: 
- Tim Penguji: 

## 2. Ringkasan Eksekutif
[Isi ringkasan]

## 3. Temuan
### 3.1 [Nama Kerentanan]
- **Tingkat Keparahan**: 
- **Lokasi**: 
- **Deskripsi**: 
- **Dampak**: 
- **Langkah Reproduksi**:
  1. [Langkah 1]
  2. [Langkah 2]
- **Rekomendasi**:
  - [Rekomendasi 1]
  - [Rekomendasi 2]
- **Referensi**: [OWASP, CVE, dll]

## 4. Kesimpulan
[Ringkasan temuan dan rekomendasi]

## 5. Lampiran
- [ ] Screenshot
- [ ] Log Pengujian
- [ ] Kode Contoh
```

## 🧩 Tantangan Lanjutan

### Tantangan 1: CTF Web Security
1. Selesaikan tantangan di https://portswigger.net/web-security
2. Fokus pada topik:
   - SQL Injection
   - XSS
   - CSRF
   - Authentication Flaws

### Tantangan 2: Pembuatan Alat Keamanan
Buat script Python sederhana untuk:
1. Mendeteksi kerentanan SQL Injection
2. Memindai direktori/file tersembunyi
3. Melakukan fuzzing parameter

Contoh kode dasar:
```python
import requests
from bs4 import BeautifulSoup

def check_sql_injection(url, param):
    payloads = ["'", "' OR '1'='1", "'--"]
    for payload in payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)
        if "error in your SQL syntax" in response.text:
            return f"Vulnerable to SQLi with payload: {payload}"
    return "No SQLi vulnerability detected"
```

## 📚 Sumber Belajar
1. [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
2. [PortSwigger Web Security Academy](https://portswigger.net/web-security)
3. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
4. [Web Security Fundamentals - MDN](https://developer.mozilla.org/en-US/docs/Web/Security)

## 📅 Jadwal Latihan
| Minggu | Topik | Durasi |
|--------|-------|--------|
| 1 | Dasar Keamanan Web | 4 JP |
| 2 | OWASP Top 10 | 6 JP |
| 3 | Pengujian Keamanan | 6 JP |
| 4 | Pengembangan Aman | 4 JP |
| 5 | Forensik Web | 4 JP |
| 6 | Ujian Praktik | 4 JP |

## ⚠️ Etika dan Legalitas
1. Hanya lakukan pengujian pada sistem yang diizinkan
2. Dapatkan persetujuan tertulis sebelum pengujian
3. Patuhi hukum yang berlaku
4. Jaga kerahasiaan temuan

---
<div align="center">
  <p>Modul Latihan - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

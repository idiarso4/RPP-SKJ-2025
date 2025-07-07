# 📚 Latihan Soal - Keamanan Aplikasi Web

## 🎯 Tujuan
Latihan ini dirancang untuk menguji pemahaman Anda tentang konsep keamanan aplikasi web dan kemampuan praktis dalam mengidentifikasi serta memitigasi kerentanan.

## 📝 Soal Teori

### 1. Analisis Kasus
**Kasus:** Sebuah situs e-commerce mengalami kebocoran data pelanggan. Setelah investigasi, ditemukan bahwa serangan terjadi melalui form pencarian yang tidak melakukan validasi input dengan benar.

**Pertanyaan:**
1. Jenis serangan apa yang mungkin terjadi? Jelaskan!
2. Bagaimana cara mencegah serangan tersebut?
3. Tools apa saja yang dapat digunakan untuk mendeteksi kerentanan ini?

### 2. Perbandingan Keamanan
Bandingkan antara:
- Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF)
- SQL Injection dan NoSQL Injection
- Session Hijacking dan Session Fixation

### 3. Kriptografi Web
1. Jelaskan perbedaan antara hashing, enkripsi, dan encoding.
2. Mengapa MD5 dan SHA-1 tidak lagi direkomendasikan untuk hashing password?
3. Apa itu salt dalam konteks hashing password?

## 🛠️ Soal Praktik

### 1. Analisis Kode
```javascript
// Kode login.js
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
    
    db.query(query, (err, result) => {
        if (err) throw err;
        if (result.length > 0) {
            req.session.user = result[0];
            res.redirect('/dashboard');
        } else {
            res.send('Login gagal');
        }
    });
});
```
**Tugas:**
1. Identifikasi kerentanan pada kode di atas.
2. Tulis ulang kode untuk memperbaikinya.
3. Jelaskan perubahan yang Anda buat dan mengapa itu lebih aman.

### 2. Konfigurasi Keamanan
Buat konfigurasi Content Security Policy (CSP) untuk aplikasi web dengan ketentuan:
- Hanya mengizinkan sumber daya dari domain sendiri
- Mengizinkan Google Fonts
- Mematikan inline JavaScript
- Mengizinkan form hanya ke domain tertentu

### 3. Analisis HTTP Headers
Analisis header HTTP berikut dan identifikasi masalah keamanan:
```http
HTTP/1.1 200 OK
Server: Apache/2.4.29
X-Powered-By: PHP/7.2.24
X-AspNet-Version: 4.0.30319
X-Content-Type-Options: nosniff
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Connection: close
```

## 🧩 Tantangan Lanjutan

### 1. Eksploitasi Kerentanan
Diberikan aplikasi web dengan fitur unggah gambar. Bagaimana Anda akan menguji apakah aplikasi tersebut rentan terhadap:
1. File Upload Bypass
2. Remote Code Execution (RCE)
3. Path Traversal

### 2. Keamanan API
Buat daftar 10 praktik terbaik untuk mengamankan RESTful API.

### 3. OWASP ZAP Automation
Buat skrip Python sederhana yang mengotomatisasi pengujian dasar dengan OWASP ZAP API.

## 📝 Jawaban

### Kunci Jawaban Soal Teori

#### 1. Analisis Kasus
1. **Jenis Serangan**: SQL Injection
   - Penjelasan: Penyerang menyisipkan perintah SQL melalui form pencarian
   - Contoh payload: `' OR '1'='1`

2. **Pencegahan**:
   - Gunakan prepared statements
   - Validasi input
   - Gunakan ORM
   - Terapkan prinsip least privilege

3. **Tools**:
   - OWASP ZAP
   - SQLmap
   - Burp Suite

#### 2. Perbandingan Keamanan

**XSS vs CSRF**
| Aspek | XSS | CSRF |
|-------|-----|------|
| Eksekusi | Kode berbahaya dijalankan di browser korban | Memaksa korban mengirim permintaan yang tidak diinginkan |
| Dampak | Pencurian sesi, defacement | Tindakan tidak sah mewakili korban |
| Pertahanan | Output encoding, CSP | CSRF tokens, SameSite cookies |

**SQL Injection vs NoSQL Injection**
| Aspek | SQL Injection | NoSQL Injection |
|-------|---------------|------------------|
| Teknik | Manipulasi query SQL | Eksploitasi operator query (seperti $where di MongoDB) |
| Contoh | `' OR 1=1 --` | `{"$where": "sleep(5000)"}` |
| Pencegahan | Prepared statements, ORM | Validasi input, sanitasi, ORM |

#### 3. Kriptografi Web
1. **Perbedaan**:
   - Hashing: Satu arah, digunakan untuk penyimpanan password
   - Enkripsi: Dua arah, membutuhkan kunci
   - Encoding: Bukan untuk keamanan, hanya mengubah format data

2. **MD5 & SHA-1 tidak aman**:
   - Rentan terhadap collision attacks
   Cepat dihitung dengan hardware modern
   Sudah ada banyak rainbow tables

3. **Salt**:
   - Nilai acak yang ditambahkan ke password sebelum di-hash
   - Mencegah penggunaan rainbow tables
   - Harus unik untuk setiap pengguna

### Solusi Praktik

#### 1. Perbaikan Kode Login
```javascript
const bcrypt = require('bcrypt');

app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        
        // Validasi input
        if (!username || !password) {
            return res.status(400).send('Username dan password diperlukan');
        }

        // Gunakan parameterized query
        const query = 'SELECT * FROM users WHERE username = ?';
        const [users] = await db.execute(query, [username]);
        
        // Verifikasi user dan password
        if (users.length === 0) {
            // Jangan beri tahu user mana yang salah (username/password)
            return res.status(401).send('Autentikasi gagal');
        }
        
        const user = users[0];
        const isMatch = await bcrypt.compare(password, user.password_hash);
        
        if (!isMatch) {
            return res.status(401).send('Autentikasi gagal');
        }
        
        // Set session
        req.session.regenerate(() => {
            req.session.user = {
                id: user.id,
                username: user.username,
                role: user.role
            };
            res.redirect('/dashboard');
        });
        
    } catch (err) {
        console.error('Login error:', err);
        res.status(500).send('Terjadi kesalahan server');
    }
});
```

**Perubahan yang Dilakukan:**
1. Menggunakan parameterized query untuk mencegah SQL Injection
2. Menyimpan password dengan hashing (bcrypt)
3. Menambahkan validasi input
4. Menangani error dengan benar
5. Tidak mengungkapkan informasi sensitif dalam pesan error
6. Menggunakan session yang aman

#### 2. Contoh CSP
```http
Content-Security-Policy: 
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://trusted.cdn.com; 
  style-src 'self' https://fonts.googleapis.com; 
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data: https://trusted.cdn.com;
  form-action 'self' https://api.payment-gateway.com;
  frame-ancestors 'none';
  base-uri 'self';
  object-src 'none';
```

#### 3. Analisis Header HTTP
**Masalah Keamanan:**
1. **Server Version Disclosure**:
   - `Server: Apache/2.4.29`
   - `X-Powered-By: PHP/7.2.24`
   - `X-AspNet-Version: 4.0.30319`
   
2. **Missing Security Headers**:
   - Tidak ada `X-Frame-Options`
   - Tidak ada `X-XSS-Protection`
   - Tidak ada `Content-Security-Policy`
   - Tidak ada `Referrer-Policy`
   - Tidak ada `Feature-Policy`
   - Tidak ada `Strict-Transport-Security`

3. **Rekomendasi**:
   - Sembunyikan versi server
   - Hapus header yang tidak perlu
   - Tambahkan security headers yang kurang

---
<div align="center">
  <p>Dokumen Latihan - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

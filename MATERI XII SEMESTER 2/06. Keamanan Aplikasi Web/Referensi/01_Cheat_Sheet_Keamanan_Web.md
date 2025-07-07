# 📚 Cheat Sheet & Referensi Cepat Keamanan Aplikasi Web

## 1. OWASP Top 10 2024

### 1.1 Daftar Kerentanan Utama
| # | Kategori | Deskripsi Singkat | Contoh |
|---|----------|-------------------|--------|
| A01 | Broken Access Control | Gagal membatasi akses pengguna | Akses ke `/admin` tanpa otentikasi |
| A02 | Cryptographic Failures | Kesalahan kriptografi | Password tidak di-hash, Enkripsi lemah |
| A03 | Injection | Eksekusi kode berbahaya | SQLi, Command Injection, LDAPi |
| A04 | Insecure Design | Kelemahan desain | Logika bisnis yang cacat |
| A05 | Security Misconfiguration | Konfigurasi tidak aman | Halaman error yang menampilkan stack trace |
| A06 | Vulnerable Components | Komponen rentan | Library/framework yang tidak di-update |
| A07 | Authentication Failures | Masalah otentikasi | Kelemahan reset password, brute force |
| A08 | Software and Data Integrity | Integritas data | Update yang tidak diverifikasi |
| A09 | Security Logging & Monitoring | Pencatatan & pemantauan | Gagal mendeteksi pelanggaran |
| A10 | Server-Side Request Forgery | Pemalsuan permintaan server | Ekspos layanan internal |

## 2. Cheat Sheet Teknis

### 2.1 SQL Injection
#### Deteksi
```sql
' OR '1'='1
' UNION SELECT null,username,password FROM users--
' OR SLEEP(5)--
```

#### Pencegahan (Python)
```python
# Tidak aman
query = f"SELECT * FROM users WHERE username = '{username}'"

# Aman (Parameterized Query)
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

### 2.2 Cross-Site Scripting (XSS)
#### Payload Umum
```html
<script>alert('XSS')</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
```

#### Pencegahan (JavaScript/Node.js)
```javascript
// Menggunakan escape-html atau library serupa
const escape = require('escape-html');
app.get('/search', (req, res) => {
    const query = escape(req.query.q);
    res.send(`<p>Hasil pencarian: ${query}</p>`);
});
```

### 2.3 Cross-Site Request Forgery (CSRF)
#### Token CSRF (PHP)
```php
// Generate token
$_SESSION['csrf_token'] = bin2hex(random_bytes(32));

// Dalam form
<input type="hidden" name="csrf_token" value="<?= $_SESSION['csrf_token'] ?>">

// Validasi
if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
    die('CSRF token validation failed');
}
```

## 3. Header Keamanan HTTP

### 3.1 Header Penting
```http
Content-Security-Policy: default-src 'self';
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: no-referrer-when-downgrade
```

### 3.2 Konfigurasi Web Server
#### Nginx
```nginx
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Content-Security-Policy "default-src 'self'" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

## 4. Tools Keamanan Web

### 4.1 Pemindaian Otomatis
- **OWASP ZAP**: Pemindaian kerentanan otomatis
- **Nikto**: Pemindai server web
- **Nmap**: Pemindaian jaringan dan port
- **SQLmap**: Deteksi & eksploitasi SQLi

### 4.2 Analisis Manual
- **Burp Suite**: Testing keamanan aplikasi web
- **Browser DevTools**: Analisis request/response
- **Wireshark**: Analisis lalu lintas jaringan

## 5. Template Laporan Keamanan

### 5.1 Ringkasan Eksekutif
```markdown
# LAPORAN PENGUJIAN KEAMANAN

## Informasi Umum
- Nama Aplikasi: [Nama Aplikasi]
- URL Target: [URL]
- Tanggal Pengujian: [Tanggal]
- Tim Penguji: [Nama Tim/Anggota]

## Ringkasan Temuan
| Tingkat Keparahan | Jumlah |
|-------------------|--------|
| Kritis           | X      |
| Tinggi           | X      |
| Sedang           | X      |
| Rendah           | X      |
```

### 5.2 Template Temuan
```markdown
## [ID] Nama Kerentanan

### Deskripsi
[Deskripsi rinci kerentanan]

### Lokasi
- URL: [URL yang terpengaruh]
- Parameter: [Parameter yang rentan]
- Metode: [GET/POST/PUT/DELETE]

### Dampak
[Deskripsi dampak potensial]

### Bukti
```
[Perintah/Output yang relevan]
```

### Rekomendasi
1. [Rekomendasi spesifik]
2. [Kode contoh perbaikan]
3. [Referensi tambahan]
```

## 6. Daftar Periksa Keamanan Aplikasi Web

### 6.1 Autentikasi & Otorisasi
- [ ] Implementasi multi-faktor autentikasi
- [ ] Perlindungan terhadap brute force
- [ ] Manajemen session yang aman
- [ ] Kontrol akses berbasis peran (RBAC)

### 6.2 Validasi Input
- [ ] Validasi sisi server untuk semua input
- [ ] Sanitasi output
- [ ] Proteksi terhadap XSS
- [ ] Pembatasan ukuran input

### 6.3 Keamanan Basis Data
- [ ] Menggunakan prepared statements
- [ ] Prinsip least privilege untuk user database
- [ ] Enkripsi data sensitif
- [ ] Backup rutin

## 7. Referensi Cepat

### 7.1 Port Umum
| Port | Layanan | Catatan Keamanan |
|------|---------|------------------|
| 80   | HTTP    | Gunakan HTTPS    |
| 443  | HTTPS   | Pastikan TLS 1.2+ |
| 22   | SSH     | Nonaktifkan login root |
| 3306 | MySQL   | Jangan expose ke internet |
| 27017| MongoDB | Wajib autentikasi |

### 7.2 Sumber Daya
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [SANS Internet Storm Center](https://isc.sans.edu/)

## 8. Template Kebijakan Keamanan

### 8.1 Kebijakan Kata Sandi
- Panjang minimal 12 karakter
- Gabungkan huruf besar, kecil, angka, dan simbol
- Ganti setiap 90 hari
- Jangan gunakan kembali 5 kata sandi terakhir

### 8.2 Kebijakan Pembaruan
- Patch keamanan di-deploy dalam 30 hari
- Uji pembaruan di lingkungan staging
- Backup sebelum pembaruan
- Rencana rollback yang terdokumentasi

---
<div align="center">
  <p>Cheat Sheet & Referensi - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

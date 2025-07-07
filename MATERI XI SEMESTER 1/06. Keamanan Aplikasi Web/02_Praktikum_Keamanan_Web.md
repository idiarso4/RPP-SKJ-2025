# 🛠️ Praktikum: Keamanan Aplikasi Web

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengidentifikasi kerentanan keamanan pada aplikasi web
2. Menerapkan teknik pengujian keamanan dasar
3. Memahami dan memitigasi kerentanan OWASP Top 10
4. Menggunakan tools keamanan web seperti OWASP ZAP dan SQLMap
5. Menerapkan pengamanan pada aplikasi web

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- Komputer dengan OS Windows/Linux/macOS
- Virtual Machine (disarankan)
- Koneksi internet
- Browser web (Chrome/Firefox)
- OWASP ZAP (Zed Attack Proxy)
- SQLMap
- Docker (opsional)

### 2. Lingkungan Praktikum
Kita akan menggunakan aplikasi web yang sengaja dibuat rentan (Vulnerable Web App) untuk keperluan praktikum:

#### Opsi 1: Menggunakan Docker (Direkomendasikan)
```bash
# Install Docker terlebih dahulu
# Jalankan container DVWA (Damn Vulnerable Web App)
docker run --rm -it -p 80:80 -p 443:443 -p 3306:3306 vulnerables/web-dvwa
```

#### Opsi 2: Menggunakan Aplikasi Lokal
1. Download XAMPP: https://www.apachefriends.org/
2. Download DVWA: https://github.com/digininja/DVWA
3. Ekstrak DVWA ke folder `htdocs` XAMPP
4. Konfigurasi database di `config/config.inc.php`
5. Akses melalui http://localhost/dvwa

## 📝 Langkah Kerja

### 1. Persiapan Lingkungan

#### 1.1 Install OWASP ZAP
```bash
# Untuk Linux (Debian/Ubuntu)
sudo apt update
sudo apt install zaproxy -y

# Untuk Windows
# Download dari: https://www.zaproxy.org/download/
```

#### 1.2 Install SQLMap
```bash
# Untuk Linux (Debian/Ubuntu)
sudo apt install sqlmap -y

# Untuk Windows
# Download dari: https://github.com/sqlmapproject/sqlmap
```

### 2. Pengujian Keamanan Dasar

#### 2.1 Pemeriksaan Dasar dengan Browser
1. Buka aplikasi web target (contoh: http://localhost/dvwa)
2. Login dengan kredensial default (admin/password)
3. Ubah level keamanan ke "low" di halaman DVWA Security
4. Jelajahi aplikasi dan identifikasi:
   - Form input
   - Parameter URL
   - Cookie
   - Header HTTP

#### 2.2 Menggunakan Browser Developer Tools
1. Buka Developer Tools (F12)
2. Periksa tab:
   - Elements: Periksa kode HTML
   - Console: Periksa error JavaScript
   - Network: Pantau permintaan HTTP
   - Application: Periksa cookies dan penyimpanan lokal

### 3. Pengujian dengan OWASP ZAP

#### 3.1 Pemindaian Otomatis
1. Buka OWASP ZAP
2. Klik "Automated Scan"
3. Masukkan URL target (contoh: http://localhost/dvwa)
4. Klik "Attack"
5. Amati hasil pemindaian di tab "Alerts"

#### 3.2 Pemindaian Manual dengan Intercepting Proxy
1. Konfigurasi browser untuk menggunakan proxy ZAP (default: localhost:8080)
2. Aktifkan mode "Intercept" di ZAP
3. Jelajahi aplikasi web
4. Analisis setiap permintaan dan respons
5. Coba modifikasi parameter dan header

#### 3.3 Contoh Pengujian XSS
1. Buka halaman "XSS Reflected" di DVWA
2. Masukkan payload XSS: `<script>alert('XSS')</script>`
3. Amati hasilnya
4. Coba payload lain:
   ```
   <img src=x onerror=alert(1)>
   <svg onload=alert(1)>
   '><script>alert(1)</script>
   ```

### 4. Pengujian SQL Injection dengan SQLMap

#### 4.1 Deteksi Awal
```bash
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=your_session_id" --batch
```

#### 4.2 Mengekstrak Informasi Database
```bash
# Daftar database
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=your_session_id" --dbs

# Daftar tabel
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=your_session_id" -D dvwa --tables

# Dump data dari tabel users
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=your_session_id" -D dvwa -T users --dump
```

### 5. Meningkatkan Keamanan Aplikasi Web

#### 5.1 Menerapkan Perlindungan XSS
```php
// Sebelum (rentan)
echo $_GET['input'];

// Sesudah (aman)
echo htmlspecialchars($_GET['input'], ENT_QUOTES, 'UTF-8');
```

#### 5.2 Mencegah SQL Injection
```php
// Sebelum (rentan)
$query = "SELECT * FROM users WHERE id = " . $_GET['id'];

// Sesudah (aman menggunakan prepared statements)
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $_GET['id']]);
$results = $stmt->fetchAll();
```

#### 5.3 Mengamankan Cookie
```php
// Set cookie dengan flag HttpOnly dan Secure
setcookie(
    'session_id',
    $sessionId,
    [
        'expires' => time() + 3600,
        'path' => '/',
        'domain' => 'example.com',
        'secure' => true,     // Hanya dikirim melalui HTTPS
        'httponly' => true,  // Tidak bisa diakses JavaScript
        'samesite' => 'Strict' // Perlindungan CSRF
    ]
);
```

### 6. Pengujian Keamanan Lanjutan

#### 6.1 Pengujian CSRF
1. Buat halaman HTML dengan form yang mengirim permintaan ke aplikasi target
2. Coba akses halaman tersebut dari domain yang berbeda
3. Periksa apakah permintaan berhasil dieksekusi

#### 6.2 Pengujian Keamanan Autentikasi
1. Coba login dengan kredensial default/umum
2. Uji kebijakan kata sandi
3. Uji mekanisme penguncian akun
4. Uji alur pemulihan akun

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum keamanan aplikasi web.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Hasil Pemindaian OWASP ZAP
```
# Tempelkan screenshot hasil pemindaian
# Analisis temuan kerentanan
```

#### 4.2 Hasil Pengujian SQL Injection
```
# Tampilkan perintah SQLMap yang digunakan
# Tampilkan hasil ekstraksi data
```

#### 4.3 Hasil Pengujian XSS
```
# Deskripsikan payload yang berhasil
# Tampilkan screenshot hasil eksploitasi
```

### 5. Analisis
1. Kerentanan apa saja yang berhasil diidentifikasi?
2. Bagaimana tingkat keparahan masing-masing kerentanan?
3. Bagaimana cara memitigasi kerentanan tersebut?
4. Apa saja praktik terbaik yang harus diterapkan dalam pengembangan aplikasi web?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Coba eksploitasi kerentanan yang lebih kompleks (contoh: Blind SQL Injection, XXE, SSRF)
2. Implementasikan mekanisme keamanan tambahan seperti:
   - Content Security Policy (CSP)
   - Subresource Integrity (SRI)
   - HTTP Strict Transport Security (HSTS)
3. Buat laporan keamanan profesional dengan rekomendasi perbaikan

## ⚠️ Keamanan dan Etika
1. Hanya lakukan pengujian pada sistem yang Anda miliki atau memiliki izin
2. Dokumentasikan semua temuan dengan baik
3. Laporkan kerentanan ke pemilik sistem dengan bertanggung jawab
4. Patuhi hukum dan etika yang berlaku

## 📚 Referensi
1. OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
2. OWASP ZAP Documentation: https://www.zaproxy.org/docs/
3. SQLMap User Guide: https://github.com/sqlmapproject/sqlmap/wiki/Usage
4. Web Security Academy: https://portswigger.net/web-security

---
<div align="center">
  <p>Lembar Kerja Praktikum - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

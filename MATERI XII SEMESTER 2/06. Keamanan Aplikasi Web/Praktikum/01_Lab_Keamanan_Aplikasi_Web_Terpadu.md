# 🛠️ Praktikum: Keamanan Aplikasi Web Terpadu

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengidentifikasi kerentanan aplikasi web umum
2. Melakukan pengujian keamanan aplikasi web
3. Mengeksploitasi kerentanan secara bertanggung jawab
4. Menerapkan perbaikan keamanan
5. Mendokumentasikan temuan keamanan

## 📋 Persiapan

### 1. Lingkungan Lab
- **Sistem Operasi**: Kali Linux 2023.x
- **Target**: OWASP Juice Shop (https://github.com/bkimminich/juice-shop)
- **Tools**:
  - OWASP ZAP
  - Burp Suite Community
  - SQLmap
  - Nmap
  - Browser dengan ekstensi keamanan (HackBar, Wappalyzer)

### 2. Setup Lingkungan
```bash
# Clone OWASP Juice Shop
git clone https://github.com/bkimminich/juice-shop.git
cd juice-shop

# Install dependencies
npm install

# Jalankan aplikasi
npm start
```

## 📝 Skenario Praktikum

### 1. Pengenalan Aplikasi Target
- Buka http://localhost:3000
- Eksplorasi fitur-fitur aplikasi
- Identifikasi teknologi yang digunakan (Wappalyzer)
- Periksa source code untuk informasi sensitif

### 2. Pemetaan Aplikasi

#### 2.1 Pemindaian Dasar dengan Nmap
```bash
nmap -sV -sC -p- localhost -oN nmap_scan.txt
```

#### 2.2 Pemetaan Fitur
Buat daftar endpoint yang ditemukan:
```
/login
/register
/search
/products
/basket
/admin
```

### 3. Identifikasi Kerentanan

#### 3.1 SQL Injection
**Tujuan**: Mengidentifikasi dan mengeksploitasi SQL Injection

1. Uji form login dengan payload:
   ```
   ' OR 1=1 --
   admin'--
   ```

2. Gunakan SQLmap untuk pengujian otomatis:
   ```bash
   sqlmap -u "http://localhost:3000/rest/products/search?q=test" --batch --dbs
   ```

#### 3.2 Cross-Site Scripting (XSS)
**Tujuan**: Menemukan dan mengeksploitasi kerentanan XSS

1. Uji kolom komentar/pencarian dengan payload:
   ```html
   <script>alert('XSS')</script>
   <img src=x onerror=alert(1)>
   ```

2. Coba simpan XSS di profil pengguna

#### 3.3 Broken Authentication
**Tujuan**: Menguji mekanisme otentikasi

1. Uji bruteforce login dengan hydra:
   ```bash
   hydra -l admin -P /usr/share/wordlists/rockyou.txt localhost http-post-form "/rest/user/login:email=^USER^&password=^PASS^:Invalid"
   ```

2. Coba reset password dengan email yang tidak terdaftar

### 4. Eksploitasi Lanjutan

#### 4.1 Insecure Direct Object Reference (IDOR)
1. Temukan endpoint yang menggunakan ID numerik
2. Ubah parameter ID untuk mengakses data pengguna lain

#### 4.2 Security Misconfiguration
1. Periksa file-file sensitif:
   ```
   /.git/HEAD
   /package.json
   /server.js
   ```

2. Cari informasi sensitif di source code:
   ```bash
   grep -r "password\|secret\|key" ./
   ```

### 5. Pengujian dengan OWASP ZAP

#### 5.1 Pemindaian Otomatis
1. Buka OWASP ZAP
2. Konfigurasi browser untuk menggunakan ZAP sebagai proxy (localhost:8080)
3. Aktifkan mode pengguna aktif (spidering)
4. Jalankan pemindaian aktif

#### 5.2 Analisis Hasil
1. Identifikasi kerentanan yang ditemukan
2. Kategorikan berdasarkan tingkat keparahan
3. Dokumentasikan bukti kerentanan

### 6. Perbaikan Keamanan

#### 6.1 Input Validation
```javascript
// Sebelum
app.get('/search', (req, res) => {
    const query = req.query.q;
    db.query(`SELECT * FROM products WHERE name LIKE '%${query}%'`);
});

// Sesudah
app.get('/search', (req, res) => {
    const query = validator.escape(req.query.q);
    db.query('SELECT * FROM products WHERE name LIKE ?', [`%${query}%`]);
});
```

#### 6.2 Pencegahan XSS
```html
<!-- Sebelum -->
<div>{{ user_input }}</div>

<!-- Sesudah -->
<div>{{ user_input | escape }}</div>
```

## 📌 Tugas Praktikum

### Tugas 1: Pemetaan Aplikasi (30 menit)
1. Buat daftar lengkap endpoint aplikasi
2. Identifikasi teknologi yang digunakan
3. Dokumentasikan alur kerja aplikasi

### Tugas 2: Pengujian Keamanan (60 menit)
1. Temukan minimal 5 kerentanan berbeda
2. Dokumentasikan langkah reproduksi
3. Ambil screenshot sebagai bukti

### Tugas 3: Laporan Keamanan (60 menit)
Buat laporan yang mencakup:
1. Ringkasan eksekutif
2. Daftar kerentanan yang ditemukan
3. Dampak potensial
4. Rekomendasi perbaikan
5. Bukti temuan

## 🧩 Tantangan Lanjutan

### Tantangan 1: RCE (Remote Code Execution)
1. Temukan dan eksploitasi kerentanan RCE
2. Dapatkan akses shell ke server
3. Dokumentasikan langkah-langkahnya

### Tantangan 2: Privilege Escalation
1. Dapatkan akses admin
2. Eksplorasi fitur admin
3. Temukan flag tersembunyi

## 📚 Referensi
1. [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
2. [PortSwigger Web Security Academy](https://portswigger.net/web-security)
3. [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
4. [ZAP Getting Started](https://www.zaproxy.org/getting-started/)

## ⚠️ Etika dan Legalitas
1. Hanya lakukan pengujian pada sistem yang diizinkan
2. Dapatkan persetujuan tertulis sebelum pengujian
3. Patuhi hukum yang berlaku
4. Jaga kerahasiaan temuan

---
<div align="center">
  <p>Panduan Praktikum - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

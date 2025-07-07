# 🛠️ Panduan Praktikum: Pengujian Keamanan Aplikasi Web

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengidentifikasi kerentanan keamanan pada aplikasi web
2. Menggunakan OWASP ZAP untuk pengujian keamanan
3. Melakukan pengujian keamanan dasar
4. Menganalisis hasil pengujian dan memberikan rekomendasi

## 🛠️ Alat dan Bahan
- Komputer dengan sistem operasi Windows/Linux/macOS
- OWASP ZAP (Zed Attack Proxy)
- Aplikasi web target (contoh: OWASP Juice Shop)
- Browser web (Chrome/Firefox)
- Koneksi internet

## 📋 Langkah 1: Persiapan Lingkungan

### 1.1 Instalasi OWASP ZAP
```bash
# Untuk Ubuntu/Debian
sudo apt update
sudo apt install -y zaproxy

# Untuk Windows
# Unduh dari https://www.zaproxy.org/download/

# Untuk macOS
brew install --cask owasp-zap
```

### 1.2 Persiapan Aplikasi Target
```bash
# Menggunakan OWASP Juice Shop (aplikasi web sengaja rentan)
npm install -g @juice-shop/juice-shop
juice-shop
# Aplikasi akan berjalan di http://localhost:3000
```

## 🔍 Langkah 2: Pengenalan OWASP ZAP

### 2.1 Menjalankan ZAP
```bash
# Jalankan ZAP dari terminal
zap.sh  # Linux/macOS
zap.bat  # Windows
```

### 2.2 Antarmuka ZAP
1. **Heads Up Display (HUD)**: Mode interaktif di browser
2. **Manual Explore**: Untuk penjelajahan manual
3. **Automated Scan**: Pemindaian otomatis

## 🎯 Langkah 3: Pemindaian Dasar

### 3.1 Pemindaian Otomatis
1. Masukkan URL target (contoh: http://localhost:3000)
2. Klik "Attack" > "Automated Scan"
3. Tinjau hasil pemindaian

### 3.2 Analisis Hasil
- **Alerts**: Daftar kerentanan yang ditemukan
- **Site Tree**: Struktur situs yang dipetakan
- **History**: Riwayat permintaan/respons

## 🕵️ Langkah 4: Pengujian Manual

### 4.1 Uji SQL Injection
```sql
-- Contoh payload sederhana
' OR '1'='1
' OR 1=1 --
' UNION SELECT username, password FROM users--
```

### 4.2 Uji XSS (Cross-Site Scripting)
```html
<script>alert('XSS')</script>
<img src="x" onerror="alert('XSS')">
```

### 4.3 Uji CSRF
1. Buat halaman HTML dengan form tersembunyi
2. Coba kirim permintaan lintas situs
3. Verifikasi perlindungan CSRF token

## 📊 Langkah 5: Analisis Hasil

### 5.1 Klasifikasi Kerentanan
| Tingkat Risiko | Contoh |
|----------------|---------|
| Tinggi | SQLi, RCE, XXE |
| Sedang | XSS, CSRF, LFI |
| Rendah | Info Leakage, Clickjacking |

### 5.2 Pelaporan
```markdown
# Laporan Kerentanan

## Detail Temuan
1. **Kerentanan**: SQL Injection
   - **Lokasi**: /search?q=
   - **Risiko**: Tinggi
   - **Deskripsi**: ...
   - **Bukti**: ...
   - **Rekomendasi**: ...

## Kesimpulan
- Ringkasan temuan
- Rekomendasi perbaikan
- Rencana tindak lanjut
```

## 🧩 Tantangan Lanjutan

### 6.1 Pengujian API
```bash
# Gunakan ZAP untuk menguji API
# Contoh endpoint:
GET /api/users
POST /api/login
```

### 6.2 Otomatisasi dengan ZAP CLI
```bash
# Jalankan pemindaian otomatis
zap-cli quick-scan -s all -r http://target.com

# Hasil dalam format XML/HTML
zap-cli report -o results.html -f html
```

## 📝 Laporan Praktikum

### Format Laporan
1. **Pendahuluan**
   - Tujuan praktikum
   - Alat dan bahan

2. **Langkah Kerja**
   - Dokumentasi setiap langkah
   - Screenshot penting
   - Temuan menarik

3. **Analisis**
   - Kerentanan yang ditemukan
   - Dampak potensial
   - Bukti kerentanan

4. **Kesimpulan**
   - Ringkasan temuan
   - Rekomendasi perbaikan
   - Refleksi pembelajaran

### Template Laporan
```markdown
# Laporan Praktikum Keamanan Web

## 1. Informasi Umum
- Nama: ______________________
- Kelas: _____________________
- Tanggal: ___________________
- Target Uji: ________________

## 2. Hasil Pengujian

### 2.1 Ringkasan
- Total temuan: ___
- Tinggi: ___, Sedang: ___, Rendah: ___, Info: ___

### 2.2 Temuan Penting
1. **Judul Kerentanan**
   - Risiko: [Tinggi/Sedang/Rendah]
   - Deskripsi: ...
   - Dampak: ...
   - Rekomendasi: ...
   - Bukti: 
     ```
     [Permintaan HTTP]
     [Respons HTTP]
     ```

## 3. Lampiran
- Screenshot
- Log pengujian
- Kode eksploit (jika ada)
```

## 📚 Referensi
1. [OWASP ZAP Documentation](https://www.zaproxy.org/docs/)
2. [Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
3. [Juice Shop Documentation](https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/)

---
<div align="center">
  <p>Panduan Praktikum - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

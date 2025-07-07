# 📝 Asesmen: Dasar-dasar Keamanan Jaringan

## 🎯 Kompetensi Dasar
3.3 Menerapkan konfigurasi keamanan jaringan dasar
3.4 Menganalisis lalu lintas jaringan
3.5 Mengimplementasikan kebijakan keamanan jaringan

## 📝 Soal Pilihan Ganda

### 1. Manakah pernyataan yang BENAR tentang firewall stateful?
   a) Hanya memeriksa header paket
   b) Menyimpan informasi status koneksi
   c) Tidak dapat memblokir koneksi masuk
   d) Hanya bekerja pada lapisan jaringan
   
   **Jawaban: b) Menyimpan informasi status koneksi**  
   *Pembahasan: Firewall stateful melacak status koneksi aktif dan membuat keputusan berdasarkan konteks koneksi, tidak hanya berdasarkan header paket.*

### 2. Port default manakah yang digunakan oleh SSH?
   a) 21  
   b) 22  
   c) 23  
   d) 25
   
   **Jawaban: b) 22**  
   *Pembahasan: Port 22 adalah port default untuk protokol SSH (Secure Shell).*

### 3. Manakah yang BUKAN termasuk dalam prinsip hardening sistem?
   a) Menonaktifkan layanan yang tidak digunakan
   b) Menggunakan password yang sama untuk semua akun
   c) Memperbarui sistem secara berkala
   d) Menerapkan prinsip least privilege
   
   **Jawaban: b) Menggunakan password yang sama untuk semua akun**  
   *Pembahasan: Menggunakan password yang sama untuk semua akun merupakan praktik keamanan yang buruk dan bertentangan dengan prinsip keamanan jaringan.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara enkripsi simetris dan asimetris, serta berikan contoh penggunaannya dalam keamanan jaringan!

**Jawaban:**
**Enkripsi Simetris:**
- Menggunakan kunci yang sama untuk enkripsi dan dekripsi
- Lebih cepat dan efisien untuk data dalam jumlah besar
- Contoh algoritma: AES, DES, 3DES
- Penggunaan: Enkripsi file, enkripsi disk, enkripsi data dalam jumlah besar

**Enkripsi Asimetris:**
- Menggunakan pasangan kunci (public key dan private key)
- Lebih lambat tetapi menyelesaikan masalah pertukaran kunci
- Contoh algoritma: RSA, ECC, ElGamal
- Penggunaan: Pertukaran kunci rahasia, tanda tangan digital, sertifikat digital

### 2. Jelaskan apa yang dimaksud dengan "defense in depth" dan berikan contoh implementasinya dalam jaringan perusahaan!

**Jawaban:**
Defense in depth adalah strategi keamanan berlapis yang mengimplementasikan beberapa lapisan pertahanan untuk melindungi aset digital.

**Contoh implementasi di perusahaan:**
1. **Fisik**: Pengamanan fisik server, CCTV, akses menggunakan kartu
2. **Jaringan**: Firewall di perbatasan jaringan, segmentasi jaringan
3. **Host**: Antivirus, HIDS (Host-based Intrusion Detection System)
4. **Aplikasi**: Web Application Firewall (WAF), validasi input
5. **Data**: Enkripsi data sensitif, DLP (Data Loss Prevention)
6. **Kebijakan**: Pelatihan kesadaran keamanan, kebijakan kata sandi
7. **Monitoring**: SIEM, log management, deteksi anomali

## 📝 Studi Kasus

### Kasus: Keamanan Jaringan di Sekolah

**Deskripsi:**
Sekolah Anda baru saja memperbarui infrastruktur jaringan. Sebagai administrator jaringan, Anda diminta untuk mengamankan jaringan sekolah dengan karakteristik sebagai berikut:
- 100+ perangkat terhubung (komputer, printer, perangkat IoT)
- Server lokal untuk e-learning dan data siswa
- Akses internet untuk siswa dan staf
- Beberapa titik akses nirkabel

**Pertanyaan:**
1. Langkah-langkah apa saja yang akan Anda lakukan untuk mengamankan jaringan sekolah?
2. Bagaimana Anda akan mengelola akses pengguna yang berbeda (siswa, guru, staf)?
3. Teknologi apa saja yang akan Anda rekomendasikan untuk memonitor dan melindungi jaringan?

**Jawaban Contoh:**
1. **Langkah-langkah Pengamanan:**
   - Segmentasi jaringan dengan VLAN untuk memisahkan lalu lintas
   - Implementasikan firewall dengan kebijakan ketat
   - Gunakan WPA3 untuk jaringan nirkabel
   - Terapkan filter konten dan bandwidth management
   - Backup data secara teratur
   - Update dan patch sistem secara berkala

2. **Manajemen Akses:**
   - Buat grup pengguna dengan hak akses berbeda
   - Terapkan autentikasi 802.1X untuk jaringan kabel dan nirkabel
   - Gunakan RADIUS server untuk otentikasi terpusat
   - Terapkan kebijakan kata sandi yang kuat
   - Gunakan captive portal untuk tamu

3. **Teknologi yang Direkomendasikan:**
   - Firewall/UTM untuk perlindungan perimeter
   - IDS/IPS untuk deteksi dan pencegahan intrusi
   - SIEM untuk monitoring terpusat
   - NAC (Network Access Control) untuk kontrol akses
   - VPN untuk akses jarak jauh yang aman

## 📝 Tugas Praktik

### Instruksi:
1. Lakukan pemindaian keamanan terhadap jaringan lokal menggunakan Nmap
2. Analisis hasil pemindaian dan identifikasi potensi kerentanan
3. Buat rekomendasi untuk meningkatkan keamanan jaringan

### Langkah Kerja:
1. **Pemindaian Jaringan**
   ```bash
   # Lakukan pemindaian dasar
   nmap -sS -sV -O -T4 <target_ip>
   
   # Periksa kerentanan umum
   nmap --script vuln <target_ip>
   ```

2. **Analisis Hasil**
   - Port apa saja yang terbuka?
   - Layanan apa saja yang berjalan?
   - Apakah ada versi layanan yang rentan?
   - Apakah ada konfigurasi yang tidak aman?

3. **Rekomendasi**
   - Tutup port yang tidak diperlukan
   - Update layanan ke versi terbaru
   - Perkuat konfigurasi layanan
   - Implementasikan kontrol keamanan tambahan

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kelengkapan Pemindaian | 25% | Pemindaian mencakup semua aspek penting |
| Kedalaman Analisis | 30% | Analisis mendalam terhadap hasil pemindaian |
| Rekomendasi | 30% | Rekomendasi relevan dan dapat dilaksanakan |
| Dokumentasi | 15% | Laporan rapi dan mudah dipahami |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. b) Menyimpan informasi status koneksi
2. b) 22
3. b) Menggunakan password yang sama untuk semua akun

### Pedoman Penskoran Esai
1. **Kesesuaian jawaban** (40%): Jawaban sesuai dengan pertanyaan
2. **Kedalaman analisis** (30%): Kedalaman pemahaman konsep
3. **Contoh relevan** (20%): Contoh yang diberikan sesuai konteks
4. **Struktur jawaban** (10%): Sistematika penyampaian jawaban

## 📚 Referensi
1. NIST Special Publication 800-123: Guide to General Server Security
2. NIST Special Publication 800-41: Guidelines on Firewalls and Firewall Policy
3. OWASP Top 10 (2024)
4. RFC 4949: Internet Security Glossary

---
<div align="center">
  <p>Dokumen Asesmen - Dasar-dasar Keamanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

# 📝 Asesmen: Ancaman dan Kerentanan Jaringan

## 🎯 Kompetensi Dasar
3.6 Menganalisis ancaman keamanan jaringan
3.7 Mengevaluasi kerentanan sistem jaringan
3.8 Mengembangkan strategi mitigasi risiko keamanan

## 📝 Soal Pilihan Ganda

### 1. Manakah yang BUKAN termasuk dalam tahapan pengujian penetrasi?
   a) Perencanaan dan persiapan  
   b) Pemindaian jaringan  
   c) Eksploitasi  
   d) Pemasangan backdoor  
   
   **Jawaban: d) Pemasangan backdoor**  
   *Pembahasan: Pemasangan backdoor tidak termasuk dalam tahapan pengujian penetrasi yang etis. Tahapan yang benar meliputi perencanaan, pengumpulan informasi, pemindaian, pengujian kerentanan, eksploitasi, analisis, dan pelaporan.*

### 2. Apa yang dimaksud dengan "zero-day vulnerability"?
   a) Kerentanan yang sudah diketahui dan memiliki patch  
   b) Kerentanan yang belum diketahui oleh vendor  
   c) Kerentanan yang tidak berbahaya  
   d) Kerentanan yang hanya ada di sistem operasi tertentu  
   
   **Jawaban: b) Kerentanan yang belum diketahui oleh vendor**  
   *Pembahasan: Zero-day vulnerability adalah kerentanan keamanan yang belum diketahui oleh vendor perangkat lunak, sehingga belum ada patch atau perbaikan yang tersedia.*

### 3. Manakah yang BUKAN termasuk dalam OWASP Top 10 2024?
   a) Injection  
   b) Cross-Site Scripting (XSS)  
   c) Buffer Overflow  
   d) Broken Access Control  
   
   **Jawaban: c) Buffer Overflow**  
   *Pembahasan: Buffer Overflow tidak termasuk dalam OWASP Top 10 2024, sementara ketiga pilihan lainnya termasuk dalam daftar tersebut.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara Vulnerability Assessment dan Penetration Testing, serta kapan masing-masing pendekatan tersebut sebaiknya digunakan!

**Jawaban:**
**Vulnerability Assessment (VA):**
- Fokus pada identifikasi dan kuantifikasi kerentanan
- Dilakukan secara otomatis menggunakan tools pemindaian
- Memberikan gambaran umum tentang kerentanan yang ada
- Cocok untuk pemantauan rutin dan penilaian kepatuhan
- Contoh tools: Nessus, OpenVAS, Qualys

**Penetration Testing (Pentest):**
- Fokus pada eksploitasi kerentanan untuk membuktikan dampaknya
- Menggabungkan pendekatan otomatis dan manual
- Menunjukkan bagaimana kerentanan dapat disalahgunakan
- Cocok untuk menguji efektivitas pertahanan keamanan
- Contoh tools: Metasploit, Burp Suite, Nmap

**Kapan digunakan:**
- VA: Untuk pemindaian rutin, audit kepatuhan, penilaian keamanan berkala
- Pentest: Sebelum peluncuran sistem baru, setelah perubahan signifikan, atau setahun sekali untuk sistem kritis

### 2. Jelaskan apa yang dimaksud dengan "defense in depth" dan berikan contoh implementasinya dalam mengamankan infrastruktur jaringan perusahaan!

**Jawaban:**
**Defense in Depth** adalah strategi keamanan yang mengimplementasikan beberapa lapisan pertahanan untuk melindungi aset digital, dengan asumsi bahwa satu lapisan pertahanan mungkin gagal.

**Contoh Implementasi:**
1. **Fisik**
   - Pengamanan fisik data center
   - Kontrol akses biometrik
   - Kamera pengawas

2. **Jaringan**
   - Firewall di perimeter jaringan
   - Segmentasi jaringan dengan VLAN
   - IDS/IPS untuk deteksi dan pencegahan intrusi

3. **Host**
   - Antivirus/antimalware
   - Host-based firewall
   - Hardening sistem operasi

4. **Aplikasi**
   - Validasi input
   - Autentikasi multi-faktor
   - Enkripsi data sensitif

5. **Data**
   - Enkripsi data saat transit dan diam
   - Manajemen kunci yang aman
   - Pemisahan peran (separation of duties)

6. **Kebijakan & Prosedur**
   - Pelatihan kesadaran keamanan
   - Manajemen patch
   - Rencana respons insiden

## 📝 Studi Kasus

### Kasus: Serangan Ransomware pada Rumah Sakit

**Latar Belakang:**
Sebuah rumah sakit terkena serangan ransomware yang mengakibatkan:
- Semua data pasien terenkripsi
- Sistem elektronik tidak dapat diakses
- Pemulangan pasien tertunda
- Kerugian finansial signifikan

**Fakta:**
1. Serangan masuk melalui email phishing yang dibuka oleh staf administrasi
2. Tidak ada backup data yang terpisah dari jaringan utama
3. Sistem operasi dan aplikasi tidak diperbarui secara teratur
4. Tidak ada segmentasi jaringan antara departemen
5. Tidak ada pelatihan kesadaran keamanan untuk staf

**Pertanyaan:**
1. Identifikasi setidaknya 5 (lima) kerentanan yang dimanfaatkan dalam serangan ini!
2. Jelaskan langkah-langkah yang seharusnya diambil untuk mencegah serangan serupa di masa depan!
3. Buat rencana tanggap darurat untuk menangani insiden serupa jika terulang!

**Jawaban Contoh:**

1. **Kerentanan yang Dimanfaatkan:**
   - Kurangnya kesadaran keamanan staf (membuka email phishing)
   - Tidak ada backup data yang terisolasi
   - Sistem yang tidak terupdate/patch
   - Tidak ada segmentasi jaringan
   - Tidak ada sistem deteksi intrusi

2. **Tindakan Pencegahan:**
   - Implementasi program pelatihan kesadaran keamanan rutin
   - Membuat dan menguji prosedur backup yang terpisah dari jaringan utama
   - Menerapkan manajemen patch yang ketat
   - Melakukan segmentasi jaringan berdasarkan departemen
   - Menginstal dan mengkonfigurasi solusi EDR/XDR
   - Menerapkan prinsip least privilege

3. **Rencana Tanggap Darurat:**
   - **Segera:** Mengisolasi sistem yang terinfeksi dari jaringan
   - **1 Jam:** Mengaktifkan tim tanggap insiden
   - **4 Jam:** Mengidentifikasi vektor serangan dan mengamankan titik masuk
   - **24 Jam:** Memulihkan sistem dari backup yang bersih
   - **48 Jam:** Melakukan analisis forensik digital
   - **1 Minggu:** Melaporkan insiden ke pihak berwenang jika diperlukan
   - **2 Minggu:** Melakukan audit keamanan menyeluruh
   - **1 Bulan:** Meninjau dan memperbarui kebijakan keamanan

## 📝 Tugas Praktik

### Instruksi:
1. Lakukan pemindaian kerentanan pada sistem target menggunakan OpenVAS/GVM
2. Analisis hasil pemindaian dan identifikasi 3 (tiga) kerentanan kritis
3. Buat laporan yang berisi:
   - Deskripsi kerentanan
   - Tingkat keparahan (CVSS Score)
   - Dampak potensial
   - Langkah-langkah mitigasi

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kelengkapan Pemindaian | 25% | Pemindaian mencakup semua aspek penting |
| Ketepatan Identifikasi | 30% | Kerentanan diidentifikasi dengan benar |
| Kedalaman Analisis | 25% | Analisis dampak dan risiko yang mendalam |
| Kualitas Rekomendasi | 20% | Rekomendasi relevan dan dapat dilaksanakan |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. d) Pemasangan backdoor
2. b) Kerentanan yang belum diketahui oleh vendor
3. c) Buffer Overflow

### Pedoman Penskoran Esai
1. **Kesesuaian jawaban** (30%): Jawaban sesuai dengan pertanyaan
2. **Kedalaman analisis** (30%): Kedalaman pemahaman konsep
3. **Contoh relevan** (20%): Contoh yang diberikan sesuai konteks
4. **Struktur jawaban** (20%): Sistematika penyampaian jawaban

## 📚 Referensi
1. NIST Special Publication 800-115: Technical Guide to Information Security Testing and Assessment
2. OWASP Testing Guide v4.2
3. ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection
4. Peraturan Menteri Kominfo No. 4/2016 tentang Keamanan Sistem Elektronik

---
<div align="center">
  <p>Dokumen Asesmen - Ancaman dan Kerentanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

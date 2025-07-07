# 🔍 Analisis Jaringan

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, peserta didik diharapkan mampu:
1. Memahami konsep dan teknik dasar analisis jaringan
2. Menggunakan tools seperti Nmap untuk melakukan port scanning
3. Menganalisis lalu lintas jaringan dengan Wireshark
4. Mengidentifikasi kerentanan keamanan jaringan
5. Mendokumentasikan hasil analisis jaringan

## 📚 Materi Pembelajaran

### 1. Konsep Dasar Analisis Jaringan
   - Pengertian dan tujuan analisis jaringan
   - Prinsip-prinsip keamanan jaringan
   - Etika dalam analisis jaringan
   - Legalitas dan regulasi terkait

### 2. Port Scanning dengan Nmap
   - Pengenalan Nmap dan fungsinya
   - Teknik-teknik scanning:
     - TCP Connect Scan
     - SYN Stealth Scan
     - UDP Scan
     - Version Detection
   - Scripting Engine (NSE)
   - Output dan interpretasi hasil scan

### 3. Analisis Lalu Lintas Jaringan
   - Konsep packet sniffing
   - Pengenalan Wireshark
   - Filtering dan analisis paket
   - Identifikasi protokol dan aplikasi
   - Analisis serangan jaringan

### 4. Vulnerability Assessment
   - Konsep vulnerability assessment
   - Tools untuk vulnerability scanning
   - Interpretasi hasil scanning
   - Rekomendasi perbaikan

## 🛠️ Praktikum

### Praktikum 1: Dasar-dasar Nmap
**Tujuan**: Menguasai teknik dasar port scanning

**Alat dan Bahan**:
- Komputer dengan OS Linux/Windows
- Nmap terinstal
- Virtual Lab Network

**Langkah Kerja**:
1. Lakukan scanning dasar ke sebuah host target
   ```bash
   nmap -sV <target_ip>
   ```
2. Identifikasi layanan yang berjalan pada port terbuka
3. Simpan hasil scanning dalam format XML
4. Analisis hasil scanning

### Praktikum 2: Analisis Paket dengan Wireshark
**Tujuan**: Menganalisis lalu lintas jaringan

**Alat dan Bahan**:
- Wireshark terinstal
- Akses ke jaringan

**Langkah Kerja**:
1. Capture lalu lintas jaringan
2. Filter paket berdasarkan protokol
3. Analisis paket HTTP/HTTPS
4. Identifikasi pola serangan (jika ada)

## 📝 Tugas

### Tugas 1: Port Scanning
1. Lakukan scanning terhadap jaringan lokal
2. Identifikasi perangkat yang terhubung
3. Buat laporan berisi:
   - Daftar perangkat yang ditemukan
   - Port terbuka dan layanan yang berjalan
   - Analisis keamanan

### Tugas 2: Analisis Lalu Lintas
1. Capture lalu lintas jaringan selama 5 menit
2. Analisis protokol yang digunakan
3. Identifikasi traffic yang mencurigakan
4. Buat laporan analisis

## 📊 Penilaian

| Komponen | Bobot |
|----------|-------|
| Partisipasi | 20% |
| Praktikum | 40% |
| Tugas | 30% |
| Kuis | 10% |

## 📚 Referensi
1. Nmap Network Scanning (Gordon Lyon)
2. Wireshark Network Analysis (Laura Chappell)
3. [Nmap Documentation](https://nmap.org/book/)
4. [Wireshark Learning](https://www.wireshark.org/learn/)

## ⚠️ Catatan
- Selalu dapatkan izin sebelum melakukan scanning
- Patuhi kebijakan keamanan yang berlaku
- Dokumentasikan setiap langkah dengan baik

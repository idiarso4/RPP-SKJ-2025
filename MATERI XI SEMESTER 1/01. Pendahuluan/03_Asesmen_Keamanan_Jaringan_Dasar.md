# 📝 Asesmen: Konsep Dasar Keamanan Jaringan

## 🎯 Kompetensi Dasar
3.1 Memahami konsep dasar keamanan jaringan
3.2 Menerapkan prinsip-prinsip keamanan jaringan
3.3 Menganalisis ancaman keamanan jaringan

## 📝 Soal Pilihan Ganda

### 1. Yang BUKAN termasuk dalam prinsip dasar CIA dalam keamanan informasi adalah...
   a) Confidentiality  
   b) Integrity  
   c) Availability  
   d) Authenticity  
   
   **Jawaban: d) Authenticity**  
   *Pembahasan: Prinsip dasar CIA terdiri dari Confidentiality, Integrity, dan Availability. Authenticity adalah prinsip tambahan yang penting tetapi bukan bagian dari prinsip dasar CIA.*

### 2. Jenis ancaman yang bertujuan membuat layanan tidak dapat diakses oleh pengguna yang berwenang disebut...
   a) Phishing  
   b) DDoS  
   c) Spoofing  
   d) SQL Injection  
   
   **Jawaban: b) DDoS**  
   *Pembahasan: DDoS (Distributed Denial of Service) adalah serangan yang bertujuan membuat layanan tidak tersedia dengan membanjiri lalu lintas jaringan.*

### 3. Alat yang digunakan untuk memindai port pada jaringan adalah...
   a) Wireshark  
   b) Nmap  
   c) Metasploit  
   d) John the Ripper  
   
   **Jawaban: b) Nmap**  
   *Pembahasan: Nmap (Network Mapper) adalah alat untuk menemukan host dan layanan di jaringan komputer dengan mengirimkan paket dan menganalisis responsnya.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara ancaman (threat), kerentanan (vulnerability), dan risiko (risk) dalam konteks keamanan jaringan!

**Jawaban:**
- **Ancaman (Threat)**: Potensi bahaya yang dapat mengeksploitasi kerentanan untuk melanggar keamanan. Contoh: malware, peretas, bencana alam.
- **Kerentanan (Vulnerability)**: Kelemahan dalam sistem yang dapat dimanfaatkan oleh ancaman. Contoh: bug perangkat lunak, konfigurasi yang salah.
- **Risiko (Risk)**: Potensi kerugian atau kerusakan yang mungkin terjadi ketika ancaman mengeksploitasi kerentanan. Risiko dapat dihitung dengan rumus: Risiko = Ancaman × Kerentanan × Dampak.

### 2. Jelaskan apa yang dimaksud dengan "Defense in Depth" dan berikan contoh implementasinya!

**Jawaban:**
Defense in Depth adalah strategi keamanan berlapis yang mengimplementasikan beberapa lapisan pertahanan untuk melindungi aset digital. Contoh implementasi:
1. Firewall di perbatasan jaringan
2. Sistem deteksi intrusi (IDS)
3. Antivirus di setiap endpoint
4. Enkripsi data sensitif
5. Pelatihan kesadaran keamanan untuk pengguna
6. Pembaruan keamanan rutin

## 📝 Studi Kasus

### Kasus: Serangan Ransomware di Sekolah

**Deskripsi:**
Sekolah Anda baru saja menjadi korban serangan ransomware. Semua file penting di server terenkripsi dan penyerang meminta tebusan untuk mengembalikan akses. Analisis menunjukkan bahwa serangan dimulai dari email phishing yang dibuka oleh salah satu staf administrasi.

**Pertanyaan:**
1. Apa yang seharusnya menjadi langkah pertama dalam menangani insiden ini?
2. Langkah-langkah pencegahan apa yang bisa diimplementasikan untuk mencegah kejadian serupa di masa depan?
3. Bagaimana prinsip least privilege dapat membantu mengurangi dampak serangan semacam ini?

**Jawaban Contoh:**
1. **Langkah pertama**: Mengisolasi sistem yang terinfeksi dari jaringan untuk mencegah penyebaran lebih lanjut, kemudian mengaktifkan rencana pemulihan bencana (disaster recovery plan) jika ada.

2. **Langkah pencegahan**:
   - Pelatihan kesadaran keamanan untuk semua staf
   - Backup data secara berkala dan simpan terpisah dari jaringan utama
   - Update dan patch sistem secara teratur
   - Implementasi solusi keamanan email untuk memfilter phishing
   - Pembatasan eksekusi file dari lokasi yang tidak tepercaya

3. **Penerapan least privilege**:
   - Memberikan akses hanya pada sumber daya yang benar-benar dibutuhkan
   - Memisahkan hak akses antara pengguna biasa dan administrator
   - Menerapkan kontrol akses berbasis peran (RBAC)
   - Audit hak akses secara berkala

## 📝 Tugas Praktik

### Instruksi:
1. Unduh dan instal Wireshark di komputer Anda
2. Tangkap lalu lintas jaringan selama 5 menit saat melakukan browsing
3. Analisis paket yang ditangkap dan jawab pertanyaan berikut:
   - Protokol apa saja yang terdeteksi?
   - Apakah ada paket yang mencurigakan? Jelaskan!
   - Bagaimana cara mengamankan komunikasi yang terlihat dalam tangkapan?

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Instalasi Tools | 20 | Berhasil menginstal dan menjalankan Wireshark |
| Penangkapan Paket | 30 | Berhasil menangkap lalu lintas jaringan |
| Analisis | 30 | Mampu menganalisis paket dengan benar |
| Rekomendasi Keamanan | 20 | Memberikan rekomendasi yang relevan |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. d) Authenticity
2. b) DDoS
3. b) Nmap

### Pedoman Penskoran Esai
1. **Kesesuaian jawaban** (40%): Jawaban sesuai dengan pertanyaan
2. **Kedalaman analisis** (30%): Kedalaman pemahaman konsep
3. **Contoh relevan** (20%): Contoh yang diberikan sesuai konteks
4. **Struktur jawaban** (10%): Sistematika penyampaian jawaban

## 📚 Referensi
1. Stallings, W. (2017). Network Security Essentials (6th ed.). Pearson.
2. NIST Special Publication 800-123: Guide to General Server Security
3. OWASP Top 10 (2024)

---
<div align="center">
  <p>Dokumen Asesmen - Konsep Dasar Keamanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

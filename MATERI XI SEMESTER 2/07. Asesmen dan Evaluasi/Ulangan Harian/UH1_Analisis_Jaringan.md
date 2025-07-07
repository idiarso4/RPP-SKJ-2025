# 📝 Ulangan Harian 1: Analisis Jaringan

**Mata Pelajaran**: Sistem Keamanan Jaringan  
**Kelas/Semester**: XI/2  
**Waktu**: 90 menit  
**Pengajar**: Idiarso, S.Kom  
**Tahun Ajaran**: 2025/2026

## 🚫 Ketentuan:
1. Kerjakan secara individu
2. Dilarang bekerjasama atau menyontek
3. Jawaban ditulis pada lembar jawaban yang disediakan
4. Waktu pengerjaan 90 menit
5. Jawaban dikumpulkan dalam format PDF

## 📚 PETUNJUK UMUM
1. Baca setiap soal dengan teliti
2. Jawablah dengan singkat, padat, dan jelas
3. Untuk soal praktik, ikuti langkah-langkah yang diminta
4. Simpan file dengan format: `Nama_Kelas_UH1.pdf`

---

## A. SOAL PILIHAN GANDA (Bobot: 30%)

Pilihlah jawaban yang paling benar dengan memberikan tanda (X) pada pilihan jawaban yang tersedia!

1. Perintah Nmap manakah yang digunakan untuk melakukan SYN stealth scan?
   a) `nmap -sT`  
   b) `nmap -sS`  
   c) `nmap -sU`  
   d) `nmap -sV`

2. Protokol berikut yang TIDAK dapat dianalisis menggunakan Wireshark adalah...
   a) HTTP  
   b) HTTPS (tanpa private key)  
   c) DNS  
   d) ICMP

3. Filter Wireshark untuk menampilkan hanya paket yang berasal dari alamat IP 192.168.1.100 adalah...
   a) `ip.addr == 192.168.1.100`  
   b) `ip.src == 192.168.1.100`  
   c) `ip.source = 192.168.1.100`  
   d) `src.ip == 192.168.1.100`

4. Tujuan utama dari port scanning adalah...
   a) Mengambil alih sistem target  
   b) Mengidentifikasi layanan yang berjalan  
   c) Memperbaiki kerusakan jaringan  
   d) Mengenkripsi lalu lintas jaringan

5. Berikut ini yang BUKAN termasuk teknik pengelabuan (evasion) dalam Nmap adalah...
   a) Fragmentasi paket  
   b) Spoofing alamat IP  
   c) Menggunakan timing template  
   d) Enkripsi payload

## B. SOAL ESAI (Bobot: 40%)

1. **Analisis Nmap** (15 poin)  
   Hasil scanning Nmap menunjukkan port 22/tcp terbuka dengan layanan OpenSSH 7.9. Analisislah potensi keamanan dari temuan tersebut dan berikan rekomendasi pengamanannya!

2. **Analisis Wireshark** (15 poin)  
   Anda menemukan beberapa paket TCP dengan flag RST/ACK dalam jumlah besar dalam capture Wireshark. Jelaskan arti dari fenomena ini dan dampaknya terhadap jaringan!

3. **Etika Hacking** (10 poin)  
   Jelaskan mengapa penting untuk mendapatkan izin sebelum melakukan scanning jaringan dan analisis paket, serta konsekuensi hukum yang mungkin timbul jika melanggar aturan ini!

## C. PRAKTIKUM (Bobot: 30%)

### Tugas 1: Scanning Jaringan (15 poin)
1. Lakukan scanning terhadap alamat IP yang ditentukan menggunakan Nmap dengan parameter:
   - Deteksi versi layanan
   - Scan port 1-1000
   - Simpan hasil dalam format XML

2. Analisis hasil scanning dan identifikasi:
   - Port terbuka
   - Layanan yang berjalan
   - Potensi kerentanan

### Tugas 2: Analisis Paket (15 poin)
1. Buka file capture yang disediakan (`capture.pcapng`)
2. Analisis untuk menjawab pertanyaan:
   - Protokol apa saja yang digunakan?
   - Adakah aktivitas mencurigakan?
   - Berikan bukti dari analisis Anda

## RUBRIK PENILAIAN

### Pilihan Ganda (6 poin/salah, maks 30 poin)
- Benar: +6 poin
- Salah: 0 poin

### Esai (Maks 40 poin)
- **Kedalaman Analisis** (0-15 poin)
- **Ketepatan Konsep** (0-15 poin)
- **Struktur Penulisan** (0-10 poin)

### Praktikum (Maks 30 poin)
- **Kelengkapan** (0-10 poin)
- **Ketepatan** (0-10 poin)
- **Analisis** (0-10 poin)

## KUNCI JAWABAN (Untuk Pengajar)

### Pilihan Ganda
1. b) `nmap -sS`
2. b) HTTPS (tanpa private key)
3. b) `ip.src == 192.168.1.100`
4. b) Mengidentifikasi layanan yang berjalan
5. d) Enkripsi payload

### Pedoman Penskoran Esai
1. **Analisis Nmap**
   - Identifikasi versi OpenSSH 7.9 (3 poin)
   - Analisis kerentanan yang diketahui (4 poin)
   - Rekomendasi pengamanan (5 poin)
   - Struktur penulisan (3 poin)

2. **Analisis Wireshark**
   - Penjelasan RST/ACK (5 poin)
   - Penyebab kemunculan (5 poin)
   - Dampak terhadap jaringan (5 poin)

3. **Etika Hacking**
   - Pentingnya izin (4 poin)
   - Konsekuensi hukum (4 poin)
   - Contoh pelanggaran (2 poin)

### Pedoman Praktikum
- **Tugas 1**:  
  - Parameter scanning benar (3 poin)
  - Analisis port dan layanan (6 poin)
  - Identifikasi kerentanan (6 poin)

- **Tugas 2**:  
  - Identifikasi protokol (5 poin)
  - Deteksi aktivitas mencurigakan (5 poin)
  - Bukti analisis (5 poin)

## CATATAN PENGUMPULAN
- Kumpulkan jawaban melalui Google Classroom
- Format file: `Nama_Kelas_UH1.pdf`
- Batas waktu: [Tanggal dan Waktu]
- Keterlambatan pengumpulan akan mengurangi nilai

---

<div align="center">
  <p>Dokumen ini merupakan bagian dari materi penilaian Sistem Keamanan Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - All Rights Reserved</p>
</div>

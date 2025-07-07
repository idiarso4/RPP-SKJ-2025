# 📝 Latihan Analisis Jaringan

## Tujuan Praktikum
Latihan ini dirancang untuk menguji pemahaman Anda tentang analisis jaringan menggunakan Nmap dan Wireshark. Setelah menyelesaikan latihan ini, Anda akan mampu:
1. Melakukan scanning jaringan dengan Nmap
2. Menganalisis lalu lintas jaringan menggunakan Wireshark
3. Mengidentifikasi potensi masalah keamanan
4. Membuat laporan hasil analisis

## 🛠️ Alat yang Dibutuhkan
- Komputer dengan OS Windows/Linux
- Nmap terinstal
- Wireshark terinstal
- Akses ke jaringan laboratorium
- Virtual Machine (opsional)

## 📋 Petunjuk Umum
1. Baca setiap soal dengan cermat
2. Lakukan langkah-langkah yang diminta
3. Dokumentasikan setiap langkah dengan screenshot
4. Jawab pertanyaan yang diberikan
5. Simpan hasil kerja Anda dalam format PDF

## 🔍 Latihan 1: Pemetaan Jaringan dengan Nmap

### Tugas:
1. Lakukan scanning terhadap jaringan laboratorium menggunakan Nmap dengan parameter berikut:
   - Scan cepat (-T4)
   - Deteksi versi layanan (-sV)
   - Simpan hasil dalam format XML (-oX)

### Pertanyaan:
1. Berapa banyak host yang aktif dalam jaringan?
2. Sebutkan layanan apa saja yang berjalan pada host yang ditemukan?
3. Apakah ada layanan yang berjalan pada port tidak standar? Jelaskan.
4. Berdasarkan versi layanan yang ditemukan, apakah ada potensi kerentanan? (Gunakan searchsploit atau internet untuk mengecek)

## 📊 Latihan 2: Analisis Lalu Lintas dengan Wireshark

### Tugas:
1. Mulai capture paket dengan Wireshark
2. Lakukan aktivitas berikut:
   - Buka browser dan kunjungi http://example.com
   - Lakukan ping ke 8.8.8.8
   - Lakukan nslookup google.com
3. Hentikan capture setelah selesai

### Analisis:
1. Filter paket HTTP dan analisis:
   - Protokol apa yang digunakan?
   - Berapa ukuran paket request dan response?
   - Header HTTP apa saja yang terlihat?

2. Filter paket ICMP (ping):
   - Berapa waktu respons (RTT) untuk setiap ping?
   - Apakah ada paket yang hilang?

3. Filter paket DNS:
   - Query DNS apa saja yang dilakukan?
   - Berapa lama waktu yang dibutuhkan untuk mendapatkan respon DNS?

## 🛡️ Latihan 3: Deteksi Masalah Jaringan

### Skenario:
Anda adalah administrator jaringan yang menerima keluhan lambatnya akses internet dari beberapa pengguna.

### Tugas:
1. Gunakan Wireshark untuk menganalisis traffic jaringan
2. Identifikasi masalah potensial menggunakan filter berikut:
   ```
   tcp.analysis.retransmission    # Retransmisi
   tcp.analysis.duplicate_ack     # Duplicate ACK
   tcp.window_size == 0           # Zero window
   tcp.analysis.zero_window       # Zero window probe
   ```

### Pertanyaan:
1. Masalah apa yang terdeteksi?
2. Apa penyebab potensial dari masalah tersebut?
3. Rekomendasi apa yang dapat Anda berikan untuk memperbaiki masalah?

## 📝 Latihan 4: Analisis Keamanan

### Tugas:
1. Lakukan scanning terhadap host target menggunakan Nmap dengan script keamanan:
   ```bash
   nmap --script=vuln <target_ip>
   ```
2. Analisis hasil scanning

### Pertanyaan:
1. Kerentanan apa saja yang ditemukan?
2. Berdasarkan CVSS score, seberapa kritis kerentanan tersebut?
3. Rekomendasi perbaikan untuk setiap kerentanan?

## 📋 Format Laporan

### Cover
- Nama Lengkap
- Kelas
- Tanggal Praktikum
- Judul Laporan

### Isi Laporan
1. Pendahuluan
2. Alat dan Bahan
3. Langkah Kerja
4. Hasil dan Pembahasan
5. Kesimpulan
6. Lampiran (screenshot)

### Ketentuan:
- Gunakan bahasa Indonesia yang baik dan benar
- Setiap langkah harus didokumentasikan dengan screenshot
- Cantumkan referensi yang digunakan

## 🎯 Kriteria Penilaian

| No | Aspek Penilaian | Bobot |
|----|-----------------|-------|
| 1  | Ketepatan Jawaban | 30%  |
| 2  | Kelengkapan Dokumen | 20%  |
| 3  | Analisis Masalah | 25%  |
| 4  | Rekomendasi Perbaikan | 15% |
| 5  | Kerapihan Laporan | 10%  |

## 📅 Tenggat Waktu
Laporan harus dikumpulkan paling lambat **1 minggu** setelah praktikum dilaksanakan.

## 📞 Bantuan
Jika mengalami kesulitan, hubungi:
- Dosen: Idiarso, S.Kom
- Email: [dosen@example.com]
- Jam Konsultasi: Senin-Jumat, 13.00-15.00 WIB

---

<div align="center">
  <p>Dokumen ini merupakan bagian dari materi praktikum Analisis Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - All Rights Reserved</p>
</div>

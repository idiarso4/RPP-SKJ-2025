# 🎯 Asesmen Kompetensi: Manajemen Insiden Keamanan

## 📋 Informasi Umum
- **Mata Pelajaran**: Manajemen Insiden Keamanan
- **Kelas**: XII
- **Semester**: 2
- **Waktu**: 120 menit
- **Bobot Nilai**: 30% dari total nilai akhir

## 🔍 Bagian 1: Pemahaman Konsep (30%)

### Soal 1: Multiple Choice (Pilih jawaban yang paling tepat)
1. Tahap pertama dalam siklus hidup manajemen insiden keamanan menurut NIST SP 800-61r2 adalah:
   a) Deteksi dan Analisis  
   b) Persiapan  
   c) Pemberantasan  
   d) Pemulihan

2. Indikator berikut yang BUKAN termasuk dalam kategori IoC (Indikator Kompromi) adalah:
   a) Alamat IP mencurigakan  
   b) Hash file yang diketahui jahat  
   c) Update sistem otomatis  
   d) Polomorfisme kode berbahaya

### Soal 2: Studi Kasus
**Skenario**:
Sebuah perusahaan finansial mengalami serangan ransomware yang mengakibatkan 50% sistem tidak dapat diakses. Serangan diduga berasal dari lampiran email phishing yang dibuka oleh seorang karyawan.

**Pertanyaan**:
1. Sebutkan 5 langkah utama yang harus dilakukan oleh tim CSIRT dalam menangani insiden ini
2. Bagaimana cara mengisolasi sistem yang terinfeksi tanpa mengganggu operasional bisnis kritis?
3. Jelaskan langkah-langkah pencegahan yang dapat diambil untuk mencegah terulangnya kejadian serupa

## 🛠️ Bagian 2: Praktik (50%)

### Tugas 1: Analisis Forensik Dasar (20%)
Diberikan file memory dump (`memory_dump.mem`) dari sistem yang diduga mengalami kompromi keamanan. Lakukan analisis untuk:

1. Identifikasi proses mencurigakan yang berjalan
2. Temukan koneksi jaringan yang tidak biasa
3. Ekstrak file mencurigakan dari memory
4. Buat timeline aktivitas sistem

**Command yang harus digunakan**:
```bash
# Identifikasi profil OS
volatility -f memory_dump.mem imageinfo

# Daftar proses
volatility -f memory_dump.mem --profile=[PROFIL] pslist

# Analisis network connections
volatility -f memory_dump.mem --profile=[PROFIL] netscan

# Dump proses mencurigakan
volatility -f memory_dump.mem --profile=[PROFIL] procdump -p [PID] -D output/
```

### Tugas 2: Pembuatan Laporan Insiden (30%)
Berdasarkan hasil analisis forensik, buat laporan insiden yang mencakup:

1. Ringkasan Eksekutif
2. Kronologi Insiden
3. Temuan Utama
   - Proses mencurigakan
   - Koneksi jaringan tidak biasa
   - File berbahaya yang teridentifikasi
4. Rekomendasi Perbaikan
5. Lampiran Bukti

**Template Laporan**:
```markdown
# LAPORAN INSIDEN KEAMANAN SI-2025-XXX

## 1. Ringkasan Eksekutif
[Isi ringkasan]

## 2. Temuan Utama
### 2.1 [Nama Temuan]
- **Deskripsi**: 
- **Dampak**: 
- **Rekomendasi**:

## 3. Lampiran
- [ ] Screenshot analisis
- [ ] Log yang relevan
- [ ] Bukti digital
```

**Kriteria Penilaian**:
- Kelengkapan analisis (10%)
- Ketepatan identifikasi indikator kompromi (10%)
- Kualitas rekomendasi (5%)
- Format dan kelengkapan laporan (5%)

## 📝 Bagian 3: Simulasi Komunikasi Krisis (20%)

### Tugas 3: Pembuatan Komunikasi
Buat komunikasi resmi untuk dua audiens berikut:

1. **Internal** (Direktur IT):
   - Teknis detail insiden
   - Dampak bisnis
   - Langkah-langkah teknis yang diambil
   - Rekomendasi teknis

2. **Eksternal** (Pelanggan):
   - Penjelasan sederhana insiden
   - Dampak terhadap pelanggan
   - Tindakan yang diambil
   - Langkah perlindungan untuk pelanggan

**Format**:
- Email bisnis profesional
- Maksimal 300 kata per komunikasi
- Gunakan bahasa yang sesuai dengan audiens

## 📊 Rubrik Penilaian

### Kategori: Pemahaman Konsep (30%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Ketepatan jawaban pilihan ganda | 10% | Minimal 80% benar |
| Analisis studi kasus | 20% | Kedalaman analisis dan kelengkapan jawaban |

### Kategori: Praktik (50%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Keakuratan analisis forensik | 15% | Ketepatan identifikasi indikator kompromi |
| Kualitas laporan insiden | 20% | Kelengkapan dan kedalaman analisis |
| Rekomendasi perbaikan | 10% | Kesesuaian dan kelayakan rekomendasi |
| Dokumentasi bukti | 5% | Kelengkapan dan relevansi bukti |

### Kategori: Komunikasi (20%)
| Kriteria | Skor | Keterangan |
|----------|------|------------|
| Kesesuaian bahasa dengan audiens | 10% | Bahasa teknis untuk internal, non-teknis untuk eksternal |
| Kejelasan pesan | 5% | Mudah dipahami dan tidak ambigu |
| Profesionalisme | 5% | Format dan nada komunikasi yang tepat |

## ⚠️ Ketentuan Umum
1. Dilarang bekerja sama selama ujian
2. Semua jawaban harus didokumentasikan dengan baik
3. Waktu pengerjaan maksimal 120 menit
4. Jawaban diserahkan dalam format PDF

## 🏆 Kriteria Kelulusan
- Nilai minimal 70 untuk lulus
- Waktu pengerjaan maksimal 120 menit
- Dilarang menggunakan perangkat elektronik tambahan

## 📚 Referensi
1. NIST SP 800-61r2: Computer Security Incident Handling Guide
2. SANS Incident Handler's Handbook
3. ISO/IEC 27035:2016 - Information security incident management
4. FIRST Standards for Incident Response

---
<div align="center">
  <p>Dokumen Asesmen - Kompetensi Manajemen Insiden Keamanan</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

# 📚 Latihan Teori dan Praktik - Standar dan Metodologi Keamanan

## 🎯 Tujuan
Melatih pemahaman dan penerapan standar keamanan serta metodologi pengujian melalui latihan teori dan praktik.

## 📝 Latihan Teori

### A. Pencocokan Istilah

#### Soal 1: Cocokkan standar/kerangka kerja dengan deskripsinya:

| No | Standar/Kerangka Kerja | Deskripsi |
|----|------------------------|-----------|
| 1  | ISO/IEC 27001         | A. Kerangka kerja manajemen risiko siber |
| 2  | NIST CSF              | B. Standar manajemen keamanan informasi |
| 3  | PCI DSS               | C. Standar keamanan untuk industri pembayaran |
| 4  | OWASP ASVS            | D. Standar pengujian keamanan aplikasi web |
| 5  | PTES                  | E. Standar eksekusi pengujian penetrasi |

**Kunci Jawaban:**
1. B, 2. A, 3. C, 4. D, 5. E

---

### B. Analisis Kasus

#### Kasus: Implementasi Keamanan di Sekolah
**Latar Belakang:**
SMKN 1 Punggelan ingin meningkatkan keamanan sistem informasinya. Sekolah memiliki:
- 1 server utama
- 50 komputer client
- Jaringan Wi-Fi untuk guru dan siswa
- Aplikasi e-learning
- Data siswa dan guru

**Tugas:**
1. Identifikasi 3 standar/kerangka kerja yang sesuai
2. Jelaskan alasan pemilihan masing-masing standar
3. Buat daftar 5 kontrol keamanan prioritas

**Contoh Jawaban:**
1. **ISO/IEC 27001** - Untuk manajemen keamanan informasi menyeluruh
2. **NIST CSF** - Untuk kerangka kerja keamanan siber yang praktis
3. **OWASP Top 10** - Untuk mengamankan aplikasi web e-learning

**Kontrol Prioritas:**
1. Enkripsi data sensitif
2. Manajemen akses berbasis peran
3. Backup data rutin
4. Pembaruan keamanan berkala
5. Pelatihan kesadaran keamanan

---

## 🔧 Latihan Praktik

### Latihan 1: Analisis Kesenjangan ISO 27001

**Tujuan:** Menganalisis kesenjangan antara praktik saat ini dengan persyaratan ISO 27001

**Langkah Kerja:**
1. Unduh daftar kontrol ISO 27001 Annex A
2. Buat tabel analisis:

| No | Kontrol | Status | Keterangan | Target Pencapaian |
|----|---------|--------|------------|-------------------|
| A.5.1 | Kebijakan Keamanan | ❌ | Belum terdokumentasi | 3 Bulan |
| A.6.1 | Organisasi Keamanan | ⚠ | Sebagian | 2 Bulan |
| A.9.1 | Manajemen Akses | ✅ | Sudah diterapkan | - |

3. Identifikasi 3 area prioritas untuk perbaikan
4. Buat rencana tindakan

---

### Latihan 2: Penerapan NIST CSF

**Tugas:**
1. Unduh dokumen NIST CSF (https://www.nist.gov/cyberframework)
2. Pilih 1 fungsi (Identify, Protect, Detect, Respond, Recover)
3. Buat matriks implementasi:

```
Fungsi: [Pilih salah satu]
Kategori: [Contoh: Manajemen Aset]
Subkategori: [Contoh: Aset fisik dan perangkat dalam lingkungan dikatalogkan]

Status Saat Ini:
- [ ] Belum dimulai
- [ ] Dalam perencanaan
- [ ] Sebagian diimplementasikan
- [ ] Sepenuhnya diimplementasikan

Dokumentasi Pendukung:
1. [Nama dokumen/kebijakan]
2. [Prosedur terkait]

Tindakan yang Diperlukan:
1. [Tindakan 1]
2. [Tindakan 2]
```

---

### Latihan 3: Simulasi Assessment Risiko

**Alat:** Microsoft Excel/LibreOffice Calc

**Langkah Kerja:**
1. Buat tabel aset:

| No | Aset | Nilai (1-5) | Ancaman | Kemungkinan (1-5) | Dampak (1-5) | Risiko (KxD) |
|----|------|------------|---------|-----------------|--------------|--------------|
| 1  | Server Utama | 5 | Serangan DDoS | 3 | 4 | 12 |
| 2  | Data Siswa | 5 | Kebocoran Data | 2 | 5 | 10 |
| 3  | Jaringan Wi-Fi | 4 | Penyusupan | 4 | 3 | 12 |

2. Hitung tingkat risiko (Kemungkinan x Dampak)
3. Kategorikan risiko:
   - Rendah: 1-5
   - Sedang: 6-12
   - Tinggi: 15-25
4. Buat grafik batang untuk visualisasi

---

## 🧩 Tantangan Lanjutan

### Tantangan 1: Buat Kebijakan Keamanan
Buat draft kebijakan keamanan informasi untuk laboratorium komputer yang mencakup:
1. Ruang lingkup dan tujuan
2. Tanggung jawab
3. Kebijakan akses
4. Penggunaan perangkat
5. Tanggap insiden

### Tantangan 2: Desain Program Pelatihan
Rancang program pelatihan kesadaran keamanan untuk guru dan siswa yang mencakup:
- Topik pelatihan
- Metode penyampaian
- Durasi
- Evaluasi
- Jadwal pelatihan

## 📋 Format Laporan Latihan

### 1. Identitas
- Nama:
- Kelas:
- Tanggal:

### 2. Hasil Latihan
#### 2.1 Analisis Teori
```
[Jawaban analisis teori]
```

#### 2.2 Hasil Praktik
```
[Ringkasan hasil praktik]
```

### 3. Refleksi
- Kesulitan yang dihadapi:
- Pelajaran yang didapat:
- Ingin mempelajari lebih lanjut tentang:

## 📚 Referensi Tambahan
1. [ISO/IEC 27001:2022](https://www.iso.org/standard/27001)
2. [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
3. [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
4. [PCI DSS Standard](https://www.pcisecuritystandards.org/)

---
<div align="center">
  <p>Dokumen Latihan - Standar dan Metodologi Keamanan</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

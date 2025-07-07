# 📚 Referensi Cepat - Manajemen Risiko Siber

## 1. Template Dokumen

### 1.1 Template Analisis Risiko
```markdown
# ANALISIS RISIKO - [NAMA PROYEK/SISTEM]

## 1. Identifikasi Aset
| ID | Aset | Kategori | Nilai | Pemilik |
|----|------|----------|-------|---------|
| A1 | [Nama Aset] | [Data/Perangkat Lunak/Perangkat Keras] | [Rendah/Sedang/Tinggi] | [Pemilik] |

## 2. Penilaian Risiko
| ID Risiko | Deskripsi | Aset Terdampak | Kemungkinan | Dampak | Tingkat Risiko | Kontrol yang Ada |
|-----------|-----------|-----------------|-------------|--------|----------------|------------------|
| R1 | [Deskripsi Risiko] | [A1, A2] | [1-5] | [1-5] | [1-25] | [Kontrol] |

## 3. Rencana Mitigasi
| ID Risiko | Tindakan Mitigasi | Tanggung Jawab | Tenggat Waktu | Status |
|-----------|-------------------|----------------|----------------|--------|
| R1 | [Tindakan] | [PIC] | [DD/MM/YYYY] | [Not Started/In Progress/Completed] |
```

### 1.2 Template Laporan Insiden Keamanan
```markdown
# LAPORAN INSIDEN KEAMANAN SI-2025-XXX

## Informasi Dasar
- Nomor Tiket: 
- Dilaporkan Oleh: 
- Tanggal/Waktu: 
- Sistem Terdampak: 
- Kategori Insiden: 

## Kronologi
1. [Waktu] - [Aktivitas]

## Analisis Dampak
- Aset Terdampak:
- Dampak Bisnis:
- Dampak Hukum/Regulasi:

## Tindakan yang Dilakukan
1. [Tindakan] - [Waktu] - [Pelaksana]

## Rekomendasi
1. [Rekomendasi 1]
2. [Rekomendasi 2]

## Lampiran
- [ ] Screenshot
- [ ] Log
- [ ] Bukti Lainnya
```

## 2. Checklist Penting

### 2.1 Checklist Penilaian Risiko Awal
- [ ] Identifikasi semua aset kritis
- [ ] Pemetaan aliran data
- [ ] Identifikasi ancaman dan kerentanan
- [ ] Penilaian dampak bisnis
- [ ] Perhitungan tingkat risiko
- [ ] Identifikasi pemangku kepentingan
- [ ] Dokumentasi temuan

### 2.2 Checklist Respons Insiden
- [ ] Konfirmasi insiden
- [ ] Aktivasi tim respons
- [ ] Isolasi sistem yang terpengaruh
- [ ] Pengumpulan bukti
- [ ] Analisis forensik
- [ ] Pemulihan sistem
- [ ] Pelaporan
- [ ] Review pasca-insiden

## 3. Matriks dan Kerangka Kerja

### 3.1 Matriks Risiko (5x5)
```
         Dampak
         5   4   3   2   1
K 5    25  20  15  10   5
e 4    20  16  12   8   4
m 3    15  12   9   6   3
u 2    10   8   6   4   2
n 1     5   4   3   2   1
g
```

### 3.2 FAIR Risk Factors
```
1. Loss Event Frequency (LEF)
   ├─ Threat Event Frequency (TEF)
   └─ Vulnerability (Vuln)
       ├─ Threat Capability (TCap)
       └─ Resistance Strength (RS)

2. Loss Magnitude (LM)
   ├─ Primary Loss
   └─ Secondary Loss
```

## 4. Tools dan Perintah Penting

### 4.1 OpenVAS
```bash
# Memulai layanan
sudo gvm-start

# Memindai target
gvm-cli --gmp-username admin --gmp-password <password> --xml "<create_task><name>Scan Jaringan</name><target><hosts>192.168.1.0/24</hosts></target></create_task>"

# Melaporkan hasil
gvm-cli --get-report <report_id> --format PDF > laporan_keamanan.pdf
```

### 4.2 Nmap untuk Penilaian Risiko
```bash
# Deteksi OS dan versi layanan
nmap -A -T4 -p- <target>

# Deteksi kerentanan umum
nmap --script vuln <target>

# Ekspor hasil ke XML untuk analisis lebih lanjut
nmap -oX hasil_scan.xml <target>
```

## 5. Regulasi dan Standar

### 5.1 ISO/IEC 27005:2022
- Manajemen risiko keamanan informasi
- Kompatibel dengan ISO 31000
- Fokus pada penilaian dan pengobatan risiko

### 5.2 NIST RMF (Risk Management Framework)
1. Kategorisasi sistem
2. Pemilihan kontrol
3. Implementasi kontrol
4. Penilaian kontrol
5. Otorisasi sistem
6. Pemantauan berkelanjutan

## 6. Daftar Periksa Keamanan

### 6.1 Keamanan Jaringan
- [ ] Firewall diaktifkan dan dikonfigurasi dengan benar
- [ ] IDS/IPS aktif
- [ ] Segmentasi jaringan diterapkan
- [ ] VPN menggunakan enkripsi yang kuat

### 6.2 Keamanan Aplikasi
- [ ] Input validation
- [ ] Autentikasi dan otorisasi
- [ ] Proteksi terhadap OWASP Top 10
- [ ] Pembaruan keamanan rutin

## 7. Glosarium
- **ALE** - Annualized Loss Expectancy
- **SLE** - Single Loss Expectancy
- **ARO** - Annualized Rate of Occurrence
- **KRI** - Key Risk Indicator
- **KPI** - Key Performance Indicator
- **MTTD** - Mean Time To Detect
- **MTTR** - Mean Time To Recover

## 8. Referensi Cepat

### 8.1 Formula Penting
```
Risiko = Kemungkinan × Dampak
SLE = Nilai Aset × Faktor Eksposur
ALE = SLE × ARO
ROI = (ALE Sebelum - ALE Sesudah) - Biaya Kontrol
```

### 8.2 Skala Kualitatif
**Kemungkinan:**
1. Sangat Rendah (<1%)
2. Rendah (1-10%)
3. Sedang (11-50%)
4. Tinggi (51-90%)
5. Sangat Tinggi (>90%)

**Dampak:**
1. Tidak Signifikan
2. Minor
3. Sedang
4. Mayor
5. Kritis

## 9. Template Komunikasi Risiko

### 9.1 Laporan untuk Manajemen
```
**Subjek:** Laporan Risiko Triwulanan - Q1 2025

**Ringkasan Eksekutif:**
- Total risiko teridentifikasi: XX
- Risiko tinggi: XX
- Tren utama: [Deskripsi]

**Rekomendasi Utama:**
1. [Rekomendasi 1]
2. [Rekomendasi 2]

**Lampiran:**
- Detail analisis risiko
- Rencana aksi
```

## 10. Daftar Sumber Daya

### 10.1 Online
- [NIST Computer Security Resource Center](https://csrc.nist.gov/)
- [ISO/IEC 27000 Series](https://www.iso.org/)
- [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)

### 10.2 Buku
- "Risk Management for Cybersecurity and IT Managers" by Thomas R. Peltier
- "How to Measure Anything in Cybersecurity Risk" by Douglas W. Hubbard
- "The Failure of Risk Management" by Douglas W. Hubbard

---
<div align="center">
  <p>Referensi Cepat - Manajemen Risiko Siber</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

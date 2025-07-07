# 🏗️ Latihan Lanjutan - Manajemen Risiko Siber

## 🎯 Tujuan Pembelajaran
Melalui latihan ini, peserta didik akan mengembangkan kemampuan:
1. Menerapkan kerangka kerja manajemen risiko tingkat lanjut
2. Melakukan analisis risiko kuantitatif dengan pendekatan FAIR
3. Mengembangkan rencana respons insiden siber
4. Menerapkan manajemen risiko pada lingkungan cloud-native

## 🔍 Latihan 1: Analisis Risiko Kuantitatif dengan FAIR

### Tugas:
Gunakan metodologi FAIR (Factor Analysis of Information Risk) untuk menganalisis skenario berikut:

**Skenario:**
Sebuah API gateway yang menangani 50.000 transaksi/hari memiliki kerentanan zero-day yang baru ditemukan. Waktu rata-rata untuk patch adalah 7 hari. Nilai aset diperkirakan Rp5 miliar dengan potensi kerugian finansial Rp500 juta jika terjadi pelanggaran data.

**Langkah Kerja:**
1. Identifikasi komponen FAIR:
   - Frequency of Threat Events (LFE)
   - Probability of Action (PoA)
   - Resistance Strength (RS)
   - Loss Event Frequency (LEF)
   - Vulnerability (Vuln)
   - Threat Capability (TCap)
   - Loss Magnitude (LM)

2. Hitung:
   - Loss Event Frequency (LEF) = LFE × Vuln
   - Loss Magnitude (LM) = Probable Loss × Asset Value
   - Risk = LEF × LM

3. Gunakan data berikut:
   ```
   LFE = 1 event/tahun
   PoA = 0.7
   TCap = 0.8
   RS = 0.3
   Vuln = TCap × (1-RS) × PoA
   ```

**Deliverable:**
- Lembar kerja perhitungan risiko
- Visualisasi heatmap risiko
- Rekomendasi mitigasi berbasis hasil analisis

## 🛡️ Latihan 2: Rencana Respons Insiden Siber

### Tugas:
Buat rencana respons insiden untuk skenario berikut:

**Skenario:**
Sistem e-commerce mengalami serangan skimming kredit card melalui kerentanan pada form pembayaran. Serangan sudah berlangsung selama 3 hari sebelum terdeteksi.

**Langkah Kerja:**
1. Buat alur respons insiden dengan fase:
   - Persiapan
   - Identifikasi
   Penahanan
   - Pemberantasan
   - Pemulihan
   - Pelajaran yang Dipetik

2. Sertakan:
   - Matriks eskalasi
   - Daftar kontak darurat
   - Template komunikasi krisis
   - Daftar periksa forensik digital

**Template Komunikasi Krisis:**
```markdown
# Template Komunikasi Insiden Keamanan

**Kepada:** [Penerima]
**Dari:** [Tim Keamanan]
**Subjek:** [Tingkat Keparahan] - [Nama Insiden]

## Ringkasan Insiden
- Waktu Kejadian:
- Sistem Terdampak:
- Dampak Awal:
- Status Saat Ini:

## Tindakan yang Dilakukan
1. [Tindakan 1]
2. [Tindakan 2]
3. [Tindakan 3]

## Langkah Selanjutnya
- [ ] Tindakan jangka pendek
- [ ] Tindakan jangka menengah
- [ ] Tindakan pencegahan

## Kontak
- PIC Utama:
- Cadangan:
- Nomor Darurat:
```

## ☁️ Latihan 3: Manajemen Risiko Cloud-Native

### Tugas:
Analisis risiko arsitektur serverless berikut:

**Arsitektur:**
```
[API Gateway] → [AWS Lambda] → [DynamoDB]
         ↓
   [CloudWatch]
      ↓      ↓
[Alarm]  [S3 Backup]
```

**Identifikasi Risiko:**
1. Buat daftar 10 risiko spesifik cloud
2. Klasifikasikan berdasarkan:
   - Keamanan Konfigurasi
   - Manajemen Identitas
   - Proteksi Data
   - Monitoring
   - Kepatuhan

**Contoh Jawaban:**
| Risiko | Kategori | Dampak | Kemungkinan | Mitigasi |
|--------|----------|--------|-------------|----------|
| API Gateway tanpa WAF | Keamanan Konfigurasi | Tinggi | Sedang | Aktifkan AWS WAF |
| IAM Over-Permission | Manajemen Identitas | Kritis | Tinggi | Terapkan prinsip least privilege |

## 📊 Latihan 4: Metrik dan Pelaporan Risiko

### Tugas:
Buat dashboard manajemen risiko dengan metrik berikut:

**Metrik Wajib:**
1. **Risk Appetite Indicator**
   - Risk Exposure vs Risk Appetite
   - Risk Velocity
   - Control Effectiveness

2. **Key Risk Indicators (KRI)**
   - Mean Time to Detect (MTTD)
   - Mean Time to Respond (MTTR)
   - Vulnerability Age
   - Patching Cadence

**Tools yang Disarankan:**
- Grafana + Prometheus
- ELK Stack
- SIEM (Wazuh, AlienVault)

**Contoh Kode Query (PromQL):**
```promql
# Risiko Exposure
sum(risk_exposure) by (severity)

# MTTD
avg_over_time(alert_detection_time_seconds[7d])

# MTTR
avg_over_time(incident_resolution_time_seconds[30d])
```

## 📝 Latihan 5: Simulasi Krisis Keamanan

### Skenario:
Sebuah perusahaan fintech mengalami insiden berikut secara bersamaan:
1. Ransomware menginfeksi sistem internal
2. Kebocoran data pelanggan di dark web
3. Serangan DDoS pada layanan utama

**Tugas Tim:**
1. **Tim Manajemen**
   - Buat keputusan bisnis kritis
   - Kelola komunikasi krisis

2. **Tim Teknis**
   - Isolasi sistem yang terinfeksi
   - Pemulihan layanan kritis

3. **Tim Hukum**
 - Analisis kewajiban pelaporan
 - Persiapan respons regulator

**Durasi:** 90 menit
**Output:**
- Laporan insiden
 -Rencana pemulihan bencana
 - Presentasi lesson learned

## 🧩 Tantangan Bonus: Threat Modeling Aplikasi Modern

**Studi Kasus:**
Aplikasi microservices dengan arsitektur:
```
[Frontend] → [API Gateway] → [Auth Service]
                             ↓
                  [Order Service] → [Payment Service]
                             ↓
                       [Database]
```

**Tugas:**
1. Buat diagram aliran data (DFD)
2. Identifikasi:
   - Trust boundaries
   - Entry points
   - Data flows
   - Komponen kritis

3. Analisis menggunakan STRIDE:
   - Spoofing
   - Tampering
   - Repudiation
   - Information Disclosure
   - Denial of Service
   - Elevation of Privilege

## 📚 Sumber Belajar
1. FAIR Institute - Risk Analysis Standards
2. NIST SP 800-37 - Risk Management Framework
3. MITRE ATT&CK Framework
4. Cloud Security Alliance - Cloud Controls Matrix

---
<div align="center">
  <p>Latihan Lanjutan - Manajemen Risiko Siber</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

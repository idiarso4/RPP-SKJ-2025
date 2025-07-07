# 🏋️ Latihan Terstruktur: Manajemen Insiden Keamanan

## 🎯 Tujuan Pembelajaran
Melalui serangkaian latihan ini, peserta didik akan mengembangkan kemampuan:
1. Menerapkan prosedur tanggap insiden keamanan siber
2. Melakukan analisis forensik digital dasar
3. Menggunakan tools incident response secara efektif
4. Mendokumentasikan dan melaporkan insiden keamanan
5. Berkomunikasi dalam situasi krisis keamanan

## 🔍 Latihan 1: Identifikasi Indikator Kompromi (IoC)

### Tujuan
Mengidentifikasi dan mengkategorikan indikator kompromi dari log sistem

### Langkah Kerja
1. Analisis log akses web berikut:
```
192.168.1.100 - - [07/Jul/2025:14:22:10 +0700] "GET /wp-admin/install.php HTTP/1.1" 200 1234
192.168.1.100 - - [07/Jul/2025:14:22:15 +0700] "POST /wp-admin/setup-config.php HTTP/1.1" 200 5678
192.168.1.100 - - [07/Jul/2025:14:23:01 +0700] "GET /wp-content/uploads/shell.php?cmd=id HTTP/1.1" 200 9012
```

2. Gunakan perintah berikut untuk menganalisis log:
```bash
# Coba perintah ini di terminal
cat access.log | grep -v "200" | awk '{print $1, $6, $7, $9}' | sort | uniq -c | sort -nr | head -20
```

### Pertanyaan
1. Aktivitas mencurigakan apa yang teridentifikasi?
2. Indikator kompromi apa saja yang dapat diambil dari log tersebut?
3. Langkah apa yang harus segera diambil berdasarkan temuan ini?

## 🛡️ Latihan 2: Analisis Memory Forensik

### Tujuan
Menganalisis memory dump untuk mengidentifikasi aktivitas berbahaya

### Langkah Kerja
1. Unduh sample memory dump dari:
   ```bash
   wget https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples
   ```

2. Gunakan Volatility untuk analisis:
   ```bash
   # Identifikasi profil OS
   python vol.py -f memory.dmp imageinfo
   
   # Daftar proses yang berjalan
   python vol.py -f memory.dmp --profile=Win7SP1x64 pslist
   
   # Analisis network connections
   python vol.py -f memory.dmp --profile=Win7SP1x64 netscan
   ```

### Pertanyaan
1. Proses mencurigakan apa yang teridentifikasi?
2. Adakah koneksi jaringan yang tidak biasa?
3. Bagaimana cara mengumpulkan bukti lebih lanjut dari proses mencurigakan?

## ⚔️ Latihan 3: Pembuatan Playbook Insiden

### Tujuan
Mengembangkan prosedur standar untuk menangani jenis insiden tertentu

### Langkah Kerja
Buat playbook untuk menangani serangan ransomware dengan mengisi template berikut:

```markdown
# PLAYBOOK: PENANGANAN RANSOMWARE

## 1. Identifikasi
- Indikator serangan: [Daftar indikator]
- Sistem terdampak: [Daftar sistem]
- Dampak awal: [Deskripsi dampak]

## 2. Penanganan Awal
- Langkah isolasi: [Tindakan]
- Komunikasi internal: [Daftar pihak yang perlu dihubungi]
- Dokumentasi: [Dokumen yang perlu disiapkan]

## 3. Analisis Forensik
- Tools yang digunakan: [Daftar tools]
- Bukti yang dikumpulkan: [Jenis bukti]
- Analisis dampak: [Langkah-langkah]

## 4. Pemulihan
- Restorasi sistem: [Prosedur]
- Pembersihan: [Tindakan pembersihan]
- Validasi: [Cara memverifikasi]

## 5. Pasca Insiden
- Pelaporan: [Template laporan]
- Evaluasi: [Metrik evaluasi]
- Peningkatan: [Rekomendasi perbaikan]
```

### Pertanyaan
1. Mengapa penting memiliki playbook insiden?
2. Bagaimana cara memastikan playbook tetap relevan?
3. Siapa saja yang harus memiliki akses ke playbook ini?

## 📊 Latihan 4: Simulasi Tabletop Exercise

### Tujuan
Melatih respon tim terhadap skenario insiden keamanan

### Skenario
**Insiden**: Serangan phishing yang berhasil menginfeksi beberapa workstation dengan malware yang mencuri kredensial.

### Langkah Kerja
1. Bagi peserta menjadi beberapa peran:
   - Manajer Insiden
   - Analis Keamanan
   - Tim Komunikasi
   - Tim IT
   - Manajemen

2. Diskusikan dan dokumentasikan:
   - Langkah-langkah penanganan
   - Komunikasi yang diperlukan
   - Dokumen yang perlu disiapkan
   - Tindakan pencegahan di masa depan

### Pertanyaan
1. Tantangan apa yang dihadapi selama simulasi?
2. Apa yang bisa ditingkatkan dari respon tim?
3. Pelajaran apa yang bisa diambil dari latihan ini?

## 📝 Latihan 5: Pembuatan Laporan Insiden

### Tujuan
Membuat laporan insiden yang komprehensif

### Langkah Kerja
Buat laporan insiden berdasarkan skenario berikut:

**Skenario**: Server web perusahaan diretas dan digunakan untuk menyebarkan malware. Serangan dideteksi melalui sistem IDS yang memantau traffic tidak biasa pada port 80/443.

Gunakan template:
```markdown
# LAPORAN INSIDEN KEAMANAN SI-2025-XXX

## 1. Ringkasan Eksekutif
[Ringkasan singkat insiden]

## 2. Kronologi
- [Waktu] - [Kejadian]

## 3. Temuan Utama
### 3.1 [Nama Temuan]
- **Deskripsi**: 
- **Dampak**: 
- **Rekomendasi**:

## 4. Tindakan yang Dilakukan
1. [Tindakan 1]
2. [Tindakan 2]
3. [Tindakan 3]

## 5. Rekomendasi
1. [Rekomendasi 1]
2. [Rekomendasi 2]
3. [Rekomendasi 3]

## 6. Lampiran
- [ ] Screenshot
- [ ] Log
- [ ] Bukti Lainnya
```

### Pertanyaan
1. Mengapa laporan insiden penting?
2. Bagaimana menyampaikan temuan teknis ke manajemen non-teknis?
3. Apa saja yang harus dihindari dalam membuat laporan insiden?

## 🧩 Tantangan Lanjutan

### Tantangan 1: Analisis Malware
1. Diberikan file mencurigakan `suspicious.exe`
2. Lakukan analisis dasar menggunakan tools seperti:
   ```bash
   # Analisis string
   strings suspicious.exe > strings.txt
   
   # Analisis hash
   md5sum suspicious.exe
   sha256sum suspicious.exe
   
   # Analisis perilaku dengan Cuckoo Sandbox
   cuckoo submit suspicious.exe
   ```

### Tantangan 2: Pembuatan Dashboard Monitoring
Buat dashboard sederhana menggunakan ELK Stack untuk memantau indikator keamanan:
1. Instal ELK Stack
2. Konfigurasi Logstash untuk menerima log
3. Buat visualisasi di Kibana
4. Atur alert untuk aktivitas mencurigakan

## 📚 Sumber Belajar
1. [NIST Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
2. [SANS Incident Handler's Handbook](https://www.sans.org/security-resources/incident-handler-handbook/)
3. [MITRE ATT&CK Framework](https://attack.mitre.org/)
4. [FIRST Standards](https://www.first.org/standards/)

## 📅 Jadwal Latihan
| Minggu | Topik | Durasi |
|--------|-------|--------|
| 1 | Dasar-dasar Manajemen Insiden | 4 JP |
| 2 | Analisis Forensik Digital | 6 JP |
| 3 | Pembuatan Playbook Insiden | 4 JP |
| 4 | Simulasi Tabletop Exercise | 4 JP |
| 5 | Pembuatan Laporan Insiden | 4 JP |
| 6 | Ujian Praktik | 4 JP |

## ⚠️ Etika dan Legalitas
1. Hanya lakukan latihan pada lingkungan yang diizinkan
2. Patuhi peraturan yang berlaku
3. Jaga kerahasiaan informasi sensitif
4. Laporkan temuan yang signifikan

---
<div align="center">
  <p>Modul Latihan - Manajemen Insiden Keamanan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

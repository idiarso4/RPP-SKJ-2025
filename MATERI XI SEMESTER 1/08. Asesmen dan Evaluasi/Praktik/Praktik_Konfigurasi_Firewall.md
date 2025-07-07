# UJIAN PRAKTIK
## Konfigurasi Firewall Dasar

**Kelas**: XI SIJA  
**Waktu**: 90 menit  
**Tempat**: Lab Komputer  
**Guru Pengampu**: Idiarso, S.Kom  

### Tujuan Praktik
Peserta didik mampu mengkonfigurasi firewall dasar pada sistem operasi untuk mengamankan koneksi jaringan.

### Peralatan yang Dibutuhkan
1. Komputer dengan sistem operasi Windows 10/11
2. Akses administrator
3. Koneksi jaringan
4. Virtual Machine (opsional)

### Langkah Kerja

#### A. Persiapan (10 menit)
1. Pastikan komputer dalam keadaan menyala dan terhubung ke jaringan
2. Buka Windows Defender Firewall dengan Advanced Security
3. Catat konfigurasi default inbound dan outbound rules

#### B. Praktik (60 menit)

### Tugas 1: Membuat Inbound Rule untuk Keamanan Remote Desktop (45 menit)

#### Teori Dasar:
Remote Desktop Protocol (RDP) menggunakan port TCP 3389 secara default. Port ini sering menjadi target serikan brute force dan eksploitasi. Implementasi aturan firewall yang tepat dapat secara signifikan mengurangi risiko keamanan.

#### Langkah-langkah Detail:

1. **Membuka Windows Defender Firewall dengan Advanced Security**
   - Klik Start → Ketik "Windows Defender Firewall with Advanced Security"
   - Atau jalankan `wf.msc` dari Run (Win + R)

2. **Membuat Inbound Rule Baru**
   - Klik kanan pada "Inbound Rules" → New Rule
   - Pilih "Port" → Next
   - Pilih "TCP" dan masukkan port "3389" → Next
   - Pilih "Block the connection" → Next
   - Pastikan semua profil (Domain, Private, Public) dicentang → Next
   - Beri nama: "Block RDP Except Lab"
   - Klik Finish

3. **Mengkonfigurasi Scope untuk Mengizinkan IP Laboratorium**
   - Klik kanan rule yang baru dibuat → Properties
   - Buka tab "Scope"
   - Di bagian "Remote IP address", pilih "These IP addresses"
   - Klik "Add..." dan masukkan alamat IP laboratorium
   - Pilih "This IP address range" dan masukkan range IP jika perlu
   - Klik OK untuk menyimpan

4. **Mengaktifkan Logging**
   - Buka tab "General"
   - Centang "Log connections"
   - Klik "Customize..." dan pilih "Log successful connections" dan "Log dropped packets"
   - Klik OK

5. **Pengujian**
   - Dari komputer di luar jaringan laboratorium, coba lakukan RDP ke komputer target
   - Verifikasi bahwa koneksi ditolak
   - Dari komputer dalam jaringan laboratorium, verifikasi RDP berfungsi normal
   - Periksa log firewall untuk memverifikasi aktivitas

### Tugas 2: Membuat Outbound Rule untuk Pembatasan Waktu Akses (45 menit)

#### Teori Dasar:
Pembatasan akses berbasis waktu adalah teknik penting dalam manajemen bandwidth dan produktivitas. Firewall dapat digunakan untuk memblokir akses ke domain tertentu selama jam-jam tertentu.

#### Langkah-langkah Detail:

1. **Mengidentifikasi Domain Media Sosial**
   - Gunakan `nslookup` atau `ping` untuk mendapatkan alamat IP
   - Contoh: 
     ```
     nslookup facebook.com
     nslookup twitter.com
     nslookup instagram.com
     ```
   - Catat alamat IP yang didapatkan

2. **Membuat Outbound Rule**
   - Buka Windows Defender Firewall with Advanced Security
   - Klik kanan "Outbound Rules" → New Rule
   - Pilih "Custom" → Next
   - Pilih "All programs" atau tentukan program tertentu → Next
   - Di bagian Protocol and Ports, biarkan default (semua port) → Next
   - Di bagian Scope, masukkan alamat IP tujuan yang ingin diblokir → Next
   - Pilih "Block the connection" → Next
   - Pilih profil yang sesuai → Next
   - Beri nama: "Block Social Media School Hours"
   - Klik Finish

3. **Menambahkan Kondisi Waktu**
   - Klik kanan rule yang baru dibuat → Properties
   - Buka tab "Programs and Services"
   - Klik "Customize..." di bagian Services
   - Pilih "Apply to services only"
   - Klik OK
   - Buka tab "Advanced"
   - Klik "Customize..." di bagian Profiles
   - Pilih "All profiles" atau sesuaikan kebutuhan
   - Klik OK

4. **Menggunakan Task Scheduler untuk Mengaktifkan/Nonaktifkan Rule**
   - Buka Task Scheduler
   - Buat task baru dengan trigger pada pukul 08:00 setiap hari sekolah
   - Tambahkan action untuk mengaktifkan rule menggunakan PowerShell:
     ```powershell
     Set-NetFirewallRule -DisplayName "Block Social Media School Hours" -Enabled True
     ```
   - Buat task kedua untuk menonaktifkan rule pada pukul 14:00

### Tugas 3: Monitoring dan Analisis Log (30 menit)

#### Teori Dasar:
Logging adalah komponen penting dalam keamanan jaringan yang memungkinkan administrator untuk memantau, menganalisis, dan menanggapi insiden keamanan.

#### Langkah-langkah Detail:

1. **Mengkonfigurasi Logging Firewall**
   - Buka Windows Defender Firewall with Advanced Security
   - Klik kanan "Windows Defender Firewall with Advanced Security" → Properties
   - Untuk setiap profil (Domain, Private, Public):
     - Klik tab yang sesuai
     - Di bagian "Logging", klik "Customize..."
     - Atur "Log dropped packets" dan "Log successful connections" ke "Yes"
     - Tentukan lokasi dan ukuran maksimum file log
     - Klik OK

2. **Menggunakan PowerShell untuk Mengekstrak dan Menganalisis Log**
   ```powershell
   # Melihat log firewall
   Get-NetFirewallRule -Enabled True | Format-Table -Property DisplayName, Enabled, Direction, Action
   
   # Mengekstrak log ke file CSV
   Get-NetFirewallRule | Where-Object { $_.Enabled -eq $true } | 
   Select-Object DisplayName, Enabled, Direction, Action | 
   Export-Csv -Path "FirewallLog_$($env:USERNAME)_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
   ```

3. **Menganalisis Log dengan Message Analyzer**
   - Unduh dan instal Microsoft Message Analyzer
   - Buka file log firewall
   - Gunakan filter untuk melihat koneksi yang diblokir:
     ```
     *[System[band(Keywords, 9007199254740992)]]
     ```
   - Analisis pola serangan atau aktivitas mencurigakan

### D. Dokumentasi dan Laporan (60 menit)

#### 1. Dokumentasi Visual
   - Ambil screenshot setiap langkah konfigurasi penting
   - Sertakan tangkapan layar dari:
     - Aturan firewall yang dibuat
     - Konfigurasi scope dan port
     - Hasil pengujian koneksi
     - Contoh log yang dihasilkan

#### 2. Laporan Teknis
Buat laporan teknis yang mencakup:

**1. Pendahuluan**
- Latar belakang dan tujuan praktikum
- Alat dan bahan yang digunakan
- Lingkungan pengujian

**2. Metodologi**
- Langkah-langkah yang dilakukan
- Parameter konfigurasi
- Alat bantu yang digunakan

**3. Hasil dan Analisis**
- Konfigurasi akhir setiap rule
- Hasil pengujian fungsionalitas
- Analisis log yang dihasilkan
  - Pola lalu lintas jaringan
  - Upaya koneksi yang diblokir
  - Anomali yang terdeteksi

**4. Kendala dan Solusi**
- Masalah yang dihadapi selama praktikum
- Analisis akar masalah
- Solusi yang diterapkan
- Alternatif solusi yang mungkin

**5. Kesimpulan dan Saran**
- Pencapaian tujuan praktikum
- Rekomendasi pengembangan
- Ide untuk penelitian lebih lanjut

#### 3. Lampiran
- Screenshot konfigurasi
- Script yang digunakan
- File log mentah (format .csv)
- Referensi yang digunakan

### E. Kriteria Penilaian Lanjutan

| No | Aspek Penilaian | Sub-Aspek | Bobot | Skor Maks |
|----|-----------------|------------|-------|-----------|
| 1. | Ketepatan Konfigurasi | - Kelengkapan rule<br>- Akurasi scope dan port<br>- Validasi waktu | 30% | 30 |
| 2. | Dokumentasi | - Kelengkapan laporan<br>- Kualitas analisis<br>- Kejelasan penyajian | 25% | 25 |
| 3. | Analisis Log | - Kedalaman analisis<br>- Identifikasi pola<br>- Rekomendasi | 25% | 25 |
| 4. | Pemecahan Masalah | - Identifikasi masalah<br>- Solusi yang diusulkan<br>- Implementasi solusi | 15% | 15 |
| 5. | Waktu Pengerjaan | - Efisiensi waktu<br>- Manajemen tugas | 5% | 5 |
|    | **Total**       |            | **100%** | **100** |

### F. Referensi Tambahan
1. Microsoft Docs: Windows Firewall with Advanced Security
2. NIST Special Publication 800-41: Guidelines on Firewalls and Firewall Policy
3. SANS Institute: Firewall Checklist
4. RFC 2979: Behavior of and Requirements for Internet Firewalls
5. Best Practices for Firewall Management (CIS Controls)

### Kriteria Penilaian

| No | Aspek Penilaian | Bobot | Skor Maks |
|----|-----------------|-------|-----------|
| 1. | Ketepatan konfigurasi Inbound Rule | 25% | 25 |
| 2. | Ketepatan konfigurasi Outbound Rule | 25% | 25 |
| 3. | Monitoring dan Logging | 20% | 20 |
| 4. | Dokumentasi | 20% | 20 |
| 5. | Waktu pengerjaan | 10% | 10 |
|    | **Total**       | **100%** | **100** |

### Rubrik Penilaian

#### Inbound Rule (25 poin)
- 25: Rule berfungsi sempurna, mengikuti spesifikasi
- 20: Rule berfungsi dengan sedikit penyimpangan
- 15: Rule berfungsi sebagian
- 10: Rule tidak berfungsi tetapi konfigurasi mendekati benar
- 0: Tidak mengerjakan

#### Outbound Rule (25 poin)
- 25: Rule berfungsi sempurna, termasuk pembatasan waktu
- 20: Rule berfungsi tetapi tanpa pembatasan waktu
- 15: Rule berfungsi sebagian
- 10: Konfigurasi ada tetapi tidak berfungsi
- 0: Tidak mengerjakan

#### Monitoring dan Logging (20 poin)
- 20: Log lengkap dan mudah dibaca
- 15: Log ada tetapi kurang lengkap
- 10: Log ada tetapi sulit dibaca
- 5: Log tidak sesuai format
- 0: Tidak ada log

#### Dokumentasi (20 poin)
- 20: Dokumentasi lengkap dan rapi
- 15: Dokumentasi lengkap tetapi kurang rapi
- 10: Dokumentasi kurang lengkap
- 5: Dokumentasi tidak sesuai
- 0: Tidak ada dokumentasi

#### Waktu Pengerjaan (10 poin)
- 10: Selesai tepat waktu
- 7: Terlambat ≤ 15 menit
- 5: Terlambat > 15 menit
- 0: Tidak selesai

### Catatan Penting
1. Dilarang bekerja sama selama ujian berlangsung
2. Dilarang menggunakan perangkat komunikasi
3. Selalu backup konfigurasi sebelum melakukan perubahan
4. Laporkan kepada pengawas jika menemui kendala teknis

### Lampiran
1. Format Laporan Praktikum
2. Contoh Konfigurasi Dasar
3. Daftar Port Umum

---
**Nilai Akhir Praktik**

Nama Siswa: ______________________

| Aspek Penilaian | Skor Maks | Skor Diperoleh |
|-----------------|-----------|----------------|
| Inbound Rule    | 25        |                |
| Outbound Rule   | 25        |                |
| Monitoring      | 20        |                |
| Dokumentasi     | 20        |                |
| Waktu           | 10        |                |
| **Total**       | **100**   |                |

Catatan Khusus:



Mengetahui,
Guru Pengampu


(Idiarso, S.Kom)

# 📚 Cheat Sheet & Template Manajemen Insiden Keamanan

## 1. Perintah Penting Incident Response

### 1.1 Analisis Sistem
```bash
# Proses yang berjalan
ps aux | grep -i "backdoor\|shell\|reverse"
top -b -n 1 | head -20

# Koneksi jaringan
netstat -tulnp
ss -tulnp
lsof -i

# File dimodifikasi baru-baru ini
find / -type f -mtime -1 -ls 2>/dev/null | sort -k8

# File dengan SUID/SGID
find / -type f \( -perm -4000 -o -perm -2000 \) -ls 2>/dev/null
```

### 1.2 Analisis Jaringan
```bash
# Capture traffic
sudo tcpdump -i eth0 -w capture.pcap

# Analisis traffic HTTP
tshark -r capture.pcap -Y "http" -V | grep -i "user\|pass\|login"

# Cari koneksi mencurigakan
netstat -antp | grep ESTABLISHED | grep -v "sshd\|cron"
```

### 1.3 Memory Forensik (Volatility)
```bash
# Identifikasi profil
volatility -f memory.dmp imageinfo

# Daftar proses
volatility -f memory.dmp --profile=Win7SP1x64 pslist

# Analisis network connections
volatility -f memory.dmp --profile=Win7SP1x64 netscan

# Dump proses mencurigakan
volatility -f memory.dmp --profile=Win7SP1x64 procdump -p [PID] -D output/
```

## 2. Template Dokumen Insiden

### 2.1 Formulir Pelaporan Awal
```markdown
# FORMULIR PELAPORAN INSIDEN KEAMANAN

## Informasi Dasar
- Nomor Tiket: 
- Pelapor: 
- Tanggal/Waktu: 
- Sistem Terdampak: 
- Kategori Insiden: 

## Deskripsi Awal
[Deskripsi singkat tentang insiden]

## Dampak Awal
- [ ] Gangguan Layanan
- [ ] Kebocoran Data
- [ ] Kerusakan Sistem
- [ ] Lainnya: ______

## Tindakan Awal yang Dilakukan
1. [Tindakan 1]
2. [Tindakan 2]
3. [Tindakan 3]

## Prioritas
- [ ] Kritis (Respon Segera)
- [ ] Tinggi (Respon < 4 jam)
- [ ] Sedang (Respon < 24 jam)
- [ ] Rendah (Respon < 72 jam)
```

### 2.2 Template Komunikasi Krisis
```markdown
# KOMUNIKASI KRISIS KEAMANAN SI

## Kepada: [Penerima]
## Dari: [Pengirim]
## Tanggal: [Tanggal]
## Subjek: [Subjek]

### Ringkasan Insiden
[Deskripsi singkat insiden]

### Dampak
- [Dampak 1]
- [Dampak 2]
- [Dampak 3]

### Tindakan yang Dilakukan
1. [Tindakan 1]
2. [Tindakan 2]
3. [Tindakan 3]

### Langkah Selanjutnya
- [Langkah 1]
- [Langkah 2]

### Untuk Informasi Lebih Lanjut
[Nama Kontak]
[No. Telepon]
[Email]
```

## 3. Checklist Tanggap Insiden

### 3.1 Deteksi dan Analisis
- [ ] Kumpulkan informasi awal
- [ ] Validasi insiden
- [ ] Klasifikasikan tingkat keparahan
- [ ] Dokumentasikan semua temuan
- [ ] Beri tahu pihak terkait

### 3.2 Penanganan (Containment)
- [ ] Isolasi sistem yang terinfeksi
- [ ] Blokir akses dari sumber berbahaya
- [ ] Backup bukti digital
- [ ] Terapkan mitigasi sementara

### 3.3 Pemberantasan (Eradication)
- [ ] Identifikasi akar masalah
- [ ] Hapus komponen berbahaya
- [ ] Perbaiki kerentanan
- [ ] Perbarui sistem dan aplikasi

### 3.4 Pemulihan (Recovery)
- [ ] Kembalikan sistem dari backup bersih
- [ ] Validasi integritas sistem
- [ ] Pantau aktivitas mencurigakan
- [ ] Kembalikan operasional normal

### 3.5 Pasca Insiden
- [ ] Buat laporan insiden lengkap
- [ ] Lakukan evaluasi tim
- [ ] Perbarui prosedur dan kebijakan
- [ ] Lakukan pelatihan tambahan jika diperlukan

## 4. Daftar Periksa Forensik Digital

### 4.1 Pengumpulan Bukti
- [ ] Ambil hash semua file yang relevan
- [ ] Buat image disk forensik
- [ ] Kumpulkan log sistem dan aplikasi
- [ ] Dokumentasikan rantai kustodi

### 4.2 Analisis Awal
- [ ] Analisis timeline sistem
- [ ] Periksa autorun dan scheduled tasks
- [ ] Analisis registry (Windows) atau cron jobs (Linux)
- [ ] Periksa file prefetch (Windows) atau auditd (Linux)

## 5. Referensi Cepat

### 5.1 Port Umum dan Layanan
| Port | Layanan | Keterangan |
|------|---------|------------|
| 22 | SSH | Akses remote aman |
| 23 | Telnet | Akses remote tidak aman |
| 80/443 | HTTP/HTTPS | Layanan web |
| 445 | SMB | Berbagi file Windows |
| 3389 | RDP | Remote Desktop |

### 5.2 File Log Penting
#### Windows
- `%SystemRoot%\System32\winevt\Logs\`
- `%SystemRoot%\System32\LogFiles\`
- `%AppData%\Microsoft\Windows\Recent\`

#### Linux
- `/var/log/auth.log`
- `/var/log/syslog`
- `/var/log/secure`
- `/var/log/apache2/access.log` (web server)

## 6. Template Laporan Insiden

```markdown
# LAPORAN INSIDEN KEAMANAN SI-2025-XXX

## 1. Ringkasan Eksekutif
- **Tanggal Insiden**: 
- **Jenis Insiden**: 
- **Tingkat Keparahan**: 
- **Dampak**: 
- **Status Saat Ini**: 

## 2. Kronologi
| Waktu | Kejadian | Tindakan |
|-------|----------|----------|
| | | |

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

## 7. Daftar Kontak Darurat

### 7.1 Internal
| Nama | Jabatan | Kontak | Waktu Kerja |
|------|---------|--------|-------------|
| | CSIRT Manager | | 24/7 |
| | IT Security | | Office Hours |
| | Manajemen | | 24/7 |

### 7.2 Eksternal
| Lembaga | Kontak | Layanan |
|---------|--------|---------|
| ID-SIRTII/CC | (021) 525-8989 | Laporan Insiden Siber |
| BSSN | 0800-1000-900 | Laporan Kebocoran Data |
| Polri | 110 | Pelaporan Hukum |

---
<div align="center">
  <p>Cheat Sheet & Template - Manajemen Insiden Keamanan</p>
  <p>© 2025 SMKN 1 Punggelan - Revisi 1.0</p>
</div>

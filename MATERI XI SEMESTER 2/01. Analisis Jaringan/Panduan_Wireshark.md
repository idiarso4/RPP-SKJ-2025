# 📡 Panduan Praktikum Wireshark

## Pendahuluan
Wireshark adalah alat analisis protokol jaringan sumber terbuka yang digunakan untuk mengatasi masalah jaringan, analisis, pengembangan perangkat lunak dan protokol, serta pendidikan.

## Instalasi Wireshark

### Windows
1. Unduh installer dari [wireshark.org](https://www.wireshark.org/download.html)
2. Jalankan installer dan ikuti petunjuk
3. Pastikan untuk menginstal WinPcap/Npcap jika diminta
4. Luncurkan Wireshark sebagai administrator

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install wireshark
sudo dpkg-reconfigure wireshark-common  # Pilih 'Yes' untuk mengizinkan non-root users
sudo usermod -aG wireshark $USER
```

## Antarmuka Wireshark

### 1. Menu Utama
- **File**: Buka/menyimpan file capture
- **Capture**: Mulai/menghentikan capture
- **Analyze**: Alat analisis paket
- **Statistics**: Statistik jaringan
- **Help**: Bantuan dan dokumentasi

### 2. Toolbar
- Ikon untuk memulai/menghentikan capture
- Filter tampilan
- Opsi capture

### 3. Daftar Interface
- Menampilkan antarmuka jaringan yang tersedia
- Traffic real-time untuk setiap interface

## Dasar-dasar Penggunaan

### 1. Memulai Capture
1. Pilih interface jaringan
2. Klik ikon "shark fin" atau gunakan Ctrl+E
3. Untuk menghentikan, klik tombol merah kotak

### 2. Membaca Hasil Capture
- **No.**: Nomor urut paket
- **Time**: Waktu relatif capture
- **Source**: Alamat sumber
- **Destination**: Alamat tujuan
- **Protocol**: Protokol yang digunakan
- **Length**: Panjang paket
- **Info**: Informasi tambahan

### 3. Filter Dasar

#### Filter Capture
```
host 192.168.1.1      # Hanya menangkap traffic dari/ke host tertentu
net 192.168.1.0/24   # Traffic dalam subnet
tcp port 80          # Hanya HTTP
tcp port 443         # Hanya HTTPS
```

#### Filter Tampilan
```
http                 # Hanya paket HTTP
dns                  # Hanya paket DNS
ip.addr == 192.168.1.1  # Traffic yang melibatkan alamat IP ini
tcp.port == 22       # Hanya SSH traffic
```

## Analisis Paket

### 1. Menganalisis HTTP Traffic
1. Filter: `http`
2. Cari paket dengan metode GET/POST
3. Klik kanan → Follow → TCP Stream
4. Analisis header dan konten

### 2. Menganalisis DNS Queries
1. Filter: `dns`
2. Perhatikan query dan response
3. Identifikasi domain yang diakses

### 3. Mendeteksi Masalah Jaringan
- **Retransmisi**: `tcp.analysis.retransmission`
- **Duplicate ACKs**: `tcp.analysis.duplicate_ack`
- **Window Full**: `tcp.window_size == 0`

## Praktikum

### Latihan 1: Analisis HTTP
1. Mulai capture
2. Buka browser dan kunjungi sebuah website
3. Hentikan capture
4. Filter `http`
5. Analisis paket HTTP

### Latihan 2: Analisis DNS
1. Mulai capture
2. Lakukan beberapa query DNS (nslookup, ping ke domain)
3. Hentikan capture
4. Filter `dns`
5. Analisis query dan response

### Latihan 3: Deteksi Masalah
1. Mulai capture
2. Lakukan beberapa operasi jaringan
3. Hentikan capture
4. Gunakan filter untuk mendeteksi masalah
5. Analisis penyebab masalah

## Tips dan Trik

### 1. Warna dalam Wireshark
- **Hijau**: Traffic TCP
- **Biru**: Traffic DNS
- **Hitam**: Paket dengan error

### 2. Shortcut Penting
- `Ctrl+E`: Mulai/menghentikan capture
- `Ctrl+K`: Hentikan semua capture
- `Ctrl+R`: Reload file capture
- `Ctrl+→`: Ke paket berikutnya
- `Ctrl+←`: Ke paket sebelumnya

### 3. Export Data
- File → Export Objects → HTTP
- File → Export Specified Packets
- File → Export Packet Dissections

## Keamanan
1. **Hati-hati** dengan informasi sensitif
2. Jangan capture di jaringan yang tidak dikenal
3. Hapus capture yang berisi data sensitif
4. Patuhi kebijakan privasi

## Troubleshooting

### Wireshark tidak mendeteksi interface
- Pastikan Npcap/WinPcap terinstal
- Jalankan sebagai administrator
- Restart Wireshark

### Performa lambat
- Gunakan capture filter
- Batasi ukuran file capture
- Nonaktifkan resolusi nama jika tidak perlu

## Referensi
1. [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/)
2. [Wireshark Display Filters](https://wiki.wireshark.org/DisplayFilters)
3. [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures)

---

<div align="center">
  <p>Dokumen ini merupakan bagian dari materi praktikum Analisis Jaringan</p>
  <p>© 2025 SMKN 1 Punggelan - All Rights Reserved</p>
</div>

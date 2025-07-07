# 📚 Latihan Soal - Keamanan IoT

## 🎯 Tujuan Latihan
- Memahami konsep keamanan IoT
- Menganalisis kerentanan perangkat IoT
- Menerapkan praktik keamanan terbaik
- Mengembangkan keterampilan pemecahan masalah

## 📝 Soal Teori

### Soal 1: Konsep Dasar
1. Jelaskan perbedaan antara autentikasi dan otorisasi dalam konteks keamanan IoT!
2. Mengapa perangkat IoT seringkali menjadi target serangan DDoS? Jelaskan minimal 3 alasan!
3. Apa yang dimaksud dengan "secure boot" dan mengapa penting untuk perangkat IoT?

### Soal 2: Analisis Kasus
4. Analisislah kasus serangan Mirai Botnet:
   - Bagaimana cara kerjanya?
   - Apa dampaknya?
   - Bagaimana cara mencegah serangan serupa?

5. Sebuah kamera IP memiliki kerentanan sebagai berikut:
   - Port 554 (RTSP) terbuka tanpa autentikasi
   - Firmware versi 1.0.0 (terakhir update 2018)
   - Menggunakan kredensial default admin:admin
   
   Analisislah risiko keamanannya dan berikan rekomendasi perbaikannya!

## 💻 Soal Praktik

### Latihan 1: Pemindaian Jaringan IoT
Buatlah laporan pemindaian keamanan untuk perangkat IoT dengan langkah-langkah:
1. Lakukan pemindaian port menggunakan Nmap
2. Identifikasi layanan yang berjalan
3. Periksa kerentanan yang diketahui
4. Berikan rekomendasi keamanan

**Contoh Output:**
```
Hasil Pemindaian Perangkat IoT (192.168.1.100):
- Port 80/tcp: HTTP (Web Interface)
- Port 554/tcp: RTSP (Tanpa Autentikasi)
- Port 8000/tcp: Layanan Tidak Dikenal

Rekomendasi:
1. Nonaktifkan RTSP atau aktifkan autentikasi
2. Update firmware ke versi terbaru
3. Ubah kredensial default
```

### Latihan 2: Analisis Lalu Lintas IoT
1. Capture lalu lintas jaringan perangkat IoT menggunakan Wireshark
2. Analisis protokol yang digunakan
3. Identifikasi data sensitif yang dikirim tanpa enkripsi
4. Buat laporan temuan

### Latihan 3: Hardening Perangkat IoT
Buatlah panduan langkah demi langkah untuk mengamankan perangkat IoT dengan spesifikasi:
- Router WiFi rumah
- Kamera IP
- Smart Speaker

## 🧩 Tantangan Lanjutan

### Tantangan 1: IoT Penetration Testing
Lakukan pengujian penetrasi terhadap perangkat IoT dengan langkah-langkah:
1. Pemetaan jaringan
2. Identifikasi kerentanan
3. Eksploitasi (hanya dengan izin)
4. Dokumentasi temuan

### Tantangan 2: IoT Security Monitoring
Buatlah sistem pemantauan keamanan IoT sederhana yang dapat:
- Mendeteksi perangkat baru di jaringan
- Memindai kerentanan umum
- Memberikan peringatan untuk aktivitas mencurigakan

## 📝 Jawaban

### Kunci Jawaban Soal Teori

#### Soal 1:
1. **Autentikasi** memverifikasi identitas pengguna/perangkat, sedangkan **Otorisasi** menentukan hak akses yang dimiliki.

2. Alasan perangkat IoT sering menjadi target DDoS:
   - Banyak perangkat menggunakan kredensial default
   - Jarang diupdate
   - Terhubung langsung ke internet
   - Sumber daya terbatas untuk keamanan

3. **Secure boot** memastikan hanya kode yang terpercaya yang dijalankan saat boot, penting untuk mencegah eksekusi kode berbahaya.

#### Soal 2:
4. **Mirai Botnet**:
   - **Cara kerja**: Menginfeksi perangkat IoT dengan kredensial default
   - **Dampak**: Menciptakan botnet besar untuk serangan DDoS
   - **Pencegahan**: Ubah kredensial default, update firmware, segmentasi jaringan

5. **Analisis Risiko Kamera IP**:
   - **Risiko**:
     1. Akses tidak sah ke stream video
     2. Perangkat dapat direkrut ke botnet
     3. Potensi serangan ke jaringan internal
   - **Rekomendasi**:
     1. Update firmware ke versi terbaru
     2. Aktifkan autentikasi RTSP
     3. Ubah kredensial default
     4. Batasi akses jaringan

## 📚 Referensi
1. OWASP IoT Project
2. NIST IoT Security Guidelines
3. ENISA Baseline Security Recommendations
4. IoT Security Foundation Best Practices

---
<div align="center">
  <p>Dokumen Latihan - Keamanan IoT</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

# 🔐 Sistem Autentikasi Terpusat

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, peserta didik diharapkan mampu:
1. Memahami konsep AAA (Authentication, Authorization, Accounting)
2. Mengimplementasikan FreeRADIUS server
3. Mengkonfigurasi autentikasi terpusat pada perangkat jaringan
4. Memecahkan masalah konfigurasi autentikasi

## 📚 Materi Pembelajaran

### 1. Konsep Dasar AAA
   - Pengenalan Authentication, Authorization, dan Accounting
   - Protokol RADIUS dan TACACS+
   - Arsitektur sistem autentikasi terpusat

### 2. FreeRADIUS Server
   - Instalasi dan konfigurasi dasar
   - Manajemen user dan grup
   - Konfigurasi client network devices
   - Testing dan troubleshooting

### 3. Integrasi dengan Perangkat Jaringan
   - Konfigurasi MikroTik sebagai RADIUS client
   - Konfigurasi switch manageable
   - Integrasi dengan wireless controller

### 4. Keamanan dan Monitoring
   - Enkripsi komunikasi RADIUS
   - Logging dan monitoring
   - Best practice keamanan

## 🛠️ Praktikum
### Praktikum 1: Instalasi FreeRADIUS
**Tujuan**: Menginstall dan mengkonfigurasi FreeRADIUS server dasar

**Langkah Kerja**:
1. Update sistem dan install paket yang diperlukan
   ```bash
   sudo apt update
   sudo apt install freeradius freeradius-mysql freeradius-utils
   ```
2. Verifikasi instalasi
   ```bash
   sudo systemctl status freeradius
   ```
3. Konfigurasi dasar di `/etc/freeradius/3.0/clients.conf`
4. Tambahkan test user di `/etc/freeradius/3.0/mods-config/files/authorize`
5. Restart service dan test koneksi

### Praktikum 2: Konfigurasi MikroTik sebagai RADIUS Client
1. Tambahkan konfigurasi di FreeRADIUS untuk mengizinkan MikroTik
2. Di MikroTik, buka Winbox dan navigasi ke:
   - Radius → +
   - Isi alamat server RADIUS
   - Masukkan shared secret
   - Aktifkan service yang diinginkan (PPP, Hotspot, dll)
3. Test koneksi dari MikroTik ke RADIUS server

## 📝 Tugas
1. Buat dokumen yang berisi:
   - Diagram arsitektur sistem autentikasi
   - Konfigurasi lengkap FreeRADIUS
   - Screenshot konfigurasi perangkat jaringan
   - Hasil testing dan validasi

## 📊 Penilaian
| Komponen | Bobot |
|----------|-------|
| Partisipasi | 20% |
| Praktikum | 40% |
| Tugas | 30% |
| Kuis | 10% |

## 📚 Referensi
1. FreeRADIUS Documentation
2. MikroTik RADIUS Integration Guide
3. RFC 2865 - Remote Authentication Dial In User Service

## ⚠️ Catatan
- Selalu backup konfigurasi sebelum perubahan
- Dokumentasikan setiap perubahan yang dilakukan
- Patuhi kebijakan keamanan yang berlaku

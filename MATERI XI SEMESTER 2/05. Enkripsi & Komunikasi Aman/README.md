# 🔒 Enkripsi & Komunikasi Aman

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, peserta didik diharapkan mampu:
1. Memahami konsep kriptografi modern
2. Mengimplementasikan enkripsi data
3. Mengkonfigurasi VPN
4. Menerapkan protokol komunikasi aman

## 📚 Materi Pembelajaran

### 1. Dasar-dasar Kriptografi
   - Konsep enkripsi simetris dan asimetris
   - Algoritma modern (AES, RSA, ECC)
   - Fungsi hash dan digital signature
   - Public Key Infrastructure (PKI)

### 2. Implementasi Enkripsi
   - Enkripsi disk (LUKS, BitLocker)
   - Enkripsi file dan folder
   - Enkripsi email (PGP/GPG)
   - Enkripsi pesan instan

### 3. Virtual Private Network (VPN)
   - Konsep dan arsitektur VPN
   - Protokol VPN (IPsec, OpenVPN, WireGuard)
   - Konfigurasi server dan client
   - Troubleshooting koneksi VPN

### 4. Protokol Komunikasi Aman
   - TLS/SSL dan implementasinya
   - SSH untuk remote access yang aman
   - SFTP/SCP untuk transfer file
   - DNS Security Extensions (DNSSEC)

## 🛠️ Praktikum

### Praktikum 1: Enkripsi File dengan GPG
**Tujuan**: Mengenkripsi dan mendekripsi file menggunakan GPG

**Langkah Kerja**:
1. Install GnuPG
   ```bash
   sudo apt install gnupg
   ```
2. Generate key pair
   ```bash
   gpg --full-generate-key
   ```
3. Enkripsi file
   ```bash
   gpg --encrypt --recipient 'recipient@example.com' file.txt
   ```
4. Dekripsi file
   ```bash
   gpg --decrypt file.txt.gpg > file.txt
   ```

### Praktikum 2: Setup OpenVPN Server
1. Install OpenVPN dan Easy-RSA
   ```bash
   sudo apt install openvpn easy-rsa
   ```
2. Setup PKI
   ```bash
   make-cadir ~/openvpn-ca
   cd ~/openvpn-ca
   ```
3. Generate CA dan sertifikat server
4. Konfigurasi server OpenVPN
5. Generate konfigurasi client
6. Uji koneksi VPN

## 📝 Tugas
1. Buat laporan yang berisi:
   - Perbandingan algoritma enkripsi
   - Dokumentasi konfigurasi VPN
   - Analisis keamanan implementasi
   - Rekomendasi penguatan keamanan

## 📊 Penilaian
| Komponen | Bobot |
|----------|-------|
| Partisipasi | 20% |
| Praktikum | 40% |
| Tugas | 30% |
| Kuis | 10% |

## 📚 Referensi
1. NIST Special Publication 800-57
2. OpenVPN Documentation
3. RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3

## ⚠️ Catatan
- Selalu backup private key dan sertifikat
- Perbarui konfigurasi keamanan secara berkala
- Dokumentasikan semua konfigurasi yang dilakukan
- Patuhi regulasi yang berlaku terkait penggunaan kriptografi

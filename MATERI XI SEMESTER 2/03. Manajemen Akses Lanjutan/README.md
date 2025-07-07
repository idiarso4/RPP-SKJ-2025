# 🔑 Manajemen Akses Lanjutan

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, peserta didik diharapkan mampu:
1. Memahami konsep Multi-Factor Authentication (MFA)
2. Mengimplementasikan berbagai metode otentikasi
3. Mengelola kebijakan akses berbasis peran (RBAC)
4. Menerapkan prinsip least privilege

## 📚 Materi Pembelajaran

### 1. Multi-Factor Authentication (MFA)
   - Konsep dasar MFA
   - Jenis faktor autentikasi (knowledge, possession, inherence)
   - Metode MFA (OTP, Biometrik, Hardware Token)
   - Aplikasi authenticator (Google Authenticator, Microsoft Authenticator)

### 2. Role-Based Access Control (RBAC)
   - Konsep dasar RBAC
   - Implementasi di sistem operasi
   - Manajemen grup dan izin
   - Best practice implementasi

### 3. Privileged Access Management (PAM)
   - Konsep least privilege
   - Manajemen akun privileged
   - Solusi PAM (CyberArk, Thycotic)
   - Audit dan monitoring akses

### 4. Identity and Access Management (IAM)
   - Arsitektur IAM
   - Single Sign-On (SSO)
   - Federated Identity
   - Integrasi dengan layanan cloud

## 🛠️ Praktikum

### Praktikum 1: Implementasi Google Authenticator
**Tujuan**: Mengimplementasikan MFA menggunakan Google Authenticator

**Langkah Kerja**:
1. Install paket yang diperlukan
   ```bash
   sudo apt install libpam-google-authenticator
   ```
2. Konfigurasi PAM
   ```
   auth required pam_google_authenticator.so
   ```
3. Setup untuk user
   ```bash
   google-authenticator
   ```
4. Scan barcode dengan aplikasi Google Authenticator
5. Test login dengan kode OTP

### Praktikum 2: Konfigurasi RBAC di Linux
1. Buat grup baru
   ```bash
   sudo groupadd developers
   ```
2. Tambahkan user ke grup
   ```bash
   sudo usermod -aG developers username
   ```
3. Atur izin direktori
   ```bash
   sudo chgrp developers /path/to/directory
   sudo chmod 775 /path/to/directory
   ```
4. Verifikasi konfigurasi

## 📝 Tugas
1. Buat laporan yang berisi:
   - Perbandingan metode MFA
   - Diagram arsitektur RBAC
   - Dokumentasi praktikum
   - Analisis keamanan implementasi

## 📊 Penilaian
| Komponen | Bobot |
|----------|-------|
| Partisipasi | 20% |
| Praktikum | 40% |
| Tugas | 30% |
| Kuis | 10% |

## 📚 Referensi
1. NIST SP 800-63B: Digital Identity Guidelines
2. OWASP Authentication Cheat Sheet
3. Google Authenticator Documentation

## ⚠️ Catatan
- Selalu uji konfigurasi sebelum diterapkan di produksi
- Backup konfigurasi sebelum perubahan
- Dokumentasikan setiap perubahan yang dilakukan

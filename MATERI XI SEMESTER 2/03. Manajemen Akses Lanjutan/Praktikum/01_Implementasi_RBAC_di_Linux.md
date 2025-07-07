# 🛠️ Panduan Praktikum: Implementasi RBAC di Linux

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Mengkonfigurasi RBAC di Linux
2. Mengelola user dan group
3. Menerapkan permission yang tepat
4. Memantau aktivitas akses

## 🖥️ Spesifikasi Sistem
- OS: Ubuntu Server 20.04 LTS
- User: Memiliki hak akses root
- Tools: 
  - `useradd`, `usermod`, `groupadd`
  - `sudo`
  - `auditd`
  - `getfacl`/`setfacl`

## 📋 Langkah Kerja

### A. Persiapan Sistem

#### 1. Update Sistem
```bash
sudo apt update
sudo apt upgrade -y
```

#### 2. Install Paket yang Diperlukan
```bash
sudo apt install -y acl auditd
```

### B. Implementasi RBAC Dasar

#### 1. Membuat Struktur Direktori
```bash
# Direktori untuk departemen
sudo mkdir -p /corp/{finance,hr,it,marketing}

# Direktori untuk role
sudo mkdir -p /corp/finance/{reports,invoices}
sudo mkdir -p /corp/hr/{payroll,recruitment}

# Set kepemilikan
sudo chown -R root:finance /corp/finance
sudo chown -R root:hr /corp/hr
```

#### 2. Membuat Group dan User
```bash
# Buat group
sudo groupadd finance
sudo groupadd hr
sudo groupadd fin_manager
sudo groupadd hr_manager

# Buat user
sudo useradd -m -s /bin/bash alice
sudo useradd -m -s /bin/bash bob
sudo useradd -m -s /bin/bash charlie

# Tambahkan user ke group
sudo usermod -aG finance alice
sudo usermod -aG hr bob
sudo usermod -aG fin_manager charlie
```

#### 3. Mengatur Permission dengan ACL
```bash
# Set default ACL untuk direktori finance
sudo setfacl -Rdm g:finance:rx /corp/finance
sudo setfacl -Rm g:finance:rx /corp/finance

# Berikan akses write ke manager
sudo setfacl -Rm g:fin_manager:rwx /corp/finance/reports

# Verifikasi ACL
getfacl /corp/finance/reports
```

### C. Menggunakan sudo untuk Delegasi Tugas

#### 1. Konfigurasi sudo
```bash
# Backup konfigurasi sudo
sudo cp /etc/sudoers /etc/sudoers.bak

# Edit sudoers
sudo visudo
```

#### 2. Tambahkan aturan RBAC
```
# User biasa bisa menjalankan perintah dasar
%users ALL=(ALL) /usr/bin/apt update, /usr/bin/apt list --upgradable

# Finance team bisa menjalankan laporan keuangan
%finance ALL=(ALL) /usr/bin/systemctl status finance-report

# HR bisa mengelola user
%hr ALL=(root) /usr/sbin/adduser, /usr/sbin/deluser, /usr/sbin/usermod

# Manager bisa restart layanan
%manager ALL=(root) /usr/bin/systemctl restart *
```

### D. Audit dan Monitoring

#### 1. Menggunakan auditd
```bash
# Install auditd jika belum ada
sudo apt install -y auditd

# Tambahkan aturan audit
sudo nano /etc/audit/rules.d/access.rules
```

#### 2. Contoh Aturan Audit
```
# Audit akses file penting
-w /etc/passwd -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/sudoers -p wa -k sudoers

# Audit perubahan permission
-a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=4294967295 -k perm_mod
-a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=4294967295 -k perm_mod
```

#### 3. Restart auditd
```bash
sudo systemctl restart auditd
sudo systemctl enable auditd
```

### E. Praktik Terkendali

#### Latihan 1: Implementasi RBAC
1. Buat struktur direktori untuk departemen IT:
   - `/corp/it/{scripts,backup,logs}`
2. Buat group dan user:
   - Group: `it_staff`, `it_manager`
   - User: `dave` (staff), `eve` (manager)
3. Atur permission:
   - Staff bisa baca semua direktori
   - Hanya manager yang bisa menulis di `scripts`
   - Backup hanya bisa diakses oleh sistem backup

#### Latihan 2: Monitoring
1. Buat aturan audit untuk:
   - Semua akses ke `/etc/shadow`
   - Eksekusi perintah dengan sudo
   - Perubahan grup
2. Analisis log dengan:
   ```bash
   sudo ausearch -k perm_mod | aureport -f -i
   ```

## 📝 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum

2. **Tujuan Praktikum**
   - Tuliskan tujuan praktikum

3. **Alat dan Bahan**
   - Spesifikasi perangkat
   - Software yang digunakan

4. **Langkah Kerja**
   - Dokumentasikan setiap langkah
   - Sertakan screenshot
   - Tuliskan perintah yang digunakan

5. **Hasil dan Pembahasan**
   - Tampilkan hasil perintah
   - Analisis hasil
   - Jawab pertanyaan:
     - Bagaimana cara memastikan prinsip least privilege?
     - Apa keuntungan menggunakan ACL dibanding permission standar?

6. **Kesimpulan**
   - Ringkasan hasil
   - Kendala yang dihadapi
   - Saran perbaikan

## 🧩 Tantangan Lanjutan
1. Implementasikan time-based access control:
   - User hanya bisa login pada jam kerja (08.00-17.00)
   - Akses ke aplikasi tertentu hanya pada waktu tertentu

2. Buat skrip otomatisasi untuk:
   - Membuat user baru dengan role tertentu
   - Memonitor perubahan permission
   - Generate laporan aktivitas user

## ⚠️ Troubleshooting

### Masalah: Permission Denied
```
bash: /corp/finance/reports: Permission denied
```
**Solusi:**
1. Periksa membership group:
   ```bash
   groups username
   ```
2. Verifikasi ACL:
   ```bash
   getfacl /corp/finance/reports
   ```
3. Pastikan user login ulang setelah perubahan group

### Masalah: Audit Log Tidak Muncul
**Solusi:**
1. Periksa status auditd:
   ```bash
   sudo systemctl status auditd
   ```
2. Cek aturan yang aktif:
   ```bash
   sudo auditctl -l
   ```
3. Lihat log audit:
   ```bash
   sudo ausearch -m ALL | aureport -i
   ```

## 📚 Referensi
1. [Linux man pages](https://man7.org/linux/man-pages/)
2. [Red Hat RBAC Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_identity_management/configuring-role-based-access-control_configuring-and-managing-idm)
3. [Linux Audit Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/auditing-the-system_security-hardening)

---
<div align="center">
  <p>Panduan Praktikum RBAC Linux - SMKN 1 Punggelan</p>
  <p>© 2025 Tim Pengajar Keamanan Jaringan</p>
</div>

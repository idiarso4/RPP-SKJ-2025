# 🛠️ Praktikum: Hardening Sistem Operasi

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Melakukan hardening pada sistem operasi Linux dan Windows
2. Mengkonfigurasi firewall dan kebijakan keamanan
3. Menerapkan manajemen pengguna dan izin yang aman
4. Mengamankan layanan jaringan
5. Menerapkan monitoring dan logging keamanan

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- Virtual Machine dengan Linux (disarankan Ubuntu Server 22.04 LTS)
- Virtual Machine dengan Windows 10/11
- VirtualBox/VMware Workstation
- Koneksi internet
- Akses administrator/root

### 2. Perangkat Lunak yang Diperlukan
- SSH Client (PuTTY, OpenSSH)
- WinSCP (untuk transfer file ke Linux)
- Notepad++ (untuk mengedit konfigurasi)
- Wireshark (untuk analisis jaringan)

## 📝 Langkah Kerja

### 1. Hardening Dasar Linux

#### 1.1 Update Sistem
```bash
# Update daftar paket
sudo apt update

# Upgrade paket yang ada
sudo apt upgrade -y

# Hapus paket yang tidak diperlukan
sudo apt autoremove -y
```

#### 1.2 Konfigurasi Firewall (UFW)
```bash
# Install UFW jika belum terinstall
sudo apt install ufw -y

# Setel kebijakan default
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Izinkan layanan yang diperlukan
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# Aktifkan firewall
sudo ufw enable

# Periksa status
sudo ufw status verbose
```

#### 1.3 Mengamankan SSH
```bash
# Backup konfigurasi SSH
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Edit konfigurasi SSH
sudo nano /etc/ssh/sshd_config
```

Ubah konfigurasi berikut:
```ini
Port 2222                            # Ubah port default
PermitRootLogin no                   # Nonaktifkan login root
PasswordAuthentication no            # Hanya mengizinkan kunci SSH
X11Forwarding no                     # Nonaktifkan X11 forwarding
MaxAuthTries 3                       # Batas percobaan login
ClientAliveInterval 300              # Batas waktu tidak aktif
ClientAliveCountMax 2                # Maksimum pesan keepalive
AllowUsers siswa1 siswa2             # Hanya izinkan pengguna tertentu
```

Restart layanan SSH:
```bash
sudo systemctl restart sshd
```

### 2. Hardening Dasar Windows

#### 2.1 Konfigurasi Kebijakan Grup
1. Buka **Local Group Policy Editor** (gpedit.msc)
2. Navigasi ke: `Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options`
3. Konfigurasi pengaturan berikut:
   - `Accounts: Limit local account use of blank passwords to console logon only` → **Enabled**
   - `Interactive logon: Do not display last username` → **Enabled**
   - `Microsoft network client: Digitally sign communications (always)` → **Enabled**
   - `Network access: Do not allow anonymous enumeration of SAM accounts` → **Enabled**
   - `Shutdown: Allow system to be shut down without having to log on` → **Disabled**

#### 2.2 Mengaktifkan Windows Defender
```powershell
# Pastikan real-time protection aktif
Set-MpPreference -DisableRealtimeMonitoring $false

# Aktifkan cloud-delivered protection
Set-MpPreference -MAPSReporting Advanced

# Aktifkan sampel pengiriman otomatis
Set-MpPreference -SubmitSamplesConsent SendAllSamples

# Perbarui definisi virus
Update-MpSignature
```

### 3. Manajemen Pengguna dan Izin

#### 3.1 Linux: Membuat Pengguna dan Grup
```bash
# Buat grup baru
sudo groupadd developer
sudo groupadd auditor

# Buat pengguna baru
sudo useradd -m -s /bin/bash alice
sudo useradd -m -s /bin/bash bob

# Setel password
sudo passwd alice
sudo passwd bob

# Tambahkan ke grup
sudo usermod -aG developer alice
sudo usermod -aG auditor bob

# Buat direktori bersama
sudo mkdir -p /srv/shared/{dev,docs}
sudo chown -R root:developer /srv/shared/dev
sudo chown -R root:auditor /srv/shared/docs
sudo chmod 770 /srv/shared/dev
sudo chmod 750 /srv/shared/docs
```

#### 3.2 Windows: Mengelola Izin NTFS
```powershell
# Buat direktori
New-Item -Path "C:\Shared" -ItemType Directory
New-Item -Path "C:\Shared\Dev" -ItemType Directory
New-Item -Path "C:\Shared\Finance" -ItemType Directory

# Atur kepemilikan
takeown /F C:\Shared\Dev /R /D Y
icacls "C:\Shared\Dev" /grant "Developers:(OI)(CI)F" /T
icacls "C:\Shared\Finance" /grant "Finance:(OI)(CI)F" /T

# Hapus akses Everyone
icacls "C:\Shared\*" /remove "Everyone" /T
```

### 4. Keamanan Layanan

#### 4.1 Linux: Nonaktifkan Layanan yang Tidak Diperlukan
```bash
# Daftar layanan yang berjalan
systemctl list-units --type=service --state=running

# Nonaktifkan layanan yang tidak diperlukan
sudo systemctl stop cups
sudo systemctl disable cups

# Nonaktifkan IPv6 jika tidak digunakan
sudo nano /etc/sysctl.conf
```

Tambahkan baris berikut:
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

Terapkan perubahan:
```bash
sudo sysctl -p
```

### 5. Monitoring dan Logging

#### 5.1 Linux: Konfigurasi auditd
```bash
# Install auditd
sudo apt install auditd -y

# Konfigurasi aturan audit
sudo nano /etc/audit/rules.d/audit.rules
```

Tambahkan aturan berikut:
```
# Monitor perubahan file penting
-w /etc/passwd -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k identity

# Monitor akses ke file log
-w /var/log/audit/ -p wa -k auditlog
-w /var/log/auth.log -p wa -k authlog

# Monitor eksekusi biner penting
-a always,exit -F path=/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged
```

Restart auditd:
```bash
sudo systemctl restart auditd
```

#### 5.2 Windows: Konfigurasi Event Forwarding
1. Buka **Event Viewer** (eventvwr.msc)
2. Navigasi ke: `Applications and Services Logs > Microsoft > Windows > EventForwarding-Plugin`
3. Klik kanan dan pilih **Enable Log**
4. Konfigurasi subscription:
   ```powershell
   # Buat subscription baru
   $subscription = @{
       Name = 'SecurityEvents'
       DestinationLog = 'ForwardedEvents'
       SubscriptionType = 'SourceInitiated'
       Query = @'
       <QueryList>
         <Query Id="0">
           <Select Path="Security">*[System[(Level=1 or Level=2 or Level=3)]]</Select>
         </Query>
       </QueryList>
'@
   }
   New-WinEvent -ProviderName Microsoft-Windows-EventCollector -Id 104 -Payload $subscription
   ```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum hardening sistem operasi.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Hardening Linux
```
# Tempelkan output perintah:
# - sudo ufw status verbose
# - sudo sshd -T | grep -i permitrootlogin
# - sudo auditctl -l
```

#### 4.2 Hardening Windows
```
# Tempelkan screenshot:
# - Hasil Get-MpComputerStatus
# - Hasil Get-NetFirewallProfile
# - Hasil Get-LocalUser
```

### 5. Analisis
1. Apa saja potensi kerentanan yang berhasil diatasi dengan konfigurasi di atas?
2. Bagaimana cara memastikan konfigurasi keamanan tetap terjaga setelah pembaruan sistem?
3. Apa yang harus dilakukan jika terjadi insiden keamanan pada sistem yang sudah di-hardening?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Implementasikan SELinux/AppArmor untuk kontrol akses wajib
2. Buat skrip otomatisasi untuk memeriksa kepatuhan keamanan (compliance checking)
3. Terapkan konfigurasi Windows Defender Advanced Threat Protection (ATP)

## ⚠️ Keamanan dan Etika
1. Selalu backup konfigurasi sebelum melakukan perubahan
2. Uji konfigurasi di lingkungan terisolasi sebelum diterapkan ke produksi
3. Dokumentasikan semua perubahan yang dilakukan
4. Patuhi kebijakan keamanan organisasi

## 📚 Referensi
1. CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
2. NIST SP 800-123: Guide to General Server Security
3. Microsoft Security Baselines: https://techcommunity.microsoft.com/t5/microsoft-security-baselines/bg-p/Microsoft-Security-Baselines
4. Linux Hardening Guide: https://github.com/trimstray/the-practical-linux-hardening-guide

---
<div align="center">
  <p>Lembar Kerja Praktikum - Hardening Sistem Operasi</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

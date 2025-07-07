# 🛠️ Panduan Praktikum: Instalasi dan Konfigurasi FreeRADIUS

## 🎯 Tujuan Praktikum
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menginstal FreeRADIUS di Linux
2. Mengkonfigurasi user dan client
3. Menguji konfigurasi
4. Mengintegrasikan dengan database

## 🖥️ Spesifikasi Sistem
- OS: Ubuntu Server 20.04 LTS
- RAM: Minimal 1GB
- Storage: Minimal 10GB
- Koneksi Internet: Diperlukan

## 📥 Langkah 1: Instalasi FreeRADIUS

### Untuk Ubuntu/Debian:
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install paket yang diperlukan
sudo apt install -y freeradius freeradius-mysql freeradius-utils

# Verifikasi instalasi
sudo systemctl status freeradius
```

### Untuk CentOS/RHEL:
```bash
sudo yum install -y freeradius freeradius-utils freeradius-mysql
sudo systemctl enable radiusd
sudo systemctl start radiusd
```

## ⚙️ Langkah 2: Konfigurasi Dasar

### 1. Konfigurasi Client
Edit file `/etc/freeradius/3.0/clients.conf`:
```bash
# Backup konfigurasi asli
sudo cp /etc/freeradius/3.0/clients.conf{,.bak}

# Edit file konfigurasi
sudo nano /etc/freeradius/3.0/clients.conf
```

Tambahkan konfigurasi client:
```
client localhost {
    ipaddr = 127.0.0.1
    secret = testing123
    require_message_authenticator = no
    nastype = other
}

client jaringan-lokal {
    ipaddr = 192.168.1.0/24
    secret = rahasia_client
    nastype = other
}
```

### 2. Menambahkan User
Edit file `/etc/freeradius/3.0/users`:
```bash
# Backup file users
sudo cp /etc/freeradius/3.0/users{,.bak}

# Tambahkan user
sudo nano /etc/freeradius/3.0/users
```

Contoh konfigurasi user:
```
# User dengan password biasa
alice Cleartext-Password := "password123"
    Service-Type = Framed-User,
    Framed-Protocol = PPP,
    Framed-IP-Address = 192.168.1.100,
    Reply-Message = "Selamat datang %{User-Name}"

# User dengan akses terbatas
bob Cleartext-Password := "rahasia456"
    Service-Type = Framed-User,
    Framed-Protocol = PPP,
    Framed-IP-Address = 192.168.1.101,
    Session-Timeout = 3600
```

## 🧪 Langkah 3: Testing

### 1. Jalankan FreeRADIUS dalam Mode Debug
```bash
sudo systemctl stop freeradius
sudo freeradius -X
```

### 2. Test Autentikasi
Buka terminal baru dan jalankan:
```bash
radtest alice password123 localhost 0 testing123
```

Output yang diharapkan:
```
Sending Access-Request of id 123 to 127.0.0.1 port 1812
    User-Name = "alice"
    User-Password = "password123"
    NAS-IP-Address = 127.0.1.1
    NAS-Port = 0
    Message-Authenticator = 0x00
rad_recv: Access-Accept packet from host 127.0.0.1 port 1812, id=123, length=32
```

## 🔄 Langkah 4: Integrasi dengan Database MySQL

### 1. Install MySQL Server
```bash
sudo apt install -y mysql-server
sudo mysql_secure_installation
```

### 2. Buat Database dan User
```bash
sudo mysql -u root -p
```

Di dalam MySQL:
```sql
CREATE DATABASE radius;
GRANT ALL ON radius.* TO 'radius'@'localhost' IDENTIFIED BY 'password_rahasia';
FLUSH PRIVILEGES;
EXIT;
```

### 3. Import Skema Database
```bash
sudo mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql
```

### 4. Konfigurasi SQL Module
Edit file `/etc/freeradius/3.0/mods-available/sql`:
```sql
sql {
    driver = "rlm_sql_mysql"
    dialect = "mysql"
    
    # Koneksi database
    server = "localhost"
    port = 3306
    login = "radius"
    password = "password_rahasia"
    
    # Nama database
    radius_db = "radius"
}
```

### 5. Aktifkan Modul SQL
```bash
sudo ln -s /etc/freeradius/3.0/mods-available/sql /etc/freeradius/3.0/mods-enabled/
sudo systemctl restart freeradius
```

## 📋 Laporan Praktikum

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

5. **Hasil dan Pembahasan**
   - Hasil testing
   - Analisis hasil
   - Kendala yang dihadapi

6. **Kesimpulan**
   - Ringkasan hasil
   - Manfaat yang diperoleh
   - Saran perbaikan

## 🧩 Latihan Tambahan
1. Buat 5 user dengan level akses berbeda
2. Konfigurasi NAS (Network Access Server) untuk terhubung ke RADIUS
3. Buat laporan monitoring aktivitas user

## ⚠️ Troubleshooting

### Masalah: Koneksi Ditolak
```
rad_recv: Access-Reject packet from host 127.0.0.1 port 1812, id=123, length=20
```
**Solusi:**
- Periksa username/password
- Pastikan client terdaftar di `clients.conf`
- Cek log di `/var/log/freeradius/radius.log`

### Masalah: Tidak Bisa Konek ke Database
**Solusi:**
- Pastikan service MySQL berjalan
- Periksa kredensial database
- Verifikasi izin user database

## 📚 Referensi
1. [FreeRADIUS Documentation](https://wiki.freeradius.org/)
2. [Network RADIUS Authentication](https://networkradius.com/doc/)
3. [Ubuntu Server Guide](https://ubuntu.com/server/docs)

---
<div align="center">
  <p>Panduan Praktikum FreeRADIUS - SMKN 1 Punggelan</p>
  <p>© 2025 Tim Pengajar Keamanan Jaringan</p>
</div>

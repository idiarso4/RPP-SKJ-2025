# 🛡️ Panduan Praktikum: Instalasi dan Konfigurasi Wazuh SIEM

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menginstal Wazuh server dan agent
2. Mengkonfigurasi deteksi dasar
3. Menganalisis alert keamanan
4. Membuat custom rule

## 🖥️ Spesifikasi Sistem

### Server
- OS: Ubuntu Server 22.04 LTS
- CPU: 4 core (minimal)
- RAM: 8GB (minimal)
- Storage: 50GB (minimal)
- IP: 192.168.1.100

### Agent
- OS: Ubuntu 22.04 / Windows 10
- CPU: 2 core
- RAM: 2GB
- Storage: 20GB

## 📥 Langkah 1: Instalasi Wazuh Server

### 1.1 Update Sistem
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl apt-transport-https lsb-release gnupg2
```

### 1.2 Tambahkan Repositori Wazuh
```bash
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && sudo chmod 644 /usr/share/keyrings/wazuh.gpg
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
```

### 1.3 Install Wazuh Server
```bash
sudo apt update
sudo WAZUH_MANAGER="192.168.1.100" apt install wazuh-manager
```

### 1.4 Install Wazuh Dashboard
```bash
curl -s https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/elasticsearch.gpg --import && sudo chmod 644 /usr/share/keyrings/elasticsearch.gpg
echo "deb [signed-by=/usr/share/keyrings/elasticsearch.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list

sudo apt update
sudo apt install -y wazuh-dashboard
```

### 1.5 Konfigurasi Awal
```bash
# Restart service
sudo systemctl daemon-reload
sudo systemctl enable wazuh-manager
sudo systemctl start wazuh-manager
sudo systemctl enable wazuh-dashboard
sudo systemctl start wazuh-dashboard

# Cek status
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-dashboard
```

## 📱 Langkah 2: Instalasi Wazuh Agent

### 2.1 Di Linux
```bash
# Tambahkan repositori (sama seperti server)
# ...

# Install agent
sudo WAZUH_MANAGER="192.168.1.100" WAZUH_AGENT_GROUP="default" apt install wazuh-agent

# Daftarkan agent ke server
sudo /var/ossec/bin/agent-auth -m 192.168.1.100 -A $(hostname)

# Start agent
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

### 2.2 Di Windows
1. Download installer dari: https://packages.wazuh.com/4.x/windows/wazuh-agent-4.3.0-1.msi
2. Jalankan installer
3. Masukkan alamat server: 192.168.1.100
4. Selesaikan instalasi
5. Daftarkan agent (Command Prompt sebagai admin):
   ```
   "C:\Program Files (x86)\ossec-agent\agent-auth.exe" -m 192.168.1.100 -A %COMPUTERNAME%
   ```
6. Restart service Wazuh Agent

## 🔍 Langkah 3: Konfigurasi Dasar

### 3.1 Menambahkan Custom Rule
Edit file `/var/ossec/etc/rules/local_rules.xml`:
```xml
<group name="custom_rules,">
  <!-- Deteksi login SSH gagal -->
  <rule id="100100" level="7">
    <if_sid>5716</if_sid>
    <description>Multiple authentication failures from same source IP</description>
    <group>authentication_failed,pci_dss_10.2.4,</group>
  </rule>
  
  <!-- Deteksi perubahan file kritis -->
  <rule id="100200" level="10">
    <if_sid>1002</if_sid>
    <field name="file">/etc/passwd|/etc/shadow</field>
    <description>Critical system file modified</description>
    <group>system_modified,pci_dss_11.5,</group>
  </rule>
</group>
```

### 3.2 Konfigurasi File Integrity Monitoring
Edit file `/var/ossec/etc/ossec.conf`:
```xml
<syscheck>
  <disabled>no</disabled>
  <directories check_all="yes" report_changes="yes" realtime="yes">/etc,/usr/bin,/usr/sbin</directories>
  <ignore>/etc/mtab</ignore>
  <ignore>/etc/mnttab</ignore>
  <ignore>/etc/hosts.deny</ignore>
  <ignore>/etc/mail/statistics</ignore>
  <ignore>/etc/random-seed</ignore>
  <ignore>/etc/random.seed</ignore>
  <ignore>/etc/adjtime</ignore>
  <ignore>/etc/httpd/logs</ignore>
</syscheck>
```

## 📊 Langkah 4: Monitoring dan Analisis

### 4.1 Mengakses Wazuh Dashboard
1. Buka browser ke: https://192.168.1.100:5601
2. Login dengan kredensial default:
   - Username: admin
   - Password: admin
3. Ganti password saat login pertama kali

### 4.2 Mengecek Status Agent
1. Buka menu Management > Agents
2. Pastikan status agent "Active"
3. Klik pada agent untuk melihat detail

### 4.3 Menganalisis Alert
1. Buka menu Security events
2. Filter berdasarkan level:
   ```
   level >= 7
   ```
3. Klik pada alert untuk detail lengkap

## 🧪 Langkah 5: Simulasi Serangan

### 5.1 Simulasi Login SSH Gagal
```bash
# Dari terminal lain, coba login SSH dengan password salah
for i in {1..5}; do ssh user@localhost; done

# Perhatikan alert yang muncul di dashboard
```

### 5.2 Simulasi Perubahan File Kritis
```bash
# Buat backup dulu
sudo cp /etc/passwd /etc/passwd.backup

# Edit file passwd
sudo nano /etc/passwd  # Tambahkan baris dummy

# Kembalikan file asli
sudo mv /etc/passwd.backup /etc/passwd
```

## 📝 Laporan Praktikum

### Format Laporan
1. **Halaman Judul**
   - Nama Praktikan
   - Kelas
   - Tanggal Praktikum

2. **Tujuan Praktikum**
   - Tuliskan tujuan dari praktikum

3. **Alat dan Bahan**
   - Spesifikasi perangkat
   - Software yang digunakan

4. **Langkah Kerja**
   - Dokumentasikan setiap langkah
   - Sertakan screenshot penting
   - Tuliskan perintah yang digunakan

5. **Hasil dan Pembahasan**
   - Tampilkan screenshot dashboard
   - Analisis alert yang muncul
   - Jawab pertanyaan:
     - Alert apa saja yang muncul saat simulasi serangan?
     - Bagaimana cara membedakan false positive dengan serangan nyata?

6. **Kesimpulan**
   - Ringkasan hasil
   - Kendala yang dihadapi
   - Saran perbaikan

## 🧩 Tantangan Lanjutan
1. Buat custom decoder untuk aplikasi web
2. Konfigurasi alert email untuk level kritis
3. Buat custom dashboard untuk memantau aset kritis

## ⚠️ Troubleshooting

### Masalah: Agent Tidak Terdaftar
**Gejala:** Agent tidak muncul di dashboard
**Solusi:**
1. Periksa koneksi ke server:
   ```bash
   telnet 192.168.1.100 1514
   ```
2. Periksa log agent:
   ```bash
   tail -f /var/ossec/logs/ossec.log
   ```
3. Pastikan port 1514/udp terbuka di firewall

### Masalah: Dashboard Tidak Bisa Diakses
**Solusi:**
1. Periksa status service:
   ```bash
   sudo systemctl status wazuh-dashboard
   ```
2. Periksa log:
   ```bash
   journalctl -u wazuh-dashboard -f
   ```
3. Pastikan port 5601 terbuka

## 📚 Referensi
1. [Dokumentasi Resmi Wazuh](https://documentation.wazuh.com/current/index.html)
2. [Wazuh Rules Documentation](https://documentation.wazuh.com/current/user-manual/ruleset/index.html)
3. [Wazuh GitHub](https://github.com/wazuh/wazuh)

---
<div align="center">
  <p>Panduan Praktikum Wazuh SIEM - SMKN 1 Punggelan</p>
  <p>© 2025 Tim Pengajar Keamanan Jaringan</p>
</div>

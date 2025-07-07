# 🛡️ Deteksi Intrusi & SIEM

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, peserta didik diharapkan mampu:
1. Memahami konsep IDS/IPS dan SIEM
2. Mengimplementasikan sistem deteksi intrusi
3. Menganalisis log keamanan
4. Merespon insiden keamanan

## 📚 Materi Pembelajaran

### 1. Konsep Dasar IDS/IPS
   - Perbedaan IDS dan IPS
   - Signature-based vs Anomaly-based detection
   - Jenis IDS (Network-based, Host-based)
   - Teknik evasi dan pencegahannya

### 2. Arsitektur SIEM
   - Komponen SIEM (Collector, Parser, Correlation Engine, dll)
   - Arsitektur terdistribusi
   - Scalability dan high availability
   - Integrasi dengan sistem lain

### 3. Analisis Log Keamanan
   - Jenis-jenis log (System, Network, Application)
   - Format log (Syslog, CEF, LEEF)
   - Normalisasi log
   - Teknik analisis log

### 4. Respon Insiden
   - Siklus hidup insiden keamanan
   - Klasifikasi insiden
   - Prosedur eskalasi
   - Dokumentasi dan pelaporan

## 🛠️ Praktikum

### Praktikum 1: Instalasi Wazuh SIEM
**Tujuan**: Menginstall dan mengkonfigurasi Wazuh SIEM

**Langkah Kerja**:
1. Update sistem dan install dependensi
   ```bash
   sudo apt update
   sudo apt install -y curl apt-transport-https lsb-release
   ```
2. Tambahkan repository Wazuh
   ```bash
   curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo apt-key add -
   echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh-agent.list
   ```
3. Install Wazuh server
   ```bash
   sudo apt update
   sudo apt install wazuh-manager
   ```
4. Install Filebeat
   ```bash
   sudo apt install filebeat
   ```
5. Konfigurasi dan start service
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable wazuh-manager
   sudo systemctl start wazuh-manager
   ```

### Praktikum 2: Monitoring Keamanan Dasar
1. Akses Wazuh web interface
2. Tambahkan agen pada sistem yang akan dimonitor
3. Konfigurasi aturan deteksi
4. Buat dashboard untuk monitoring
5. Uji dengan melakukan scanning dari host lain

## 📝 Tugas
1. Buat laporan yang berisi:
   - Arsitektur implementasi SIEM
   - Analisis log keamanan
   - Deteksi anomali
   - Rekomendasi peningkatan keamanan

## 📊 Penilaian
| Komponen | Bobot |
|----------|-------|
| Partisipasi | 20% |
| Praktikum | 40% |
| Tugas | 30% |
| Kuis | 10% |

## 📚 Referensi
1. Wazuh Documentation
2. NIST SP 800-94: Guide to Intrusion Detection and Prevention Systems
3. MITRE ATT&CK Framework

## ⚠️ Catatan
- Pastikan sistem memiliki sumber daya yang memadai
- Backup konfigurasi sebelum perubahan
- Patuhi kebijakan keamanan organisasi
- Dokumentasikan setiap insiden dan responnya

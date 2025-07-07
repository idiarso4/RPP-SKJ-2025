# Modul 4: Keamanan Cloud

## Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Konsep Dasar Komputasi Awan](#konsep-dasar)
3. [Model Layanan dan Penyebaran Cloud](#model-layanan)
4. [Arsitektur Keamanan Cloud](#arsitektur-keamanan)
5. [Tantangan dan Ancaman Keamanan Cloud](#tantangan-dan-ancaman)
6. [Prinsip Keamanan Cloud](#prinsip-keamanan)
7. [Manajemen Identitas dan Akses (IAM)](#iam)
8. [Enkripsi Data di Cloud](#enkripsi-data)
9. [Kepatuhan dan Regulasi](#kepatuhan-dan-regulasi)
10. [Studi Kasus](#studi-kasus)
11. [Best Practices](#best-practices)
12. [Latihan dan Tugas](#latihan-dan-tugas)
13. [Referensi](#referensi)

## 1. Pendahuluan
Komputasi awan (cloud computing) telah mengubah cara organisasi mengelola infrastruktur TI. Modul ini membahas konsep, tantangan, dan praktik terbaik dalam mengamankan lingkungan cloud, dengan fokus pada model layanan IaaS, PaaS, dan SaaS.

## 2. Konsep Dasar Komputasi Awan
### 2.1 Karakteristik Utama
- Layanan mandiri sesuai permintaan (On-demand self-service)
- Akses jaringan yang luas (Broad network access)
- Penggabungan sumber daya (Resource pooling)
- Elastisitas cepat (Rapid elasticity)
- Layanan terukur (Measured service)

### 2.2 Manfaat Cloud Computing
- Skalabilitas yang fleksibel
- Pengurangan biaya modal (CapEx)
- Akses dari mana saja
- Pemeliharaan yang lebih mudah

## 3. Model Layanan dan Penyebaran Cloud
### 3.1 Model Layanan
- **Infrastructure as a Service (IaaS)**
  - Contoh: AWS EC2, Google Compute Engine
  - Tanggung jawab keamanan: Jaringan, Host, Aplikasi, Data

- **Platform as a Service (PaaS)**
  - Contoh: Google App Engine, Heroku
  - Tanggung jawab keamanan: Aplikasi, Data

- **Software as a Service (SaaS)**
  - Contoh: Google Workspace, Microsoft 365
  - Tanggung jawab keamanan: Data, Akses

### 3.2 Model Penyebaran
- **Public Cloud**
  - Dibagikan oleh banyak organisasi
  - Contoh: AWS, Azure, GCP

- **Private Cloud**
  - Digunakan secara eksklusif oleh satu organisasi
  - Kontrol keamanan penuh

- **Hybrid Cloud**
  - Gabungan public dan private cloud
  - Fleksibilitas dan kontrol yang lebih baik

- **Multi-Cloud**
  - Menggunakan beberapa penyedia cloud
  - Menghindari vendor lock-in

## 4. Arsitektur Keamanan Cloud
### 4.1 Shared Responsibility Model
- Tanggung jawab penyedia cloud vs. pelanggan
- Perbedaan tanggung jawab berdasarkan model layanan

### 4.2 Komponen Keamanan
- Keamanan fisik (Data center)
- Keamanan jaringan (VPC, Security Groups)
- Keamanan host (Hardening, Patch Management)
- Keamanan aplikasi (WAF, API Security)
- Keamanan data (Enkripsi, DLP)

## 5. Tantangan dan Ancaman Keamanan Cloud
### 5.1 Ancaman Umum
- Salah konfigurasi (Misconfiguration)
- Pelanggaran data (Data breaches)
- Kerentanan antarmuka API
- Akun yang dikompromikan
- Serangan DDoS

### 5.2 Tantangan Khusus
- Visibilitas dan kontrol yang terbatas
- Kepatuhan terhadap regulasi
- Manajemen identitas yang kompleks
- Keamanan data lintas yurisdiksi

## 6. Prinsip Keamanan Cloud
### 6.1 Zero Trust Architecture
- Never trust, always verify
- Least privilege access
- Micro-segmentation

### 6.2 Defense in Depth
- Multiple layers of security controls
- Deteksi dan respons ancaman
- Pemantauan dan logging yang komprehensif

## 7. Manajemen Identitas dan Akses (IAM)
### 7.1 Konsep Dasar IAM
- Autentikasi dan otorisasi
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)

### 7.2 Praktik Terbaik IAM
- Prinsip least privilege
- Rotasi kredensial secara berkala
- Audit akses secara teratur

## 8. Enkripsi Data di Cloud
### 8.1 Jenis Enkripsi
- Data in-transit (TLS/SSL)
- Data at-rest (AES-256)
- Data in-use (Homomorphic encryption)

### 8.2 Manajemen Kunci
- Customer Managed Keys (CMK)
- Bring Your Own Key (BYOK)
- Hardware Security Module (HSM)

## 9. Kepatuhan dan Regulasi
### 9.1 Standar Internasional
- ISO/IEC 27017:2015 - Cloud security
- ISO/IEC 27018:2019 - Protection of PII in cloud
- CSA STAR Certification

### 9.2 Regulasi Indonesia
- Peraturan Menteri Kominfo No. 5 Tahun 2020 tentang Penyelenggara Sistem Elektronik
- Peraturan BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi
- UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi

## 10. Studi Kasus
### 10.1 Kebocoran Data Perusahaan Fintech (2024)
- **Gambaran**: Konfigurasi bucket S3 yang salah
- **Dampak**: 10 juta data pengguna terekspos
- **Penyebab**: IAM yang tidak tepat dan enkripsi yang tidak diaktifkan
- **Solusi**: Penerapan kebijakan bucket yang ketat dan enkripsi default

### 10.2 Serangan Ransomware pada Penyedia Layanan Kesehatan (2023)
- **Gambaran**: Ransomware menginfeksi sistem cloud
- **Dampak**: Gangguan layanan selama 3 hari
- **Penyebab**: Kurangnya segmentasi jaringan dan backup
- **Solusi**: Penerapan Zero Trust dan strategi backup 3-2-1

## 11. Best Practices
### 11.1 Pra-Implementasi
- Lakukan penilaian risiko
- Pilih penyedia cloud yang sesuai
- Pahami model tanggung jawab bersama

### 11.2 Implementasi
- Terapkan prinsip least privilege
- Enkripsi data sensitif
- Aktifkan logging dan monitoring

### 11.3 Operasional
- Lakukan audit keamanan berkala
- Update dan patch sistem secara teratur
- Latih staf tentang keamanan cloud

## 12. Latihan dan Tugas
### Latihan Individu
1. Analisis konfigurasi keamanan akun cloud gratis (AWS Free Tier/GCP Free Tier)
2. Terapkan kebijakan IAM yang aman
3. Konfigurasi enkripsi untuk penyimpanan cloud

### Tugas Kelompok
1. Rancang arsitektur keamanan cloud untuk startup fintech
2. Analisis kasus pelanggaran data cloud dan presentasikan temuan
3. Buat panduan keamanan cloud untuk organisasi

## 13. Referensi
### Buku Teks
1. "Cloud Security For Dummies" by Ted Coombs
2. "Cloud Security and Privacy" by Tim Mather et al.
3. "Architecting Cloud Computing Solutions" by Kevin L. Jackson and Scott Goessling

### Standar dan Kerangka Kerja
1. **CSA Security Guidance** - Cloud Security Alliance
2. **NIST SP 800-210** - General Access Control Guidance for Cloud Systems
3. **ISO/IEC 27017** - Code of practice for information security controls for cloud services

### Sumber Online
1. **Cloud Security Alliance**: https://cloudsecurityalliance.org/
2. **NIST Cloud Computing Program**: https://www.nist.gov/programs-projects/nist-cloud-computing-program-nccp
3. **CIS Benchmarks for Cloud**: https://www.cisecurity.org/cis-benchmarks/

### Regulasi Indonesia
1. Peraturan Menteri Kominfo No. 5 Tahun 2020 tentang Penyelenggara Sistem Elektronik
2. Peraturan BSSN No. 8 Tahun 2022 tentang Pedoman Teknis Keamanan Informasi
3. Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi

**Catatan Versi**:
- Versi Dokumen: 1.0
- Terakhir Diperbarui: 8 Juli 2025
- Penulis: Tim Pengembang Kurikulum Keamanan Jaringan

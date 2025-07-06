

1.  **Pengalaman & Lingkungan Kerja (Kelas XI):** Kita akan memulai dari nol, membangun pengalaman dari dasar dengan menyiapkan "bengkel kerja" virtual terlebih dahulu.
2.  **Alokasi Khusus Virtualisasi:** Kebutuhan VM/Container akan dijadikan satu elemen pembelajaran tersendiri di awal.
3.  **Integrasi Bahasa Python:** Alokasi khusus untuk Python akan kita masukkan pada momen yang paling strategis, yaitu saat siswa sudah memiliki fondasi jaringan dan pertahanan yang kuat, untuk digunakan sebagai alat bantu analisis dan otomatisasi.

Berikut adalah susunan ulang ATP selama 4 semester yang telah disempurnakan berdasarkan masukan Anda.

---

### **ATP (Alur Tujuan Pembelajaran) yang Disempurnakan (4 Semester)**

#### **KELAS XI, SEMESTER 1: Persiapan Lingkungan & Fondasi Pertahanan Jaringan**
*(16 Pertemuan @ 3 JP = 135 Menit/Pertemuan)*

Fokus: Membangun "pengalaman" dari awal. Siswa tidak langsung diberi teori, tetapi membangun lingkungan kerjanya sendiri, lalu mempelajari konsep dasar dan praktik pertahanan pertama.

| Elemen / Modul Pembelajaran | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- |
| **1. Persiapan Lingkungan Kerja Virtual (BARU)** | **Konsep Virtualisasi (VM & Container)**, instalasi dan konfigurasi Hypervisor (VirtualBox/VMware), manajemen *snapshot*, dan **konfigurasi jaringan virtual (NAT, Bridged, Host-only)**. | **Instalasi VirtualBox**, membuat beberapa VM (Linux & Mikrotik RouterOS), dan mengatur topologi jaringan lab virtual. |
| **2. Pengenalan Keamanan & Etika Profesi** | Konsep dasar keamanan, sejarah & tantangan digital, regulasi, etika profesi (*responsible disclosure*). | Analisis studi kasus insiden siber, diskusi dilema etika, penggunaan lab virtual yang sudah dibuat. |
| **3. Prinsip Fundamental Keamanan** | CIA Triad, Defense in Depth, Least Privilege. | Merancang arsitektur keamanan sederhana untuk topologi lab virtual yang ada. |
| **4. Analisis Ancaman & Kerentanan** | Klasifikasi ancaman (Malware, Serangan Jaringan), teknik Social Engineering. | Analisis jenis-jenis malware dan identifikasi potensi serangan pada topologi lab. |
| **5. Praktik Pertahanan Jaringan (Firewall)** | Konfigurasi Firewall, Network Address Translation (NAT), dan dasar *System Hardening*. | **Praktik intensif konfigurasi Firewall Filter & NAT di Mikrotik RouterOS** untuk mengamankan VM dalam lab. |
| **6. Proyek Mini Semester 1** | Mengintegrasikan modul 1-5. | Proyek: "Membangun dan Mengamankan Jaringan Lab Virtual" (Membangun topologi, mengamankan dengan firewall, dan membuat dokumentasi). |

---

#### **KELAS XI, SEMESTER 2: Analisis, Autentikasi, & Deteksi**
*(16 Pertemuan @ 3 JP = 135 Menit/Pertemuan)*

Fokus: Setelah mampu bertahan, siswa belajar menganalisis, mengelola akses pengguna secara terpusat, dan mendeteksi aktivitas mencurigakan secara lebih canggih.

| Elemen / Modul Pembelajaran | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- |
| **1. Praktik Analisis Jaringan** | Konsep Scanning, Analisis Lalu Lintas Jaringan. | **Praktik intensif Nmap** untuk pemindaian & **Wireshark** untuk analisis paket pada lingkungan lab yang sudah ada. |
| **2. Sistem Autentikasi Terpusat** | Konsep AAA, protokol RADIUS, konsep dasar direktori (LDAP). | **Praktik integrasi Mikrotik (Hotspot/PPPoE) sebagai RADIUS Client ke FreeRADIUS Server**. |
| **3. Manajemen Akses Lanjutan** | Konsep Multi-Factor Authentication (MFA), konsep integrasinya via RADIUS. | Simulasi dan analisis alur login dengan MFA. |
| **4. Deteksi Intrusi & Analisis Log (SIEM)** | Konsep IDS/IPS (Snort sebagai contoh teori), **Konsep SIEM dan Log Management**. | **Praktik Implementasi SIEM dengan Wazuh**: Mengirim log dari Mikrotik & VM lain ke Wazuh, lalu menganalisis *dashboard*. |
| **5. Enkripsi & Komunikasi Aman** | Dasar-dasar Kriptografi, Fungsi Hash. | **Praktik VPN Remote Access sederhana (misal: PPTP/L2TP) di Mikrotik** sebagai aplikasi nyata dari komunikasi terenkripsi. |
| **6. Proyek Mini Semester 2** | Mengintegrasikan modul semester 2. | Proyek: "Implementasikan Autentikasi Terpusat dan Monitoring Keamanan pada Jaringan Lab Virtual". |

---

#### **KELAS XII, SEMESTER 1: Otomatisasi & Teknologi Keamanan Terapan**
*(16 Pertemuan @ 4 JP = 180 Menit/Pertemuan)*

Fokus: Memberikan siswa *superpower* baru (Python) untuk otomatisasi, lalu mendalami teknologi keamanan spesifik yang sangat relevan di industri. Waktu per pertemuan lebih panjang untuk mengakomodasi kompleksitas materi.

| Elemen / Modul Pembelajaran | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- |
| **1. Dasar Pemrograman Python untuk Keamanan (BARU)** | Sintaks dasar Python, tipe data, fungsi, dan **penggunaan library relevan (misal: `requests`, `socket`, `os`)**. | Membuat skrip-skrip sederhana untuk otomatisasi tugas jaringan (misal: *port scanner* sederhana, *banner grabbing*). |
| **2. Virtual Private Network (VPN) Lanjutan** | Protokol VPN (IPsec, SSL/TLS), konsep Tunneling. | **Praktik konfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik** untuk menghubungkan dua jaringan virtual. |
| **3. Keamanan Aplikasi Web** | Kerentanan Web (OWASP Top 10), SQL Injection, XSS, Konsep WAF. | Praktik pengujian keamanan pada aplikasi web rentan (DVWA/Juice Shop) menggunakan Burp Suite/ZAP. |
| **4. Keamanan Cloud & Container** | Model Keamanan Cloud, IAM di Cloud, **Konsep & Risiko Keamanan Container (Docker)**. | **Praktik dasar mengamankan Dockerfile dan image container**. |

---

#### **KELAS XII, SEMESTER 2: Ethical Hacking, Manajemen, & Proyek Akhir**
*(16 Pertemuan @ 4 JP = 180 Menit/Pertemuan)*

Fokus: Puncak pembelajaran. Siswa mengaplikasikan semua ilmunya dalam simulasi ofensif yang etis, memahami aspek manajerial, dan menyelesaikan proyek akhir sebagai portofolio.

| Elemen / Modul Pembelajaran | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- |
| **1. Ethical Hacking & Penetration Testing** | Metodologi Penetration Testing (PTES), *Cyber Kill Chain*. | **Praktik utama pada platform gamifikasi: TryHackMe, OverTheWire, VulnHub**. Siswa didorong menggunakan skrip Python yang mereka buat. |
| **2. Manajemen Keamanan & Tata Kelola** | Manajemen Risiko, Standar Kepatuhan, *Incident Response*, *Disaster Recovery Plan (DRP)*. | Praktik simulasi insiden keamanan, **Praktik DRP dengan backup & restore konfigurasi jaringan Mikrotik yang kompleks**. |
| **3. Proyek Akhir (Capstone)** | Mengintegrasikan seluruh pengetahuan dari kelas XI-XII. | **Proyek komprehensif:** *Security assessment* pada topologi jaringan simulasi kompleks, diakhiri dengan laporan profesional dan presentasi. |
| **4. Persiapan Karir & Ujian Kejuruan** | Tinjauan jalur karir, penyusunan portofolio, **persiapan Ujian Kompetensi Kejuruan (termasuk ujian Mikrotik Academy)**. | Penyempurnaan portofolio digital, simulasi UKK. |
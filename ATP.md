# Alur Tujuan Pembelajaran (ATP) - VERSI REVISI 2 (Sesuai CP Kemdikbud)

## Capaian Pembelajaran (CP) Fase F (Sumber: Kemdikbud)

### Capaian Umum
Pada akhir fase F peserta didik akan mampu mengimplementasikan teknologi layanan komputasi awan, keamanan jaringan, dan Internet-of-Things.

### Capaian per Elemen
*   **Service Design**: Memahami, menerapkan, dan mengkomunikasikan desain User Experience (UX) dan Customer Experience (CX).
*   **Infrastructure-as-a-Service**: Menerapkan, mendokumentasikan, dan mengkomunikasikan instalasi serta pengelolaan layanan pada infrastruktur komputasi awan, termasuk sistem operasi jaringan, virtualisasi, dan otomasi.
*   **Platform-as-a-Service**: Menerapkan, mendokumentasikan, mengkomunikasikan, dan memecahkan masalah terkait layanan server seperti Web Server, Database Server, DNS Server, dan Mail Server.
*   **Software-as-a-service**: Menerapkan pemrograman web, RESTful API, pemrograman perangkat bergerak, serta instalasi dan konfigurasi framework big data.
*   **Sistem Keamanan Jaringan**: Menerapkan, mendokumentasikan, mengkomunikasikan, dan memecahkan masalah terkait sistem keamanan jaringan, firewall, VPN, serta menerapkan *ethical hacking*.
*   **Internet-of-Things**: Menerapkan perangkat IoT, pemrograman mikrokontroler, platform IoT, serta manajemen dan visualisasi data.

## Prinsip Penyusunan Revisi

1.  **Kesesuaian dengan CP Fase F:** Alur pembelajaran direvisi untuk secara eksplisit mencakup dan memetakan semua elemen dalam Capaian Pembelajaran (CP) Fase F, termasuk Keamanan Jaringan, Layanan Cloud (IaaS, PaaS, SaaS), Service Design, dan IoT.
2.  **Fondasi Teori Terlebih Dahulu (Kelas XI):** Alur tetap dimulai dengan fondasi konseptual yang kuat sebelum masuk ke aspek teknis.
3.  **Alokasi Khusus Virtualisasi (IaaS):** Kebutuhan VM/Container diposisikan sebagai implementasi dasar *Infrastructure-as-a-Service* (IaaS).
4.  **Integrasi Teknologi Terapan:** Python, Keamanan Aplikasi Web, dan IoT diintegrasikan di Kelas XII saat siswa memiliki fondasi yang kuat.

Berikut adalah susunan ulang ATP selama 4 semester yang telah direvisi dan dipetakan ke CP.

---

### **ATP (Alur Tujuan Pembelajaran) yang Disempurnakan (4 Semester)**

#### **KELAS XI, SEMESTER 1: Fondasi Keamanan, Desain Layanan, & Infrastruktur Dasar**
*(16 Pertemuan @ 3 JP = 135 Menit/Pertemuan)*

**Fokus**: Membangun fondasi konseptual keamanan, memahami desain layanan, dan menyiapkan lingkungan kerja virtual sebagai implementasi IaaS.

| Elemen / Modul Pembelajaran | Keterkaitan dengan Elemen CP | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- | :--- |
| **1. Pengenalan Keamanan, Etika & Desain Layanan (BARU)** | **Service Design**, Sistem Keamanan Jaringan | Konsep dasar keamanan, regulasi, etika profesi, dan **prinsip dasar User Experience (UX) & Customer Experience (CX)**. | Analisis studi kasus insiden siber dan diskusi bagaimana UX/CX yang buruk bisa menjadi celah keamanan. |
| **2. Prinsip Fundamental Keamanan** | Sistem Keamanan Jaringan | CIA Triad, Defense in Depth, Least Privilege. | Merancang arsitektur keamanan sederhana secara konseptual untuk sebuah studi kasus. |
| **3. Analisis Ancaman & Kerentanan** | Sistem Keamanan Jaringan | Klasifikasi ancaman (Malware, Serangan Jaringan), teknik Social Engineering. | Analisis jenis-jenis malware dan identifikasi potensi serangan pada sebuah studi kasus. |
| **4. Persiapan Lingkungan Kerja Virtual (IaaS)** | **Infrastructure-as-a-Service** | **Konsep Virtualisasi (VM & Container)**, instalasi Hypervisor (VirtualBox), manajemen *snapshot*, dan **konfigurasi jaringan virtual**. | **Instalasi VirtualBox**, membuat beberapa VM (Linux & Mikrotik RouterOS), dan mengatur topologi jaringan lab virtual. |
| **5. Praktik Pertahanan Jaringan (Firewall)** | Sistem Keamanan Jaringan | Konfigurasi Firewall, Network Address Translation (NAT), dan dasar *System Hardening*. | **Praktik intensif konfigurasi Firewall Filter & NAT di Mikrotik RouterOS** untuk mengamankan VM dalam lab. |
| **6. Proyek Mini Semester 1** | IaaS, Sistem Keamanan Jaringan | Mengintegrasikan modul 1-5. | Proyek: "Membangun dan Mengamankan Infrastruktur Jaringan Lab Virtual" (Membangun topologi, mengamankan dengan firewall, dokumentasi). |

---

#### **KELAS XI, SEMESTER 2: Analisis, Layanan Platform (PaaS), & Deteksi**
*(16 Pertemuan @ 3 JP = 135 Menit/Pertemuan)*

**Fokus**: Menganalisis, mengelola akses dengan layanan tingkat platform (PaaS), dan mendeteksi aktivitas mencurigakan.

| Elemen / Modul Pembelajaran | Keterkaitan dengan Elemen CP | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- | :--- |
| **1. Praktik Analisis Jaringan** | Sistem Keamanan Jaringan | Konsep Scanning, Analisis Lalu Lintas Jaringan. | **Praktik intensif Nmap** untuk pemindaian & **Wireshark** untuk analisis paket pada lingkungan lab. |
| **2. Sistem Autentikasi Terpusat (PaaS)** | **Platform-as-a-Service** | Konsep AAA, protokol RADIUS. Implementasi **layanan server** untuk autentikasi. | **Praktik integrasi Mikrotik sebagai RADIUS Client ke FreeRADIUS Server (layanan PaaS)**. |
| **3. Manajemen Akses Lanjutan** | Platform-as-a-Service | Konsep Multi-Factor Authentication (MFA), konsep integrasinya via RADIUS. | Simulasi dan analisis alur login dengan MFA pada layanan yang ada. |
| **4. Deteksi Intrusi & Analisis Log (SIEM)** | Sistem Keamanan Jaringan | Konsep IDS/IPS, **Konsep SIEM dan Log Management**. | **Praktik Implementasi SIEM dengan Wazuh**: Mengirim log dari Mikrotik & VM lain ke Wazuh, lalu menganalisis *dashboard*. |
| **5. Enkripsi & Komunikasi Aman** | Sistem Keamanan Jaringan | Dasar-dasar Kriptografi, Fungsi Hash, **Praktik VPN Remote Access** (PPTP/L2TP). | **Praktik VPN di Mikrotik** sebagai aplikasi nyata dari komunikasi terenkripsi. |
| **6. Proyek Mini Semester 2** | PaaS, Sistem Keamanan Jaringan | Mengintegrasikan modul semester 2. | Proyek: "Implementasikan Autentikasi Terpusat (PaaS) dan Monitoring Keamanan pada Jaringan Lab Virtual". |

---

#### **KELAS XII, SEMESTER 1: Otomatisasi (SaaS), IoT, & Keamanan Terapan**
*(16 Pertemuan @ 4 JP = 180 Menit/Pertemuan)*

**Fokus**: Menggunakan skrip sebagai *Software-as-a-Service* (SaaS) internal, menerapkan IoT, dan mendalami teknologi keamanan spesifik.

| Elemen / Modul Pembelajaran | Keterkaitan dengan Elemen CP | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- | :--- |
| **1. Dasar Pemrograman Python untuk Keamanan (SaaS)** | **Software-as-a-Service** | Sintaks dasar Python, fungsi, dan **penggunaan library relevan (`requests`, `socket`)** untuk membuat alat bantu (*tooling*). | Membuat skrip-skrip sederhana (dianggap sebagai SaaS internal) untuk otomatisasi tugas (misal: *port scanner*, *banner grabbing*). |
| **2. Dasar Internet-of-Things (IoT) (BARU)** | **Internet-of-Things** | **Konsep & Arsitektur Keamanan IoT**, identifikasi kerentanan umum pada perangkat IoT, teknik pengamanan (otentikasi, enkripsi, segmentasi jaringan untuk IoT), dan platform IoT (Blynk/Thingspeak) dari perspektif keamanan. | **Praktik mengamankan perangkat IoT sederhana** (misal: monitor suhu) dan mengintegrasikannya secara aman ke dalam jaringan. |
| **3. Virtual Private Network (VPN) Lanjutan** | Sistem Keamanan Jaringan | Protokol VPN (IPsec, SSL/TLS), konsep Tunneling. | **Praktik konfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik**. |
| **4. Keamanan Aplikasi Web** | Software-as-a-Service | Kerentanan Web (OWASP Top 10), SQL Injection, XSS, Konsep WAF. | Praktik pengujian keamanan pada aplikasi web rentan (DVWA/Juice Shop) menggunakan Burp Suite/ZAP. |
| **5. Keamanan Cloud & Container** | IaaS, PaaS | Model Keamanan Cloud, IAM di Cloud, **Konsep & Risiko Keamanan Container (Docker)**. | **Praktik dasar mengamankan Dockerfile dan image container**. |

---

#### **KELAS XII, SEMESTER 2: Ethical Hacking, Manajemen, & Proyek Akhir**
*(16 Pertemuan @ 4 JP = 180 Menit/Pertemuan)*

**Fokus**: Mengaplikasikan semua ilmu dalam simulasi ofensif yang etis, memahami aspek manajerial, dan menyelesaikan proyek akhir.

| Elemen / Modul Pembelajaran | Keterkaitan dengan Elemen CP | Fokus Materi Utama | Praktik Inti |
| :--- | :--- | :--- | :--- |
| **1. Ethical Hacking & Penetration Testing** | Sistem Keamanan Jaringan | Metodologi Penetration Testing (PTES), *Cyber Kill Chain*. | **Praktik utama pada platform gamifikasi: TryHackMe, VulnHub**. Menerapkan semua teknik dari IaaS, PaaS, SaaS, dan IoT. |
| **2. Manajemen Keamanan & Tata Kelola** | Sistem Keamanan Jaringan | Manajemen Risiko, Standar Kepatuhan, *Incident Response*, *Disaster Recovery Plan (DRP)*. | Praktik simulasi insiden, **Praktik DRP dengan backup & restore konfigurasi jaringan & server**. |
| **3. Proyek Akhir (Capstone)** | **Semua Elemen CP** | Mengintegrasikan seluruh pengetahuan dari kelas XI-XII. | **Proyek komprehensif:** *Security assessment* pada topologi simulasi kompleks (termasuk VM, container, dan perangkat IoT). |
| **4. Persiapan Karir & Ujian Kejuruan** | - | Tinjauan jalur karir, penyusunan portofolio, **persiapan Ujian Kompetensi Kejuruan**. | Penyempurnaan portofolio digital, simulasi UKK. |

---

C.	Dimensi Profil Pelajar Pancasila DPL 

Dimensi	Implementasi dalam Pembelajaran
Beriman & Berakhlak Mulia	Berdoa sebelum/sesudah belajar, etika hacking, responsible disclosure, menghargai data pribadi

Berkebinekaan Global	Memahami standar internasional, menghargai perbedaan, mengikuti tren global, bekerja sama dalam tim beragam
Bergotong Royong	Kerja kelompok, kolaborasi, berbagi pengetahuan, saling membantu

Mandiri	Belajar mandiri, troubleshooting, bertanggung jawab, menyelesaikan tugas dengan inisiatif

Bernalar Kritis	Analisis ancaman, evaluasi metode, identifikasi akar masalah, menyimpulkan hasil analisis
Kreatif	Solusi inovatif, strategi keamanan, otomatisasi tugas, membuat dokumentasi menarik

D.	Metode Pembelajaran Utama
E.	

Metode	Deskripsi
Pembelajaran Berbasis Proyek PjBL 	Proyek nyata keamanan jaringan
Pembelajaran Berbasis Masalah PBL 	Studi kasus insiden keamanan
Pembelajaran Inkuiri	Investigasi kerentanan dan ancaman
Pembelajaran Kooperatif	Kerja tim dalam simulasi dan praktik
Pembelajaran Berbasis Pengalaman	Simulasi, CTF, dan hands-on practice

F.	Asesmen

Jenis Asesmen	
Bentuk Penilaian
Formatif	Observasi, diskusi, LKPD, kuis harian, tugas individu/kelompok, laporan praktikum

Sumatif	Ulangan Harian UH , Ujian Tengah Semester UTS , Ujian Akhir Semester UAS , Ujian Praktik Kelompok/Proyek Akhir Capstone Project)


G.	Media, Alat, dan Sumber Belajar

Kategori	Spesifikasi
Media	Presentasi digital, video tutorial, simulasi jaringan, platform e-learning

Alat	Komputer (spesifikasi memadai), perangkat jaringan (router, switch, server), virtualisasi (VirtualBox, VMware, Docker), **Mikrokontroler (ESP32/ESP8266) & Sensor**, Tools (Wireshark, Nmap, Kali Linux, Metasploit, Snort, Burp Suite, OWASP ZAP, FreeRADIUS)

Sumber Belajar	Buku teks Sistem Keamanan Jaringan, dokumentasi resmi Cisco, Microsoft, AWS, MikroTik, FreeRADIUS, OWASP, NIST, SANS , modul praktikum, platform CTF TryHackMe, Hack The Box, OverTheWire Bandit), **Platform IoT (Blynk, Thingspeak)**

Catatan: ATP ini disusun untuk mencapai seluruh Capaian Pembelajaran Fase F (Sistem Informasi, Jaringan, dan Aplikasi) dengan pendekatan praktis dan komprehensif.




Mengetahui 					Punggelan, 7 Juli 2025
Kepala SMK Negeri 1 Punggelan			Guru Mapel



Pontjo Nugroho, S.Pd  					Idiarso, S.Kom 
NIP. 19710810199803 1 008  				NIP. 19830804202221 1 006
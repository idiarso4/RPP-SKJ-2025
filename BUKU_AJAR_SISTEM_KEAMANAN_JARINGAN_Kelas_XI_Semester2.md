# Kata Pengantar

Puji syukur kehadirat Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga dokumen RPP Sistem Keamanan Jaringan Semester 2 ini dapat disusun sebagai panduan pembelajaran komprehensif bagi peserta didik Kelas XI Program Keahlian Sistem Informasi Jaringan dan Aplikasi (SIJA) di SMK, sesuai Kurikulum Merdeka Fase F. RPP ini mengintegrasikan teori, praktik, dan asesmen otentik berbasis kebutuhan industri, serta menanamkan nilai-nilai Profil Pelajar Pancasila. Semoga dokumen ini bermanfaat dan mendukung terwujudnya lulusan yang kompeten, adaptif, dan berkarakter.

# Identitas Modul
- Nama Sekolah: SMKN 1 Punggelan
- Program Keahlian: Sistem Informasi Jaringan dan Aplikasi (SIJA)
- Mata Pelajaran: Sistem Keamanan Jaringan
- Fase/Kelas/Semester: Fase F / XI / Semester 2
- Tahun Pelajaran: 2024/2025
- Penyusun: Idiarso, S.Kom
- Alokasi Waktu: 16 pertemuan (48 jam pelajaran @ 45 menit)

# Panduan Penggunaan RPP

## Untuk Guru
- Setiap pertemuan dirancang untuk 3 JP (135 menit), dengan pembagian waktu antara teori, praktik, diskusi, dan refleksi.
- Gunakan QR Code (jika tersedia) untuk mengakses materi digital tambahan, video tutorial, dan platform online.
- Manfaatkan rubrik penilaian yang disediakan untuk memantau perkembangan peserta didik secara objektif.
- Sesuaikan kecepatan pembelajaran dengan kemampuan siswa, dan berikan pengayaan atau remedial sesuai kebutuhan.

## Untuk Siswa
- Baca tujuan pembelajaran di setiap pertemuan sebelum memulai.
- Ikuti langkah-langkah praktik dengan teliti, dokumentasikan setiap langkah.
- Gunakan LKPD (Lembar Kerja Peserta Didik) untuk mencatat temuan, hasil analisis, dan refleksi pembelajaran.
- Diskusikan dengan teman untuk memperdalam pemahaman dan berbagi pengalaman.
- Manfaatkan sumber referensi tambahan yang disediakan, baik berupa buku, artikel, maupun materi digital.

## Simbol dan Notasi
|Simbol|Keterangan|
|---|---|
|🎯|Tujuan Pembelajaran|
|💡|Tips Pembelajaran|
|⚠️|Perhatian Khusus|
|🔧|Praktik Hands-on|
|📝|Asesmen|
|🌐|Sumber Digital|
|👥|Kerja Kelompok|
|🔍|Discovery Learning|

## Tips Praktikum
- Persiapkan lingkungan virtual sebelum praktik, pastikan semua tools dan software yang dibutuhkan sudah terinstal.
- Backup data sebelum melakukan perubahan konfigurasi.
- Dokumentasikan setiap langkah praktik untuk evaluasi dan portofolio.
- Patuhi etika hacking dan aspek legal dalam pembelajaran.

# RENCANA PELAKSANAAN PEMBELAJARAN {RPP}
No : ..........
Mata Pelajaran	: Sistem Keamanan Jaringan
Fase/Kelas/Semester	: Fase F / XI / Semester 2
Alokasi Waktu	: 16 pertemuan
durasi pertemuan 1 kali pertemuan 3 x 45 menit 

## A. Tujuan Pembelajaran
Setelah mengikuti pembelajaran ini, peserta didik mampu:
1. Memahami konsep scanning dan menganalisis lalu lintas jaringan menggunakan tools.
2. Menjelaskan konsep AAA dan protokol RADIUS, serta mengimplementasikan sistem autentikasi terpusat.
3. Memahami konsep Multi-Factor Authentication (MFA) dan mengintegrasikannya.
4. Menjelaskan konsep IDS/IPS, SIEM, dan Log Management, serta mengimplementasikan SIEM untuk analisis log.
5. Memahami dasar-dasar kriptografi, fungsi hash, dan mengimplementasikan VPN Remote Access.
6. Mengintegrasikan seluruh pengetahuan untuk mengimplementasikan autentikasi terpusat dan monitoring keamanan pada jaringan lab virtual.

## B. Materi Pembelajaran
1. **Praktik Analisis Jaringan**
   - Konsep Scanning (Port Scanning, Vulnerability Scanning)
   - Analisis Lalu Lintas Jaringan (Packet Sniffing)
   - Tools: Nmap, Wireshark

2. **Sistem Autentikasi Terpusat (PaaS)**
   - Konsep AAA (Authentication, Authorization, Accounting)
   - Protokol RADIUS (Remote Authentication Dial-In User Service)
   - Implementasi FreeRADIUS Server
   - Integrasi Mikrotik sebagai RADIUS Client

3. **Manajemen Akses Lanjutan**
   - Konsep Multi-Factor Authentication (MFA)
   - Jenis-jenis MFA (OTP, Biometrik, Hardware Token)
   - Integrasi MFA via RADIUS (konseptual)

4. **Deteksi Intrusi & Analisis Log (SIEM)**
   - Konsep IDS/IPS (Intrusion Detection/Prevention System)
   - Konsep SIEM (Security Information and Event Management)
   - Log Management dan Korelasi Log
   - Implementasi SIEM dengan Wazuh (Agent & Manager)

5. **Enkripsi & Komunikasi Aman**
   - Dasar-dasar Kriptografi (Symmetric, Asymmetric)
   - Fungsi Hash (MD5, SHA)
   - Konsep VPN (Virtual Private Network)
   - Protokol VPN Remote Access (PPTP, L2TP/IPsec)
   - Implementasi VPN di Mikrotik

6. **Proyek Mini Semester 2**
   - Integrasi modul 1-5
   - Implementasi Autentikasi Terpusat (PaaS) dan Monitoring Keamanan pada Jaringan Lab Virtual

## C. Praktik Pedagogis
1. **Pembelajaran Berbasis Proyek (PjBL)**
   - Implementasi proyek keamanan jaringan dasar
   - Pengembangan solusi keamanan berbasis skenario
   - Presentasi dan evaluasi proyek

2. **Pembelajaran Berbasis Masalah (PBL)**
   - Analisis insiden keamanan jaringan
   - Pemecahan masalah keamanan jaringan
   - Diskusi solusi berbasis standar industri

3. **Pembelajaran Inkuiri**
   - Investigasi kerentanan jaringan
   - Eksperimen konfigurasi keamanan
   - Analisis pola serangan

4. **Pembelajaran Kooperatif**
   - Kerja tim dalam simulasi keamanan
   - Peer teaching untuk topik dasar
   - Review kebijakan keamanan berkelompok

5. **Pembelajaran Berbasis Pengalaman**
   - Simulasi insiden keamanan
   - Praktik respon insiden dasar
   - Analisis forensik digital dasar

## D. Kemitraan Pembelajaran
1. **Kolaborasi dengan Industri**
   - Kerjasama dengan CSIRT lokal (jika memungkinkan)
   - Kunjungan ke pusat operasi keamanan (jika memungkinkan)
   - Guest lecture dari analis keamanan (jika memungkinkan)

2. **Kemitraan Lintas Sekolah**
   - Kompetisi keamanan jaringan antar sekolah (jika memungkinkan)
   - Berbagi sumber daya pembelajaran
   - Kolaborasi dalam simulasi keamanan

3. **Keterlibatan Komunitas**
   - Kerjasama dengan komunitas keamanan siber
   - Partisipasi dalam program kesadaran keamanan
   - Kontribusi proyek open source keamanan

4. **Peran Orang Tua**
   - Workshop keamanan digital keluarga
   - Pemantauan kolaboratif aktivitas belajar
   - Dukungan pengembangan portofolio siswa

## E. Lingkungan Pembelajaran
1. **Ruang Kelas yang Dinamis**
   - Zona praktik keamanan jaringan
   - Ruang diskusi kasus keamanan
   - Area presentasi dan debat teknis

2. **Laboratorium Keamanan**
   - Lingkungan praktik yang aman
   - Simulasi jaringan terisolasi
   - Peralatan forensik digital dasar

3. **Budaya Belajar Kolaboratif**
   - Lingkungan berbagi pengetahuan
   - Penghargaan atas inovasi
   - Kebebasan bereksperimen yang bertanggung jawab

4. **Ruang Digital Terkelola**
   - Platform kolaborasi aman
   - Repositori sumber daya pembelajaran
   - Forum diskusi terpantau

## F. Pemanfaatan Digital
1. **Platform Pembelajaran**
   - Platform CTF (Capture The Flag)
   - Laboratorium virtual keamanan
   - Sistem manajemen pembelajaran (LMS)

2. **Alat Kolaborasi**
   - Platform version control (Git)
   - Alat dokumentasi kolaboratif
   - Komunikasi tim terenkripsi

3. **Sumber Belajar Digital**
   - Video tutorial keamanan jaringan
   - Lab virtual interaktif
   - Database kerentanan dan eksploitasi

4. **Alat Asesmen Digital**
   - Platform penilaian otomatis
   - Tools analisis keamanan
   - Sistem pelacakan kemajuan belajar

## G. Metode Pembelajaran
1. Diskusi kelompok dan presentasi
2. Demonstrasi dan praktik langsung
3. Studi kasus keamanan jaringan
4. Simulasi serangan dan pertahanan
5. Proyek keamanan jaringan laboratorium

## H. Media, Alat, dan Sumber Belajar
1. **Media**
   - Presentasi digital
   - Video tutorial
   - Simulasi jaringan
   - Platform e-learning

2. **Alat**
   - Komputer dengan spesifikasi memadai
   - Perangkat jaringan (router, switch)
   - Virtualisasi (VirtualBox, VMware)
   - Tools: Nmap, Wireshark, FreeRADIUS, Wazuh, Kali Linux, Mikrotik RouterOS

3. **Sumber Belajar**
   - Buku teks Sistem Keamanan Jaringan
   - Dokumentasi resmi (Nmap, Wireshark, FreeRADIUS, Wazuh, Mikrotik, dll)
   - Sumber online (OWASP, SANS, NIST)
   - Modul praktikum

## I. Langkah-langkah Pembelajaran (RPP Harian)

### **MODUL 1: PRAKTIK ANALISIS JARINGAN**

#### **RPP - Pertemuan 1: Konsep Scanning & Nmap**
1.  **Tujuan**: Memahami konsep scanning dan melakukan pemindaian port menggunakan Nmap. (UbD: Memahami cara mengidentifikasi target dan layanan yang berjalan).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara kita mengetahui 'pintu-pintu' yang terbuka di sebuah rumah tanpa masuk ke dalamnya?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan apa yang mereka ketahui tentang "pemindaian" dalam konteks jaringan.
        -   Guru menampilkan hasil scan Nmap sederhana dan memancing diskusi tentang informasi yang bisa didapatkan.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep Scanning (30 mnt)**: Guru menjelaskan konsep port scanning, host discovery, dan service/version detection. Memperkenalkan Nmap sebagai tool utama. (Diferensiasi: Menyediakan cheat sheet perintah Nmap dasar).
        -   **Praktik Terbimbing Nmap (45 mnt)**: Guru memandu siswa menggunakan Nmap untuk:
            -   Melakukan ping scan untuk host discovery.
            -   Melakukan port scan (TCP/UDP) pada VM target di lab virtual.
            -   Melakukan service/version detection.
            -   Melakukan OS detection.
            (SEL: Manajemen diri, ketekunan).
        -   **Analisis Hasil Scan (30 mnt)**: Siswa menganalisis hasil scan Nmap, mengidentifikasi port terbuka, layanan yang berjalan, dan potensi kerentanan. Diskusi kelompok tentang temuan. (Diferensiasi: Memberikan skenario target yang berbeda untuk setiap kelompok).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 3 informasi penting yang bisa didapatkan dari Nmap.
        -   Guru memimpin refleksi tentang pentingnya Nmap sebagai tool reconnaissance.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat perintah Nmap yang paling berguna. Guru menawarkan sumber belajar tambahan tentang Nmap scripting engine (NSE). (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Wireshark).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menggunakan Nmap dan menganalisis hasilnya.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Nmap (detail rubrik di Lampiran).

#### **RPP - Pertemuan 2: Analisis Lalu Lintas Jaringan & Wireshark**
1.  **Tujuan**: Menganalisis lalu lintas jaringan menggunakan Wireshark. (UbD: Memahami bagaimana data bergerak di jaringan dan mengidentifikasi anomali).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Jika kamu ingin tahu apa yang dibicarakan dua orang di telepon, bagaimana caranya?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan apa itu "paket data" dalam jaringan.
        -   Guru menampilkan tangkapan layar Wireshark dan memancing diskusi tentang informasi yang bisa dilihat.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep Packet Sniffing (30 mnt)**: Guru menjelaskan konsep packet sniffing, fungsi Wireshark, dan filter dasar (capture filter, display filter). (Diferensiasi: Menyediakan daftar filter Wireshark yang sering digunakan).
        -   **Praktik Terbimbing Wireshark (45 mnt)**: Guru memandu siswa menggunakan Wireshark untuk:
            -   Melakukan capture lalu lintas di interface jaringan VM.
            -   Menerapkan display filter untuk menganalisis protokol tertentu (misal: HTTP, DNS, ICMP).
            -   Menganalisis isi paket (header, payload).
            -   Mengidentifikasi komunikasi yang tidak terenkripsi.
            (SEL: Manajemen diri, ketekunan).
        -   **Analisis Skenario (30 mnt)**: Siswa diberikan file .pcap (tangkapan paket) yang berisi skenario sederhana (misal: login HTTP, transfer file FTP). Siswa menganalisis file tersebut untuk menemukan informasi sensitif atau anomali. (Diferensiasi: Menyediakan skenario dengan tingkat kesulitan berbeda).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 2 jenis informasi yang bisa ditemukan dengan Wireshark.
        -   Guru memimpin refleksi tentang pentingnya Wireshark untuk troubleshooting dan analisis keamanan.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat filter Wireshark yang paling berguna. Guru menawarkan sumber belajar tambahan tentang analisis forensik jaringan. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Sistem Autentikasi Terpusat).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menggunakan Wireshark dan menganalisis lalu lintas jaringan.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Wireshark (detail rubrik di Lampiran).

### **MODUL 2: SISTEM AUTENTIKASI TERPUSAT (PaaS)**

#### **RPP - Pertemuan 3: Konsep AAA & Protokol RADIUS**
1.  **Tujuan**: Menjelaskan konsep AAA dan protokol RADIUS. (UbD: Memahami pentingnya manajemen akses terpusat).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Jika ada banyak pintu di sebuah gedung, dan setiap orang punya kunci yang berbeda, bagaimana cara mengelola semua kunci itu agar tidak kacau?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan apa itu "autentikasi".
        -   Guru memperkenalkan konsep autentikasi terpusat sebagai solusi.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep AAA (30 mnt)**: Guru menjelaskan konsep Authentication, Authorization, dan Accounting (AAA) dengan contoh nyata. (Diferensiasi: Menyediakan studi kasus di mana salah satu aspek AAA gagal).
        -   **Eksplorasi Protokol RADIUS (45 mnt)**: Guru menjelaskan protokol RADIUS (Remote Authentication Dial-In User Service): fungsi, komponen (client, server), dan alur komunikasi. (Diferensiasi: Menyediakan diagram alur RADIUS yang jelas).
        -   **Diskusi Penerapan (30 mnt)**: Siswa dalam kelompok berdiskusi tentang skenario di mana RADIUS dapat diterapkan (misal: autentikasi Wi-Fi, akses VPN, akses perangkat jaringan). (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan perbedaan antara Authentication dan Authorization.
        -   Guru memimpin refleksi tentang manfaat autentikasi terpusat.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat komponen utama RADIUS. Guru menawarkan sumber belajar tambahan tentang protokol autentikasi lain (misal: TACACS+). (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Implementasi FreeRADIUS).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang konsep AAA dan RADIUS.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 4: Implementasi FreeRADIUS Server**
1.  **Tujuan**: Menginstal dan mengkonfigurasi FreeRADIUS Server. (UbD: Membangun layanan autentikasi terpusat).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara kita membuat 'pusat' yang bisa memverifikasi semua kunci di gedung kita?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan peran "server" dalam autentikasi.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Persiapan Lingkungan (30 mnt)**: Guru memandu siswa menyiapkan VM Linux baru untuk FreeRADIUS Server (instalasi OS, update). (Diferensiasi: Menyediakan skrip instalasi dasar).
        -   **Praktik Terbimbing Instalasi FreeRADIUS (45 mnt)**: Guru memandu siswa menginstal FreeRADIUS dan mengkonfigurasi klien (misal: Mikrotik) serta pengguna di FreeRADIUS. (SEL: Manajemen diri, ketekunan).
        -   **Pengujian Dasar (30 mnt)**: Siswa menguji konektivitas antara Mikrotik (sebagai klien) dan FreeRADIUS Server. Memastikan FreeRADIUS merespons permintaan autentikasi. (Diferensiasi: Memberikan tantangan untuk menambahkan lebih banyak pengguna).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 2 konfigurasi penting di FreeRADIUS.
        -   Guru memimpin refleksi tentang tantangan instalasi server.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat langkah-langkah instalasi FreeRADIUS. Guru menawarkan sumber belajar tambahan tentang konfigurasi FreeRADIUS yang lebih kompleks. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Integrasi Mikrotik RADIUS Client).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menginstal dan mengkonfigurasi FreeRADIUS.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Instalasi FreeRADIUS (detail rubrik di Lampiran).

#### **RPP - Pertemuan 5: Integrasi Mikrotik sebagai RADIUS Client**
1.  **Tujuan**: Mengintegrasikan Mikrotik sebagai RADIUS Client ke FreeRADIUS Server. (UbD: Menerapkan autentikasi terpusat pada perangkat jaringan).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara 'pintu-pintu' di gedung kita bisa 'berbicara' dengan 'pusat verifikasi kunci'?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan peran "klien" dalam sistem autentikasi.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Review Konfigurasi (30 mnt)**: Guru mereview konfigurasi FreeRADIUS Server dan Mikrotik dasar. Memastikan konektivitas antar VM.
        -   **Praktik Terbimbing Konfigurasi Mikrotik RADIUS Client (45 mnt)**: Guru memandu siswa mengkonfigurasi Mikrotik untuk menggunakan FreeRADIUS sebagai server autentikasi untuk login (misal: login WinBox/SSH). (SEL: Manajemen diri, ketekunan).
        -   **Pengujian Autentikasi (30 mnt)**: Siswa menguji login ke Mikrotik menggunakan kredensial yang dikelola di FreeRADIUS. Melakukan troubleshooting jika ada masalah. (Diferensiasi: Memberikan tantangan untuk mengintegrasikan autentikasi hotspot Mikrotik dengan RADIUS).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan manfaat utama integrasi Mikrotik dengan RADIUS.
        -   Guru memimpin refleksi tentang proses integrasi sistem.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat langkah-langkah konfigurasi RADIUS client di Mikrotik. Guru menawarkan sumber belajar tambahan tentang atribut RADIUS. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Manajemen Akses Lanjutan).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam mengintegrasikan Mikrotik dengan FreeRADIUS dan melakukan troubleshooting.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Integrasi RADIUS (detail rubrik di Lampiran).

### **MODUL 3: MANAJEMEN AKSES LANJUTAN**

#### **RPP - Pertemuan 6: Konsep Multi-Factor Authentication (MFA)**
1.  **Tujuan**: Memahami konsep Multi-Factor Authentication (MFA) dan jenis-jenisnya. (UbD: Memahami pentingnya lapisan keamanan tambahan untuk autentikasi).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Jika kunci rumahmu hilang, apa yang bisa kamu lakukan agar orang lain tidak bisa masuk?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan mengapa password saja tidak cukup aman.
        -   Guru menampilkan contoh MFA (misal: login Google dengan OTP).
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep MFA (45 mnt)**: Guru menjelaskan konsep MFA (Something You Know, Something You Have, Something You Are) dan berbagai jenisnya (OTP, biometrik, hardware token, push notification). (Diferensiasi: Menyediakan video demonstrasi MFA).
        -   **Diskusi Studi Kasus (45 mnt)**: Siswa dalam kelompok menganalisis studi kasus pelanggaran keamanan yang bisa dicegah dengan MFA. Diskusi tentang pro dan kontra setiap jenis MFA. (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
        -   **Analisis Alur Login (15 mnt)**: Siswa menganalisis alur login dari beberapa layanan populer (misal: Gmail, perbankan online) dan mengidentifikasi faktor autentikasi yang digunakan.
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 3 faktor autentikasi yang berbeda.
        -   Guru memimpin refleksi tentang pentingnya MFA dalam kehidupan digital sehari-hari.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa menuliskan komitmen untuk mengaktifkan MFA pada akun penting mereka. Guru menawarkan sumber belajar tambahan tentang FIDO Alliance atau WebAuthn. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Integrasi MFA via RADIUS).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang MFA dan kesadaran keamanannya.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 7: Konsep Integrasi MFA via RADIUS (Konseptual)**
1.  **Tujuan**: Memahami konsep integrasi MFA dengan sistem autentikasi terpusat (RADIUS). (UbD: Memahami arsitektur keamanan yang lebih kompleks).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara 'pusat verifikasi kunci' kita bisa meminta 'sidik jari' atau 'kode dari HP' sebelum memberikan akses?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan bagaimana RADIUS bekerja.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Arsitektur Integrasi (45 mnt)**: Guru menjelaskan secara konseptual bagaimana MFA dapat diintegrasikan dengan RADIUS (misal: menggunakan FreeRADIUS dengan modul OTP, atau integrasi dengan layanan MFA pihak ketiga). (Diferensiasi: Menyediakan diagram arsitektur yang kompleks namun jelas).
        -   **Simulasi Alur Login dengan MFA (45 mnt)**: Siswa dalam kelompok mensimulasikan alur login ke Mikrotik yang terintegrasi dengan RADIUS dan MFA. Mengidentifikasi setiap langkah dan interaksi antar komponen. (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
        -   **Diskusi Tantangan Implementasi (15 mnt)**: Diskusi tentang tantangan teknis dan non-teknis dalam mengimplementasikan MFA skala besar.
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan satu tantangan dalam mengintegrasikan MFA.
        -   Guru memimpin refleksi tentang kompleksitas dan manfaat keamanan dari arsitektur terintegrasi.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa menuliskan skenario di mana integrasi MFA sangat krusial. Guru menawarkan sumber belajar tambahan tentang implementasi MFA di lingkungan enterprise. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Deteksi Intrusi & Analisis Log).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang arsitektur integrasi MFA dan kemampuan mereka dalam menganalisis alur sistem.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Simulasi Alur (detail rubrik di Lampiran).

### **MODUL 4: DETEKSI INTRUSI & ANALISIS LOG (SIEM)**

#### **RPP - Pertemuan 8: Konsep IDS/IPS dan SIEM**
1.  **Tujuan**: Menjelaskan konsep IDS/IPS, SIEM, dan Log Management. (UbD: Memahami pentingnya pemantauan dan deteksi ancaman).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Jika ada penyusup di rumah, bagaimana cara kita tahu ada penyusup dan apa yang mereka lakukan?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan apa itu "log" dalam konteks komputer.
        -   Guru menampilkan contoh alert dari IDS atau dashboard SIEM.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep IDS/IPS (30 mnt)**: Guru menjelaskan perbedaan antara Intrusion Detection System (IDS) dan Intrusion Prevention System (IPS), serta jenis-jenisnya (Network-based, Host-based). (Diferensiasi: Menyediakan studi kasus di mana IDS/IPS berhasil mendeteksi/mencegah serangan).
        -   **Eksplorasi Konsep SIEM & Log Management (45 mnt)**: Guru menjelaskan konsep Security Information and Event Management (SIEM): fungsi (koleksi, normalisasi, korelasi, analisis log), manfaat, dan pentingnya log dari berbagai sumber. (Diferensiasi: Menyediakan diagram arsitektur SIEM sederhana).
        -   **Diskusi Sumber Log (30 mnt)**: Siswa dalam kelompok mengidentifikasi berbagai sumber log dalam jaringan lab virtual mereka (Mikrotik, Linux VM, FreeRADIUS) dan jenis informasi yang terkandung di dalamnya. (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan perbedaan utama antara IDS dan IPS.
        -   Guru memimpin refleksi tentang pentingnya SIEM untuk visibilitas keamanan.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat jenis log yang paling penting untuk dikumpulkan. Guru menawarkan sumber belajar tambahan tentang aturan korelasi SIEM. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Implementasi Wazuh).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang IDS/IPS dan SIEM.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 9: Implementasi SIEM dengan Wazuh (Agent & Manager)**
1.  **Tujuan**: Menginstal dan mengkonfigurasi Wazuh Manager dan Agent. (UbD: Membangun sistem pemantauan keamanan terpusat).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara kita mengumpulkan semua 'catatan kejadian' dari berbagai ruangan di rumah ke satu 'pusat kendali'?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan fungsi "agent" dalam sistem monitoring.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Persiapan Lingkungan (30 mnt)**: Guru memandu siswa menyiapkan VM Linux baru untuk Wazuh Manager (instalasi OS, update). (Diferensiasi: Menyediakan skrip instalasi dasar).
        -   **Praktik Terbimbing Instalasi Wazuh Manager (45 mnt)**: Guru memandu siswa menginstal Wazuh Manager (termasuk Elasticsearch/OpenSearch dan Kibana/Dashboards). (SEL: Manajemen diri, ketekunan).
        -   **Praktik Terbimbing Instalasi Wazuh Agent (30 mnt)**: Guru memandu siswa menginstal Wazuh Agent pada VM Linux lain (misal: VM klien/server) dan mendaftarkannya ke Wazuh Manager. (Diferensiasi: Memberikan tantangan untuk menginstal agent pada OS yang berbeda).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 2 komponen utama Wazuh.
        -   Guru memimpin refleksi tentang kompleksitas instalasi SIEM.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat langkah-langkah instalasi Wazuh. Guru menawarkan sumber belajar tambahan tentang konfigurasi Wazuh rules. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Analisis Dashboard Wazuh).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menginstal Wazuh Manager dan Agent.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Instalasi Wazuh (detail rubrik di Lampiran).

#### **RPP - Pertemuan 10: Analisis Log & Dashboard Wazuh**
1.  **Tujuan**: Mengirim log dari Mikrotik & VM lain ke Wazuh dan menganalisis dashboard. (UbD: Menganalisis data keamanan untuk deteksi ancaman).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Setelah semua 'catatan kejadian' terkumpul di 'pusat kendali', bagaimana cara kita 'membaca' dan 'memahami' apa yang terjadi dengan cepat?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan manfaat dashboard dalam monitoring.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Konfigurasi Pengiriman Log (45 mnt)**: Guru memandu siswa mengkonfigurasi Mikrotik untuk mengirim log ke Wazuh Manager (syslog). Memastikan log dari VM Linux (via agent) dan Mikrotik masuk ke Wazuh. (SEL: Manajemen diri, ketekunan).
        -   **Eksplorasi Dashboard Wazuh (45 mnt)**: Guru memandu siswa menjelajahi dashboard Wazuh (Discover, Alerts, Agents, Modules). Menganalisis log, mencari anomali, dan memahami korelasi event. (Diferensiasi: Memberikan skenario serangan sederhana untuk dideteksi di Wazuh).
        -   **Diskusi Temuan (15 mnt)**: Siswa dalam kelompok mendiskusikan temuan dari log dan dashboard Wazuh, mengidentifikasi potensi insiden keamanan.
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 2 jenis anomali yang bisa dideteksi dengan Wazuh.
        -   Guru memimpin refleksi tentang kekuatan SIEM dalam deteksi dini.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa menuliskan bagaimana SIEM dapat membantu dalam respon insiden. Guru menawarkan sumber belajar tambahan tentang integrasi Wazuh dengan TheHive/Cortex. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Enkripsi & Komunikasi Aman).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menganalisis log dan menggunakan dashboard Wazuh.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Analisis Dashboard Wazuh (detail rubrik di Lampiran).

### **MODUL 5: ENKRIPSI & KOMUNIKASI AMAN**

#### **RPP - Pertemuan 11: Dasar-dasar Kriptografi & Fungsi Hash**
1.  **Tujuan**: Memahami dasar-dasar kriptografi (simetris, asimetris) dan fungsi hash. (UbD: Memahami prinsip kerahasiaan dan integritas data).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara kita mengirim pesan rahasia agar hanya orang yang dituju yang bisa membacanya?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan apa itu "kode rahasia".
        -   Guru menampilkan contoh teks terenkripsi dan hash.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep Kriptografi (45 mnt)**: Guru menjelaskan konsep kriptografi simetris (misal: AES) dan asimetris (misal: RSA), perbedaan, dan kapan digunakan. (Diferensiasi: Menyediakan analogi sederhana untuk setiap jenis kriptografi).
        -   **Eksplorasi Fungsi Hash (45 mnt)**: Guru menjelaskan fungsi hash (misal: MD5, SHA-256): sifat-sifatnya (one-way, collision resistance), dan penggunaannya (integritas data, penyimpanan password). (Diferensiasi: Meminta siswa mencoba menghitung hash online dari teks yang sama/berbeda).
        -   **Diskusi Penerapan (15 mnt)**: Siswa dalam kelompok berdiskusi tentang penerapan kriptografi dan hash dalam kehidupan sehari-hari (misal: HTTPS, tanda tangan digital, blockchain). (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan perbedaan utama antara enkripsi dan hashing.
        -   Guru memimpin refleksi tentang pentingnya kriptografi untuk keamanan data.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa menuliskan bagaimana kriptografi melindungi privasi mereka. Guru menawarkan sumber belajar tambahan tentang algoritma kriptografi modern. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Konsep VPN).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang konsep kriptografi dan hash.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 12: Konsep VPN & Praktik VPN Remote Access (PPTP/L2TP)**
1.  **Tujuan**: Memahami konsep VPN dan mengimplementasikan VPN Remote Access (PPTP/L2TP) di Mikrotik. (UbD: Menerapkan komunikasi aman melalui jaringan tidak terpercaya).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru bertanya: "Bagaimana cara kita mengakses jaringan kantor dari rumah dengan aman, seolah-olah kita berada di kantor?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menjelaskan apa itu "jaringan pribadi virtual".
        -   Guru menampilkan diagram VPN sederhana.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Presentasi Konsep VPN (30 mnt)**: Guru menjelaskan konsep Virtual Private Network (VPN): fungsi, manfaat (kerahasiaan, integritas, autentikasi), dan jenis-jenisnya (Remote Access, Site-to-Site). Memperkenalkan protokol PPTP dan L2TP/IPsec. (Diferensiasi: Menyediakan video animasi cara kerja VPN).
        -   **Praktik Terbimbing VPN Remote Access (45 mnt)**: Guru memandu siswa mengkonfigurasi VPN Server (PPTP atau L2TP/IPsec) di Mikrotik. Kemudian, siswa mengkonfigurasi VPN Client di komputer host atau VM Linux untuk terhubung ke Mikrotik VPN Server. (SEL: Manajemen diri, ketekunan).
        -   **Pengujian Konektivitas Aman (30 mnt)**: Siswa menguji konektivitas ke jaringan internal Mikrotik melalui VPN. Memverifikasi bahwa lalu lintas terenkripsi (jika menggunakan L2TP/IPsec). (Diferensiasi: Memberikan tantangan untuk mengintegrasikan VPN dengan RADIUS autentikasi).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 2 manfaat utama VPN.
        -   Guru memimpin refleksi tentang pentingnya VPN untuk akses jarak jauh yang aman.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa mencatat langkah-langkah konfigurasi VPN. Guru menawarkan sumber belajar tambahan tentang protokol VPN lain (misal: OpenVPN, WireGuard). (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul proyek.
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam mengimplementasikan VPN Remote Access.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik VPN (detail rubrik di Lampiran).

### **MODUL 6: PROYEK MINI SEMESTER 2**

#### **RPP - Pertemuan 13: Penjelasan dan Perencanaan Proyek**
1.  **Tujuan**: Memahami spesifikasi proyek dan merencanakan pengerjaan dalam kelompok. (UbD: Mengaplikasikan pemahaman untuk merancang solusi keamanan terintegrasi).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru memotivasi siswa: "Saatnya menggabungkan semua yang telah kita pelajari di semester ini! Kita akan membangun sistem autentikasi terpusat dan monitoring keamanan. Apa tantangan terbesar yang kalian bayangkan?" (SEL: Motivasi diri, kesadaran diri).
        -   **Pre-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan 3 komponen penting dalam sistem keamanan terintegrasi.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (105 mnt)**:
        -   **Penjelasan Detail Proyek (30 mnt)**: Guru menjelaskan spesifikasi proyek mini semester 2: "Implementasikan Autentikasi Terpusat (PaaS) dan Monitoring Keamanan pada Jaringan Lab Virtual" (misal: topologi yang harus dibuat, integrasi RADIUS, implementasi Wazuh, skenario pengujian). (Diferensiasi: Menyediakan rubrik penilaian proyek yang jelas dan contoh proyek sebelumnya).
        -   **Pembentukan Kelompok (15 mnt)**: Siswa dibagi menjadi kelompok (3-4 orang). (SEL: Keterampilan hubungan, kesadaran sosial).
        -   **Diskusi Kelompok & Perencanaan (60 mnt)**: Setiap kelompok berdiskusi untuk menyusun rencana kerja: pembagian tugas, timeline, desain topologi jaringan, dan strategi implementasi keamanan. (Diferensiasi: Guru berkeliling memberikan bimbingan individual atau kelompok, menyediakan template perencanaan proyek).
    -   **Penutup (15 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Setiap kelompok mempresentasikan singkat rencana kerja mereka. Guru memberikan umpan balik awal dan memastikan semua kelompok memiliki pemahaman yang jelas.
        -   **Refleksi & Diferensiasi (5 mnt)**: Siswa menuliskan satu tantangan yang mereka antisipasi dalam proyek ini dan bagaimana mereka berencana mengatasinya. Guru mengingatkan tentang pentingnya komunikasi dalam tim. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan umpan balik awal dan memastikan semua kelompok memiliki pemahaman yang jelas.
        -   **Refleksi Guru**: Guru mencatat kualitas perencanaan proyek oleh kelompok dan pemahaman mereka terhadap spesifikasi proyek.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Rencana Proyek (detail rubrik di Lampiran).

#### **RPP - Pertemuan 14: Pengerjaan Proyek (Implementasi)**
1.  **Tujuan**: Mengimplementasikan konfigurasi dasar proyek sesuai rencana. (UbD: Menerapkan pengetahuan dan keterampilan dalam konteks nyata).
2.  **Langkah-langkah**:
    -   **Pendahuluan (10 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru meminta setiap kelompok untuk berbagi satu tantangan yang mereka hadapi saat merencanakan proyek dan bagaimana mereka berencana mengatasinya. (SEL: Kesadaran diri, pemecahan masalah).
        -   Guru mereview singkat rencana kerja setiap kelompok dan mengingatkan tentang pentingnya kolaborasi.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (115 mnt)**:
        -   **Sesi Kerja Kelompok (115 mnt)**: Peserta didik bekerja dalam kelompok untuk membangun topologi jaringan virtual (membuat VM, mengkonfigurasi jaringan virtual), menginstal dan mengkonfigurasi FreeRADIUS, mengintegrasikan Mikrotik sebagai RADIUS client, menginstal Wazuh Manager dan Agent, serta mengkonfigurasi pengiriman log. Guru berkeliling sebagai fasilitator, memberikan bimbingan, dan membantu troubleshooting. (Diferensiasi: Guru dapat memberikan bantuan terfokus kepada kelompok yang kesulitan, atau memberikan tantangan tambahan bagi kelompok yang sudah maju).
    -   **Penutup (10 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Setiap kelompok melaporkan progres yang dicapai dan kendala yang dihadapi. Guru memberikan umpan balik singkat.
        -   Guru memberikan motivasi dan arahan untuk pertemuan berikutnya. (SEL: Motivasi diri, manajemen diri).
        -   **Refleksi Guru**: Guru mencatat progres implementasi proyek setiap kelompok, kemampuan kolaborasi, dan kemandirian dalam troubleshooting.
        -   **Asesmen yang dipakai**: Observasi, Laporan Progres Proyek (detail rubrik di Lampiran).

#### **RPP - Pertemuan 15: Finalisasi Proyek dan Penyusunan Laporan**
1.  **Tujuan**: Menyelesaikan proyek dan menyusun laporan/dokumentasi teknis. (UbD: Mengkomunikasikan hasil kerja secara profesional).
2.  **Langkah-langkah**:
    -   **Pendahuluan (10 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru meminta setiap kelompok untuk berbagi satu "temuan" menarik atau "solusi cerdas" yang mereka dapatkan selama pengerjaan proyek. (SEL: Kesadaran diri, apresiasi).
        -   Guru mereview progres terakhir dan memberikan kesempatan untuk troubleshooting akhir.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (115 mnt)**:
        -   **Sesi Kerja Kelompok (80 mnt)**: Peserta didik melanjutkan finalisasi konfigurasi proyek mereka. Memastikan semua integrasi (RADIUS, Wazuh) berfungsi sesuai harapan. Melakukan pengujian menyeluruh terhadap sistem autentikasi dan monitoring. (Diferensiasi: Guru dapat memberikan panduan khusus untuk troubleshooting masalah umum, atau menyediakan checklist finalisasi proyek).
        -   **Penyusunan Laporan Teknis (35 mnt)**: Setiap kelompok mulai menyusun laporan teknis proyek, yang mencakup: topologi jaringan (diagram), konfigurasi FreeRADIUS, konfigurasi Wazuh, hasil pengujian autentikasi dan deteksi, serta analisis keamanan. (SEL: Manajemen diri, ketekunan). (Diferensiasi: Menyediakan template laporan yang berbeda tingkat kerinciannya, atau contoh laporan yang baik).
    -   **Penutup (10 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta setiap kelompok untuk menyebutkan satu bagian terpenting dari laporan teknis mereka dan mengapa.
        -   Guru mengingatkan tentang persiapan presentasi proyek untuk pertemuan berikutnya.
        -   Siswa memastikan semua anggota kelompok memahami isi laporan. (SEL: Keterampilan hubungan, kesadaran sosial).
        -   **Refleksi Guru**: Guru mencatat kualitas finalisasi proyek dan kelengkapan dokumentasi teknis yang dibuat siswa.
        -   **Asesmen yang dipakai**: Observasi, Laporan Teknis Proyek (detail rubrik di Lampiran).

#### **RPP - Pertemuan 16: Presentasi Proyek dan Evaluasi Semester**
1.  **Tujuan**: Mempresentasikan dan mendemonstrasikan hasil proyek. (UbD: Menunjukkan pemahaman melalui kinerja otentik).
2.  **Langkah-langkah**:
    -   **Pendahuluan (10 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (5 mnt)**: Guru meminta siswa untuk melakukan peregangan ringan atau "power pose" untuk membangun kepercayaan diri sebelum presentasi. (SEL: Manajemen diri, kesadaran diri).
        -   Guru mempersiapkan kelas untuk presentasi, termasuk pengundian urutan presentasi.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (115 mnt)**:
        -   **Presentasi & Demonstrasi Proyek (90 mnt)**: Setiap kelompok mempresentasikan laporan teknis mereka (sekitar 10-15 menit per kelompok) dan mendemonstrasikan fungsionalitas sistem autentikasi terpusat dan monitoring keamanan yang telah mereka bangun. (SEL: Keterampilan hubungan, kesadaran sosial).
        -   **Sesi Tanya Jawab & Umpan Balik (25 mnt)**: Guru dan siswa lain memberikan pertanyaan dan umpan balik konstruktif. (Diferensiasi: Guru dapat memandu pertanyaan agar sesuai dengan tingkat pemahaman siswa, atau memberikan umpan balik tertulis yang lebih detail setelah presentasi).
    -   **Penutup (10 mnt)**:
        -   **Post-test Sederhana (5 mnt)**: Guru meminta siswa menuliskan satu hal yang paling mereka banggakan dari proyek ini atau satu pelajaran terbesar yang mereka dapatkan selama semester ini.
        -   Guru memimpin refleksi pembelajaran keseluruhan semester, menyoroti pencapaian dan area yang perlu ditingkatkan.
        -   Guru memberikan umpan balik umum tentang proyek dan menutup semester. (SEL: Refleksi diri, manajemen diri).
        -   **Refleksi Guru**: Guru mencatat kualitas presentasi, kemampuan demonstrasi, dan pemahaman keseluruhan siswa terhadap materi semester ini.
        -   **Asesmen yang dipakai**: Observasi, Presentasi Proyek, Demonstrasi Proyek (detail rubrik di Lampiran).


## J. Penilaian
1. **Asesmen Formatif**
   - Kuis harian
   - Tugas individu/kelompok
   - Observasi aktivitas pembelajaran
   - Laporan praktikum

2. **Asesmen Sumatif**
   - Ujian Tengah Semester
   - Ujian Akhir Semester
   - Proyek akhir

3. **Rubrik Penilaian**
   - Ketepatan konsep (30%)
   - Keterampilan praktik (40%)
   - Kemampuan analisis (20%)
   - Kerjasama tim (10%)

## K. Sumber Belajar
1. Buku teks Sistem Keamanan Jaringan
2. Dokumentasi resmi:
   - Nmap Documentation
   - Wireshark Documentation
   - FreeRADIUS Documentation
   - Wazuh Documentation
   - MikroTik Documentation
   - OWASP Top 10
   - NIST Cybersecurity Framework
3. Sumber online:
   - Video tutorial keamanan jaringan
   - Lab virtual interaktif
   - Artikel dan jurnal keamanan siber

## L. CATATAN :

### 1. Pencapaian Pembelajaran
- Tujuan pembelajaran yang tercapai dengan baik:
  • _________________________________________________________________
  • _________________________________________________________________
- Tujuan pembelajaran yang belum tercapai optimal:
  • _________________________________________________________________
  • _________________________________________________________________

### 2. Asesmen dan Evaluasi
- Asesmen yang berjalan efektif:
  • _________________________________________________________________
- Kendala dalam pelaksanaan asesmen:
  • _________________________________________________________________
- Hasil analisis capaian belajar siswa:
  • Rata-rata kelas: ______ (dari skala 100)
  • Tingkat ketuntasan: ______%
  • Siswa yang memerlukan remedial: ______ orang

### 3. Strategi Pembelajaran
- Metode yang efektif:
  • _________________________________________________________________
- Metode yang perlu diperbaiki:
  • _________________________________________________________________
- Inovasi yang berhasil diterapkan:
  • _________________________________________________________________

### 4. Kendala dan Solusi
- Kendala teknis:
  • _________________________________________________________________
  Solusi: __________________________________________________________
- Kendala non-teknis:
  • _________________________________________________________________
  Solusi: __________________________________________________________

### 5. Umpan Balik Siswa
- Aspek yang disukai siswa:
  • _________________________________________________________________
- Kesulitan yang dialami siswa:
  • _________________________________________________________________
- Saran perbaikan dari siswa:
  • _________________________________________________________________

### 6. Rencana Perbaikan
- Untuk materi yang sama:
  • _________________________________________________________________
  • _________________________________________________________________
- Untuk pembelajaran berikutnya:
  • _________________________________________________________________
  • _________________________________________________________________

### 7. Catatan Khusus
- Prestasi siswa yang menonjol:
  • _________________________________________________________________
- Isu khusus yang perlu perhatian:
  • _________________________________________________________________
- Rekomendasi untuk sekolah/orang tua:
  • _________________________________________________________________

Nama Kota, Tanggal
Mengetahui	Guru Kelas / Mapel,
Kepala Sekolah,

…………………………………………	…………………………………………….
NIP. …………………………………….	NIP. …………………………………………

LAMPIRAN – LAMPIRAN
- Lembar Kerja Peserta Didik (LKPD)
- Materi pembelajaran lengkap
- Instrumen asesmen
- Sumber referensi
- Glosarium
- Daftar pustaka
- Bukti fisik praktik, laporan, dan hasil kerja siswa

## LAMPIRAN - LEMBAR KERJA PESERTA DIDIK (LKPD)

### LKPD Pertemuan 1: Konsep Scanning & Nmap
**Tujuan Pembelajaran**: Memahami konsep scanning dan melakukan pemindaian port menggunakan Nmap.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang konsep scanning dan penggunaan Nmap.
2.  Lakukan praktik pemindaian menggunakan Nmap pada lingkungan lab virtual.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu port scanning dan mengapa penting dalam keamanan jaringan.
2.  Sebutkan minimal 3 (tiga) jenis pemindaian yang dapat dilakukan oleh Nmap.
3.  Lakukan pemindaian host discovery (ping scan) pada jaringan lab virtualmu. Lampirkan *screenshot* perintah dan hasilnya.
4.  Lakukan pemindaian port (TCP) pada salah satu VM target di lab virtualmu. Identifikasi port yang terbuka dan layanan yang berjalan. Lampirkan *screenshot* perintah dan hasilnya.
5.  Lakukan pemindaian versi layanan pada port yang terbuka. Lampirkan *screenshot* perintah dan hasilnya.

**Pertanyaan Refleksi**:
1.  Apa informasi paling berharga yang kamu dapatkan dari hasil pemindaian Nmap?
2.  Bagaimana Nmap dapat membantu seorang profesional keamanan dalam mengidentifikasi kerentanan?

---

### LKPD Pertemuan 2: Analisis Lalu Lintas Jaringan & Wireshark
**Tujuan Pembelajaran**: Menganalisis lalu lintas jaringan menggunakan Wireshark.

**Petunjuk Pengerjaan**:
1.  Pahami konsep packet sniffing dan penggunaan Wireshark.
2.  Lakukan praktik analisis lalu lintas jaringan menggunakan Wireshark pada lingkungan lab virtual.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu packet sniffing dan mengapa Wireshark menjadi tool yang penting.
2.  Sebutkan perbedaan antara capture filter dan display filter di Wireshark. Berikan contoh penggunaan masing-masing.
3.  Lakukan capture lalu lintas jaringan pada interface VM Linuxmu. Lakukan aktivitas sederhana (misal: ping ke VM lain, browsing ke situs HTTP). Lampirkan *screenshot* proses capture.
4.  Gunakan display filter di Wireshark untuk menampilkan hanya paket HTTP. Identifikasi permintaan dan respons HTTP. Lampirkan *screenshot* hasilnya.
5.  Analisis file .pcap yang diberikan oleh guru. Temukan informasi sensitif (misal: username/password yang tidak terenkripsi) jika ada. Jelaskan langkah-langkah yang kamu lakukan untuk menemukannya.

**Pertanyaan Refleksi**:
1.  Apa risiko keamanan jika lalu lintas jaringan tidak dienkripsi?
2.  Bagaimana Wireshark dapat digunakan untuk troubleshooting masalah jaringan?

---

### LKPD Pertemuan 3: Konsep AAA & Protokol RADIUS
**Tujuan Pembelajaran**: Menjelaskan konsep AAA dan protokol RADIUS.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang konsep AAA dan protokol RADIUS.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan konsep AAA (Authentication, Authorization, Accounting) dengan bahasamu sendiri. Berikan contoh nyata untuk masing-masing aspek.
2.  Apa itu protokol RADIUS? Jelaskan fungsi utama dan komponen-komponennya (RADIUS Client, RADIUS Server).
3.  Gambarkan alur komunikasi sederhana antara RADIUS Client dan RADIUS Server saat seorang pengguna mencoba login.
4.  Sebutkan minimal 2 (dua) skenario di mana penggunaan RADIUS sangat bermanfaat dalam sebuah organisasi.
5.  Mengapa autentikasi terpusat lebih baik daripada autentikasi lokal pada setiap perangkat?

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar dalam mengelola autentikasi dan otorisasi di jaringan besar tanpa sistem terpusat?
2.  Bagaimana pemahaman tentang AAA dapat membantumu merancang sistem keamanan yang lebih baik?

---

### LKPD Pertemuan 4: Implementasi FreeRADIUS Server
**Tujuan Pembelajaran**: Menginstal dan mengkonfigurasi FreeRADIUS Server.

**Petunjuk Pengerjaan**:
1.  Pahami langkah-langkah instalasi dan konfigurasi FreeRADIUS Server.
2.  Lakukan praktik instalasi dan konfigurasi pada VM Linux.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Siapkan sebuah VM Linux baru (misal: Ubuntu Server) untuk FreeRADIUS Server. Lampirkan *screenshot* setelah instalasi OS selesai.
2.  Lakukan instalasi FreeRADIUS di VM tersebut. Lampirkan *screenshot* proses instalasi.
3.  Konfigurasi FreeRADIUS untuk mengenali Mikrotik sebagai RADIUS Client. Sertakan *shared secret* yang kuat. Lampirkan *screenshot* konfigurasi klien.
4.  Tambahkan minimal 2 (dua) pengguna baru di FreeRADIUS dengan username dan password. Lampirkan *screenshot* konfigurasi pengguna.
5.  Lakukan pengujian dasar dari FreeRADIUS Server untuk memverifikasi bahwa klien dan pengguna telah dikonfigurasi dengan benar. Lampirkan *screenshot* hasil pengujian.

**Pertanyaan Refleksi**:
1.  Apa saja file konfigurasi utama yang perlu diedit saat mengkonfigurasi FreeRADIUS?
2.  Bagaimana kamu memastikan bahwa FreeRADIUS Server berjalan dengan aman?

---

### LKPD Pertemuan 5: Integrasi Mikrotik sebagai RADIUS Client
**Tujuan Pembelajaran**: Mengintegrasikan Mikrotik sebagai RADIUS Client ke FreeRADIUS Server.

**Petunjuk Pengerjaan**:
1.  Pahami langkah-langkah integrasi Mikrotik dengan FreeRADIUS.
2.  Lakukan praktik konfigurasi Mikrotik sebagai RADIUS Client.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Pastikan Mikrotik RouterOS VM dan FreeRADIUS Server VM sudah berjalan dan dapat saling berkomunikasi.
2.  Konfigurasi Mikrotik untuk menambahkan FreeRADIUS Server sebagai server RADIUS baru. Sertakan IP address FreeRADIUS Server dan *shared secret* yang sama. Lampirkan *screenshot* konfigurasi.
3.  Konfigurasi Mikrotik agar menggunakan RADIUS untuk autentikasi login (misal: untuk login WinBox atau SSH). Lampirkan *screenshot* konfigurasi.
4.  Uji login ke Mikrotik menggunakan username dan password yang telah kamu buat di FreeRADIUS Server. Lampirkan *screenshot* hasil login berhasil.
5.  Jelaskan bagaimana proses autentikasi terjadi ketika kamu mencoba login ke Mikrotik yang terintegrasi dengan RADIUS.

**Pertanyaan Refleksi**:
1.  Apa manfaat utama dari mengintegrasikan Mikrotik dengan RADIUS untuk autentikasi login?
2.  Apa yang akan terjadi jika *shared secret* antara Mikrotik dan FreeRADIUS tidak cocok?

---

### LKPD Pertemuan 6: Konsep Multi-Factor Authentication (MFA)
**Tujuan Pembelajaran**: Memahami konsep Multi-Factor Authentication (MFA) dan jenis-jenisnya.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang MFA dan berbagai faktor autentikasi.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu Multi-Factor Authentication (MFA) dan mengapa sangat penting untuk keamanan akun digital.
2.  Sebutkan dan jelaskan 3 (tiga) kategori faktor autentikasi dalam MFA (Something You Know, Something You Have, Something You Are). Berikan minimal 2 contoh untuk setiap kategori.
3.  Identifikasi jenis MFA yang digunakan oleh layanan online yang sering kamu gunakan (misal: Google, Instagram, perbankan online).
4.  Diskusikan dalam kelompok: Apa kelebihan dan kekurangan dari setiap jenis MFA (misal: OTP via SMS, aplikasi authenticator, biometrik, hardware token)?
5.  Skenario: Sebuah perusahaan mengalami kebocoran data karena password karyawan yang lemah. Bagaimana penerapan MFA dapat mencegah insiden serupa di masa depan?

**Pertanyaan Refleksi**:
1.  Apakah kamu sudah mengaktifkan MFA pada akun-akun pentingmu? Mengapa atau mengapa tidak?
2.  Menurutmu, jenis MFA apa yang paling aman dan paling nyaman digunakan? Jelaskan alasannya.

---

### LKPD Pertemuan 7: Konsep Integrasi MFA via RADIUS (Konseptual)
**Tujuan Pembelajaran**: Memahami konsep integrasi MFA dengan sistem autentikasi terpusat (RADIUS).

**Petunjuk Pengerjaan**:
1.  Pahami arsitektur konseptual integrasi MFA dengan RADIUS.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Gambarkan diagram arsitektur konseptual yang menunjukkan bagaimana MFA dapat diintegrasikan dengan sistem RADIUS untuk autentikasi login ke perangkat jaringan (misal: Mikrotik). Sertakan komponen-komponen utama (pengguna, Mikrotik, RADIUS Server, MFA Server/Provider).
2.  Jelaskan alur langkah demi langkah ketika seorang pengguna mencoba login ke Mikrotik yang terintegrasi dengan RADIUS dan MFA.
3.  Sebutkan minimal 2 (dua) tantangan teknis yang mungkin muncul saat mengimplementasikan integrasi MFA dengan RADIUS.
4.  Bagaimana integrasi MFA dapat meningkatkan keamanan sistem autentikasi terpusat yang sudah ada?
5.  Diskusikan: Jika kamu adalah administrator jaringan, apakah kamu akan mewajibkan MFA untuk semua akses ke perangkat jaringan? Jelaskan alasannya.

**Pertanyaan Refleksi**:
1.  Apa perbedaan utama antara MFA yang berdiri sendiri dan MFA yang terintegrasi dengan RADIUS?
2.  Bagaimana pemahaman tentang arsitektur ini membantumu melihat keamanan sebagai sistem yang berlapis?

---

### LKPD Pertemuan 8: Konsep IDS/IPS dan SIEM
**Tujuan Pembelajaran**: Menjelaskan konsep IDS/IPS, SIEM, dan Log Management.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang IDS/IPS, SIEM, dan Log Management.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan perbedaan antara Intrusion Detection System (IDS) dan Intrusion Prevention System (IPS). Berikan contoh kapan masing-masing digunakan.
2.  Apa itu SIEM (Security Information and Event Management)? Jelaskan fungsi-fungsi utamanya (koleksi, normalisasi, korelasi, analisis log).
3.  Sebutkan minimal 3 (tiga) sumber log yang berbeda dalam sebuah jaringan (misal: router, server, firewall) dan jenis informasi keamanan apa yang bisa didapatkan dari masing-masing log tersebut.
4.  Mengapa korelasi log dari berbagai sumber sangat penting dalam SIEM? Berikan contoh skenario.
5.  Diskusikan: Bagaimana SIEM dapat membantu tim keamanan dalam merespons insiden lebih cepat?

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar dalam mengelola dan menganalisis log dalam jumlah besar?
2.  Bagaimana SIEM dapat mengubah pendekatan keamanan dari reaktif menjadi proaktif?

---

### LKPD Pertemuan 9: Implementasi SIEM dengan Wazuh (Agent & Manager)
**Tujuan Pembelajaran**: Menginstal dan mengkonfigurasi Wazuh Manager dan Agent.

**Petunjuk Pengerjaan**:
1.  Pahami langkah-langkah instalasi Wazuh Manager dan Agent.
2.  Lakukan praktik instalasi dan konfigurasi pada VM Linux.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Siapkan sebuah VM Linux baru (misal: Ubuntu Server) untuk Wazuh Manager. Lampirkan *screenshot* setelah instalasi OS selesai.
2.  Lakukan instalasi Wazuh Manager (termasuk komponen Elastic Stack/OpenSearch) di VM tersebut. Lampirkan *screenshot* proses instalasi.
3.  Siapkan sebuah VM Linux lain (misal: VM klien/server) untuk Wazuh Agent. Lampirkan *screenshot* setelah instalasi OS selesai.
4.  Instal Wazuh Agent pada VM klien/server dan daftarkan ke Wazuh Manager. Lampirkan *screenshot* proses pendaftaran agent.
5.  Verifikasi bahwa agent telah terhubung ke manager dan statusnya aktif di dashboard Wazuh. Lampirkan *screenshot* dashboard yang menunjukkan agent aktif.

**Pertanyaan Refleksi**:
1.  Apa saja prasyarat sistem untuk menginstal Wazuh Manager?
2.  Apa peran utama Wazuh Agent dalam ekosistem Wazuh?

---

### LKPD Pertemuan 10: Analisis Log & Dashboard Wazuh
**Tujuan Pembelajaran**: Mengirim log dari Mikrotik & VM lain ke Wazuh dan menganalisis dashboard.

**Petunjuk Pengerjaan**:
1.  Pahami cara mengkonfigurasi pengiriman log ke Wazuh.
2.  Lakukan praktik pengiriman log dan analisis dashboard Wazuh.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Konfigurasi Mikrotik RouterOS untuk mengirim log ke Wazuh Manager menggunakan syslog. Lampirkan *screenshot* konfigurasi syslog di Mikrotik.
2.  Lakukan beberapa aktivitas di VM Linux yang memiliki Wazuh Agent (misal: login/logout, mencoba akses file yang tidak diizinkan).
3.  Akses dashboard Wazuh dan verifikasi bahwa log dari Mikrotik dan VM Linux telah masuk. Lampirkan *screenshot* log yang masuk.
4.  Gunakan fitur pencarian dan filter di dashboard Wazuh untuk mencari event keamanan tertentu (misal: login gagal, perubahan konfigurasi). Lampirkan *screenshot* hasil pencarian.
5.  Jelaskan bagaimana kamu akan menggunakan dashboard Wazuh untuk mendeteksi potensi serangan atau anomali dalam jaringan lab virtualmu.

**Pertanyaan Refleksi**:
1.  Apa manfaat utama dari memvisualisasikan log keamanan melalui dashboard seperti Wazuh?
2.  Bagaimana Wazuh dapat membantu dalam investigasi insiden keamanan?

---

### LKPD Pertemuan 11: Dasar-dasar Kriptografi & Fungsi Hash
**Tujuan Pembelajaran**: Memahami dasar-dasar kriptografi (simetris, asimetris) dan fungsi hash.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang kriptografi dan fungsi hash.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan perbedaan antara kriptografi simetris dan asimetris. Berikan contoh algoritma untuk masing-masing.
2.  Kapan kamu akan menggunakan kriptografi simetris dan kapan asimetris? Berikan contoh skenario.
3.  Apa itu fungsi hash? Sebutkan 3 (tiga) sifat penting dari fungsi hash yang baik.
4.  Sebutkan minimal 2 (dua) penggunaan fungsi hash dalam keamanan informasi.
5.  Diskusikan: Mengapa penting untuk tidak menyimpan password pengguna dalam bentuk plaintext di database? Bagaimana fungsi hash membantu mengatasi masalah ini?

**Pertanyaan Refleksi**:
1.  Bagaimana kriptografi melindungi kerahasiaan data?
2.  Bagaimana fungsi hash melindungi integritas data?

---

### LKPD Pertemuan 12: Konsep VPN & Praktik VPN Remote Access (PPTP/L2TP)
**Tujuan Pembelajaran**: Memahami konsep VPN dan mengimplementasikan VPN Remote Access (PPTP/L2TP) di Mikrotik.

**Petunjuk Pengerjaan**:
1.  Pahami konsep VPN dan protokolnya.
2.  Lakukan praktik konfigurasi VPN Remote Access di Mikrotik.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu Virtual Private Network (VPN) dan mengapa ia penting untuk komunikasi aman.
2.  Sebutkan perbedaan antara VPN Remote Access dan VPN Site-to-Site. Kapan masing-masing digunakan?
3.  Konfigurasi Mikrotik RouterOS sebagai VPN Server menggunakan protokol PPTP atau L2TP/IPsec. Lampirkan *screenshot* konfigurasi server.
4.  Buat sebuah pengguna VPN di Mikrotik. Lampirkan *screenshot* konfigurasi pengguna.
5.  Konfigurasi VPN Client di komputer host atau VM Linuxmu untuk terhubung ke VPN Server Mikrotik. Lakukan pengujian konektivitas ke jaringan internal Mikrotik melalui VPN. Lampirkan *screenshot* hasil koneksi VPN dan pengujian konektivitas.

**Pertanyaan Refleksi**:
1.  Apa manfaat keamanan utama dari menggunakan VPN untuk akses jarak jauh?
2.  Apa saja risiko keamanan yang perlu dipertimbangkan saat mengimplementasikan VPN?

---

### LKPD Pertemuan 13: Penjelasan dan Perencanaan Proyek
**Tujuan Pembelajaran**: Memahami spesifikasi proyek dan merencanakan pengerjaan dalam kelompok.

**Petunjuk Pengerjaan**:
1.  Pahami spesifikasi proyek mini semester 2.
2.  Diskusikan dalam kelompok untuk menyusun rencana kerja proyek.
3.  Isi bagian-bagian di bawah ini sebagai bagian dari perencanaan proyekmu.

**Kegiatan/Tugas**:
1.  **Spesifikasi Proyek**:
    *   Tuliskan kembali tujuan utama dari proyek mini semester 2 ini.
    *   Sebutkan minimal 3 (tiga) komponen utama yang harus ada dalam jaringan lab virtualmu (misal: Mikrotik, FreeRADIUS, Wazuh Manager, Wazuh Agent).
    *   Sebutkan minimal 3 (tiga) integrasi atau fungsionalitas keamanan yang wajib diimplementasikan (misal: autentikasi Mikrotik via RADIUS, pengiriman log Mikrotik ke Wazuh, deteksi anomali di Wazuh).
2.  **Pembagian Tugas Kelompok**:
    *   Sebutkan nama anggota kelompokmu dan peran/tanggung jawab masing-masing dalam proyek ini.
3.  **Desain Topologi Jaringan**:
    *   Gambarkan diagram topologi jaringan lab virtual yang akan kamu bangun. Sertakan:
        *   Semua VM (Mikrotik, FreeRADIUS Server, Wazuh Manager, Wazuh Agent).
        *   Koneksi jaringan (NAT, Host-only).
        *   Alokasi IP Address untuk setiap interface.
        *   Arah aliran log dan autentikasi.
4.  **Rencana Implementasi Keamanan**:
    *   Jelaskan secara singkat strategi keamanan yang akan kamu terapkan berdasarkan prinsip yang sudah dipelajari (AAA, SIEM, Kriptografi).
    *   Sebutkan langkah-langkah utama yang akan kamu lakukan untuk mengimplementasikan integrasi RADIUS dan Wazuh.
5.  **Timeline Proyek**:
    *   Buatlah jadwal singkat pengerjaan proyek dari sekarang hingga presentasi.

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar yang kamu antisipasi dalam proyek ini dan bagaimana kelompokmu berencana mengatasinya?
2.  Bagaimana kolaborasi dalam tim dapat membantumu menyelesaikan proyek ini dengan lebih baik?

---

### LKPD Pertemuan 14: Pengerjaan Proyek (Implementasi)
**Tujuan Pembelajaran**: Mengimplementasikan konfigurasi dasar proyek sesuai rencana.

**Petunjuk Pengerjaan**:
1.  Ikuti rencana kerja proyek yang telah disusun.
2.  Lakukan implementasi konfigurasi sistem autentikasi terpusat dan monitoring keamanan.
3.  Catat setiap progres dan kendala yang dihadapi.

**Kegiatan/Tugas**:
1.  **Progres Implementasi**:
    *   Jelaskan bagian mana dari topologi jaringan yang sudah berhasil kamu bangun hari ini (misal: instalasi FreeRADIUS, instalasi Wazuh Manager/Agent).
    *   Integrasi atau konfigurasi apa saja yang sudah berhasil kamu implementasikan (misal: Mikrotik sebagai RADIUS client, pengiriman log Mikrotik ke Wazuh)?
    *   Lampirkan *screenshot* dari konfigurasi penting yang sudah berhasil.
2.  **Kendala & Solusi**:
    *   Apakah ada kendala teknis atau non-teknis yang kamu hadapi hari ini? Jelaskan.
    *   Bagaimana kelompokmu mencoba mengatasi kendala tersebut?
3.  **Pengujian Awal**:
    *   Lakukan pengujian dasar (misal: login Mikrotik via RADIUS, verifikasi log masuk di Wazuh). Catat hasilnya.
4.  **Rencana Selanjutnya**:
    *   Apa yang akan menjadi fokus pengerjaan proyekmu di pertemuan berikutnya?

**Pertanyaan Refleksi**:
1.  Apa hal yang paling kamu pelajari dari proses troubleshooting hari ini?
2.  Bagaimana perasaanmu saat berhasil mengatasi kendala dalam proyek?

---

### LKPD Pertemuan 15: Finalisasi Proyek dan Penyusunan Laporan
**Tujuan Pembelajaran**: Menyelesaikan proyek dan menyusun laporan/dokumentasi teknis.

**Petunjuk Pengerjaan**:
1.  Selesaikan semua konfigurasi proyek.
2.  Susun laporan teknis proyek sesuai format yang ditentukan.
3.  Pastikan semua anggota kelompok memahami isi laporan.

**Kegiatan/Tugas**:
1.  **Finalisasi Konfigurasi**:
    *   Daftar semua konfigurasi yang telah diselesaikan hari ini untuk memastikan proyek berfungsi penuh (misal: semua log masuk ke Wazuh, autentikasi RADIUS berfungsi).
    *   Lakukan pengujian menyeluruh terhadap sistem autentikasi dan monitoring. Catat hasilnya.
2.  **Penyusunan Laporan Teknis**:
    *   Sertakan diagram topologi jaringan final dengan semua detail (IP address, mode jaringan, aliran data).
    *   Lampirkan konfigurasi penting (FreeRADIUS, Wazuh, Mikrotik RADIUS client, syslog).
    *   Sertakan *screenshot* dari hasil pengujian fungsionalitas dan keamanan (misal: login via RADIUS, deteksi anomali di Wazuh).
    *   Tuliskan kesimpulan singkat tentang proyekmu, termasuk analisis keamanan dari sistem yang dibangun.
3.  **Persiapan Presentasi**:
    *   Bagaimana kelompokmu akan membagi tugas presentasi?
    *   Poin-poin penting apa yang akan ditekankan dalam presentasi?

**Pertanyaan Refleksi**:
1.  Apa bagian tersulit dalam menyusun laporan teknis dan mengapa?
2.  Bagaimana proses dokumentasi ini membantumu memahami proyek secara lebih mendalam?

---

### LKPD Pertemuan 16: Presentasi Proyek dan Evaluasi Semester
**Tujuan Pembelajaran**: Mempresentasikan dan mendemonstrasikan hasil proyek.

**Petunjuk Pengerjaan**:
1.  Presentasikan laporan teknis dan demonstrasikan proyekmu di depan kelas.
2.  Berikan umpan balik konstruktif kepada kelompok lain.
3.  Lakukan refleksi akhir semester.

**Kegiatan/Tugas**:
1.  **Presentasi Proyek**:
    *   Sajikan laporan teknis proyekmu secara jelas dan ringkas.
    *   Demonstrasikan fungsionalitas sistem autentikasi terpusat dan monitoring keamanan yang telah kamu bangun.
    *   Jawab pertanyaan dari guru dan teman-teman dengan percaya diri.
2.  **Umpan Balik**:
    *   Berikan umpan balik positif dan area pengembangan untuk presentasi kelompok lain.
3.  **Evaluasi Diri Proyek**:
    *   Apa hal yang paling kamu banggakan dari proyek ini?
    *   Apa tantangan terbesar yang berhasil kamu atasi selama proyek?
    *   Jika kamu bisa mengulang proyek ini, apa yang akan kamu lakukan secara berbeda?
4.  **Refleksi Akhir Semester**:
    *   Apa pelajaran terbesar yang kamu dapatkan dari mata pelajaran Sistem Keamanan Jaringan semester ini?
    *   Bagaimana pengetahuan dan keterampilan yang kamu peroleh akan membantumu di masa depan?

**Pertanyaan Refleksi**:
1.  Bagaimana perasaanmu setelah berhasil menyelesaikan dan mempresentasikan proyek ini?
2.  Apa yang akan kamu lakukan untuk terus mengembangkan keterampilan keamanan jaringanmu di masa depan?

## LAMPIRAN - INSTRUMEN ASESMEN

Instrumen asesmen ini digunakan untuk mengukur pencapaian tujuan pembelajaran peserta didik sepanjang semester, mencakup aspek pengetahuan, keterampilan, dan sikap. Asesmen dilakukan secara formatif dan sumatif.

### 1. Observasi (Pengamatan)

*   **Tujuan**: Menilai partisipasi aktif, sikap kolaboratif, kemandirian, dan etika selama proses pembelajaran dan praktik. Observasi ini dilakukan secara berkelanjutan untuk mendapatkan gambaran holistik tentang perkembangan peserta didik.
*   **Waktu Pelaksanaan**: Sepanjang kegiatan inti, diskusi, sesi praktik, dan presentasi di setiap pertemuan. Guru dapat menggunakan lembar observasi atau catatan anekdot.
*   **Fokus Pengamatan**:
    *   **Keaktifan dalam Diskusi Kelompok dan Kelas**: Seberapa sering peserta didik mengajukan pertanyaan, menjawab, memberikan ide, atau menanggapi pendapat teman.
    *   **Kemampuan Bekerja Sama dalam Tim**: Peran peserta didik dalam kelompok, kemampuan mendengarkan, berbagi tugas, menyelesaikan konflik, dan mendukung anggota tim.
    *   **Sikap Proaktif dalam Memecahkan Masalah (Troubleshooting)**: Inisiatif peserta didik dalam mengidentifikasi masalah, mencari solusi (mandiri atau bertanya secara efektif), dan tidak mudah menyerah saat menghadapi kendala teknis.
    *   **Kepatuhan terhadap Etika dan Prosedur Keamanan**: Pemahaman dan penerapan etika siber (misal: *responsible disclosure*, tidak melakukan akses ilegal), serta kepatuhan terhadap prosedur praktik (misal: backup data sebelum konfigurasi, penggunaan lingkungan virtual yang terisolasi).
    *   **Kemampuan Mengikuti Instruksi Praktik dengan Teliti**: Akurasi dalam menjalankan langkah-langkah praktikum, perhatian terhadap detail, dan kemampuan untuk mereplikasi hasil yang diharapkan.
*   **Rubrik Observasi (Contoh)**:
    | Aspek yang Dinilai | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
    |---|---|---|---|---|
    | **Partisipasi Diskusi** | Sangat aktif, selalu mengajukan pertanyaan relevan, memberikan ide orisinal, dan memfasilitasi diskusi kelompok. | Aktif, sering mengajukan pertanyaan atau memberikan tanggapan yang relevan, berkontribusi pada diskusi. | Cukup aktif, kadang-kadang mengajukan pertanyaan atau memberikan tanggapan, perlu dorongan untuk berpartisipasi lebih. | Kurang aktif, jarang mengajukan pertanyaan atau memberikan tanggapan, cenderung pasif dalam diskusi. |
    | **Kerja Sama Tim** | Sangat kolaboratif, memimpin inisiatif kelompok, mendukung penuh anggota tim, dan efektif dalam pembagian tugas. | Kolaboratif, berkontribusi positif pada kelompok, mampu berbagi tugas dan mendengarkan pendapat orang lain. | Cukup kolaboratif, terkadang perlu diingatkan untuk bekerja sama, cenderung fokus pada tugas individu. | Kurang kolaboratif, kesulitan bekerja dalam tim, cenderung mendominasi atau pasif. |
    | **Kemandirian & Proaktif** | Sangat mandiri, proaktif mengidentifikasi masalah, mencari solusi inovatif, dan membantu teman yang kesulitan. | Mandiri, mencoba mencari solusi sendiri sebelum bertanya, menunjukkan inisiatif dalam praktik. | Cukup mandiri, sering membutuhkan bimbingan atau arahan, kurang inisiatif dalam memecahkan masalah. | Kurang mandiri, mudah menyerah saat menghadapi kendala, selalu menunggu instruksi. |
    | **Kepatuhan Etika & Prosedur** | Selalu patuh pada etika dan prosedur keamanan, menunjukkan kesadaran tinggi terhadap implikasi tindakan siber. | Patuh pada etika dan prosedur keamanan, memahami pentingnya aturan. | Cukup patuh, terkadang perlu diingatkan tentang etika atau prosedur tertentu. | Kurang patuh, sering mengabaikan etika atau prosedur keamanan, menunjukkan kurangnya kesadaran. |
    | **Ketelitian Praktik** | Sangat teliti, mengikuti setiap langkah instruksi dengan akurat, dan menghasilkan output yang sesuai harapan. | Teliti, mengikuti sebagian besar instruksi dengan akurat, output sesuai harapan. | Cukup teliti, beberapa langkah terlewat atau kurang akurat, output kurang sesuai harapan. | Kurang teliti, banyak kesalahan dalam mengikuti instruksi, output tidak sesuai harapan. |

### 2. Penilaian Kuis/Tes Singkat (Pre-test & Post-test Sederhana)

*   **Tujuan**: Mengukur pemahaman konsep dasar sebelum dan sesudah pembelajaran pada setiap pertemuan.
*   **Waktu Pelaksanaan**: Awal dan akhir setiap pertemuan (5-10 menit).
*   **Bentuk**: Pertanyaan lisan, polling cepat, atau tulisan singkat (exit ticket).
*   **Fokus Penilaian**: Pemahaman definisi, perbedaan konsep, identifikasi contoh.
*   **Rubrik Penilaian (Contoh)**:
    | Kriteria | Skor 2 (Benar & Lengkap) | Skor 1 (Benar, Kurang Lengkap) | Skor 0 (Salah/Tidak Menjawab) |
    |---|---|---|---|
    | Pemahaman Konsep | Menjelaskan konsep dengan tepat dan memberikan contoh relevan. | Menjelaskan konsep dengan cukup tepat, contoh kurang relevan/tidak ada. | Tidak memahami konsep atau jawaban salah. |
    | Identifikasi Perbedaan | Mampu membedakan konsep dengan jelas. | Mampu membedakan namun kurang detail. | Tidak mampu membedakan konsep. |

### 3. Penilaian LKPD/Tugas Harian

*   **Tujuan**: Menilai kemampuan peserta didik dalam menganalisis studi kasus, menerapkan konsep, dan mendokumentasikan hasil praktik.
*   **Waktu Pelaksanaan**: Selama kegiatan inti dan sebagai tugas mandiri/kelompok.
*   **Bentuk**: Jawaban tertulis pada LKPD, laporan singkat hasil riset/praktik.
*   **Fokus Penilaian**:
    *   Ketepatan analisis (studi kasus, skenario).
    *   Kesesuaian penerapan konsep (misal: konfigurasi RADIUS, Wazuh).
    *   Kelengkapan dan kejelasan dokumentasi (screenshot, topologi).
    *   Kemampuan menjawab pertanyaan refleksi.
*   **Rubrik Penilaian (Contoh)**:
    | Aspek yang Dinilai | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
    |---|---|---|---|---|
    | Ketepatan Analisis | Analisis sangat tepat, mendalam, dan relevan. | Analisis tepat dan relevan. | Analisis cukup tepat, kurang mendalam. | Analisis kurang tepat/tidak relevan. |
    | Penerapan Konsep | Menerapkan konsep dengan benar dan efektif. | Menerapkan konsep dengan benar. | Menerapkan konsep dengan beberapa kesalahan. | Kesulitan menerapkan konsep. |
    | Dokumentasi & Kelengkapan | Dokumentasi sangat jelas, lengkap, dan rapi. | Dokumentasi jelas dan lengkap. | Dokumentasi cukup jelas, ada bagian kurang lengkap. | Dokumentasi tidak jelas/tidak lengkap. |
    | Refleksi Diri | Refleksi mendalam, menunjukkan pemahaman diri. | Refleksi cukup baik. | Refleksi kurang mendalam. | Tidak ada refleksi/tidak relevan. |

### 4. Penilaian Proyek Mini Semester

*   **Tujuan**: Mengukur kemampuan peserta didik dalam mengintegrasikan seluruh pengetahuan dan keterampilan untuk membangun dan mengamankan jaringan lab virtual secara komprehensif.
*   **Waktu Pelaksanaan**: Akhir semester (Pertemuan 13-16).
*   **Bentuk**: Laporan teknis proyek, presentasi, dan demonstrasi fungsionalitas.
*   **Fokus Penilaian**:
    *   **Desain Topologi**: Kelengkapan dan kejelasan diagram topologi, alokasi IP, aliran data.
    *   **Implementasi Konfigurasi**: Ketepatan konfigurasi FreeRADIUS, Wazuh, Mikrotik, VPN.
    *   **Fungsionalitas**: Semua layanan dan integrasi berfungsi sesuai spesifikasi.
    *   **Analisis Keamanan**: Pemahaman terhadap risiko dan mitigasi yang diterapkan.
    *   **Dokumentasi Teknis**: Kualitas laporan (struktur, isi, kejelasan).
    *   **Presentasi & Demonstrasi**: Kemampuan presentasi, menjawab pertanyaan, dan mendemonstrasikan proyek.
*   **Rubrik Penilaian (Contoh)**:
    | Aspek yang Dinilai | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
    |---|---|---|---|---|
    | Desain Topologi | Sangat detail, logis, dan mudah dipahami. | Detail dan logis. | Cukup detail, ada bagian kurang jelas. | Kurang detail/tidak logis. |
    | Implementasi Konfigurasi | Semua konfigurasi tepat, efisien, dan berfungsi sempurna. | Konfigurasi tepat, berfungsi baik. | Konfigurasi ada kesalahan minor, berfungsi sebagian. | Banyak kesalahan konfigurasi, tidak berfungsi. |
    | Fungsionalitas Proyek | Semua fungsionalitas berjalan sempurna. | Sebagian besar fungsionalitas berjalan. | Beberapa fungsionalitas berjalan. | Fungsionalitas tidak berjalan. |
    | Analisis Keamanan | Analisis mendalam, mengidentifikasi risiko dan mitigasi. | Analisis cukup baik, mengidentifikasi risiko. | Analisis kurang mendalam. | Tidak ada analisis keamanan. |
    | Dokumentasi Teknis | Laporan sangat komprehensif, jelas, dan profesional. | Laporan komprehensif dan jelas. | Laporan cukup jelas, ada bagian kurang lengkap. | Laporan tidak jelas/tidak lengkap. |
    | Presentasi & Demonstrasi | Sangat percaya diri, jelas, dan demonstrasi lancar. | Percaya diri, jelas, demonstrasi cukup lancar. | Cukup percaya diri, kurang jelas, demonstrasi tersendat. | Tidak percaya diri, tidak jelas, demonstrasi gagal. |

## LAMPIRAN - MATERI PEMBELAJARAN LENGKAP

### MODUL 1: PRAKTIK ANALISIS JARINGAN

#### Pertemuan 1: Konsep Scanning & Nmap

**1. Konsep Scanning**

Scanning adalah proses pengumpulan informasi tentang target (host, jaringan, aplikasi) dengan mengirimkan permintaan dan menganalisis responsnya. Ini adalah fase awal dalam pengujian penetrasi dan audit keamanan.

*   **Port Scanning**:
    *   Tujuan: Mengidentifikasi port-port yang terbuka pada sebuah host. Port terbuka menunjukkan adanya layanan yang berjalan dan berpotensi menjadi titik masuk bagi penyerang.
    *   Jenis: TCP Connect Scan, SYN Scan (Stealth Scan), UDP Scan, dll.
*   **Host Discovery**:
    *   Tujuan: Mengidentifikasi host-host yang aktif dalam sebuah jaringan.
    *   Metode: Ping sweep (ICMP Echo Request), ARP scan, TCP/UDP ping.
*   **Service/Version Detection**:
    *   Tujuan: Mengidentifikasi jenis dan versi layanan yang berjalan pada port terbuka. Informasi ini penting untuk mencari kerentanan yang spesifik pada versi layanan tertentu.
*   **OS Detection**:
    *   Tujuan: Mengidentifikasi sistem operasi yang berjalan pada target. Informasi ini membantu penyerang memilih eksploitasi yang sesuai.

**2. Nmap (Network Mapper)**

Nmap adalah tool *open-source* yang sangat populer dan kuat untuk eksplorasi jaringan dan audit keamanan.

*   **Fungsi Utama Nmap**:
    *   **Host Discovery**: Menemukan host yang aktif di jaringan.
    *   **Port Scanning**: Mengidentifikasi port terbuka dan tertutup.
    *   **Service/Version Detection**: Menentukan aplikasi dan versi yang berjalan pada port.
    *   **OS Detection**: Mengidentifikasi sistem operasi target.
    *   **Nmap Scripting Engine (NSE)**: Memungkinkan otomatisasi berbagai tugas, seperti deteksi kerentanan, brute-force, dan eksploitasi sederhana.

*   **Contoh Perintah Nmap Dasar**:
    *   `nmap [target]` : Melakukan scan default (SYN scan pada 1000 port populer).
    *   `nmap -sP [target]` atau `nmap -sn [target]` : Ping scan (host discovery saja, tanpa port scan).
    *   `nmap -p 1-65535 [target]` : Scan semua port.
    *   `nmap -sV [target]` : Service/version detection.
    *   `nmap -O [target]` : OS detection.
    *   `nmap -A [target]` : Agresif scan (mencakup OS detection, version detection, script scanning, dan traceroute).

#### Pertemuan 2: Analisis Lalu Lintas Jaringan & Wireshark

**1. Konsep Packet Sniffing**

Packet sniffing (atau packet analysis) adalah proses menangkap dan menganalisis paket data yang mengalir melalui jaringan. Ini memungkinkan analis keamanan untuk melihat komunikasi yang terjadi secara detail.

*   **Tujuan Packet Sniffing**:
    *   **Troubleshooting Jaringan**: Mengidentifikasi masalah konektivitas, latensi, atau konfigurasi.
    *   **Analisis Keamanan**: Mendeteksi aktivitas mencurigakan, serangan, atau kebocoran informasi sensitif (misal: password plaintext).
    *   **Pengembangan Aplikasi**: Memahami bagaimana aplikasi berkomunikasi di jaringan.

**2. Wireshark**

Wireshark adalah *network protocol analyzer* *open-source* yang paling banyak digunakan di dunia. Ia memungkinkan pengguna untuk menangkap dan menganalisis lalu lintas jaringan secara interaktif.

*   **Fungsi Utama Wireshark**:
    *   **Packet Capture**: Menangkap paket data secara *real-time* dari interface jaringan.
    *   **Display Filters**: Memungkinkan pengguna untuk menyaring dan menampilkan hanya paket yang relevan berdasarkan protokol, alamat IP, port, dll.
    *   **Protocol Dissection**: Menganalisis dan menampilkan detail setiap lapisan protokol (Ethernet, IP, TCP, HTTP, dll.).
    *   **Follow TCP Stream**: Membangun kembali percakapan TCP untuk melihat data yang ditransfer.
    *   **Export Objects**: Mengekstrak file atau objek yang ditransfer melalui protokol tertentu.

*   **Contoh Penggunaan Wireshark**:
    *   **Capture Filter (saat memulai capture)**:
        *   `host 192.168.1.100` : Hanya menangkap lalu lintas yang melibatkan IP 192.168.1.100.
        *   `port 80` : Hanya menangkap lalu lintas pada port 80.
    *   **Display Filter (setelah capture)**:
        *   `http` : Menampilkan semua lalu lintas HTTP.
        *   `ip.addr == 192.168.1.100 && tcp.port == 22` : Menampilkan lalu lintas TCP antara IP tersebut pada port 22.
        *   `http.request.method == "POST"` : Menampilkan hanya permintaan HTTP POST.
        *   `contains "password"` : Mencari paket yang berisi string "password".

### MODUL 2: SISTEM AUTENTIKASI TERPUSAT (PaaS)

#### Pertemuan 3: Konsep AAA & Protokol RADIUS

**1. Konsep AAA (Authentication, Authorization, Accounting)**

AAA adalah kerangka kerja fundamental dalam manajemen akses dan keamanan jaringan.

*   **Authentication (Autentikasi)**:
    *   Tujuan: Memverifikasi identitas pengguna. Menjawab pertanyaan "Siapa Anda?".
    *   Metode: Username/password, sertifikat digital, biometrik, token.
*   **Authorization (Otorisasi)**:
    *   Tujuan: Menentukan hak akses atau izin yang dimiliki pengguna yang telah terautentikasi. Menjawab pertanyaan "Apa yang boleh Anda lakukan?".
    *   Metode: Hak akses berbasis peran (Role-Based Access Control - RBAC), daftar kontrol akses (Access Control List - ACL).
*   **Accounting (Akuntansi)**:
    *   Tujuan: Melacak aktivitas pengguna (apa yang mereka lakukan, kapan, berapa lama, berapa banyak sumber daya yang digunakan). Penting untuk audit, penagihan, dan forensik.
    *   Metode: Pencatatan log, data penggunaan.

**2. Protokol RADIUS (Remote Authentication Dial-In User Service)**

RADIUS adalah protokol jaringan client/server yang menyediakan layanan AAA terpusat untuk pengguna yang terhubung ke jaringan.

*   **Fungsi Utama RADIUS**:
    *   **Autentikasi Terpusat**: Mengelola kredensial pengguna di satu lokasi (RADIUS Server) daripada di setiap perangkat jaringan.
    *   **Otorisasi**: Memberikan hak akses tertentu kepada pengguna berdasarkan kebijakan yang dikelola di server.
    *   **Akuntansi**: Mencatat sesi pengguna (waktu login/logout, data yang ditransfer).

*   **Komponen RADIUS**:
    *   **RADIUS Client (Network Access Server - NAS)**: Perangkat jaringan (misal: router Mikrotik, switch, access point Wi-Fi, VPN server) yang menerima permintaan koneksi dari pengguna dan meneruskannya ke RADIUS Server untuk autentikasi.
    *   **RADIUS Server**: Server yang menyimpan database pengguna dan kebijakan akses. Ia memproses permintaan autentikasi dari klien dan mengirimkan respons (Access-Accept, Access-Reject, Access-Challenge).

*   **Alur Komunikasi Sederhana (Autentikasi)**:
    1.  Pengguna mencoba terhubung ke RADIUS Client (misal: login ke Mikrotik).
    2.  RADIUS Client mengirimkan permintaan Access-Request (berisi username, password terenkripsi, IP klien) ke RADIUS Server.
    3.  RADIUS Server memverifikasi kredensial pengguna.
    4.  Jika kredensial valid, Server mengirimkan Access-Accept ke Client. Jika tidak, Access-Reject.
    5.  Client mengizinkan atau menolak akses pengguna berdasarkan respons dari Server.

#### Pertemuan 4: Implementasi FreeRADIUS Server

**1. FreeRADIUS**

FreeRADIUS adalah implementasi *open-source* yang paling populer dari protokol RADIUS. Ia berjalan di sistem operasi mirip Unix (seperti Linux) dan sangat fleksibel serta dapat diperluas.

*   **Fitur Utama FreeRADIUS**:
    *   Mendukung berbagai metode autentikasi (PAP, CHAP, EAP, dll.).
    *   Dapat terintegrasi dengan berbagai backend database (SQL, LDAP, flat files).
    *   Mendukung otorisasi berbasis atribut.
    *   Modul yang dapat diperluas untuk fungsionalitas tambahan.

*   **Langkah-langkah Instalasi Dasar FreeRADIUS di Ubuntu/Debian**:
    1.  **Update Sistem**: `sudo apt update && sudo apt upgrade -y`
    2.  **Instal FreeRADIUS**: `sudo apt install freeradius freeradius-utils -y`
    3.  **Konfigurasi Klien (NAS)**: Edit file `/etc/freeradius/3.0/clients.conf` untuk menambahkan perangkat yang akan menjadi RADIUS Client (misal: Mikrotik).
        ```
        client mikrotik_router {
            ipaddr = 192.168.88.1  # IP Mikrotik
            secret = testing123   # Shared secret, harus sama dengan di Mikrotik
            require_message_authenticator = yes
            nas_type = other
        }
        ```
    4.  **Konfigurasi Pengguna**: Edit file `/etc/freeradius/3.0/users` untuk menambahkan pengguna lokal.
        ```
        user1 Auth-Type := Local, User-Password == "password123"
            Reply-Message = "Hello, user1!"

        user2 Auth-Type := Local, User-Password == "password456"
            Reply-Message = "Welcome, user2!"
        ```
    5.  **Restart Layanan**: `sudo systemctl restart freeradius`
    6.  **Uji dari Server**: Gunakan `radtest` untuk menguji autentikasi dari server itu sendiri.
        `radtest user1 password123 127.0.0.1 0 testing123`

#### Pertemuan 5: Integrasi Mikrotik sebagai RADIUS Client

**1. Konfigurasi Mikrotik sebagai RADIUS Client**

Mikrotik RouterOS dapat dikonfigurasi untuk menggunakan RADIUS Server eksternal untuk autentikasi berbagai layanan, seperti login router, hotspot, PPP, dan VPN.

*   **Langkah-langkah Konfigurasi di Mikrotik (WinBox/CLI)**:
    1.  **Tambahkan RADIUS Server**:
        *   CLI: `/radius add service=login address=192.168.88.20 secret=testing123 timeout=3000ms`
            (Ganti `192.168.88.20` dengan IP FreeRADIUS Server Anda, dan `testing123` dengan *shared secret* yang sama).
        *   WinBox: `IP -> RADIUS -> Add`
            *   Centang `login` di `Service`
            *   Isi `Address` dengan IP FreeRADIUS Server
            *   Isi `Secret` dengan *shared secret*
    2.  **Konfigurasi Autentikasi Login (untuk WinBox/SSH)**:
        *   CLI: `/system login add authentication=radius`
        *   WinBox: `System -> Users -> AAA` tab
            *   Centang `Use RADIUS`
            *   Pilih `login` di `Default Authentication` (jika ada opsi)
    3.  **Pastikan Urutan Autentikasi**: Secara default, Mikrotik akan mencoba autentikasi lokal terlebih dahulu, lalu RADIUS. Anda bisa mengubah urutan ini di `System -> Users -> AAA` atau `/system login`. Untuk tujuan lab, pastikan RADIUS diaktifkan.

*   **Pengujian Autentikasi**:
    *   Coba login ke Mikrotik (via WinBox atau SSH) menggunakan username dan password yang telah Anda buat di FreeRADIUS Server.
    *   Jika berhasil, ini menunjukkan bahwa Mikrotik berhasil berkomunikasi dengan FreeRADIUS Server dan memverifikasi kredensial pengguna.
    *   Periksa log di Mikrotik (`/log print`) dan di FreeRADIUS Server (`sudo tail -f /var/log/freeradius/freeradius.log`) untuk melihat proses autentikasi.

### MODUL 3: MANAJEMEN AKSES LANJUTAN

#### Pertemuan 6: Konsep Multi-Factor Authentication (MFA)

**1. Multi-Factor Authentication (MFA)**

MFA adalah metode autentikasi yang mengharuskan pengguna untuk memberikan dua atau lebih faktor verifikasi yang berbeda dari kategori yang berbeda untuk mendapatkan akses ke akun atau sistem. Ini secara signifikan meningkatkan keamanan dibandingkan hanya menggunakan password.

*   **Tiga Kategori Faktor Autentikasi**:
    *   **Something You Know (Sesuatu yang Anda Ketahui)**: Informasi yang hanya diketahui oleh pengguna.
        *   Contoh: Password, PIN, jawaban pertanyaan keamanan.
    *   **Something You Have (Sesuatu yang Anda Miliki)**: Objek fisik yang hanya dimiliki oleh pengguna.
        *   Contoh: Smartphone (untuk OTP via SMS/aplikasi), hardware token (YubiKey), kartu pintar.
    *   **Something You Are (Sesuatu yang Melekat pada Diri Anda)**: Karakteristik biometrik unik pengguna.
        *   Contoh: Sidik jari, pemindaian wajah, pemindaian retina, suara.

*   **Mengapa MFA Penting?**:
    *   **Meningkatkan Keamanan**: Jika satu faktor dikompromikan (misal: password dicuri), penyerang masih memerlukan faktor kedua untuk mendapatkan akses.
    *   **Melindungi dari Serangan Umum**: Efektif melawan serangan phishing, brute-force, dan credential stuffing.

*   **Jenis-jenis MFA Populer**:
    *   **OTP (One-Time Password)**: Kode unik yang berlaku hanya untuk satu sesi login.
        *   Via SMS: Kode dikirim ke nomor telepon terdaftar.
        *   Via Authenticator App (TOTP): Aplikasi seperti Google Authenticator atau Authy menghasilkan kode yang berubah setiap 30-60 detik.
    *   **Biometrik**: Menggunakan karakteristik fisik unik (sidik jari, wajah).
    *   **Hardware Token**: Perangkat fisik kecil yang menghasilkan kode atau memerlukan sentuhan untuk autentikasi.
    *   **Push Notification**: Notifikasi dikirim ke perangkat terdaftar, pengguna cukup menyetujui login.

#### Pertemuan 7: Konsep Integrasi MFA via RADIUS (Konseptual)

**1. Integrasi MFA dengan RADIUS**

Meskipun RADIUS secara native tidak mendukung MFA yang kompleks, ia dapat diintegrasikan dengan solusi MFA eksternal untuk menyediakan lapisan keamanan tambahan.

*   **Arsitektur Konseptual**:
    1.  **Pengguna**: Memulai permintaan autentikasi (misal: login ke VPN Mikrotik).
    2.  **RADIUS Client (Mikrotik)**: Menerima kredensial pertama (misal: username/password) dan meneruskannya ke RADIUS Server.
    3.  **RADIUS Server (FreeRADIUS)**:
        *   Menerima permintaan dari klien.
        *   Dikonfigurasi untuk berinteraksi dengan **MFA Server/Provider** eksternal.
        *   Jika password pertama valid, RADIUS Server mengirimkan Access-Challenge kembali ke klien, meminta faktor kedua (misal: OTP).
        *   Atau, RADIUS Server dapat meneruskan permintaan autentikasi ke MFA Server, yang kemudian menangani verifikasi faktor kedua.
    4.  **MFA Server/Provider**:
        *   Memverifikasi faktor kedua (misal: OTP yang dimasukkan pengguna, atau menerima push notification dari aplikasi).
        *   Mengirimkan hasil verifikasi kembali ke RADIUS Server.
    5.  **RADIUS Server (lanjutan)**:
        *   Jika faktor kedua valid, RADIUS Server mengirimkan Access-Accept ke RADIUS Client.
        *   Jika tidak valid, Access-Reject.
    6.  **RADIUS Client (Mikrotik)**: Mengizinkan atau menolak akses pengguna berdasarkan respons akhir dari RADIUS Server.

*   **Tantangan Implementasi**:
    *   **Kompleksitas Konfigurasi**: Membutuhkan pemahaman mendalam tentang RADIUS dan solusi MFA yang digunakan.
    *   **Kompatibilitas Protokol**: Memastikan RADIUS Server dapat berkomunikasi dengan MFA Server (misal: melalui API, atau modul khusus).
    *   **Pengalaman Pengguna**: Menyeimbangkan keamanan dengan kemudahan penggunaan.
    *   **Skalabilitas**: Memastikan sistem dapat menangani banyak pengguna dan permintaan autentikasi.

### MODUL 4: DETEKSI INTRUSI & ANALISIS LOG (SIEM)

#### Pertemuan 8: Konsep IDS/IPS dan SIEM

**1. IDS (Intrusion Detection System) & IPS (Intrusion Prevention System)**

*   **IDS (Intrusion Detection System)**:
    *   Tujuan: Mendeteksi aktivitas mencurigakan atau serangan di jaringan atau host.
    *   Fungsi: Memantau lalu lintas jaringan atau log sistem, membandingkannya dengan *signature* serangan yang diketahui atau perilaku normal, dan menghasilkan *alert* jika ada anomali.
    *   Sifat: Pasif (hanya mendeteksi dan memberi peringatan, tidak menghentikan serangan).
    *   Jenis:
        *   **NIDS (Network-based IDS)**: Memantau lalu lintas jaringan secara keseluruhan.
        *   **HIDS (Host-based IDS)**: Memantau aktivitas pada satu host (file system, log, proses).
*   **IPS (Intrusion Prevention System)**:
    *   Tujuan: Mendeteksi dan secara aktif mencegah serangan.
    *   Fungsi: Mirip dengan IDS, tetapi memiliki kemampuan untuk memblokir atau menghentikan lalu lintas berbahaya secara *real-time*.
    *   Sifat: Aktif (mendeteksi dan mencegah).
    *   Jenis: NIPS (Network-based IPS), HIPS (Host-based IPS).

**2. SIEM (Security Information and Event Management)**

SIEM adalah solusi perangkat lunak yang mengumpulkan, menganalisis, dan menyajikan data keamanan dari berbagai sumber dalam satu platform terpusat.

*   **Fungsi Utama SIEM**:
    *   **Log Collection**: Mengumpulkan log dari berbagai perangkat (firewall, router, server, aplikasi, IDS/IPS).
    *   **Log Normalization**: Mengubah format log yang berbeda menjadi format standar agar mudah dianalisis.
    *   **Log Correlation**: Mengidentifikasi hubungan antara event-event yang tampaknya tidak terkait dari berbagai sumber untuk mendeteksi pola serangan yang kompleks.
    *   **Alerting**: Menghasilkan peringatan otomatis ketika pola serangan atau anomali terdeteksi.
    *   **Dashboarding & Reporting**: Menyediakan visualisasi data keamanan dan laporan untuk analisis dan kepatuhan.
    *   **Forensic Analysis**: Membantu dalam investigasi insiden keamanan dengan menyediakan data log yang terorganisir.

*   **Manfaat SIEM**:
    *   **Visibilitas Keamanan Menyeluruh**: Pandangan terpusat terhadap seluruh aktivitas keamanan.
    *   **Deteksi Ancaman Dini**: Mengidentifikasi serangan yang kompleks yang mungkin terlewat oleh alat keamanan individual.
    *   **Kepatuhan Regulasi**: Membantu memenuhi persyaratan audit dan kepatuhan.
    *   **Respon Insiden yang Lebih Cepat**: Mempercepat waktu deteksi dan respon terhadap insiden.

#### Pertemuan 9: Implementasi SIEM dengan Wazuh (Agent & Manager)

**1. Wazuh**

Wazuh adalah platform keamanan *open-source* yang komprehensif untuk deteksi ancaman, pemantauan integritas, respons insiden, dan kepatuhan. Ini adalah solusi HIDS (Host-based IDS) yang kuat dengan kemampuan SIEM.

*   **Komponen Utama Wazuh**:
    *   **Wazuh Agent**: Diinstal pada host yang ingin dipantau (server, workstation, VM). Mengumpulkan data log, memantau integritas file, mendeteksi kerentanan, dan mengirimkannya ke Wazuh Manager.
    *   **Wazuh Manager**: Server pusat yang menerima data dari agent, menganalisisnya, mengkorelasikannya, dan menghasilkan peringatan.
    *   **Elastic Stack (Elasticsearch, Kibana/OpenSearch Dashboards)**: Digunakan untuk penyimpanan data log, indeksing, pencarian, dan visualisasi (dashboard).

*   **Langkah-langkah Instalasi Dasar (Ringkasan)**:
    1.  **Instalasi Wazuh Manager**:
        *   Siapkan VM Linux (misal: Ubuntu Server) dengan spesifikasi yang cukup.
        *   Instal Wazuh Manager, OpenSearch, dan OpenSearch Dashboards (atau Elasticsearch dan Kibana jika versi lama). Ikuti panduan resmi Wazuh.
        *   Pastikan semua layanan berjalan dan dashboard dapat diakses.
    2.  **Instalasi Wazuh Agent**:
        *   Pada VM yang ingin dipantau (misal: VM Linux klien/server), instal Wazuh Agent.
        *   Daftarkan agent ke Wazuh Manager menggunakan kunci pendaftaran atau metode autentikasi lainnya.
        *   Pastikan agent terhubung dan aktif di dashboard Wazuh.

#### Pertemuan 10: Analisis Log & Dashboard Wazuh

**1. Pengiriman Log ke Wazuh**

Wazuh Agent secara otomatis mengumpulkan log dari host tempat ia diinstal. Untuk perangkat jaringan seperti Mikrotik, log dapat dikirim ke Wazuh Manager menggunakan protokol Syslog.

*   **Konfigurasi Syslog di Mikrotik**:
    *   Mikrotik dapat dikonfigurasi untuk mengirim log ke server Syslog eksternal (Wazuh Manager).
    *   CLI: `/system logging action add name=remote_wazuh remote=192.168.X.Y remote-port=514 protocol=udp`
        `/system logging add topics=info,error,debug,critical action=remote_wazuh`
        (Ganti `192.168.X.Y` dengan IP Wazuh Manager Anda).
    *   Pastikan port Syslog (UDP 514) terbuka di firewall Wazuh Manager.

**2. Analisis Dashboard Wazuh**

Setelah log terkumpul di Wazuh Manager dan diindeks oleh OpenSearch, Anda dapat menganalisisnya melalui OpenSearch Dashboards (atau Kibana).

*   **Fitur Dashboard Penting**:
    *   **Discover**: Melihat semua log mentah yang masuk, mencari, dan memfilter event.
    *   **Alerts**: Melihat peringatan keamanan yang dihasilkan oleh Wazuh berdasarkan aturan deteksi.
    *   **Agents**: Melihat status dan informasi tentang semua agent yang terhubung.
    *   **Modules**: Melihat data yang dikumpulkan oleh berbagai modul Wazuh (misal: pemantauan integritas file, deteksi kerentanan).
    *   **Dashboards**: Visualisasi data keamanan dalam bentuk grafik, tabel, dan metrik.

*   **Contoh Analisis**:
    *   Mencari "authentication failed" untuk mendeteksi upaya brute-force.
    *   Melihat perubahan pada file sistem penting (pemantauan integritas file).
    *   Mendeteksi kerentanan pada software yang terinstal di agent.
    *   Mengkorelasikan event login dari Mikrotik dengan aktivitas di VM Linux.

### MODUL 5: ENKRIPSI & KOMUNIKASI AMAN

#### Pertemuan 11: Dasar-dasar Kriptografi & Fungsi Hash

**1. Dasar-dasar Kriptografi**

Kriptografi adalah ilmu dan seni menyembunyikan informasi (enkripsi) dan mengungkapkannya kembali (dekripsi) agar hanya pihak yang berwenang yang dapat mengaksesnya.

*   **Enkripsi Simetris (Symmetric-key Cryptography)**:
    *   Deskripsi: Menggunakan kunci yang sama untuk proses enkripsi dan dekripsi. Kunci ini harus dijaga kerahasiaannya dan dibagikan secara aman antara pengirim dan penerima.
    *   Contoh Algoritma: AES (Advanced Encryption Standard), DES (Data Encryption Standard), Triple DES.
    *   Kelebihan: Cepat dan efisien untuk mengenkripsi data dalam jumlah besar.
    *   Kekurangan: Masalah distribusi kunci (bagaimana membagikan kunci secara aman?).
*   **Enkripsi Asimetris (Asymmetric-key Cryptography / Public-key Cryptography)**:
    *   Deskripsi: Menggunakan sepasang kunci yang saling terkait: kunci publik (dapat dibagikan secara luas) dan kunci privat (harus dijaga kerahasiaannya oleh pemiliknya). Data yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat yang sesuai, dan sebaliknya.
    *   Contoh Algoritma: RSA, ECC (Elliptic Curve Cryptography).
    *   Kelebihan: Mengatasi masalah distribusi kunci, memungkinkan tanda tangan digital dan pertukaran kunci yang aman.
    *   Kekurangan: Lebih lambat daripada enkripsi simetris, tidak cocok untuk mengenkripsi data dalam jumlah besar.

**2. Fungsi Hash (Cryptographic Hash Function)**

Fungsi hash adalah algoritma matematika yang mengambil input (data) dengan ukuran berapa pun dan menghasilkan output (hash value/digest) dengan ukuran tetap.

*   **Sifat Penting Fungsi Hash yang Baik**:
    *   **One-Way (Satu Arah)**: Sangat sulit (secara komputasi tidak mungkin) untuk merekonstruksi input asli dari hash value.
    *   **Deterministic**: Input yang sama akan selalu menghasilkan output hash yang sama.
    *   **Collision Resistance**: Sangat sulit untuk menemukan dua input berbeda yang menghasilkan hash value yang sama (collision).
    *   **Avalanche Effect**: Perubahan kecil pada input akan menghasilkan perubahan besar pada output hash.

*   **Penggunaan Fungsi Hash dalam Keamanan**:
    *   **Integritas Data**: Memverifikasi bahwa data tidak diubah. Jika hash dari data asli cocok dengan hash dari data yang diterima, maka data tersebut utuh.
    *   **Penyimpanan Password**: Password tidak disimpan dalam bentuk plaintext, melainkan hash-nya. Saat login, password yang dimasukkan di-hash dan dibandingkan dengan hash yang tersimpan.
    *   **Tanda Tangan Digital**: Digunakan dalam kombinasi dengan kriptografi asimetris untuk memverifikasi keaslian dan integritas dokumen.

#### Pertemuan 12: Konsep VPN & Praktik VPN Remote Access (PPTP/L2TP)

**1. Konsep VPN (Virtual Private Network)**

VPN adalah teknologi yang menciptakan koneksi jaringan yang aman dan terenkripsi melalui jaringan publik yang tidak aman (seperti internet). Ini memungkinkan pengguna untuk mengirim dan menerima data seolah-olah perangkat mereka terhubung langsung ke jaringan pribadi.

*   **Fungsi Utama VPN**:
    *   **Kerahasiaan**: Data dienkripsi saat transit.
    *   **Integritas**: Data tidak diubah saat transit.
    *   **Autentikasi**: Memverifikasi identitas pengguna dan/atau perangkat.
    *   **Anonimitas/Privasi**: Menyembunyikan alamat IP asli pengguna.

*   **Jenis-jenis VPN**:
    *   **Remote Access VPN**: Menghubungkan pengguna individu (misal: karyawan yang bekerja dari rumah) ke jaringan pribadi perusahaan.
    *   **Site-to-Site VPN**: Menghubungkan dua atau lebih jaringan lokal (misal: kantor cabang ke kantor pusat) secara aman melalui internet.

*   **Protokol VPN Umum**:
    *   **PPTP (Point-to-Point Tunneling Protocol)**: Protokol VPN lama, mudah dikonfigurasi, tetapi dianggap kurang aman karena kerentanan yang diketahui.
    *   **L2TP/IPsec (Layer 2 Tunneling Protocol over IPsec)**: Kombinasi L2TP untuk tunneling dan IPsec untuk enkripsi dan keamanan. Lebih aman dari PPTP.
    *   **OpenVPN**: Protokol *open-source* yang sangat fleksibel dan aman, menggunakan SSL/TLS untuk enkripsi.
    *   **WireGuard**: Protokol VPN modern yang dirancang untuk kesederhanaan, kecepatan, dan keamanan.

**2. Praktik VPN Remote Access di Mikrotik (PPTP/L2TP)**

Mikrotik RouterOS dapat berfungsi sebagai VPN Server untuk koneksi Remote Access.

*   **Langkah-langkah Konfigurasi PPTP Server di Mikrotik (Ringkasan)**:
    1.  **Aktifkan PPTP Server**: `/interface pptp-server server set enabled=yes`
    2.  **Buat Pool IP untuk Klien VPN**: `/ip pool add name=vpn_pool ranges=192.168.200.10-192.168.200.20`
    3.  **Buat Profil PPP**: `/ppp profile add name=vpn_profile local-address=192.168.200.1 remote-address=vpn_pool use-encryption=yes`
    4.  **Buat Pengguna PPP Secret**: `/ppp secret add name=vpnuser password=vpnpass service=pptp profile=vpn_profile`
    5.  **Konfigurasi Firewall (jika diperlukan)**: Izinkan koneksi PPTP (TCP port 1723 dan GRE protocol 47) ke Mikrotik.

*   **Langkah-langkah Konfigurasi L2TP/IPsec Server di Mikrotik (Ringkasan)**:
    1.  **Aktifkan L2TP Server**: `/interface l2tp-server server set enabled=yes use-ipsec=yes ipsec-secret=myipsecsecret`
    2.  **Buat Pool IP dan Profil PPP** (sama seperti PPTP).
    3.  **Buat Pengguna PPP Secret**: `/ppp secret add name=vpnuser password=vpnpass service=l2tp profile=vpn_profile`
    4.  **Konfigurasi Firewall (jika diperlukan)**: Izinkan koneksi L2TP (UDP port 1701) dan IPsec (UDP port 500, 4500, dan ESP protocol 50) ke Mikrotik.

*   **Konfigurasi Klien VPN (Windows/Linux)**:
    *   Pada sistem operasi klien, buat koneksi VPN baru dengan memilih jenis PPTP atau L2TP/IPsec.
    *   Masukkan alamat IP publik Mikrotik, username, dan password VPN.
    *   Untuk L2TP/IPsec, masukkan juga *IPsec pre-shared key*.
    *   Setelah terhubung, klien akan mendapatkan IP dari `vpn_pool` dan dapat mengakses jaringan internal Mikrotik.

### MODUL 6: PROYEK MINI SEMESTER 2

#### Pertemuan 13: Penjelasan dan Perencanaan Proyek

**1. Tujuan Proyek Mini Semester 2**

Proyek mini ini bertujuan untuk mengintegrasikan konsep dan praktik yang telah dipelajari dari Modul 1 hingga Modul 5 di Semester 2. Peserta didik akan secara mandiri atau berkelompok membangun dan mengamankan jaringan lab virtual dengan fokus pada autentikasi terpusat dan monitoring keamanan.

*   **Tujuan Utama**:
    *   Menerapkan sistem autentikasi terpusat menggunakan FreeRADIUS dan Mikrotik.
    *   Mengimplementasikan sistem deteksi intrusi dan analisis log menggunakan Wazuh.
    *   Mengkonfigurasi komunikasi aman (VPN) sebagai bagian dari infrastruktur.
    *   Mendokumentasikan seluruh proses dan hasil proyek.
    *   Menganalisis data keamanan untuk mengidentifikasi potensi ancaman.

**2. Spesifikasi Proyek (Contoh)**

Setiap proyek mungkin memiliki spesifikasi yang sedikit berbeda, namun umumnya mencakup:

*   **Topologi Jaringan**: Desain jaringan lab virtual yang mencakup Mikrotik Router, FreeRADIUS Server, Wazuh Manager, dan setidaknya satu Wazuh Agent (pada VM klien/server).
*   **Autentikasi Terpusat**: Mikrotik harus menggunakan FreeRADIUS untuk autentikasi login.
*   **Monitoring Keamanan**: Wazuh Manager harus mengumpulkan log dari Mikrotik (via syslog) dan Wazuh Agent (dari VM klien/server).
*   **Deteksi Ancaman**: Mendemonstrasikan deteksi anomali atau serangan sederhana di dashboard Wazuh (misal: login gagal, perubahan file).
*   **Komunikasi Aman (Opsional/Tambahan)**: Implementasi VPN Remote Access di Mikrotik.
*   **Dokumentasi Teknis**: Laporan yang mencakup diagram topologi, konfigurasi, hasil pengujian, dan analisis keamanan.

**3. Perencanaan Proyek Kelompok**

Perencanaan yang matang adalah kunci keberhasilan proyek. Setiap kelompok harus menyusun rencana kerja yang jelas.

*   **Pembagian Tugas**: Tentukan peran dan tanggung jawab masing-masing anggota kelompok (misal: konfigurator RADIUS, konfigurator Wazuh, penguji, dokumentator).
*   **Timeline**: Buat jadwal pengerjaan proyek dengan target waktu yang realistis untuk setiap tahapan (desain, implementasi, pengujian, dokumentasi, presentasi).
*   **Desain Topologi**: Gambarkan diagram topologi jaringan yang akan dibangun, termasuk:
    *   Jumlah dan jenis VM yang digunakan.
    *   Mode jaringan VirtualBox (NAT, Host-only) untuk setiap koneksi.
    *   Alokasi IP address untuk setiap VM dan interface Mikrotik.
    *   Arah aliran data autentikasi dan log.
*   **Strategi Implementasi Keamanan**: Jelaskan bagaimana prinsip-prinsip keamanan (AAA, SIEM, Kriptografi) akan diterapkan dalam desain dan konfigurasi proyek.
*   **Rencana Pengujian**: Bagaimana kelompok akan menguji fungsionalitas sistem autentikasi dan kemampuan deteksi Wazuh.

#### Pertemuan 14: Pengerjaan Proyek (Implementasi)

**1. Tahap Implementasi**

Pada tahap ini, kelompok akan mulai membangun jaringan lab virtual sesuai dengan rencana yang telah disusun. Ini melibatkan konfigurasi perangkat lunak dan sistem operasi.

*   **Langkah-langkah Umum**:
    *   **Pembuatan VM**: Membuat semua Virtual Machine yang diperlukan (Mikrotik, FreeRADIUS Server, Wazuh Manager, Wazuh Agent VM).
    *   **Konfigurasi Jaringan Virtual**: Menghubungkan VM menggunakan adapter jaringan VirtualBox (NAT, Host-only) sesuai topologi.
    *   **Instalasi OS dan Tools**: Menginstal sistem operasi pada VM dan tools yang diperlukan (FreeRADIUS, Wazuh).
    *   **Konfigurasi FreeRADIUS**: Menginstal dan mengkonfigurasi FreeRADIUS Server, menambahkan klien dan pengguna.
    *   **Integrasi Mikrotik RADIUS Client**: Mengkonfigurasi Mikrotik untuk menggunakan FreeRADIUS untuk autentikasi login.
    *   **Instalasi Wazuh**: Menginstal Wazuh Manager dan Wazuh Agent pada VM yang relevan.
    *   **Konfigurasi Pengiriman Log**: Mengkonfigurasi Mikrotik untuk mengirim log ke Wazuh Manager via syslog.
    *   **Implementasi VPN (Opsional)**: Mengkonfigurasi VPN Server di Mikrotik.

**2. Pencatatan Progres dan Kendala**

Penting untuk mendokumentasikan progres yang dicapai dan setiap kendala yang dihadapi, beserta solusinya. Ini akan membantu dalam proses debugging dan penyusunan laporan akhir.

*   **Progres**: Catat bagian mana dari topologi yang sudah berhasil dibangun, integrasi yang sudah berfungsi, dan hasil pengujian awal.
*   **Kendala**: Identifikasi masalah teknis (misal: konektivitas, konfigurasi salah) atau non-teknis (misal: kesulitan kolaborasi). Jelaskan bagaimana kelompok mencoba mengatasi kendala tersebut.
*   **Screenshot**: Ambil screenshot dari konfigurasi penting (misal: daftar VM, konfigurasi FreeRADIUS, Wazuh dashboard, konfigurasi Mikrotik) sebagai bukti implementasi.

#### Pertemuan 15: Finalisasi Proyek dan Penyusunan Laporan

**1. Finalisasi Konfigurasi Proyek**

Pada tahap ini, kelompok akan memastikan semua konfigurasi telah selesai dan berfungsi sesuai spesifikasi proyek. Lakukan pengujian menyeluruh untuk memverifikasi fungsionalitas dan keamanan.

*   **Checklist Finalisasi**:
    *   Semua VM berfungsi dengan baik.
    *   Autentikasi Mikrotik via RADIUS berfungsi sempurna.
    *   Semua log dari Mikrotik dan Wazuh Agent masuk ke Wazuh Manager.
    *   Wazuh dapat mendeteksi anomali atau serangan sederhana.
    *   VPN (jika diimplementasikan) berfungsi dengan baik.
    *   Tidak ada kerentanan yang jelas atau akses tidak sah yang ditemukan.

**2. Penyusunan Laporan Teknis Proyek**

Laporan teknis adalah bagian krusial dari proyek, menunjukkan pemahaman dan kemampuan dokumentasi peserta didik. Laporan harus jelas, ringkas, dan profesional.

*   **Komponen Laporan Teknis**:
    *   **Pendahuluan**: Latar belakang, tujuan proyek.
    *   **Desain Topologi Jaringan**: Diagram topologi yang jelas dengan semua detail (IP address, mode jaringan, aliran data autentikasi dan log).
    *   **Implementasi Konfigurasi**: Penjelasan langkah-langkah konfigurasi utama (instalasi FreeRADIUS, Wazuh, integrasi Mikrotik, VPN).
    *   **Hasil Pengujian**: Screenshot dan deskripsi hasil pengujian fungsionalitas (login RADIUS, pengiriman log, deteksi anomali, koneksi VPN).
    *   **Analisis Keamanan**: Diskusi tentang bagaimana prinsip keamanan (AAA, SIEM, Kriptografi) diterapkan dan potensi risiko yang masih ada.
    *   **Kesimpulan**: Ringkasan pencapaian proyek dan pelajaran yang didapat.
    *   **Lampiran**: Screenshot tambahan, log, atau file konfigurasi.

**3. Persiapan Presentasi**

Kelompok harus mempersiapkan presentasi yang efektif untuk memamerkan hasil proyek mereka.

*   **Materi Presentasi**: Buat slide presentasi yang ringkas dan visual.
*   **Pembagian Peran**: Tentukan siapa yang akan mempresentasikan setiap bagian dan siapa yang akan melakukan demonstrasi.
*   **Latihan**: Latih presentasi dan demonstrasi untuk memastikan kelancaran dan alokasi waktu yang tepat.

#### Pertemuan 16: Presentasi Proyek dan Evaluasi Semester

**1. Presentasi dan Demonstrasi Proyek**

Ini adalah kesempatan bagi setiap kelompok untuk menunjukkan hasil kerja keras mereka dan mendemonstrasikan pemahaman mereka tentang keamanan jaringan.

*   **Aspek yang Dinilai**:
    *   **Kejelasan Presentasi**: Kemampuan menjelaskan konsep dan implementasi dengan baik.
    *   **Fungsionalitas Proyek**: Apakah sistem autentikasi terpusat dan monitoring keamanan berfungsi sesuai spesifikasi.
    *   **Demonstrasi**: Kelancaran dan efektivitas demonstrasi konfigurasi dan pengujian.
    *   **Pemahaman Teknis**: Kemampuan menjawab pertanyaan dari guru dan teman-teman.
    *   **Kerjasama Tim**: Bagaimana kelompok bekerja sama selama presentasi.

**2. Sesi Tanya Jawab dan Umpan Balik**

Setelah setiap presentasi, akan ada sesi tanya jawab untuk memperdalam pemahaman dan memberikan umpan balik konstruktif.

*   **Tujuan**: Mengidentifikasi area yang perlu diperbaiki, memberikan apresiasi atas pekerjaan yang baik, dan mendorong pemikiran kritis.

**3. Evaluasi Semester Keseluruhan**

Pada akhir semester, akan ada refleksi dan evaluasi menyeluruh terhadap proses pembelajaran dan pencapaian peserta didik.

*   **Refleksi Diri**: Peserta didik merenungkan apa yang telah mereka pelajari, tantangan yang dihadapi, dan bagaimana mereka tumbuh.
*   **Umpan Balik Guru**: Guru memberikan umpan balik umum tentang kinerja kelas, menyoroti kekuatan dan area untuk pengembangan.
*   **Rencana Tindak Lanjut**: Diskusi tentang bagaimana pengetahuan dan keterampilan yang diperoleh akan diterapkan di masa depan, serta area yang mungkin perlu didalami lebih lanjut.

## LAMPIRAN - GLOSARIUM

*   **AAA (Authentication, Authorization, Accounting)**: Kerangka kerja fundamental dalam manajemen akses dan keamanan jaringan yang memverifikasi identitas, menentukan hak akses, dan melacak aktivitas pengguna.
*   **Accounting (Akuntansi)**: Aspek AAA yang melacak aktivitas pengguna (apa yang mereka lakukan, kapan, berapa lama, berapa banyak sumber daya yang digunakan).
*   **Agent (Wazuh)**: Komponen Wazuh yang diinstal pada host yang ingin dipantau, bertugas mengumpulkan data log dan mengirimkannya ke Wazuh Manager.
*   **Authentication (Autentikasi)**: Aspek AAA yang memverifikasi identitas pengguna.
*   **Authorization (Otorisasi)**: Aspek AAA yang menentukan hak akses atau izin yang dimiliki pengguna yang telah terautentikasi.
*   **Capture Filter (Wireshark)**: Aturan yang diterapkan saat memulai penangkapan paket untuk membatasi jenis lalu lintas yang akan direkam.
*   **Collision Resistance (Hash Function)**: Sifat fungsi hash yang sangat sulit untuk menemukan dua input berbeda yang menghasilkan hash value yang sama.
*   **Cryptographic Hash Function**: Algoritma matematika yang menghasilkan output (hash value) dengan ukuran tetap dari input data, digunakan untuk integritas data dan penyimpanan password.
*   **Dashboard (SIEM)**: Antarmuka visual yang menyajikan data keamanan dalam bentuk grafik, tabel, dan metrik untuk analisis cepat.
*   **Display Filter (Wireshark)**: Aturan yang diterapkan setelah penangkapan paket untuk menyaring dan menampilkan hanya paket yang relevan.
*   **Enkripsi Asimetris (Asymmetric-key Cryptography)**: Metode enkripsi yang menggunakan sepasang kunci (publik dan privat) yang berbeda untuk enkripsi dan dekripsi.
*   **Enkripsi Simetris (Symmetric-key Cryptography)**: Metode enkripsi yang menggunakan kunci yang sama untuk proses enkripsi dan dekripsi.
*   **FreeRADIUS**: Implementasi *open-source* yang populer dari protokol RADIUS.
*   **Function Hash**: Lihat Cryptographic Hash Function.
*   **Host Discovery**: Proses mengidentifikasi host-host yang aktif dalam sebuah jaringan.
*   **HIDS (Host-based Intrusion Detection System)**: IDS yang memantau aktivitas pada satu host (file system, log, proses).
*   **IPS (Intrusion Prevention System)**: Sistem keamanan yang mendeteksi dan secara aktif mencegah serangan.
*   **IDS (Intrusion Detection System)**: Sistem keamanan yang mendeteksi aktivitas mencurigakan atau serangan di jaringan atau host.
*   **Kriptografi**: Ilmu dan seni menyembunyikan informasi (enkripsi) dan mengungkapkannya kembali (dekripsi).
*   **L2TP/IPsec (Layer 2 Tunneling Protocol over IPsec)**: Protokol VPN yang menggabungkan L2TP untuk tunneling dan IPsec untuk enkripsi dan keamanan.
*   **Log Correlation (SIEM)**: Proses mengidentifikasi hubungan antara event-event yang tampaknya tidak terkait dari berbagai sumber log untuk mendeteksi pola serangan yang kompleks.
*   **Log Management**: Proses pengumpulan, penyimpanan, dan pengelolaan log dari berbagai sumber untuk tujuan keamanan dan operasional.
*   **Multi-Factor Authentication (MFA)**: Metode autentikasi yang mengharuskan pengguna untuk memberikan dua atau lebih faktor verifikasi yang berbeda dari kategori yang berbeda.
*   **NIDS (Network-based Intrusion Detection System)**: IDS yang memantau lalu lintas jaringan secara keseluruhan.
*   **Nmap (Network Mapper)**: Tool *open-source* untuk eksplorasi jaringan dan audit keamanan, digunakan untuk port scanning, host discovery, dll.
*   **One-Way (Hash Function)**: Sifat fungsi hash yang sangat sulit untuk merekonstruksi input asli dari hash value.
*   **OTP (One-Time Password)**: Kode unik yang berlaku hanya untuk satu sesi login, sering digunakan dalam MFA.
*   **Packet Sniffing**: Proses menangkap dan menganalisis paket data yang mengalir melalui jaringan.
*   **Port Scanning**: Proses mengidentifikasi port-port yang terbuka pada sebuah host.
*   **PPTP (Point-to-Point Tunneling Protocol)**: Protokol VPN lama yang mudah dikonfigurasi tetapi kurang aman.
*   **RADIUS Client**: Perangkat jaringan (misal: router, switch) yang menerima permintaan koneksi dari pengguna dan meneruskannya ke RADIUS Server untuk autentikasi.
*   **RADIUS Server**: Server yang menyimpan database pengguna dan kebijakan akses, memproses permintaan autentikasi dari klien.
*   **Remote Access VPN**: Jenis VPN yang menghubungkan pengguna individu ke jaringan pribadi perusahaan.
*   **Scanning**: Proses pengumpulan informasi tentang target dengan mengirimkan permintaan dan menganalisis responsnya.
*   **Service/Version Detection**: Proses mengidentifikasi jenis dan versi layanan yang berjalan pada port terbuka.
*   **SIEM (Security Information and Event Management)**: Solusi perangkat lunak yang mengumpulkan, menganalisis, dan menyajikan data keamanan dari berbagai sumber dalam satu platform terpusat.
*   **Site-to-Site VPN**: Jenis VPN yang menghubungkan dua atau lebih jaringan lokal secara aman melalui internet.
*   **VPN (Virtual Private Network)**: Teknologi yang menciptakan koneksi jaringan yang aman dan terenkripsi melalui jaringan publik yang tidak aman.
*   **Wazuh**: Platform keamanan *open-source* komprehensif untuk deteksi ancaman, pemantauan integritas, respons insiden, dan kepatuhan, dengan kemampuan HIDS dan SIEM.
*   **Wireshark**: *Network protocol analyzer* *open-source* yang digunakan untuk menangkap dan menganalisis lalu lintas jaringan.

## LAMPIRAN - DAFTAR PUSTAKA

Berikut adalah daftar pustaka dan sumber referensi yang digunakan dalam penyusunan modul ini, serta rekomendasi untuk pendalaman materi lebih lanjut:

### Buku Teks dan Publikasi Ilmiah
*   Stallings, William. (2017). *Cryptography and Network Security: Principles and Practice*. Pearson.
*   Easttom, William. (2018). *Computer Security Fundamentals*. Pearson.
*   Chirillo, John. (2000). *Hack Attacks Revealed: A Complete Guide to Network Security, Exploitation, and Survival*. Wiley.
*   Kim, David, & Solomon, Michael G. (2019). *Fundamentals of Information Systems Security*. Jones & Bartlett Learning.
*   Vacca, John R. (2017). *Cyber Security and IT Infrastructure Protection*. Syngress.
*   Al-Fares, M., Loukides, M., & O'Reilly, T. (2010). *Network Security with OpenSSL*. O'Reilly Media. (Untuk kriptografi dan SSL/TLS)
*   Stevens, W. Richard, & Fenner, Bill. (2003). *UNIX Network Programming, Volume 1: The Sockets Networking API*. Addison-Wesley Professional. (Untuk pemahaman jaringan dasar)

### Dokumentasi Resmi Vendor/Organisasi
*   **Nmap Documentation**: Official Nmap User's Guide.
    *   [https://nmap.org/book/](https://nmap.org/book/)
*   **Wireshark Documentation**: Official Wireshark User's Guide and Wiki.
    *   [https://www.wireshark.org/docs/](https://www.wireshark.org/docs/)
*   **FreeRADIUS Documentation**: Official FreeRADIUS Wiki and documentation.
    *   [https://wiki.freeradius.org/](https://wiki.freeradius.org/)
*   **Wazuh Documentation**: Official Wazuh Documentation.
    *   [https://documentation.wazuh.com/](https://documentation.wazuh.com/)
*   **MikroTik Wiki**: Official documentation for MikroTik RouterOS and RouterBOARD devices.
    *   [https://wiki.mikrotik.com/](https://wiki.mikrotik.com/)
*   **OWASP Top 10 - 2021**: The OWASP Foundation.
    *   [https://owasp.org/www-project-top-10/](https://owasp.org/www-project-top-10/)
*   **NIST Cybersecurity Framework (CSF)**: Framework for Improving Critical Infrastructure Cybersecurity. National Institute of Standards and Technology.
    *   [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
*   **ISO/IEC 27001**: Information security management systems — Requirements. International Organization for Standardization.
    *   [https://www.iso.org/isoiec-27001-information-security.html](https://www.iso.org/isoiec-27001-information-security.html)
*   **Undang-Undang Republik Indonesia Nomor 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik (UU ITE)** sebagaimana telah diubah dengan Undang-Undang Nomor 19 Tahun 2016.

### Sumber Online dan Platform Pembelajaran
*   **SANS Institute**: Berbagai artikel, whitepaper, dan kursus tentang keamanan informasi.
    *   [https://www.sans.org/](https://www.sans.org/)
*   **KrebsOnSecurity**: Blog investigasi jurnalisme tentang kejahatan siber dan keamanan komputer.
    *   [https://krebsonsecurity.com/](https://krebsonsecurity.com/)
*   **The Hacker News**: Sumber berita keamanan siber terkemuka.
    *   [https://thehackernews.com/](https://thehackernews.com/)
*   **TryHackMe**: Platform pembelajaran keamanan siber interaktif dengan lab praktis.
    *   [https://tryhackme.com/](https://tryhackme.com/)
*   **Hack The Box Academy**: Platform pembelajaran hacking etis.
    *   [https://academy.hackthebox.com/](https://academy.hackthebox.com/)
*   **CyberDefenders**: Platform lab forensik dan insiden respon.
    *   [https://cyberdefenders.org/](https://cyberdefenders.org/)
*   **YouTube Channels**: Berbagai kanal yang menyediakan tutorial dan penjelasan tentang keamanan jaringan (misal: The Cyber Mentor, NetworkChuck, Professor Messer).

### Tools dan Software Referensi
*   **Nmap**: [https://www.nmap.org/](https://www.nmap.org/)
*   **Wireshark**: [https://www.wireshark.org/](https://www.wireshark.org/)
*   **FreeRADIUS**: [https://freeradius.org/](https://freeradius.org/)
*   **Wazuh**: [https://wazuh.com/](https://wazuh.com/)
*   **Kali Linux**: [https://www.kali.org/](https://www.kali.org/)
*   **MikroTik RouterOS**: [https://mikrotik.com/](https://mikrotik.com/)
*   **VirtualBox**: [https://www.virtualbox.org/](https://www.virtualbox.org/)
*   **VMware Workstation Player**: [https://www.vmware.com/products/workstation-player.html](https://www.vmware.com/products/workstation-player.html)

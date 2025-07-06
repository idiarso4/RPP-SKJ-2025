# Kata Pengantar

Puji syukur kehadirat Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga dokumen RPP Sistem Keamanan Jaringan Semester 1 ini dapat disusun sebagai panduan pembelajaran komprehensif bagi peserta didik Kelas XII Program Keahlian Sistem Informasi Jaringan dan Aplikasi (SIJA) di SMK, sesuai Kurikulum Merdeka Fase F. RPP ini mengintegrasikan teori, praktik, dan asesmen otentik berbasis kebutuhan industri, serta menanamkan nilai-nilai Profil Pelajar Pancasila. Semoga dokumen ini bermanfaat dan mendukung terwujudnya lulusan yang kompeten, adaptif, dan berkarakter.

# Identitas Modul
- Nama Sekolah: SMKN 1 Punggelan
- Program Keahlian: Sistem Informasi Jaringan dan Aplikasi (SIJA)
- Mata Pelajaran: Sistem Keamanan Jaringan
- Fase/Kelas/Semester: Fase F / XII / Semester 1
- Tahun Pelajaran: 2025/2026
- Penyusun: Idiarso, S.Kom
- Alokasi Waktu: 16 pertemuan (64 jam pelajaran @ 45 menit)

# Panduan Penggunaan RPP

## Untuk Guru
- Setiap pertemuan dirancang untuk 4 JP (180 menit), dengan pembagian waktu antara teori, praktik, diskusi, dan refleksi.
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
Fase/Kelas/Semester	: Fase F / XII / Semester 1
Alokasi Waktu	: 16 pertemuan
durasi pertemuan 1 kali pertemuan 4 x 45 menit 

## A. Tujuan Pembelajaran
Setelah mengikuti pembelajaran ini, peserta didik mampu:
1. Memahami sintaks dasar Python dan menggunakan library untuk membuat alat bantu keamanan.
2. Memahami konsep dan arsitektur keamanan IoT, serta mengamankan perangkat IoT sederhana.
3. Mengkonfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik.
4. Mengidentifikasi dan menguji kerentanan aplikasi web (OWASP Top 10) menggunakan tools.
5. Memahami model keamanan cloud, IAM, dan risiko keamanan container (Docker), serta mengamankan Dockerfile dan image container.

## B. Materi Pembelajaran
1. **Dasar Pemrograman Python untuk Keamanan (SaaS)**
   - Sintaks dasar Python (variabel, tipe data, kontrol aliran)
   - Fungsi dan modularitas
   - Penggunaan library `requests` (interaksi HTTP)
   - Penggunaan library `socket` (pemrograman jaringan dasar)
   - Membuat skrip sederhana untuk otomatisasi tugas keamanan (port scanner, banner grabbing)

2. **Dasar Internet-of-Things (IoT)**
   - Konsep dasar IoT dan arsitektur keamanan IoT
   - Identifikasi kerentanan umum pada perangkat IoT
   - Teknik pengamanan IoT (otentikasi, enkripsi, segmentasi jaringan)
   - Platform IoT (Blynk/Thingspeak) dari perspektif keamanan
   - Praktik mengamankan perangkat IoT sederhana (misal: monitor suhu)

3. **Virtual Private Network (VPN) Lanjutan**
   - Protokol VPN (IPsec, SSL/TLS)
   - Konsep Tunneling (GRE, IPIP)
   - Perbedaan Site-to-Site VPN dan Remote Access VPN
   - Praktik konfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik

4. **Keamanan Aplikasi Web**
   - Kerentanan Web Umum (OWASP Top 10: SQL Injection, XSS, Broken Authentication, dll.)
   - Konsep Web Application Firewall (WAF)
   - Tools pengujian keamanan aplikasi web (Burp Suite, OWASP ZAP)
   - Praktik pengujian keamanan pada aplikasi web rentan (DVWA/Juice Shop)

5. **Keamanan Cloud & Container**
   - Model Keamanan Cloud (IaaS, PaaS, SaaS)
   - Identity and Access Management (IAM) di Cloud
   - Konsep Container (Docker) dan risiko keamanannya
   - Praktik dasar mengamankan Dockerfile dan image container

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
   - Virtualisasi (VirtualBox, VMware, Docker)
   - Mikrokontroler (ESP32/ESP8266) & Sensor
   - Tools: Python IDE, Wireshark, Nmap, Kali Linux, Metasploit, Burp Suite, OWASP ZAP, Mikrotik RouterOS

3. **Sumber Belajar**
   - Buku teks Sistem Keamanan Jaringan
   - Dokumentasi resmi (Python, Docker, Mikrotik, OWASP, NIST)
   - Sumber online (OWASP, SANS, NIST, platform IoT)
   - Modul praktikum

## I. Langkah-langkah Pembelajaran (RPP Harian)

### **MODUL 1: DASAR PEMROGRAMAN PYTHON UNTUK KEAMANAN (SaaS)**

#### **RPP - Pertemuan 1: Sintaks Dasar Python & Fungsi**
1.  **Tujuan**: Memahami sintaks dasar Python (variabel, tipe data, kontrol aliran) dan konsep fungsi. (UbD: Membangun fondasi pemrograman untuk otomatisasi keamanan).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Jika kita ingin melakukan tugas yang sama berulang kali di komputer, bagaimana cara kita membuatnya otomatis?" atau "Apa yang kalian bayangkan ketika mendengar 'bahasa pemrograman'?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan contoh perintah sederhana yang mereka ketahui di komputer dan apa fungsinya.
        -   Guru memperkenalkan Python sebagai bahasa yang mudah dipelajari dan sangat berguna untuk otomatisasi keamanan.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Sintaks Dasar Python (45 mnt)**: Guru menjelaskan konsep variabel, tipe data (string, integer, list, dictionary), operator, dan kontrol aliran (if-else, for, while). (Diferensiasi: Menyediakan contoh kode sederhana yang dapat langsung dicoba siswa).
        -   **Praktik Terbimbing Fungsi Python (45 mnt)**: Guru memandu siswa membuat fungsi sederhana, memahami parameter, dan nilai kembalian. (SEL: Manajemen diri, ketekunan).
        -   **Latihan Pemrograman Sederhana (45 mnt)**: Siswa mengerjakan latihan-latihan singkat untuk mengaplikasikan sintaks dasar dan fungsi (misal: program kalkulator sederhana, program untuk memvalidasi input). (Diferensiasi: Memberikan tantangan tambahan bagi siswa yang cepat menyelesaikan).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 jenis tipe data di Python dan contoh penggunaannya.
        -   Guru memimpin refleksi tentang pentingnya logika pemrograman.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat sintaks dasar yang paling sering digunakan. Guru menawarkan sumber belajar tambahan tentang Python for Beginners. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Library Python untuk Jaringan).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam memahami sintaks dasar Python dan membuat fungsi sederhana.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Latihan Pemrograman (detail rubrik di Lampiran).

#### **RPP - Pertemuan 2: Library Python untuk Interaksi HTTP (`requests`)**
1.  **Tujuan**: Menggunakan library `requests` untuk interaksi HTTP. (UbD: Memahami cara berinteraksi dengan aplikasi web secara terprogram).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana cara browser kita 'berbicara' dengan website?" atau "Jika kita ingin mengambil informasi dari banyak website secara otomatis, bagaimana caranya?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu HTTP.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Konsep HTTP & Library `requests` (45 mnt)**: Guru menjelaskan dasar-dasar HTTP (GET, POST, header, status code) dan memperkenalkan library `requests` untuk membuat permintaan HTTP. (Diferensiasi: Menyediakan contoh kode untuk berbagai jenis permintaan HTTP).
        -   **Praktik Terbimbing Mengambil Data Web (45 mnt)**: Guru memandu siswa menggunakan `requests` untuk:
            -   Melakukan permintaan GET ke URL publik.
            -   Mengambil konten halaman web.
            -   Mengirimkan data POST (misal: simulasi login sederhana ke form test).
            (SEL: Manajemen diri, ketekunan).
        -   **Latihan Otomatisasi Sederhana (45 mnt)**: Siswa mengerjakan latihan untuk mengambil data dari API publik atau melakukan interaksi sederhana dengan website. (Diferensiasi: Memberikan tantangan untuk memparsing data JSON dari API).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 metode HTTP yang sering digunakan dan fungsinya.
        -   Guru memimpin refleksi tentang potensi `requests` untuk otomatisasi web.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat cara menginstal library Python. Guru menawarkan sumber belajar tambahan tentang web scraping etis. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Library Python untuk Jaringan).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menggunakan library `requests` untuk interaksi HTTP.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Latihan Pemrograman (detail rubrik di Lampiran).

#### **RPP - Pertemuan 3: Library Python untuk Pemrograman Jaringan (`socket`)**
1.  **Tujuan**: Menggunakan library `socket` untuk pemrograman jaringan dasar dan membuat skrip *port scanner* sederhana. (UbD: Memahami interaksi jaringan tingkat rendah).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana aplikasi di komputer kita bisa 'mendengarkan' atau 'mengirim' data ke aplikasi lain di komputer yang berbeda?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu "port" dalam konteks jaringan.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Konsep Socket & Library `socket` (45 mnt)**: Guru menjelaskan konsep socket (TCP/UDP), IP address, dan port. Memperkenalkan library `socket` untuk membuat koneksi jaringan. (Diferensiasi: Menyediakan diagram alur koneksi TCP).
        -   **Praktik Terbimbing Membuat Port Scanner Sederhana (45 mnt)**: Guru memandu siswa membuat skrip Python sederhana untuk:
            -   Mencoba koneksi ke port tertentu pada target.
            -   Menentukan apakah port terbuka atau tertutup.
            -   Melakukan scan pada rentang port.
            (SEL: Manajemen diri, ketekunan).
        -   **Latihan Banner Grabbing Sederhana (45 mnt)**: Siswa mengembangkan skrip untuk melakukan banner grabbing (mengambil informasi versi layanan dari port terbuka). (Diferensiasi: Memberikan tantangan untuk menyimpan hasil scan ke file).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan perbedaan antara TCP dan UDP.
        -   Guru memimpin refleksi tentang bagaimana skrip sederhana dapat menjadi alat keamanan yang kuat.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat fungsi-fungsi penting dari library `socket`. Guru menawarkan sumber belajar tambahan tentang pengembangan tool keamanan dengan Python. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Dasar Internet-of-Things (IoT)).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menggunakan library `socket` dan membuat skrip jaringan dasar.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Latihan Pemrograman (detail rubrik di Lampiran).

### **MODUL 2: DASAR INTERNET-OF-THINGS (IoT)**

#### **RPP - Pertemuan 4: Konsep & Arsitektur Keamanan IoT**
1.  **Tujuan**: Memahami konsep dasar IoT dan arsitektur keamanannya. (UbD: Memahami tantangan keamanan unik di ekosistem IoT).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bayangkan semua benda di sekitar kita bisa terhubung ke internet dan 'berbicara' satu sama lain. Apa saja manfaat dan bahayanya?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menyebutkan contoh perangkat IoT yang mereka ketahui.
        -   Guru menampilkan berita atau studi kasus insiden keamanan IoT (misal: kamera pintar diretas).
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Konsep Dasar IoT (45 mnt)**: Guru menjelaskan definisi IoT, komponen utama (sensor/aktuator, konektivitas, platform, aplikasi), dan contoh penerapannya. (Diferensiasi: Menyediakan video singkat tentang cara kerja perangkat IoT).
        -   **Eksplorasi Arsitektur Keamanan IoT (45 mnt)**: Guru menjelaskan lapisan-lapisan arsitektur IoT (perangkat, jaringan, cloud/platform, aplikasi) dan tantangan keamanan di setiap lapisan. (Diferensiasi: Menyediakan diagram arsitektur keamanan IoT).
        -   **Diskusi Kerentanan Umum IoT (45 mnt)**: Siswa dalam kelompok berdiskusi tentang kerentanan umum pada perangkat IoT (misal: password default, firmware tidak diperbarui, komunikasi tidak terenkripsi). (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 tantangan keamanan unik pada perangkat IoT.
        -   Guru memimpin refleksi tentang pentingnya keamanan sejak tahap desain IoT.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu hal yang akan mereka perhatikan saat membeli perangkat IoT. Guru menawarkan sumber belajar tambahan tentang OWASP IoT Top 10. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Teknik Pengamanan IoT).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang konsep dasar dan arsitektur keamanan IoT.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 5: Teknik Pengamanan IoT & Platform IoT**
1.  **Tujuan**: Memahami teknik pengamanan perangkat IoT dan peran platform IoT dari perspektif keamanan. (UbD: Menerapkan praktik terbaik untuk mengamankan ekosistem IoT).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana cara kita membuat 'benda pintar' kita aman dari 'penyusup digital'?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menyebutkan satu cara untuk mengamankan perangkat digital.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Teknik Pengamanan IoT (45 mnt)**: Guru menjelaskan teknik pengamanan IoT: otentikasi kuat, enkripsi komunikasi, pembaruan firmware, segmentasi jaringan untuk perangkat IoT, dan manajemen patch. (Diferensiasi: Menyediakan checklist keamanan IoT sederhana).
        -   **Eksplorasi Platform IoT dari Perspektif Keamanan (45 mnt)**: Guru menjelaskan peran platform IoT (misal: Blynk, Thingspeak) dalam mengelola perangkat dan data, serta fitur keamanan yang ditawarkan (manajemen identitas, otorisasi API, enkripsi data). (Diferensiasi: Menampilkan demo singkat platform IoT).
        -   **Diskusi Studi Kasus Pengamanan (45 mnt)**: Siswa dalam kelompok menganalisis studi kasus perangkat IoT yang berhasil diamankan atau insiden yang dicegah berkat implementasi keamanan yang baik. (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 teknik pengamanan IoT yang paling penting.
        -   Guru memimpin refleksi tentang pendekatan keamanan berlapis untuk IoT.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu langkah yang akan mereka ambil untuk mengamankan perangkat IoT di rumah. Guru menawarkan sumber belajar tambahan tentang keamanan protokol IoT (MQTT, CoAP). (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Praktik Mengamankan Perangkat IoT Sederhana).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang teknik pengamanan IoT dan peran platform IoT.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 6: Praktik Mengamankan Perangkat IoT Sederhana**
1.  **Tujuan**: Melakukan praktik dasar mengamankan perangkat IoT sederhana (misal: monitor suhu) dan mengintegrasikannya secara aman ke dalam jaringan. (UbD: Menerapkan konsep keamanan IoT secara hands-on).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana cara kita membuat 'sensor suhu pintar' kita tidak bisa diretas oleh orang iseng?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menyebutkan satu risiko keamanan pada sensor suhu yang terhubung ke internet.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Persiapan Perangkat & Lingkungan (45 mnt)**: Guru memandu siswa menyiapkan mikrokontroler (misal: ESP32/ESP8266) dan sensor suhu. Memastikan IDE (Arduino IDE/PlatformIO) terinstal dan driver terdeteksi. (Diferensiasi: Menyediakan kode dasar untuk membaca sensor).
        -   **Praktik Terbimbing Implementasi Keamanan (45 mnt)**: Guru memandu siswa mengimplementasikan praktik keamanan dasar pada kode mikrokontroler:
            -   Menggunakan kredensial Wi-Fi yang aman (tidak hardcode).
            -   Menggunakan HTTPS/SSL untuk komunikasi ke platform IoT (jika didukung).
            -   Menggunakan API key/token yang aman.
            (SEL: Manajemen diri, ketekunan).
        -   **Integrasi Aman ke Platform IoT (45 mnt)**: Siswa mengintegrasikan perangkat IoT ke platform (misal: Blynk/Thingspeak) dengan konfigurasi keamanan yang tepat. Menguji pengiriman data dan memastikan data terkirim dengan aman. (Diferensiasi: Memberikan tantangan untuk menambahkan otentikasi dua faktor pada akun platform IoT).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 praktik keamanan yang diterapkan pada perangkat IoT hari ini.
        -   Guru memimpin refleksi tentang pentingnya keamanan dalam pengembangan IoT.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat tantangan dalam pemrograman mikrokontroler. Guru menawarkan sumber belajar tambahan tentang keamanan firmware IoT. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Virtual Private Network (VPN) Lanjutan).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam mengamankan perangkat IoT sederhana dan mengintegrasikannya secara aman.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik IoT (detail rubrik di Lampiran).

### **MODUL 3: VIRTUAL PRIVATE NETWORK (VPN) LANJUTAN**

#### **RPP - Pertemuan 7: Protokol VPN (IPsec, SSL/TLS) & Konsep Tunneling**
1.  **Tujuan**: Memahami protokol VPN lanjutan (IPsec, SSL/TLS) dan konsep tunneling. (UbD: Memahami mekanisme di balik komunikasi VPN yang aman).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Jika kita ingin membuat 'terowongan rahasia' antara dua kantor yang jauh, bagaimana cara kerjanya agar aman dan tidak terlihat dari luar?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu VPN.
        -   Guru menampilkan diagram IPsec VPN.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Protokol VPN Lanjutan (45 mnt)**: Guru menjelaskan secara detail protokol IPsec (AH, ESP, IKE, fase 1 & 2) dan SSL/TLS VPN (OpenVPN). Membandingkan kelebihan dan kekurangan masing-masing. (Diferensiasi: Menyediakan tabel perbandingan protokol VPN).
        -   **Eksplorasi Konsep Tunneling (45 mnt)**: Guru menjelaskan konsep tunneling (GRE, IPIP) sebagai dasar pembentukan VPN. Membedakan antara tunneling dan enkripsi. (Diferensiasi: Menyediakan animasi atau ilustrasi visual proses tunneling).
        -   **Diskusi Perbedaan VPN (45 mnt)**: Siswa dalam kelompok berdiskusi tentang perbedaan mendasar antara Remote Access VPN dan Site-to-Site VPN, serta skenario penggunaan yang tepat untuk masing-masing. (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 komponen utama IPsec.
        -   Guru memimpin refleksi tentang kompleksitas dan kekuatan VPN.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat protokol VPN yang paling aman. Guru menawarkan sumber belajar tambahan tentang konfigurasi VPN di berbagai platform. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Praktik Site-to-Site VPN).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang protokol VPN lanjutan dan konsep tunneling.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 8: Praktik Konfigurasi Site-to-Site VPN (IPsec) - Bagian 1**
1.  **Tujuan**: Mengkonfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik (Fase 1: IKE). (UbD: Menerapkan koneksi aman antar dua jaringan).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana cara kita menghubungkan dua kantor yang berbeda kota agar komputer di kedua kantor bisa 'berbicara' satu sama lain dengan aman?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu Site-to-Site VPN.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Persiapan Lingkungan (45 mnt)**: Guru memandu siswa menyiapkan dua VM Mikrotik RouterOS yang mensimulasikan dua lokasi berbeda (misal: Kantor A dan Kantor B), dengan IP publik yang berbeda dan jaringan internal yang berbeda. (Diferensiasi: Menyediakan template konfigurasi dasar Mikrotik).
        -   **Praktik Terbimbing Konfigurasi IPsec Fase 1 (IKE) (45 mnt)**: Guru memandu siswa mengkonfigurasi IPsec Proposal dan Peer (Fase 1) di kedua Mikrotik. Memastikan kedua peer dapat saling terhubung dan membentuk Security Association (SA) Fase 1. (SEL: Manajemen diri, ketekunan).
        -   **Pengujian Konektivitas Fase 1 (45 mnt)**: Siswa menguji status SA Fase 1 di kedua Mikrotik. Melakukan troubleshooting jika ada masalah. (Diferensiasi: Memberikan tantangan untuk mencoba berbagai algoritma enkripsi/hash di Fase 1).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 parameter penting dalam konfigurasi IPsec Peer.
        -   Guru memimpin refleksi tentang pentingnya Fase 1 dalam IPsec.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat langkah-langkah konfigurasi IPsec Fase 1. Guru menawarkan sumber belajar tambahan tentang debugging IPsec. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (IPsec Fase 2).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam mengkonfigurasi IPsec Fase 1 dan melakukan troubleshooting.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik IPsec Fase 1 (detail rubrik di Lampiran).

#### **RPP - Pertemuan 9: Praktik Konfigurasi Site-to-Site VPN (IPsec) - Bagian 2**
1.  **Tujuan**: Menyelesaikan konfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik (Fase 2: ESP/AH). (UbD: Mengamankan lalu lintas data antar jaringan).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Setelah 'terowongan rahasia' kita terbentuk, bagaimana cara kita memastikan 'barang-barang' yang lewat di dalamnya benar-benar aman dan tidak bisa dilihat orang lain?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan tujuan Fase 2 IPsec.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Review & Troubleshooting Fase 1 (45 mnt)**: Guru mereview konfigurasi IPsec Fase 1 dan membantu siswa yang masih mengalami masalah konektivitas.
        -   **Praktik Terbimbing Konfigurasi IPsec Fase 2 (ESP/AH) (45 mnt)**: Guru memandu siswa mengkonfigurasi IPsec Policy dan Proposal (Fase 2) di kedua Mikrotik. Menentukan jaringan yang akan dienkripsi dan diizinkan melalui VPN tunnel. (SEL: Manajemen diri, ketekunan).
        -   **Pengujian Konektivitas End-to-End (45 mnt)**: Siswa menguji konektivitas (misal: ping, akses share folder) antara VM di jaringan internal Kantor A dan VM di jaringan internal Kantor B melalui VPN. Memverifikasi bahwa lalu lintas terenkripsi. (Diferensiasi: Memberikan tantangan untuk mengkonfigurasi NAT traversal untuk IPsec).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan perbedaan antara IPsec AH dan ESP.
        -   Guru memimpin refleksi tentang keberhasilan membangun VPN Site-to-Site.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa mencatat langkah-langkah konfigurasi IPsec Fase 2. Guru menawarkan sumber belajar tambahan tentang implementasi VPN IPsec di perangkat lain. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Keamanan Aplikasi Web).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam mengkonfigurasi IPsec Fase 2 dan memverifikasi konektivitas VPN.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik IPsec Fase 2 (detail rubrik di Lampiran).

### **MODUL 4: KEAMANAN APLIKASI WEB**

#### **RPP - Pertemuan 10: Kerentanan Web Umum (OWASP Top 10) & SQL Injection**
1.  **Tujuan**: Mengidentifikasi kerentanan web umum (OWASP Top 10) dan memahami SQL Injection. (UbD: Memahami ancaman paling kritis terhadap aplikasi web).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Jika sebuah website adalah sebuah toko, apa saja 'celah keamanan' yang bisa dimanfaatkan pencuri untuk masuk atau mengambil barang?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menyebutkan satu jenis serangan yang mereka ketahui pada website.
        -   Guru menampilkan contoh serangan SQL Injection.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi OWASP Top 10 (45 mnt)**: Guru menjelaskan konsep OWASP Top 10 sebagai daftar kerentanan aplikasi web paling kritis. Membahas beberapa kerentanan teratas (misal: Broken Access Control, Cryptographic Failures, Injection). (Diferensiasi: Menyediakan infografis OWASP Top 10).
        -   **Eksplorasi SQL Injection (45 mnt)**: Guru menjelaskan secara detail kerentanan SQL Injection: cara kerja, jenis-jenis (Error-based, Union-based, Blind), dan dampaknya. (Diferensiasi: Menampilkan demo singkat SQL Injection pada aplikasi web yang rentan).
        -   **Latihan Identifikasi SQL Injection (45 mnt)**: Siswa menggunakan aplikasi web yang sengaja dibuat rentan (misal: DVWA - Damn Vulnerable Web Application) untuk mencoba mengidentifikasi dan mengeksploitasi kerentanan SQL Injection. (SEL: Manajemen diri, ketekunan).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 jenis kerentanan dari OWASP Top 10.
        -   Guru memimpin refleksi tentang pentingnya validasi input.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu cara untuk mencegah SQL Injection. Guru menawarkan sumber belajar tambahan tentang SQL Injection prevention. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (XSS & WAF).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang OWASP Top 10 dan SQL Injection.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Latihan Eksploitasi (detail rubrik di Lampiran).

#### **RPP - Pertemuan 11: Kerentanan Web (XSS) & Konsep WAF**
1.  **Tujuan**: Memahami kerentanan Cross-Site Scripting (XSS) dan konsep Web Application Firewall (WAF). (UbD: Memahami serangan sisi klien dan pertahanannya).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana sebuah website bisa 'menipu' browser kita untuk menjalankan kode jahat?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu "script" dalam konteks web.
        -   Guru menampilkan contoh serangan XSS.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Eksplorasi Cross-Site Scripting (XSS) (45 mnt)**: Guru menjelaskan secara detail kerentanan XSS: jenis-jenis (Stored, Reflected, DOM-based), cara kerja, dan dampaknya (pencurian cookie, defacement). (Diferensiasi: Menampilkan demo singkat XSS pada aplikasi web yang rentan).
        -   **Konsep Web Application Firewall (WAF) (45 mnt)**: Guru menjelaskan fungsi WAF sebagai lapisan pertahanan khusus untuk aplikasi web. Membahas bagaimana WAF mendeteksi dan memblokir serangan seperti SQL Injection dan XSS. (Diferensiasi: Menyediakan perbandingan WAF berbasis signature vs. berbasis anomali).
        -   **Latihan Identifikasi XSS (45 mnt)**: Siswa menggunakan aplikasi web yang sengaja dibuat rentan (DVWA/Juice Shop) untuk mencoba mengidentifikasi dan mengeksploitasi kerentanan XSS. (SEL: Manajemen diri, ketekunan).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan perbedaan antara Stored XSS dan Reflected XSS.
        -   Guru memimpin refleksi tentang pentingnya sanitasi input dan output.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu cara untuk mencegah XSS. Guru menawarkan sumber belajar tambahan tentang Content Security Policy (CSP). (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Tools Pengujian Keamanan Web).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang XSS dan WAF.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Latihan Eksploitasi (detail rubrik di Lampiran).

#### **RPP - Pertemuan 12: Tools Pengujian Keamanan Web (Burp Suite/OWASP ZAP)**
1.  **Tujuan**: Menggunakan tools pengujian keamanan aplikasi web (Burp Suite/OWASP ZAP) untuk menemukan kerentanan. (UbD: Menguasai alat bantu profesional untuk audit keamanan web).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Jika kita ingin 'mengintip' semua komunikasi antara browser dan website, dan bahkan 'mengubah' pesan yang dikirim, alat apa yang bisa kita gunakan?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menyebutkan satu tool yang digunakan untuk menguji website.
        -   Guru menampilkan antarmuka Burp Suite/OWASP ZAP.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Burp Suite/OWASP ZAP (45 mnt)**: Guru memperkenalkan Burp Suite (Community Edition) atau OWASP ZAP sebagai proxy intersepsi dan scanner kerentanan. Menjelaskan fitur-fitur utama (Proxy, Repeater, Intruder/Fuzzer, Scanner). (Diferensiasi: Menyediakan panduan instalasi dan konfigurasi proxy browser).
        -   **Praktik Terbimbing Intersepsi & Modifikasi Request (45 mnt)**: Guru memandu siswa mengkonfigurasi browser untuk menggunakan proxy Burp/ZAP. Melakukan intersepsi permintaan HTTP, memodifikasi, dan meneruskannya. (SEL: Manajemen diri, ketekunan).
        -   **Latihan Fuzzing Sederhana (45 mnt)**: Siswa menggunakan fitur Repeater/Intruder (Burp) atau Fuzzer (ZAP) untuk mencoba menemukan kerentanan sederhana (misal: error-based SQL Injection, XSS) pada aplikasi web rentan. (Diferensiasi: Memberikan tantangan untuk menggunakan payload list).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan fungsi utama dari fitur Proxy di Burp Suite/OWASP ZAP.
        -   Guru memimpin refleksi tentang kekuatan tools ini untuk pengujian keamanan.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu fitur yang paling menarik dari tools ini. Guru menawarkan sumber belajar tambahan tentang penggunaan Burp Suite/OWASP ZAP untuk berbagai jenis serangan. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Keamanan Cloud & Container).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam menggunakan tools pengujian keamanan web.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Tools (detail rubrik di Lampiran).

#### **RPP - Pertemuan 13: Konsep Web Application Firewall (WAF)**
1.  **Tujuan**: Memahami konsep Web Application Firewall (WAF) dan cara kerjanya dalam melindungi aplikasi web. (UbD: Memahami solusi pertahanan tingkat aplikasi).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Jika website kita adalah sebuah toko, bagaimana kita bisa punya 'satpam khusus' yang memeriksa setiap orang yang masuk dan setiap barang yang dibawa, untuk mencegah pencurian atau kerusakan?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan perbedaan antara firewall jaringan dan firewall aplikasi.
        -   Guru menampilkan diagram posisi WAF dalam arsitektur web.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Konsep WAF (60 mnt)**: Guru menjelaskan definisi WAF, mengapa WAF diperlukan (melengkapi firewall jaringan), posisi WAF dalam arsitektur web, dan cara kerjanya (signature-based, anomaly-based, positive/negative security model). Membahas kemampuan WAF dalam memitigasi OWASP Top 10. (Diferensiasi: Menyediakan studi kasus implementasi WAF di perusahaan besar).
        -   **Diskusi Perbandingan & Implementasi (75 mnt)**: Siswa dalam kelompok berdiskusi tentang berbagai jenis WAF (hardware, software, cloud-based) dan skenario implementasi yang tepat. Membandingkan WAF dengan IDS/IPS dan firewall jaringan. (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 jenis serangan yang dapat dicegah oleh WAF.
        -   Guru memimpin refleksi tentang pentingnya pertahanan berlapis untuk aplikasi web.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu pertanyaan yang masih mereka miliki tentang WAF. Guru menawarkan sumber belajar tambahan tentang ModSecurity atau Cloudflare WAF. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Keamanan Cloud & Container).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang konsep WAF dan perannya dalam keamanan aplikasi web.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

### **MODUL 5: KEAMANAN CLOUD & CONTAINER**

#### **RPP - Pertemuan 14: Model Keamanan Cloud & IAM di Cloud**
1.  **Tujuan**: Memahami model keamanan cloud (Shared Responsibility Model) dan Identity and Access Management (IAM) di cloud. (UbD: Memahami pembagian tanggung jawab keamanan di lingkungan cloud).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Jika kita menyewa rumah, siapa yang bertanggung jawab atas keamanan pintu dan jendela? Siapa yang bertanggung jawab atas keamanan barang di dalam rumah?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu "cloud computing".
        -   Guru menampilkan diagram Shared Responsibility Model.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Model Keamanan Cloud (60 mnt)**: Guru menjelaskan Shared Responsibility Model di cloud (IaaS, PaaS, SaaS). Membahas apa yang menjadi tanggung jawab penyedia cloud dan apa yang menjadi tanggung jawab pengguna. (Diferensiasi: Menyediakan tabel perbandingan tanggung jawab untuk setiap model layanan cloud).
        -   **Eksplorasi IAM di Cloud (75 mnt)**: Guru menjelaskan konsep Identity and Access Management (IAM) di platform cloud (misal: AWS IAM, Azure AD). Membahas prinsip Least Privilege dalam konteks cloud, peran, kebijakan, dan grup. (Diferensiasi: Menampilkan demo singkat konfigurasi IAM di konsol cloud publik).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan perbedaan tanggung jawab keamanan antara IaaS dan SaaS.
        -   Guru memimpin refleksi tentang pentingnya memahami Shared Responsibility Model.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu praktik terbaik IAM di cloud. Guru menawarkan sumber belajar tambahan tentang cloud security best practices. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Keamanan Container).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang model keamanan cloud dan IAM.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 15: Konsep & Risiko Keamanan Container (Docker)**
1.  **Tujuan**: Memahami konsep container (Docker) dan risiko keamanannya. (UbD: Memahami tantangan keamanan dalam lingkungan containerized).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bayangkan kita ingin mengemas sebuah aplikasi dan semua yang dibutuhkan agar bisa berjalan di mana saja, tanpa perlu instalasi rumit. Bagaimana caranya? Apa bahaya jika 'kemasan' itu tidak aman?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu "virtual machine".
        -   Guru menampilkan perbandingan VM dan Container.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Presentasi Konsep Container (Docker) (45 mnt)**: Guru menjelaskan konsep container (Docker) sebagai alternatif ringan dari VM. Membahas perbedaan antara VM dan container, manfaat (portabilitas, efisiensi), dan komponen Docker (Dockerfile, Image, Container, Registry). (Diferensiasi: Menyediakan video singkat tentang cara kerja Docker).
        -   **Eksplorasi Risiko Keamanan Container (45 mnt)**: Guru menjelaskan risiko keamanan spesifik pada container: kerentanan image dasar, konfigurasi Docker daemon yang tidak aman, privilege escalation, supply chain attacks, dan kurangnya segmentasi jaringan antar container. (Diferensiasi: Menyediakan studi kasus pelanggaran keamanan container).
        -   **Diskusi Praktik Terbaik Keamanan Container (45 mnt)**: Siswa dalam kelompok berdiskusi tentang praktik terbaik untuk mengamankan container (misal: menggunakan image dasar yang minimal, memindai kerentanan image, menjalankan container dengan hak akses minimal, segmentasi jaringan). (SEL: Kolaborasi, pengambilan keputusan bertanggung jawab).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 perbedaan utama antara VM dan Container.
        -   Guru memimpin refleksi tentang pentingnya keamanan di seluruh siklus hidup container.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu praktik keamanan yang akan mereka terapkan jika menggunakan Docker. Guru menawarkan sumber belajar tambahan tentang Kubernetes security. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau materi pertemuan berikutnya (Praktik Mengamankan Dockerfile).
        -   **Refleksi Guru**: Guru mencatat pemahaman siswa tentang konsep container dan risiko keamanannya.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Diskusi Kelompok (detail rubrik di Lampiran).

#### **RPP - Pertemuan 16: Praktik Dasar Mengamankan Dockerfile dan Image Container**
1.  **Tujuan**: Melakukan praktik dasar mengamankan Dockerfile dan image container. (UbD: Menerapkan praktik keamanan dalam pengembangan dan deployment container).
2.  **Langkah-langkah**:
    -   **Pendahuluan (15 mnt)**:
        -   Guru menyampaikan salam dan melakukan absen kehadiran.
        -   **Ice Breaking (15 mnt)**: Guru bertanya: "Bagaimana cara kita membuat 'kemasan aplikasi' kita seaman mungkin sejak awal pembuatannya?" (SEL: Pemecahan masalah, kesadaran diri).
        -   **Pre-test Sederhana (15 mnt)**: Guru meminta siswa menjelaskan apa itu Dockerfile.
        -   Guru menyampaikan tujuan pembelajaran.
    -   **Kegiatan Inti (135 mnt)**:
        -   **Persiapan Lingkungan (45 mnt)**: Guru memandu siswa menyiapkan lingkungan Docker (instalasi Docker Desktop/Engine di VM Linux). (Diferensiasi: Menyediakan Dockerfile sederhana yang rentan).
        -   **Praktik Terbimbing Mengamankan Dockerfile (45 mnt)**: Guru memandu siswa memodifikasi Dockerfile untuk menerapkan praktik terbaik keamanan:
            -   Menggunakan image dasar yang minimal (misal: `alpine`).
            -   Menjalankan aplikasi dengan user non-root.
            -   Menghapus dependensi yang tidak perlu.
            -   Menggunakan `COPY` daripada `ADD`.
            -   Menentukan `WORKDIR`.
            (SEL: Manajemen diri, ketekunan).
        -   **Praktik Membangun & Memindai Image (45 mnt)**: Siswa membangun image dari Dockerfile yang sudah diamankan. Menggunakan tool pemindai kerentanan image (misal: Trivy, Clair) untuk memindai image yang dibuat dan menganalisis hasilnya. (Diferensiasi: Memberikan tantangan untuk membandingkan hasil scan image rentan vs. image yang diamankan).
    -   **Penutup (30 mnt)**:
        -   **Post-test Sederhana (15 mnt)**: Guru meminta siswa menuliskan 2 praktik terbaik untuk mengamankan Dockerfile.
        -   Guru memimpin refleksi tentang pentingnya DevSecOps.
        -   **Refleksi & Diferensiasi (15 mnt)**: Siswa menuliskan satu hal yang akan mereka ingat saat membuat Dockerfile. Guru menawarkan sumber belajar tambahan tentang Docker security hardening. (SEL: Refleksi diri, manajemen diri).
        -   Guru memberikan pratinjau modul berikutnya (Ethical Hacking & Penetration Testing).
        -   **Refleksi Guru**: Guru mencatat kemampuan siswa dalam mengamankan Dockerfile dan image container.
        -   **Asesmen yang dipakai**: Observasi, Pre-test/Post-test Sederhana, Hasil Praktik Docker (detail rubrik di Lampiran).

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
   - Python Documentation
   - Docker Documentation
   - MikroTik Documentation
   - OWASP Top 10
   - NIST Cybersecurity Framework
   - Blynk/Thingspeak Documentation
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

### LKPD Pertemuan 1: Sintaks Dasar Python & Fungsi
**Tujuan Pembelajaran**: Memahami sintaks dasar Python (variabel, tipe data, kontrol aliran) dan konsep fungsi.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang sintaks dasar Python dan fungsi.
2.  Lakukan latihan pemrograman sederhana.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu variabel dan tipe data dalam Python. Berikan contoh untuk tipe data `string`, `integer`, `list`, dan `dictionary`.
2.  Buatlah program Python sederhana yang meminta input nama dan usia dari pengguna, lalu mencetak pesan sapaan yang berisi nama dan kategori usia (misal: "Anak-anak", "Remaja", "Dewasa").
3.  Buatlah sebuah fungsi Python yang menerima dua angka sebagai parameter, lalu mengembalikan hasil penjumlahan dan perkalian kedua angka tersebut.
4.  Jelaskan mengapa penggunaan fungsi penting dalam pemrograman.
5.  Apa perbedaan antara `for` loop dan `while` loop dalam Python? Berikan contoh penggunaan masing-masing.

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar yang kamu hadapi saat memulai pemrograman Python hari ini?
2.  Bagaimana pemahaman tentang sintaks dasar ini akan membantumu dalam otomatisasi keamanan?

---

### LKPD Pertemuan 2: Library Python untuk Interaksi HTTP (`requests`)
**Tujuan Pembelajaran**: Menggunakan library `requests` untuk interaksi HTTP.

**Petunjuk Pengerjaan**:
1.  Pahami dasar-dasar HTTP dan penggunaan library `requests`.
2.  Lakukan praktik mengambil data dari web menggunakan Python.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu HTTP dan mengapa penting untuk memahami cara kerjanya dalam konteks keamanan web.
2.  Buatlah skrip Python menggunakan library `requests` untuk melakukan permintaan GET ke URL `https://httpbin.org/get`. Cetak status code dan konten responsnya.
3.  Buatlah skrip Python yang melakukan permintaan POST ke URL `https://httpbin.org/post` dengan data JSON sederhana (misal: `{"nama": "[Nama Anda]", "pesan": "Halo"}`). Cetak respons JSON dari server.
4.  Apa perbedaan antara metode HTTP GET dan POST? Kapan kamu akan menggunakan masing-masing?
5.  Bagaimana library `requests` dapat digunakan untuk menguji kerentanan Broken Access Control pada aplikasi web (secara konseptual)?

**Pertanyaan Refleksi**:
1.  Apa hal yang paling menarik yang kamu pelajari tentang interaksi web menggunakan Python?
2.  Bagaimana `requests` dapat membantu dalam otomatisasi tugas-tugas keamanan web?

---

### LKPD Pertemuan 3: Library Python untuk Pemrograman Jaringan (`socket`)
**Tujuan Pembelajaran**: Menggunakan library `socket` untuk pemrograman jaringan dasar dan membuat skrip *port scanner* sederhana.

**Petunjuk Pengerjaan**:
1.  Pahami konsep socket dan penggunaan library `socket`.
2.  Lakukan praktik membuat skrip *port scanner* sederhana.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu socket dalam pemrograman jaringan.
2.  Buatlah skrip Python menggunakan library `socket` untuk membuat *port scanner* sederhana. Skrip ini harus:
    *   Menerima alamat IP target dan rentang port (misal: 1-100) sebagai input.
    *   Mencoba koneksi TCP ke setiap port dalam rentang tersebut.
    *   Mencetak "Port [nomor port] terbuka" jika koneksi berhasil, atau "Port [nomor port] tertutup" jika gagal.
3.  Lakukan pengujian skrip *port scanner* pada VM Linux di lab virtualmu. Lampirkan *screenshot* hasil scan.
4.  Apa perbedaan antara TCP socket dan UDP socket? Kapan kamu akan menggunakan masing-masing?
5.  Bagaimana skrip *port scanner* sederhana ini dapat dikembangkan menjadi alat yang lebih canggih untuk audit keamanan?

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar yang kamu hadapi saat membuat skrip *port scanner*?
2.  Bagaimana pemahaman tentang `socket` membantumu memahami cara kerja Nmap?

---

### LKPD Pertemuan 4: Konsep & Arsitektur Keamanan IoT
**Tujuan Pembelajaran**: Memahami konsep dasar IoT dan arsitektur keamanannya.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang konsep dasar IoT dan arsitektur keamanannya.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu Internet of Things (IoT) dan berikan 3 (tiga) contoh perangkat IoT yang sering kamu temui.
2.  Sebutkan dan jelaskan 3 (tiga) komponen utama dalam ekosistem IoT.
3.  Gambarkan arsitektur keamanan IoT yang mencakup lapisan perangkat, jaringan, dan cloud/platform. Jelaskan tantangan keamanan yang mungkin muncul di setiap lapisan.
4.  Identifikasi minimal 3 (tiga) kerentanan umum yang sering ditemukan pada perangkat IoT.
5.  Diskusikan: Mengapa keamanan IoT seringkali lebih kompleks daripada keamanan sistem IT tradisional?

**Pertanyaan Refleksi**:
1.  Apa hal yang paling mengejutkan yang kamu pelajari tentang keamanan IoT hari ini?
2.  Bagaimana kesadaran akan kerentanan IoT dapat memengaruhi keputusanmu dalam membeli atau menggunakan perangkat pintar?

---

### LKPD Pertemuan 5: Teknik Pengamanan IoT & Platform IoT
**Tujuan Pembelajaran**: Memahami teknik pengamanan perangkat IoT dan peran platform IoT dari perspektif keamanan.

**Petunjuk Pengerjaan**:
1.  Pahami teknik pengamanan perangkat IoT dan peran platform IoT.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan minimal 3 (tiga) teknik pengamanan yang dapat diterapkan pada perangkat IoT untuk mengurangi risiko serangan.
2.  Bagaimana peran platform IoT (misal: Blynk, Thingspeak) dalam menyediakan fitur keamanan untuk perangkat yang terhubung?
3.  Skenario: Sebuah smart home system menggunakan password default yang lemah. Jelaskan bagaimana teknik pengamanan yang kamu pelajari dapat mencegah insiden keamanan pada sistem ini.
4.  Diskusikan: Mengapa penting untuk melakukan pembaruan firmware secara berkala pada perangkat IoT?
5.  Apa itu segmentasi jaringan dalam konteks IoT dan mengapa penting untuk mengisolasi perangkat IoT dari jaringan utama?

**Pertanyaan Refleksi**:
1.  Apa praktik terbaik keamanan IoT yang menurutmu paling mudah diterapkan oleh pengguna awam?
2.  Bagaimana kamu bisa menjadi advokat keamanan IoT di lingkunganmu?

---

### LKPD Pertemuan 6: Praktik Mengamankan Perangkat IoT Sederhana
**Tujuan Pembelajaran**: Melakukan praktik dasar mengamankan perangkat IoT sederhana (misal: monitor suhu) dan mengintegrasikannya secara aman ke dalam jaringan.

**Petunjuk Pengerjaan**:
1.  Siapkan perangkat mikrokontroler dan sensor suhu.
2.  Lakukan praktik implementasi keamanan pada kode dan integrasi ke platform IoT.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Siapkan mikrokontroler (misal: ESP32/ESP8266) dan sensor suhu. Pastikan lingkungan pengembangan (IDE) sudah siap.
2.  Tulis kode dasar untuk membaca data dari sensor suhu dan mengirimkannya ke serial monitor.
3.  Modifikasi kode agar menggunakan kredensial Wi-Fi yang aman (tidak hardcode di dalam kode utama). Jelaskan bagaimana kamu mengimplementasikannya.
4.  Integrasikan perangkat IoT ke platform (misal: Blynk atau Thingspeak) dengan menggunakan API key/token yang aman. Lampirkan *screenshot* data yang berhasil terkirim ke platform.
5.  Jelaskan langkah-langkah yang kamu lakukan untuk memastikan komunikasi antara perangkat IoT dan platform aman (misal: penggunaan HTTPS/SSL).

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar yang kamu hadapi saat memprogram dan mengamankan perangkat IoT hari ini?
2.  Bagaimana praktik ini mengubah pandanganmu tentang keamanan perangkat yang terhubung?

---

### LKPD Pertemuan 7: Protokol VPN (IPsec, SSL/TLS) & Konsep Tunneling
**Tujuan Pembelajaran**: Memahami protokol VPN lanjutan (IPsec, SSL/TLS) dan konsep tunneling.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang protokol VPN lanjutan dan konsep tunneling.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan perbedaan mendasar antara protokol VPN IPsec dan SSL/TLS (misal: OpenVPN) dari segi lapisan OSI dan penggunaannya.
2.  Sebutkan dan jelaskan 2 (dua) komponen utama dari protokol IPsec.
3.  Apa itu tunneling dalam konteks VPN? Jelaskan bagaimana tunneling membantu menciptakan "jalur pribadi" di atas jaringan publik.
4.  Sebutkan perbedaan antara Remote Access VPN dan Site-to-Site VPN. Berikan contoh skenario penggunaan untuk masing-masing.
5.  Diskusikan: Mengapa IPsec sering digunakan untuk Site-to-Site VPN, sementara SSL/TLS VPN lebih populer untuk Remote Access?

**Pertanyaan Refleksi**:
1.  Apa hal yang paling menarik yang kamu pelajari tentang cara kerja VPN secara teknis?
2.  Bagaimana pemahaman tentang protokol VPN dapat membantumu memilih solusi VPN yang tepat?

---

### LKPD Pertemuan 8: Praktik Konfigurasi Site-to-Site VPN (IPsec) - Bagian 1
**Tujuan Pembelajaran**: Mengkonfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik (Fase 1: IKE).

**Petunjuk Pengerjaan**:
1.  Siapkan dua VM Mikrotik yang mensimulasikan dua lokasi.
2.  Lakukan konfigurasi IPsec Fase 1 (IKE) di kedua Mikrotik.
3.  Catat setiap langkah dan hasil pengujian.

**Kegiatan/Tugas**:
1.  Siapkan dua VM Mikrotik RouterOS (misal: Mikrotik A dan Mikrotik B) dengan konfigurasi jaringan yang sesuai untuk simulasi Site-to-Site VPN (IP publik berbeda, jaringan internal berbeda).
2.  Konfigurasi IPsec Proposal di kedua Mikrotik. Tentukan algoritma enkripsi dan hash yang akan digunakan untuk Fase 1. Lampirkan *screenshot* konfigurasi.
3.  Konfigurasi IPsec Peer (Fase 1) di kedua Mikrotik. Tentukan alamat IP peer, *authentication method* (misal: pre-shared key), dan *secret key*. Lampirkan *screenshot* konfigurasi.
4.  Verifikasi bahwa Security Association (SA) Fase 1 telah terbentuk di kedua Mikrotik. Lampirkan *screenshot* status SA.
5.  Jelaskan tujuan dari Fase 1 (IKE) dalam pembentukan IPsec VPN.

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar yang kamu hadapi saat mengkonfigurasi IPsec Fase 1?
2.  Bagaimana kamu melakukan troubleshooting jika Fase 1 tidak terbentuk?

---

### LKPD Pertemuan 9: Praktik Konfigurasi Site-to-Site VPN (IPsec) - Bagian 2
**Tujuan Pembelajaran**: Menyelesaikan konfigurasi Site-to-Site VPN menggunakan IPsec di Mikrotik (Fase 2: ESP/AH).

**Petunjuk Pengerjaan**:
1.  Lanjutkan konfigurasi IPsec Fase 2 (ESP/AH) di kedua Mikrotik.
2.  Lakukan pengujian konektivitas end-to-end melalui VPN.
3.  Catat setiap langkah dan hasil pengujian.

**Kegiatan/Tugas**:
1.  Pastikan IPsec Fase 1 sudah terbentuk antara Mikrotik A dan Mikrotik B.
2.  Konfigurasi IPsec Policy di kedua Mikrotik. Tentukan jaringan sumber dan tujuan yang akan dienkripsi melalui VPN tunnel. Lampirkan *screenshot* konfigurasi.
3.  Konfigurasi IPsec Proposal untuk Fase 2 (ESP/AH). Tentukan algoritma enkripsi dan autentikasi untuk data payload. Lampirkan *screenshot* konfigurasi.
4.  Lakukan pengujian konektivitas (misal: ping) dari VM di jaringan internal Mikrotik A ke VM di jaringan internal Mikrotik B. Lampirkan *screenshot* hasil ping yang berhasil.
5.  Jelaskan tujuan dari Fase 2 (ESP/AH) dalam pembentukan IPsec VPN dan bagaimana ia mengamankan lalu lintas data.

**Pertanyaan Refleksi**:
1.  Apa perbedaan antara IPsec Policy dan IPsec Proposal?
2.  Bagaimana kamu memastikan bahwa lalu lintas data benar-benar melewati VPN tunnel dan terenkripsi?

---

### LKPD Pertemuan 10: Kerentanan Web Umum (OWASP Top 10) & SQL Injection
**Tujuan Pembelajaran**: Mengidentifikasi kerentanan web umum (OWASP Top 10) dan memahami SQL Injection.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang OWASP Top 10 dan SQL Injection.
2.  Lakukan latihan identifikasi dan eksploitasi SQL Injection pada aplikasi web rentan.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu OWASP Top 10 dan mengapa penting bagi pengembang dan profesional keamanan web.
2.  Sebutkan minimal 3 (tiga) kerentanan dari OWASP Top 10 (selain Injection) dan jelaskan secara singkat dampaknya.
3.  Jelaskan apa itu SQL Injection dan bagaimana serangan ini dapat terjadi pada aplikasi web.
4.  Gunakan aplikasi web yang sengaja dibuat rentan (misal: DVWA - Damn Vulnerable Web Application) untuk mencoba mengidentifikasi dan mengeksploitasi kerentanan SQL Injection. Lampirkan *screenshot* hasil eksploitasi (misal: berhasil mendapatkan data yang tidak seharusnya).
5.  Bagaimana cara mencegah serangan SQL Injection pada aplikasi web?

**Pertanyaan Refleksi**:
1.  Apa hal yang paling mengejutkan yang kamu temukan saat mencoba SQL Injection?
2.  Bagaimana pemahaman tentang SQL Injection dapat membantumu menulis kode yang lebih aman?

---

### LKPD Pertemuan 11: Kerentanan Web (XSS) & Konsep WAF
**Tujuan Pembelajaran**: Memahami kerentanan Cross-Site Scripting (XSS) dan konsep Web Application Firewall (WAF).

**Petunjuk Pengerjaan**:
1.  Pahami kerentanan XSS dan konsep WAF.
2.  Lakukan latihan identifikasi dan eksploitasi XSS pada aplikasi web rentan.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu Cross-Site Scripting (XSS) dan mengapa berbahaya bagi pengguna website.
2.  Sebutkan dan jelaskan 3 (tiga) jenis XSS (Stored, Reflected, DOM-based). Berikan contoh sederhana untuk masing-masing.
3.  Gunakan aplikasi web yang sengaja dibuat rentan (DVWA/Juice Shop) untuk mencoba mengidentifikasi dan mengeksploitasi kerentanan XSS. Lampirkan *screenshot* hasil eksploitasi (misal: muncul alert box).
4.  Apa itu Web Application Firewall (WAF)? Jelaskan bagaimana WAF dapat melindungi aplikasi web dari serangan seperti XSS dan SQL Injection.
5.  Apa perbedaan antara WAF dan firewall jaringan tradisional?

**Pertanyaan Refleksi**:
1.  Bagaimana XSS dapat dimanfaatkan oleh penyerang untuk mencuri informasi pengguna?
2.  Menurutmu, apakah WAF sudah cukup untuk melindungi aplikasi web sepenuhnya? Mengapa atau mengapa tidak?

---

### LKPD Pertemuan 12: Tools Pengujian Keamanan Web (Burp Suite/OWASP ZAP)
**Tujuan Pembelajaran**: Menggunakan tools pengujian keamanan aplikasi web (Burp Suite/OWASP ZAP) untuk menemukan kerentanan.

**Petunjuk Pengerjaan**:
1.  Pahami fitur-fitur utama Burp Suite/OWASP ZAP.
2.  Lakukan praktik intersepsi dan modifikasi permintaan HTTP.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Instal Burp Suite Community Edition atau OWASP ZAP di komputermu. Lampirkan *screenshot* antarmuka utama tool.
2.  Konfigurasi browser webmu untuk menggunakan Burp Suite/OWASP ZAP sebagai proxy. Lampirkan *screenshot* konfigurasi proxy di browser.
3.  Lakukan intersepsi permintaan HTTP saat mengakses aplikasi web rentan (DVWA/Juice Shop). Modifikasi permintaan tersebut (misal: ubah nilai parameter) dan teruskan. Jelaskan apa yang kamu ubah dan mengapa.
4.  Gunakan fitur Repeater (Burp Suite) atau Fuzzer (OWASP ZAP) untuk mencoba mengirimkan payload SQL Injection atau XSS ke aplikasi web rentan. Lampirkan *screenshot* hasil percobaanmu.
5.  Jelaskan bagaimana tools seperti Burp Suite atau OWASP ZAP dapat membantu seorang *penetration tester* dalam menemukan kerentanan aplikasi web.

**Pertanyaan Refleksi**:
1.  Apa fitur yang paling berguna dari Burp Suite/OWASP ZAP menurutmu?
2.  Bagaimana tools ini dapat membantu dalam proses *ethical hacking*?

---

### LKPD Pertemuan 13: Konsep Web Application Firewall (WAF)
**Tujuan Pembelajaran**: Memahami konsep Web Application Firewall (WAF) dan cara kerjanya dalam melindungi aplikasi web.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang Web Application Firewall (WAF).
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu Web Application Firewall (WAF) dan mengapa ia menjadi komponen penting dalam keamanan aplikasi web.
2.  Bagaimana WAF mendeteksi serangan? Jelaskan perbedaan antara deteksi berbasis *signature* dan berbasis *anomaly*.
3.  Sebutkan minimal 3 (tiga) serangan web dari OWASP Top 10 yang dapat dimitigasi oleh WAF.
4.  Diskusikan: Apa saja pertimbangan dalam memilih dan mengimplementasikan WAF (misal: hardware, software, cloud-based)?
5.  Gambarkan posisi WAF dalam arsitektur aplikasi web (misal: di depan web server, di cloud). Jelaskan mengapa posisi tersebut strategis.

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar dalam mengelola WAF agar tidak memblokir lalu lintas yang sah (false positive)?
2.  Bagaimana WAF berkontribusi pada strategi *Defense in Depth* untuk aplikasi web?

---

### LKPD Pertemuan 14: Model Keamanan Cloud & IAM di Cloud
**Tujuan Pembelajaran**: Memahami model keamanan cloud (Shared Responsibility Model) dan Identity and Access Management (IAM) di cloud.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang model keamanan cloud dan IAM.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu Shared Responsibility Model dalam komputasi awan. Mengapa model ini penting untuk dipahami oleh pengguna cloud?
2.  Berikan contoh pembagian tanggung jawab keamanan antara penyedia cloud dan pengguna untuk model layanan IaaS, PaaS, dan SaaS.
3.  Apa itu Identity and Access Management (IAM) di cloud? Jelaskan mengapa IAM adalah pilar utama keamanan cloud.
4.  Sebutkan minimal 3 (tiga) praktik terbaik dalam mengelola IAM di cloud untuk menerapkan prinsip *Least Privilege*.
5.  Diskusikan: Jika sebuah perusahaan memindahkan aplikasinya ke cloud, apa saja pertimbangan keamanan utama yang harus mereka pikirkan terkait data dan akses?

**Pertanyaan Refleksi**:
1.  Apa hal yang paling mengejutkan yang kamu pelajari tentang tanggung jawab keamanan di cloud?
2.  Bagaimana pemahaman tentang IAM dapat membantumu mengamankan akun cloud pribadimu?

---

### LKPD Pertemuan 15: Konsep & Risiko Keamanan Container (Docker)
**Tujuan Pembelajaran**: Memahami konsep container (Docker) dan risiko keamanannya.

**Petunjuk Pengerjaan**:
1.  Baca dan pahami materi tentang konsep container (Docker) dan risiko keamanannya.
2.  Diskusikan dalam kelompok dan jawab pertanyaan-pertanyaan di bawah ini.

**Kegiatan/Tugas**:
1.  Jelaskan dengan bahasamu sendiri apa itu container (Docker) dan apa perbedaannya dengan Virtual Machine (VM).
2.  Sebutkan minimal 3 (tiga) manfaat utama penggunaan container dalam pengembangan dan deployment aplikasi.
3.  Identifikasi minimal 3 (tiga) risiko keamanan spesifik yang terkait dengan penggunaan container (misal: kerentanan image, konfigurasi Docker daemon yang tidak aman).
4.  Diskusikan: Bagaimana serangan *supply chain* dapat memengaruhi keamanan image container?
5.  Apa itu *privilege escalation* dalam konteks container dan bagaimana cara mencegahnya?

**Pertanyaan Refleksi**:
1.  Apa tantangan terbesar dalam mengamankan lingkungan containerized?
2.  Bagaimana pemahaman tentang keamanan container dapat membantumu dalam karir di bidang DevOps atau keamanan?

---

### LKPD Pertemuan 16: Praktik Dasar Mengamankan Dockerfile dan Image Container
**Tujuan Pembelajaran**: Melakukan praktik dasar mengamankan Dockerfile dan image container.

**Petunjuk Pengerjaan**:
1.  Siapkan lingkungan Docker.
2.  Lakukan praktik memodifikasi Dockerfile dan memindai image.
3.  Catat setiap langkah dan hasil yang kamu peroleh.

**Kegiatan/Tugas**:
1.  Instal Docker Desktop atau Docker Engine di VM Linuxmu. Lampirkan *screenshot* setelah instalasi berhasil dan verifikasi Docker berjalan.
2.  Buatlah sebuah Dockerfile sederhana untuk aplikasi web (misal: Nginx atau Python Flask). Pastikan Dockerfile tersebut memiliki setidaknya satu praktik keamanan yang kurang baik (misal: berjalan sebagai root, menyertakan dependensi yang tidak perlu).
3.  Modifikasi Dockerfile yang kamu buat untuk menerapkan minimal 3 (tiga) praktik terbaik keamanan (misal: menggunakan image dasar minimal, menjalankan sebagai user non-root, menghapus dependensi build).
4.  Bangun image Docker dari Dockerfile yang sudah diamankan. Gunakan tool pemindai kerentanan image (misal: Trivy atau Clair) untuk memindai image tersebut. Lampirkan *screenshot* hasil pemindaian dan jelaskan temuan utamanya.
5.  Bandingkan hasil pemindaian image yang rentan (jika kamu membuatnya) dengan image yang sudah diamankan. Jelaskan perbedaannya.

**Pertanyaan Refleksi**:
1.  Apa manfaat utama dari memindai image container untuk kerentanan?
2.  Bagaimana praktik DevSecOps (Development, Security, Operations) dapat membantu membangun aplikasi containerized yang lebih aman?

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
*   **Waktu Pelaksanaan**: Awal dan akhir setiap pertemuan (15-30 menit).
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
    *   Kesesuaian penerapan konsep (misal: skrip Python, konfigurasi VPN, eksploitasi web).
    *   Kelengkapan dan kejelasan dokumentasi (screenshot, kode).
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
*   **Waktu Pelaksanaan**: Akhir semester (jika ada proyek mini).
*   **Bentuk**: Laporan teknis proyek, presentasi, dan demonstrasi fungsionalitas.
*   **Fokus Penilaian**:
    *   **Desain Solusi**: Kelengkapan dan kejelasan desain (misal: skrip, topologi IoT, konfigurasi VPN).
    *   **Implementasi Konfigurasi**: Ketepatan implementasi (misal: kode Python, konfigurasi perangkat IoT, VPN, Docker).
    *   **Fungsionalitas**: Semua skrip/konfigurasi berfungsi sesuai spesifikasi.
    *   **Analisis Keamanan**: Pemahaman terhadap risiko dan mitigasi yang diterapkan.
    *   **Dokumentasi Teknis**: Kualitas laporan (struktur, isi, kejelasan).
    *   **Presentasi & Demonstrasi**: Kemampuan presentasi, menjawab pertanyaan, dan mendemonstrasikan proyek.
*   **Rubrik Penilaian (Contoh)**:
    | Aspek yang Dinilai | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
    |---|---|---|---|---|
    | Desain Solusi | Sangat detail, logis, dan mudah dipahami. | Detail dan logis. | Cukup detail, ada bagian kurang jelas. | Kurang detail/tidak logis. |
    | Implementasi Konfigurasi | Semua konfigurasi/kode tepat, efisien, dan berfungsi sempurna. | Konfigurasi/kode tepat, berfungsi baik. | Konfigurasi/kode ada kesalahan minor, berfungsi sebagian. | Banyak kesalahan konfigurasi/kode, tidak berfungsi. |
    | Fungsionalitas Proyek | Semua fungsionalitas berjalan sempurna. | Sebagian besar fungsionalitas berjalan. | Beberapa fungsionalitas berjalan. | Fungsionalitas tidak berjalan. |
    | Analisis Keamanan | Analisis mendalam, mengidentifikasi risiko dan mitigasi. | Analisis cukup baik, mengidentifikasi risiko. | Analisis kurang mendalam. | Tidak ada analisis keamanan. |
    | Dokumentasi Teknis | Laporan sangat komprehensif, jelas, dan profesional. | Laporan komprehensif dan jelas. | Laporan cukup jelas, ada bagian kurang lengkap. | Laporan tidak jelas/tidak lengkap. |
    | Presentasi & Demonstrasi | Sangat percaya diri, jelas, dan demonstrasi lancar. | Percaya diri, jelas, demonstrasi cukup lancar. | Cukup percaya diri, kurang jelas, demonstrasi tersendat. | Tidak percaya diri, tidak jelas, demonstrasi gagal. |

## LAMPIRAN - MATERI PEMBELAJARAN LENGKAP

### MODUL 1: DASAR PEMROGRAMAN PYTHON UNTUK KEAMANAN (SaaS)

#### Pertemuan 1: Sintaks Dasar Python & Fungsi

**1. Sintaks Dasar Python**

Python adalah bahasa pemrograman tingkat tinggi yang populer, mudah dibaca, dan serbaguna, sering digunakan dalam otomatisasi, pengembangan web, analisis data, dan keamanan siber.

*   **Variabel**: Digunakan untuk menyimpan nilai. Tidak perlu deklarasi tipe data eksplisit.
    *   Contoh: `nama = "Budi"`, `usia = 17`, `is_active = True`
*   **Tipe Data Dasar**:
    *   `str` (String): Teks, diapit oleh tanda kutip tunggal atau ganda. Contoh: `"Hello World"`
    *   `int` (Integer): Bilangan bulat. Contoh: `10`, `-5`
    *   `float`: Bilangan desimal. Contoh: `3.14`, `0.5`
    *   `bool` (Boolean): Nilai kebenaran (`True` atau `False`).
    *   `list`: Koleksi item yang berurutan dan dapat diubah. Contoh: `[1, 2, 3]`, `["apel", "jeruk"]`
    *   `tuple`: Koleksi item yang berurutan dan tidak dapat diubah. Contoh: `(1, 2, 3)`
    *   `dict` (Dictionary): Koleksi pasangan kunci-nilai yang tidak berurutan. Contoh: `{"nama": "Ani", "usia": 20}`
*   **Operator**: Aritmatika (`+`, `-`, `*`, `/`), Perbandingan (`==`, `!=`, `<`, `>`), Logika (`and`, `or`, `not`).
*   **Kontrol Aliran**:
    *   `if-elif-else`: Untuk membuat keputusan berdasarkan kondisi.
        ```python
        if usia < 18:
            print("Remaja")
        elif usia >= 18 and usia < 60:
            print("Dewasa")
        else:
            print("Lansia")
        ```
    *   `for` loop: Untuk iterasi melalui urutan (list, string, dll.).
        ```python
        for i in range(5):
            print(i) # Output: 0, 1, 2, 3, 4
        ```
    *   `while` loop: Untuk mengulang blok kode selama kondisi `True`.
        ```python
        count = 0
        while count < 3:
            print(count)
            count += 1 # Output: 0, 1, 2
        ```

**2. Fungsi dalam Python**

Fungsi adalah blok kode yang terorganisir dan dapat digunakan kembali untuk melakukan tugas tertentu. Fungsi membantu memecah program menjadi bagian-bagian yang lebih kecil dan mudah dikelola.

*   **Definisi Fungsi**: Menggunakan kata kunci `def`.
    ```python
    def sapa(nama):
        print(f"Halo, {nama}!")

    sapa("Dian") # Memanggil fungsi
    ```
*   **Parameter dan Argumen**: Parameter adalah variabel yang tercantum dalam definisi fungsi. Argumen adalah nilai yang dikirimkan ke fungsi saat dipanggil.
*   **Nilai Kembalian (`return`)**: Fungsi dapat mengembalikan nilai menggunakan kata kunci `return`.
    ```python
    def tambah(a, b):
        return a + b

    hasil = tambah(5, 3)
    print(hasil) # Output: 8
    ```

#### Pertemuan 2: Library Python untuk Interaksi HTTP (`requests`)

**1. Dasar-dasar HTTP**

HTTP (Hypertext Transfer Protocol) adalah protokol dasar yang digunakan untuk komunikasi data di World Wide Web. Ini adalah protokol *request-response*.

*   **Metode HTTP Umum**:
    *   `GET`: Digunakan untuk meminta data dari server (misal: membuka halaman web).
    *   `POST`: Digunakan untuk mengirimkan data ke server (misal: mengisi formulir login, mengirim komentar).
    *   `PUT`: Mengganti semua representasi target sumber daya dengan konten permintaan.
    *   `DELETE`: Menghapus sumber daya yang ditentukan.
*   **Header HTTP**: Informasi tambahan yang dikirim bersama permintaan atau respons (misal: `User-Agent`, `Content-Type`, `Authorization`).
*   **Status Code HTTP**: Kode numerik yang menunjukkan status respons server (misal: `200 OK`, `404 Not Found`, `500 Internal Server Error`).

**2. Library `requests`**

`requests` adalah library Python yang populer dan mudah digunakan untuk membuat permintaan HTTP. Ini menyederhanakan interaksi dengan web.

*   **Instalasi**: `pip install requests`
*   **Contoh Penggunaan**:
    *   **Permintaan GET**:
        ```python
        import requests

        response = requests.get("https://api.github.com/users/octocat")
        print(response.status_code)
        print(response.json()) # Mengubah respons JSON menjadi dictionary Python
        ```
    *   **Permintaan POST**:
        ```python
        import requests

        url = "https://httpbin.org/post"
        data = {"username": "testuser", "password": "testpass"}
        response = requests.post(url, data=data)
        print(response.status_code)
        print(response.json()) # Melihat data yang dikirimkan
        ```
    *   **Mengirim Header Kustom**:
        ```python
        import requests

        headers = {"User-Agent": "MyCustomApp/1.0", "Accept": "application/json"}
        response = requests.get("https://httpbin.org/headers", headers=headers)
        print(response.json())
        ```

#### Pertemuan 3: Library Python untuk Pemrograman Jaringan (`socket`)

**1. Konsep Socket**

Socket adalah titik akhir komunikasi dalam jaringan. Ini adalah antarmuka pemrograman yang memungkinkan aplikasi untuk mengirim dan menerima data melalui jaringan.

*   **Jenis Socket**:
    *   **TCP (Transmission Control Protocol)**: Menyediakan koneksi yang andal, berurutan, dan berorientasi koneksi. Digunakan untuk HTTP, FTP, SSH.
    *   **UDP (User Datagram Protocol)**: Menyediakan komunikasi tanpa koneksi, tidak ada jaminan pengiriman atau urutan. Digunakan untuk DNS, DHCP, streaming video.
*   **IP Address**: Alamat unik yang mengidentifikasi perangkat di jaringan.
*   **Port**: Nomor yang mengidentifikasi aplikasi atau layanan tertentu yang berjalan pada sebuah IP address.

**2. Library `socket`**

Library `socket` di Python menyediakan akses ke antarmuka socket BSD standar, memungkinkan pemrograman jaringan tingkat rendah.

*   **Contoh Port Scanner Sederhana**:
    ```python
    import socket

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: IPv4, SOCK_STREAM: TCP
        sock.settimeout(1) # Timeout 1 detik
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} terbuka")
        sock.close()
    except socket.error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Masukkan IP target: ")
    for p in range(1, 101): # Scan port 1 sampai 100
        scan_port(target, p)
    ```
*   **Contoh Banner Grabbing Sederhana**:
    ```python
    import socket

def banner_grab(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target_ip, port))
        banner = sock.recv(1024).decode().strip()
        print(f"Port {port} Banner: {banner}")
        sock.close()
    except Exception as e:
        print(f"Could not grab banner from port {port}: {e}")

if __name__ == "__main__":
    target = input("Masukkan IP target: ")
    # Contoh: coba grab banner dari port HTTP (80) atau SSH (22)
    banner_grab(target, 80)
    banner_grab(target, 22)
    ```

### MODUL 2: DASAR INTERNET-OF-THINGS (IoT)

#### Pertemuan 4: Konsep & Arsitektur Keamanan IoT

**1. Konsep Dasar IoT**

Internet of Things (IoT) adalah jaringan objek fisik yang tertanam dengan sensor, perangkat lunak, dan teknologi lain untuk tujuan menghubungkan dan bertukar data dengan perangkat dan sistem lain melalui internet.

*   **Komponen Utama Ekosistem IoT**:
    *   **Perangkat IoT (Things)**: Sensor, aktuator, mikrokontroler yang mengumpulkan data atau melakukan tindakan.
    *   **Konektivitas**: Jaringan yang menghubungkan perangkat (Wi-Fi, Bluetooth, Zigbee, LoRaWAN, Cellular).
    *   **Platform IoT**: Infrastruktur cloud yang mengelola perangkat, mengumpulkan, memproses, dan menyimpan data IoT.
    *   **Aplikasi IoT**: Antarmuka pengguna yang memungkinkan interaksi dengan perangkat dan visualisasi data.

**2. Arsitektur Keamanan IoT**

Keamanan IoT melibatkan perlindungan di berbagai lapisan karena kompleksitas dan heterogenitas ekosistemnya.

*   **Lapisan Perangkat (Device Layer)**:
    *   **Tantangan**: Sumber daya terbatas, kerentanan firmware, password default, kurangnya pembaruan keamanan.
    *   **Fokus Keamanan**: Secure boot, enkripsi data di perangkat, otentikasi perangkat, manajemen patch firmware.
*   **Lapisan Jaringan (Network Layer)**:
    *   **Tantangan**: Protokol komunikasi yang tidak aman, serangan Man-in-the-Middle, DDoS.
    *   **Fokus Keamanan**: Enkripsi komunikasi (TLS/SSL), segmentasi jaringan, firewall, IDS/IPS.
*   **Lapisan Cloud/Platform (Cloud/Platform Layer)**:
    *   **Tantangan**: Akses tidak sah ke data, kerentanan API, konfigurasi cloud yang salah.
    *   **Fokus Keamanan**: Identity and Access Management (IAM), otorisasi API, enkripsi data saat istirahat dan transit, audit log.
*   **Lapisan Aplikasi (Application Layer)**:
    *   **Tantangan**: Kerentanan aplikasi web/mobile, otentikasi/otorisasi yang lemah.
    *   **Fokus Keamanan**: Secure coding practices, pengujian keamanan aplikasi, WAF.

**3. Kerentanan Umum pada Perangkat IoT**

*   **Password Default/Lemah**: Banyak perangkat IoT datang dengan kredensial default yang mudah ditebak atau tidak diubah oleh pengguna.
*   **Firmware Tidak Aman/Tidak Diperbarui**: Kerentanan dalam firmware yang tidak diperbaiki karena kurangnya pembaruan atau pengguna tidak menginstal pembaruan.
*   **Komunikasi Tidak Terenkripsi**: Data sensitif dikirim dalam bentuk plaintext melalui jaringan.
*   **Antarmuka yang Tidak Aman**: Port terbuka yang tidak perlu, layanan debug yang aktif, atau antarmuka web yang rentan.
*   **Kurangnya Manajemen Akses**: Tidak ada kontrol yang memadai atas siapa yang dapat mengakses dan mengontrol perangkat.

#### Pertemuan 5: Teknik Pengamanan IoT & Platform IoT

**1. Teknik Pengamanan IoT**

Mengamankan perangkat IoT memerlukan pendekatan berlapis dan praktik terbaik.

*   **Otentikasi Kuat**: Mengganti password default, menggunakan password yang kompleks, menerapkan MFA (Multi-Factor Authentication) jika didukung.
*   **Enkripsi Komunikasi**: Memastikan semua data yang dikirimkan antara perangkat, gateway, dan cloud dienkripsi (misal: menggunakan TLS/SSL, DTLS).
*   **Pembaruan Firmware Teratur**: Selalu perbarui firmware perangkat ke versi terbaru untuk menambal kerentanan yang diketahui.
*   **Segmentasi Jaringan**: Mengisolasi perangkat IoT dalam segmen jaringan terpisah (misal: VLAN khusus IoT) untuk membatasi pergerakan lateral penyerang jika satu perangkat dikompromikan.
*   **Manajemen Patch**: Menerapkan patch keamanan pada sistem operasi dan perangkat lunak yang berjalan di gateway atau server IoT.
*   **Prinsip Least Privilege**: Memberikan hak akses minimal yang diperlukan kepada perangkat dan pengguna.

**2. Platform IoT dari Perspektif Keamanan**

Platform IoT (misal: Blynk, Thingspeak, AWS IoT Core, Azure IoT Hub) memainkan peran krusial dalam keamanan dengan menyediakan fitur-fitur terpusat.

*   **Manajemen Identitas dan Akses (IAM)**: Mengelola identitas perangkat dan pengguna, serta otorisasi akses ke data dan fungsi.
*   **Otentikasi Perangkat**: Mekanisme untuk memverifikasi identitas perangkat yang terhubung (misal: sertifikat X.509, token).
*   **Enkripsi Data**: Menyediakan enkripsi data saat transit (TLS/SSL) dan saat istirahat (enkripsi database).
*   **Manajemen Kunci**: Mengelola kunci enkripsi untuk perangkat dan data.
*   **Audit Log dan Pemantauan**: Mengumpulkan log aktivitas perangkat dan platform untuk deteksi anomali dan forensik.
*   **Manajemen Pembaruan Over-the-Air (OTA)**: Memungkinkan pembaruan firmware perangkat secara aman dari jarak jauh.

#### Pertemuan 6: Praktik Mengamankan Perangkat IoT Sederhana

**1. Persiapan Lingkungan Praktik**

*   **Mikrokontroler**: ESP32 atau ESP8266 adalah pilihan populer karena kemampuan Wi-Fi bawaan dan komunitas yang besar.
*   **Sensor**: Sensor suhu (misal: DHT11/DHT22) untuk mengumpulkan data.
*   **IDE**: Arduino IDE atau PlatformIO untuk menulis dan mengunggah kode ke mikrokontroler.
*   **Platform IoT**: Blynk atau Thingspeak untuk visualisasi dan manajemen data.

**2. Implementasi Keamanan Dasar pada Kode Mikrokontroler**

*   **Kredensial Wi-Fi Aman**: Hindari menyimpan SSID dan password Wi-Fi secara langsung di kode. Gunakan metode yang lebih aman (misal: menyimpan di EEPROM, atau menggunakan konfigurasi via portal).
    ```cpp
    // Hindari ini:
    // const char* ssid = "MyWiFi";
    // const char* password = "MyPassword";

    // Lebih baik:
    // Minta pengguna memasukkan kredensial saat pertama kali setup
    // Atau gunakan WiFiManager library
    ```
*   **Penggunaan HTTPS/SSL**: Jika platform IoT mendukung, selalu gunakan koneksi terenkripsi (HTTPS) untuk mengirim data.
    ```cpp
    // Contoh (konseptual dengan library HTTPClient)
    // #include <HTTPClient.h>
    // HTTPClient http;
    // http.begin("https://your-iot-platform.com/api"); // Perhatikan 'https'
    // ...
    ```
*   **API Key/Token Aman**: Jangan mengekspos API key atau token di tempat yang mudah diakses. Gunakan variabel konstanta atau metode penyimpanan yang aman.

**3. Integrasi Aman ke Platform IoT**

*   **Blynk/Thingspeak**: Kedua platform ini menyediakan API key atau token untuk otentikasi perangkat. Pastikan hanya perangkat yang berwenang yang dapat mengirim data.
*   **Verifikasi Koneksi**: Pastikan perangkat berhasil terhubung ke Wi-Fi dan platform IoT, serta data terkirim dengan benar.
*   **Pemantauan Log**: Periksa log di platform IoT untuk memastikan tidak ada upaya akses tidak sah atau anomali.

### MODUL 3: VIRTUAL PRIVATE NETWORK (VPN) LANJUTAN

#### Pertemuan 7: Protokol VPN (IPsec, SSL/TLS) & Konsep Tunneling

**1. Protokol VPN Lanjutan**

*   **IPsec (Internet Protocol Security)**:
    *   Deskripsi: Kumpulan protokol untuk mengamankan komunikasi IP dengan menyediakan autentikasi, integritas, dan kerahasiaan data. Beroperasi pada lapisan jaringan (Layer 3).
    *   **Komponen Utama IPsec**:
        *   **Authentication Header (AH)**: Menyediakan autentikasi dan integritas data, tetapi tidak enkripsi.
        *   **Encapsulating Security Payload (ESP)**: Menyediakan enkripsi, autentikasi, dan integritas data. Lebih umum digunakan.
        *   **Internet Key Exchange (IKE)**: Protokol untuk pertukaran kunci kriptografi secara aman. Memiliki dua fase:
            *   **Fase 1 (IKE SA)**: Membangun saluran komunikasi yang aman antara dua peer IPsec (Main Mode atau Aggressive Mode).
            *   **Fase 2 (IPsec SA)**: Membangun Security Association (SA) untuk lalu lintas data aktual (Quick Mode).
*   **SSL/TLS VPN (misal: OpenVPN)**:
    *   Deskripsi: Menggunakan protokol SSL/TLS (Secure Sockets Layer/Transport Layer Security) untuk membuat tunnel VPN. Beroperasi pada lapisan transport (Layer 4).
    *   Kelebihan: Sangat fleksibel, dapat melewati firewall dengan mudah (karena menggunakan port standar seperti 443/TCP), dan didukung luas.

**2. Konsep Tunneling**

Tunneling adalah proses enkapsulasi (membungkus) satu protokol jaringan di dalam protokol jaringan lain. Ini menciptakan "terowongan" virtual melalui jaringan yang tidak aman.

*   **Cara Kerja**: Paket data dari protokol asli dibungkus dengan header protokol tunneling, kemudian dikirim melalui jaringan. Di ujung lain, header tunneling dilepas, dan paket asli diteruskan.
*   **Contoh Protokol Tunneling**:
    *   **GRE (Generic Routing Encapsulation)**: Protokol tunneling yang dapat membungkus berbagai protokol jaringan di dalam paket IP. Tidak menyediakan enkripsi secara native.
    *   **IPIP (IP over IP)**: Protokol tunneling sederhana yang membungkus paket IP di dalam paket IP lain. Juga tidak menyediakan enkripsi.
*   **Hubungan dengan VPN**: VPN menggunakan tunneling untuk membuat jalur komunikasi pribadi, dan kemudian menambahkan enkripsi (misal: IPsec atau SSL/TLS) untuk mengamankan data di dalam tunnel tersebut.

#### Pertemuan 8: Praktik Konfigurasi Site-to-Site VPN (IPsec) - Bagian 1

**1. Site-to-Site VPN**

Site-to-Site VPN menghubungkan dua atau lebih jaringan lokal (misal: kantor cabang ke kantor pusat) secara aman melalui jaringan publik (internet). Ini menciptakan koneksi permanen antara dua router atau firewall.

**2. Konfigurasi IPsec Fase 1 (IKE) di Mikrotik**

Fase 1 IPsec (IKE) bertujuan untuk membangun saluran komunikasi yang aman antara dua peer VPN. Ini melibatkan negosiasi algoritma kriptografi dan pertukaran kunci.

*   **Langkah-langkah Konfigurasi di Mikrotik (WinBox/CLI)**:
    1.  **Buat IPsec Proposal (Definisi Algoritma Fase 1)**:
        *   CLI: `/ip ipsec proposal add name=ike_proposal auth-algorithms=sha256 enc-algorithms=aes-256-cbc dh-group=modp2048 lifetime=8h`
        *   WinBox: `IP -> IPsec -> Proposals -> Add`
            *   `Name`: ike_proposal
            *   `Auth. Algorithms`: sha256
            *   `Enc. Algorithms`: aes-256-cbc
            *   `DH Group`: modp2048
            *   `Lifetime`: 8h
    2.  **Buat IPsec Peer (Definisi Peer VPN dan Kunci)**:
        *   CLI: `/ip ipsec peer add address=203.0.113.254/32 secret=mysecretkey proposal=ike_proposal exchange-mode=ike2`
            (Ganti `203.0.113.254` dengan IP publik peer VPN lainnya, dan `mysecretkey` dengan kunci yang sama di kedua sisi).
        *   WinBox: `IP -> IPsec -> Peers -> Add`
            *   `Address`: IP publik peer lainnya
            *   `Secret`: mysecretkey
            *   `Proposal`: ike_proposal
            *   `Exchange Mode`: ike2 (atau main-mode jika menggunakan IKEv1)

*   **Verifikasi Fase 1**: Setelah konfigurasi di kedua Mikrotik, periksa status Security Association (SA) Fase 1:
    *   CLI: `/ip ipsec sa print`
    *   WinBox: `IP -> IPsec -> Installed SAs`
    *   Anda seharusnya melihat entri untuk IKE SA yang menunjukkan status `established` atau `active`.

#### Pertemuan 9: Praktik Konfigurasi Site-to-Site VPN (IPsec) - Bagian 2

**1. Konfigurasi IPsec Fase 2 (ESP/AH) di Mikrotik**

Fase 2 IPsec bertujuan untuk membangun SA untuk lalu lintas data aktual yang akan dienkripsi dan ditunnel melalui VPN. Ini menentukan jaringan mana yang akan melewati tunnel.

*   **Langkah-langkah Konfigurasi di Mikrotik (WinBox/CLI)**:
    1.  **Buat IPsec Policy (Definisi Lalu Lintas yang Akan Dienkripsi)**:
        *   CLI: `/ip ipsec policy add src-address=192.168.10.0/24 dst-address=192.168.20.0/24 protocol=all action=encrypt level=require tunnel=yes sa-src-address=192.0.2.1 sa-dst-address=203.0.113.254`
            (Ganti `192.168.10.0/24` dengan jaringan lokal Anda, `192.168.20.0/24` dengan jaringan lokal peer, `192.0.2.1` dengan IP publik Anda, dan `203.0.113.254` dengan IP publik peer).
        *   WinBox: `IP -> IPsec -> Policies -> Add`
            *   `Src. Address`: Jaringan lokal Anda
            *   `Dst. Address`: Jaringan lokal peer
            *   `Action`: encrypt
            *   `Level`: require
            *   `Tunnel`: yes
            *   `SA Src. Address`: IP publik Anda
            *   `SA Dst. Address`: IP publik peer
    2.  **Pastikan Firewall Mengizinkan Lalu Lintas IPsec**: Tambahkan aturan firewall untuk mengizinkan UDP port 500 (IKE), UDP port 4500 (NAT-T), dan protokol ESP (IP protocol 50) jika ada firewall di depan Mikrotik.

*   **Verifikasi Konektivitas End-to-End**:
    *   Dari VM di jaringan internal Mikrotik A, coba ping ke VM di jaringan internal Mikrotik B.
    *   Periksa status SA Fase 2:
        *   CLI: `/ip ipsec sa print`
        *   WinBox: `IP -> IPsec -> Installed SAs`
        *   Anda seharusnya melihat entri untuk IPsec SA yang menunjukkan lalu lintas data terenkripsi.

### MODUL 4: KEAMANAN APLIKASI WEB

#### Pertemuan 10: Kerentanan Web Umum (OWASP Top 10) & SQL Injection

**1. OWASP Top 10**

OWASP (Open Web Application Security Project) Top 10 adalah daftar konsensus tentang 10 risiko keamanan paling kritis terhadap aplikasi web. Ini diperbarui secara berkala dan berfungsi sebagai panduan penting bagi pengembang dan profesional keamanan.

*   **Beberapa Kerentanan dari OWASP Top 10 (2021)**:
    *   **A01:2021-Broken Access Control**: Kegagalan dalam menerapkan pembatasan akses yang tepat, memungkinkan pengguna untuk mengakses fungsi atau data yang tidak seharusnya.
    *   **A02:2021-Cryptographic Failures**: Kegagalan terkait kriptografi yang menyebabkan data sensitif terekspos atau sistem rentan terhadap serangan.
    *   **A03:2021-Injection**: Data yang tidak terpercaya dikirim ke interpreter sebagai bagian dari perintah atau query. (Termasuk SQL Injection, NoSQL Injection, Command Injection, dll.).
    *   **A04:2021-Insecure Design**: Cacat desain atau arsitektur yang memungkinkan serangan logis.
    *   **A05:2021-Security Misconfiguration**: Konfigurasi keamanan yang tidak tepat pada server, aplikasi, atau database.
    *   **A06:2021-Vulnerable and Outdated Components**: Penggunaan komponen (library, framework) dengan kerentanan yang diketahui.
    *   **A07:2021-Identification and Authentication Failures**: Kegagalan terkait fungsi identifikasi dan autentikasi pengguna.
    *   **A08:2021-Software and Data Integrity Failures**: Kegagalan dalam menjaga integritas perangkat lunak atau data.
    *   **A09:2021-Security Logging and Monitoring Failures**: Kurangnya logging dan monitoring yang memadai untuk mendeteksi dan merespons insiden.
    *   **A10:2021-Server-Side Request Forgery (SSRF)**: Aplikasi mengambil sumber daya jarak jauh tanpa memvalidasi URL yang disediakan pengguna, memungkinkan penyerang memaksa aplikasi mengirim permintaan ke target yang tidak diinginkan.

**2. SQL Injection**

SQL Injection adalah jenis serangan injeksi di mana penyerang menyisipkan atau "menyuntikkan" kode SQL berbahaya ke dalam input yang tidak divalidasi oleh aplikasi web. Ini memungkinkan penyerang untuk memanipulasi database, mencuri data, atau bahkan mengontrol server.

*   **Cara Kerja**: Aplikasi membangun query SQL secara dinamis menggunakan input pengguna tanpa membersihkan atau memvalidasi input tersebut dengan benar.
*   **Contoh Sederhana**: Jika aplikasi memiliki query seperti:
    `SELECT * FROM users WHERE username = '` + `[input_username]` + `' AND password = '` + `[input_password]` + `'`
    Penyerang bisa memasukkan `admin' OR '1'='1` sebagai username. Query akan menjadi:
    `SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = '...'`
    Karena `'1'='1'` selalu `True`, penyerang akan berhasil login sebagai admin.
*   **Dampak**: Pencurian data sensitif, modifikasi/penghapusan data, bypass autentikasi, eksekusi perintah pada sistem operasi (tergantung konfigurasi database).
*   **Pencegahan**: Menggunakan *prepared statements* dengan *parameterized queries*, validasi input yang ketat, *least privilege* untuk akun database, dan Web Application Firewall (WAF).

#### Pertemuan 11: Kerentanan Web (XSS) & Konsep WAF

**1. Cross-Site Scripting (XSS)**

XSS adalah jenis serangan injeksi kode sisi klien di mana penyerang menyisipkan skrip berbahaya (biasanya JavaScript) ke dalam halaman web yang kemudian dieksekusi di browser korban. Ini memungkinkan penyerang untuk mencuri cookie sesi, mengubah konten halaman, atau mengarahkan pengguna ke situs berbahaya.

*   **Jenis-jenis XSS**:
    *   **Stored XSS (Persistent XSS)**: Skrip berbahaya disimpan secara permanen di server (misal: di database komentar blog). Setiap kali pengguna lain mengunjungi halaman tersebut, skrip akan dieksekusi.
    *   **Reflected XSS (Non-Persistent XSS)**: Skrip berbahaya direfleksikan dari server ke browser korban sebagai bagian dari respons HTTP (misal: melalui parameter URL). Tidak disimpan di server.
    *   **DOM-based XSS**: Kerentanan terjadi di sisi klien, di mana skrip berbahaya dieksekusi karena manipulasi DOM (Document Object Model) oleh JavaScript di browser korban, tanpa interaksi dengan server.
*   **Dampak**: Pencurian cookie sesi (mengarah ke *session hijacking*), defacement website, pengalihan pengguna ke situs phishing, eksekusi kode arbitrer di browser korban.
*   **Pencegahan**: Sanitasi input (membersihkan input pengguna dari karakter berbahaya), *output encoding* (mengubah karakter khusus menjadi entitas HTML), Content Security Policy (CSP), dan Web Application Firewall (WAF).

**2. Web Application Firewall (WAF)**

WAF adalah jenis firewall yang dirancang khusus untuk melindungi aplikasi web dari serangan tingkat aplikasi. WAF beroperasi pada lapisan aplikasi (Layer 7) dari model OSI, menganalisis lalu lintas HTTP/HTTPS untuk mendeteksi dan memblokir serangan yang ditargetkan pada aplikasi web.

*   **Posisi WAF**: Biasanya ditempatkan di depan aplikasi web, bertindak sebagai proxy terbalik yang memeriksa semua permintaan masuk dan respons keluar.
*   **Cara Kerja WAF**:
    *   **Signature-based Detection**: Membandingkan lalu lintas dengan *signature* serangan yang diketahui (misal: pola SQL Injection, skrip XSS yang umum).
    *   **Anomaly-based Detection**: Membangun profil perilaku normal aplikasi dan menandai setiap penyimpangan sebagai potensi serangan.
    *   **Positive Security Model**: Hanya mengizinkan lalu lintas yang secara eksplisit didefinisikan sebagai "baik" atau "aman".
    *   **Negative Security Model**: Memblokir lalu lintas yang cocok dengan *signature* serangan yang diketahui.
*   **Manfaat**: Melindungi dari OWASP Top 10, mencegah *zero-day exploits* (dengan anomaly-based), membantu kepatuhan regulasi, dan memberikan visibilitas ke lalu lintas aplikasi web.

#### Pertemuan 12: Tools Pengujian Keamanan Web (Burp Suite/OWASP ZAP)

**1. Burp Suite (Community Edition)**

Burp Suite adalah platform terintegrasi untuk melakukan pengujian keamanan aplikasi web. Versi Community Edition menyediakan fitur dasar yang kuat untuk *ethical hacking*.

*   **Fitur Utama**:
    *   **Proxy**: Mencegat, melihat, dan memodifikasi semua lalu lintas antara browser dan aplikasi web. Ini adalah fitur paling fundamental.
    *   **Repeater**: Mengirim ulang permintaan HTTP yang dimodifikasi berkali-kali untuk menguji respons aplikasi.
    *   **Intruder**: Melakukan serangan otomatis yang dapat disesuaikan (fuzzing, brute-force, dictionary attacks) dengan memodifikasi permintaan secara sistematis.
    *   **Scanner (Limited in Community)**: Memindai kerentanan web secara otomatis (fitur penuh di versi Pro).

**2. OWASP ZAP (Zed Attack Proxy)**

OWASP ZAP adalah *open-source* *web application security scanner* yang dikelola oleh OWASP. Ini juga merupakan proxy intersepsi yang kuat.

*   **Fitur Utama**:
    *   **Proxy**: Mirip dengan Burp Suite, memungkinkan intersepsi dan modifikasi lalu lintas.
    *   **Automated Scanner**: Melakukan pemindaian kerentanan pasif dan aktif.
    *   **Fuzzer**: Mengirimkan berbagai payload ke input aplikasi untuk menemukan kerentanan.
    *   **Spider**: Mengidentifikasi semua halaman dan fungsionalitas dalam aplikasi web.
    *   **Brute Force**: Melakukan serangan brute-force pada formulir autentikasi.

**3. Cara Penggunaan (Umum)**:

1.  **Konfigurasi Proxy**: Atur browser web Anda untuk menggunakan Burp Suite atau OWASP ZAP sebagai proxy HTTP/HTTPS (biasanya `127.0.0.1` dan port `8080`).
2.  **Intersepsi**: Saat Anda menjelajahi aplikasi web, permintaan dan respons akan dicegat oleh proxy. Anda dapat melihat, memodifikasi, dan meneruskannya.
3.  **Analisis & Eksploitasi**: Gunakan fitur lain seperti Repeater, Intruder/Fuzzer untuk menguji kerentanan yang ditemukan atau dicurigai.

#### Pertemuan 13: Konsep Web Application Firewall (WAF)

**1. Definisi dan Peran WAF**

Web Application Firewall (WAF) adalah solusi keamanan yang dirancang khusus untuk melindungi aplikasi web dari berbagai serangan siber. Berbeda dengan firewall jaringan tradisional yang beroperasi pada lapisan jaringan (Layer 3/4), WAF beroperasi pada lapisan aplikasi (Layer 7) dari model OSI.

*   **Mengapa WAF Diperlukan?**:
    *   Firewall jaringan tidak dapat memahami konteks lalu lintas HTTP/HTTPS, sehingga tidak efektif melawan serangan tingkat aplikasi seperti SQL Injection atau XSS.
    *   WAF dapat menganalisis payload permintaan dan respons HTTP/HTTPS secara mendalam untuk mendeteksi pola serangan yang spesifik untuk aplikasi web.

**2. Cara Kerja WAF**

WAF memeriksa setiap permintaan HTTP/HTTPS yang masuk ke aplikasi web dan setiap respons yang keluar dari aplikasi web. Berdasarkan seperangkat aturan keamanan, WAF dapat memblokir, memberi peringatan, atau mengizinkan lalu lintas.

*   **Model Keamanan**:
    *   **Negative Security Model (Blacklisting)**: Memblokir lalu lintas yang cocok dengan *signature* serangan yang diketahui. Ini adalah pendekatan yang paling umum.
    *   **Positive Security Model (Whitelisting)**: Hanya mengizinkan lalu lintas yang secara eksplisit didefinisikan sebagai "baik" atau "aman". Ini lebih aman tetapi lebih sulit dikelola.
*   **Mekanisme Deteksi**:
    *   **Signature-based Detection**: Menggunakan database *signature* serangan yang diketahui (mirip antivirus) untuk mengidentifikasi dan memblokir serangan seperti SQL Injection, XSS, Command Injection.
    *   **Anomaly-based Detection**: Membangun profil perilaku normal aplikasi web dan menandai setiap penyimpangan dari profil tersebut sebagai potensi serangan. Ini efektif untuk mendeteksi *zero-day exploits*.
*   **Mitigasi OWASP Top 10**: WAF sangat efektif dalam memitigasi sebagian besar kerentanan yang tercantum dalam OWASP Top 10, terutama Injection, Cross-Site Scripting (XSS), Broken Access Control (tertentu), dan Security Misconfiguration.

**3. Jenis-jenis WAF dan Implementasi**

*   **Hardware WAF**: Perangkat fisik yang ditempatkan di jaringan.
*   **Software WAF**: Aplikasi yang diinstal pada server atau VM.
*   **Cloud-based WAF**: Layanan yang disediakan oleh penyedia cloud (misal: Cloudflare WAF, AWS WAF). Ini populer karena skalabilitas dan kemudahan pengelolaan.

### MODUL 5: KEAMANAN CLOUD & CONTAINER

#### Pertemuan 14: Model Keamanan Cloud & IAM di Cloud

**1. Model Keamanan Cloud (Shared Responsibility Model)**

Shared Responsibility Model adalah konsep fundamental dalam keamanan cloud yang menjelaskan pembagian tanggung jawab keamanan antara penyedia layanan cloud (CSP) dan pelanggan cloud. Tanggung jawab ini bervariasi tergantung pada model layanan cloud yang digunakan (IaaS, PaaS, SaaS).

*   **Penyedia Cloud (CSP) Bertanggung Jawab atas "Security *of* the Cloud"**:
    *   Keamanan infrastruktur fisik (data center, hardware, jaringan).
    *   Keamanan virtualisasi (hypervisor).
    *   Keamanan layanan dasar yang mereka sediakan.
*   **Pelanggan Cloud Bertanggung Jawab atas "Security *in* the Cloud"**:
    *   **IaaS (Infrastructure as a Service)**: Pelanggan bertanggung jawab atas sistem operasi, aplikasi, data, konfigurasi jaringan, dan firewall virtual.
    *   **PaaS (Platform as a Service)**: Pelanggan bertanggung jawab atas aplikasi dan data mereka. Penyedia mengelola platform (OS, runtime, middleware).
    *   **SaaS (Software as a Service)**: Pelanggan bertanggung jawab atas data mereka, konfigurasi pengguna, dan manajemen akses. Penyedia mengelola seluruh aplikasi dan infrastruktur.

**2. Identity and Access Management (IAM) di Cloud**

IAM adalah kerangka kerja keamanan yang memungkinkan organisasi untuk mengelola identitas digital dan mengontrol akses ke sumber daya cloud. Ini adalah pilar utama keamanan cloud.

*   **Fungsi Utama IAM**:
    *   **Manajemen Identitas**: Membuat, mengelola, dan menghapus identitas pengguna (manusia dan mesin).
    *   **Autentikasi**: Memverifikasi identitas pengguna (misal: username/password, MFA).
    *   **Otorisasi**: Menentukan sumber daya apa yang dapat diakses oleh identitas yang terautentikasi dan tindakan apa yang dapat mereka lakukan.
*   **Prinsip Least Privilege**: Menerapkan prinsip ini di cloud sangat penting. Berikan hanya izin minimum yang diperlukan untuk pengguna atau layanan untuk melakukan tugas mereka.
*   **Komponen IAM Umum (misal: AWS IAM)**:
    *   **Users**: Identitas individu.
    *   **Groups**: Kumpulan user yang memiliki izin yang sama.
    *   **Roles**: Izin sementara yang dapat diasumsikan oleh user atau layanan.
    *   **Policies**: Dokumen JSON yang mendefinisikan izin (apa yang boleh dilakukan, pada sumber daya apa, dalam kondisi apa).

#### Pertemuan 15: Konsep & Risiko Keamanan Container (Docker)

**1. Konsep Container (Docker)**

Container (misal: Docker) adalah teknologi virtualisasi tingkat sistem operasi yang memungkinkan pengembang untuk mengemas aplikasi dan semua dependensinya (library, konfigurasi) ke dalam unit yang terisolasi dan portabel. Berbeda dengan Virtual Machine (VM) yang memvirtualisasikan seluruh hardware, container berbagi kernel sistem operasi host.

*   **Perbedaan Utama dengan VM**:
    *   **VM**: Memiliki OS tamu sendiri, isolasi lebih kuat, overhead lebih besar.
    *   **Container**: Berbagi kernel OS host, lebih ringan, startup lebih cepat, isolasi tingkat proses.
*   **Komponen Docker**:
    *   **Dockerfile**: Berkas teks yang berisi instruksi untuk membangun image Docker.
    *   **Image**: Template read-only yang berisi aplikasi dan semua dependensinya.
    *   **Container**: Instansi yang dapat dijalankan dari sebuah image.
    *   **Registry**: Repositori untuk menyimpan dan berbagi image Docker (misal: Docker Hub).

**2. Risiko Keamanan Container**

Meskipun container menawarkan banyak manfaat, mereka juga memperkenalkan risiko keamanan baru:

*   **Kerentanan Image Dasar**: Jika image dasar yang digunakan (misal: `ubuntu:latest`) memiliki kerentanan, semua container yang dibangun di atasnya akan rentan.
*   **Konfigurasi Docker Daemon yang Tidak Aman**: Konfigurasi default atau yang salah dapat membuka celah keamanan (misal: API Docker yang terekspos).
*   **Privilege Escalation**: Penyerang dapat keluar dari container dan mendapatkan akses ke sistem host jika container dijalankan dengan hak akses yang berlebihan (misal: sebagai root).
*   **Supply Chain Attacks**: Kerentanan dapat disuntikkan ke dalam image selama proses build atau dari registry yang tidak terpercaya.
*   **Kurangnya Segmentasi Jaringan Antar Container**: Secara default, container dalam satu host dapat berkomunikasi satu sama lain, yang dapat memungkinkan pergerakan lateral penyerang.
*   **Manajemen Secret yang Buruk**: Menyimpan kredensial atau kunci API langsung di Dockerfile atau image.

#### Pertemuan 16: Praktik Dasar Mengamankan Dockerfile dan Image Container

**1. Mengamankan Dockerfile**

Dockerfile adalah "resep" untuk membangun image Docker. Mengamankan Dockerfile adalah langkah pertama dalam mengamankan container.

*   **Praktik Terbaik Mengamankan Dockerfile**:
    *   **Gunakan Image Dasar Minimal**: Pilih image dasar yang kecil dan hanya berisi komponen yang diperlukan (misal: `alpine`, `distroless`). Ini mengurangi permukaan serangan.
    *   **Jalankan Aplikasi dengan User Non-Root**: Hindari menjalankan proses aplikasi sebagai user `root` di dalam container. Gunakan instruksi `USER`.
    *   **Hapus Dependensi yang Tidak Perlu**: Hapus tool atau library yang hanya diperlukan selama proses build (`RUN --mount=type=cache` atau multi-stage builds).
    *   **Gunakan `COPY` daripada `ADD`**: `COPY` hanya menyalin file, `ADD` dapat mengekstrak tarball dan mengambil URL, yang berpotensi memperkenalkan kerentanan.
    *   **Tentukan `WORKDIR`**: Atur direktori kerja untuk aplikasi.
    *   **Pindai Kerentanan Selama CI/CD**: Integrasikan pemindai kerentanan image ke dalam pipeline CI/CD.

**2. Membangun dan Memindai Image Container**

Setelah Dockerfile diamankan, langkah selanjutnya adalah membangun image dan memindainya untuk kerentanan.

*   **Membangun Image**: `docker build -t my-secure-app:latest .`
*   **Tool Pemindai Kerentanan Image**:
    *   **Trivy**: *Open-source* dan mudah digunakan, dapat memindai kerentanan OS, library, dan konfigurasi.
        *   Contoh: `trivy image my-secure-app:latest`
    *   **Clair**: *Open-source* dan lebih kompleks, menyediakan analisis kerentanan statis untuk image Docker.
    *   **Snyk**: Komersial, tetapi menawarkan versi gratis untuk proyek *open-source*.

*   **Analisis Hasil Pemindaian**: Pemindai akan melaporkan kerentanan yang ditemukan, tingkat keparahan, dan saran perbaikan. Penting untuk meninjau laporan ini dan memprioritaskan perbaikan kerentanan kritis.

## LAMPIRAN - GLOSARIUM

*   **AH (Authentication Header)**: Komponen IPsec yang menyediakan autentikasi dan integritas data, tetapi tidak enkripsi.
*   **Anomaly-based Detection (WAF)**: Metode deteksi WAF yang membangun profil perilaku normal aplikasi dan menandai setiap penyimpangan sebagai potensi serangan.
*   **Container (Docker)**: Teknologi virtualisasi tingkat sistem operasi yang mengemas aplikasi dan semua dependensinya ke dalam unit yang terisolasi dan portabel, berbagi kernel OS host.
*   **COPY (Dockerfile)**: Instruksi Dockerfile untuk menyalin file atau direktori dari sumber ke tujuan dalam image.
*   **Cross-Site Scripting (XSS)**: Jenis serangan injeksi kode sisi klien di mana penyerang menyisipkan skrip berbahaya ke dalam halaman web yang dieksekusi di browser korban.
*   **Dockerfile**: Berkas teks yang berisi instruksi untuk membangun image Docker.
*   **Docker Image**: Template read-only yang berisi aplikasi dan semua dependensinya, digunakan untuk membuat container.
*   **Docker Registry**: Repositori untuk menyimpan dan berbagi image Docker (misal: Docker Hub).
*   **DOM-based XSS**: Jenis XSS di mana kerentanan terjadi di sisi klien karena manipulasi DOM oleh JavaScript di browser korban.
*   **ESP (Encapsulating Security Payload)**: Komponen IPsec yang menyediakan enkripsi, autentikasi, dan integritas data.
*   **Fuzzing**: Teknik pengujian keamanan yang melibatkan pengiriman data input yang tidak valid, tidak terduga, atau acak ke aplikasi untuk menemukan kerentanan.
*   **GRE (Generic Routing Encapsulation)**: Protokol tunneling yang dapat membungkus berbagai protokol jaringan di dalam paket IP, tidak menyediakan enkripsi secara native.
*   **HTTP (Hypertext Transfer Protocol)**: Protokol dasar yang digunakan untuk komunikasi data di World Wide Web.
*   **IAM (Identity and Access Management)**: Kerangka kerja keamanan yang memungkinkan organisasi untuk mengelola identitas digital dan mengontrol akses ke sumber daya.
*   **IKE (Internet Key Exchange)**: Protokol untuk pertukaran kunci kriptografi secara aman dalam IPsec, memiliki Fase 1 dan Fase 2.
*   **Injection (OWASP)**: Kerentanan di mana data yang tidak terpercaya dikirim ke interpreter sebagai bagian dari perintah atau query (misal: SQL Injection, Command Injection).
*   **Internet of Things (IoT)**: Jaringan objek fisik yang tertanam dengan sensor, perangkat lunak, dan teknologi lain untuk menghubungkan dan bertukar data melalui internet.
*   **IPsec (Internet Protocol Security)**: Kumpulan protokol untuk mengamankan komunikasi IP dengan menyediakan autentikasi, integritas, dan kerahasiaan data.
*   **IPIP (IP over IP)**: Protokol tunneling sederhana yang membungkus paket IP di dalam paket IP lain, tidak menyediakan enkripsi.
*   **OWASP Top 10**: Daftar konsensus tentang 10 risiko keamanan paling kritis terhadap aplikasi web, diperbarui secara berkala.
*   **PaaS (Platform as a Service)**: Model layanan cloud di mana penyedia mengelola platform (OS, runtime, middleware) dan pelanggan bertanggung jawab atas aplikasi dan data mereka.
*   **Privilege Escalation (Container)**: Penyerang dapat keluar dari container dan mendapatkan akses ke sistem host jika container dijalankan dengan hak akses yang berlebihan.
*   **Python `requests` library**: Library Python populer untuk membuat permintaan HTTP.
*   **Python `socket` library**: Library Python yang menyediakan akses ke antarmuka socket BSD standar, memungkinkan pemrograman jaringan tingkat rendah.
*   **Reflected XSS**: Jenis XSS di mana skrip berbahaya direfleksikan dari server ke browser korban sebagai bagian dari respons HTTP, tidak disimpan di server.
*   **SaaS (Software as a Service)**: Model layanan cloud di mana penyedia mengelola seluruh aplikasi dan infrastruktur, pelanggan bertanggung jawab atas data dan manajemen akses.
*   **Shared Responsibility Model (Cloud)**: Konsep fundamental dalam keamanan cloud yang menjelaskan pembagian tanggung jawab keamanan antara penyedia layanan cloud dan pelanggan cloud.
*   **Signature-based Detection (WAF)**: Metode deteksi WAF yang membandingkan lalu lintas dengan *signature* serangan yang diketahui.
*   **Site-to-Site VPN**: Jenis VPN yang menghubungkan dua atau lebih jaringan lokal secara aman melalui jaringan publik.
*   **SQL Injection**: Jenis serangan injeksi di mana penyerang menyisipkan kode SQL berbahaya ke dalam input yang tidak divalidasi oleh aplikasi web untuk memanipulasi database.
*   **SSL/TLS VPN**: Jenis VPN yang menggunakan protokol SSL/TLS untuk membuat tunnel VPN (misal: OpenVPN).
*   **Stored XSS (Persistent XSS)**: Jenis XSS di mana skrip berbahaya disimpan secara permanen di server (misal: di database komentar blog).
*   **Supply Chain Attacks (Container)**: Kerentanan dapat disuntikkan ke dalam image selama proses build atau dari registry yang tidak terpercaya.
*   **Tunneling**: Proses enkapsulasi (membungkus) satu protokol jaringan di dalam protokol jaringan lain untuk menciptakan "terowongan" virtual.
*   **Web Application Firewall (WAF)**: Jenis firewall yang dirancang khusus untuk melindungi aplikasi web dari serangan tingkat aplikasi, beroperasi pada Layer 7.

## LAMPIRAN - DAFTAR PUSTAKA

Berikut adalah daftar pustaka dan sumber referensi yang digunakan dalam penyusunan modul ini, serta rekomendasi untuk pendalaman materi lebih lanjut:

### Buku Teks dan Publikasi Ilmiah
*   Stallings, William. (2017). *Cryptography and Network Security: Principles and Practice*. Pearson.
*   Easttom, William. (2018). *Computer Security Fundamentals*. Pearson.
*   Kim, David, & Solomon, Michael G. (2019). *Fundamentals of Information Systems Security*. Jones & Bartlett Learning.
*   Vacca, John R. (2017). *Cyber Security and IT Infrastructure Protection*. Syngress.
*   Python Software Foundation. (2024). *The Python Tutorial*. [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
*   Reitz, Kenneth. (2024). *Requests: HTTP for Humans™*. [https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)
*   Docker. (2024). *Docker Documentation*. [https://docs.docker.com/](https://docs.docker.com/)
*   OWASP Foundation. (2021). *OWASP Top Ten Web Application Security Risks*. [https://owasp.org/www-project-top-10/](https://owasp.org/www-project-top-10/)
*   NIST. (2024). *IoT Cybersecurity Program*. [https://www.nist.gov/cybersecurity/internet-things-iot](https://www.nist.gov/cybersecurity/internet-things-iot)

### Dokumentasi Resmi Vendor/Organisasi
*   **Python Documentation**: Official Python language documentation.
    *   [https://docs.python.org/](https://docs.python.org/)
*   **Docker Documentation**: Official documentation for Docker products.
    *   [https://docs.docker.com/](https://docs.docker.com/)
*   **MikroTik Wiki**: Official documentation for MikroTik RouterOS and RouterBOARD devices.
    *   [https://wiki.mikrotik.com/](https://wiki.mikrotik.com/)
*   **OWASP Top 10**: The OWASP Foundation.
    *   [https://owasp.org/www-project-top-10/](https://owasp.org/www-project-top-10/)
*   **NIST Cybersecurity Framework (CSF)**: Framework for Improving Critical Infrastructure Cybersecurity. National Institute of Standards and Technology.
    *   [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
*   **Blynk Documentation**: Official documentation for Blynk IoT platform.
    *   [https://docs.blynk.io/](https://docs.blynk.io/)
*   **Thingspeak Documentation**: Official documentation for Thingspeak IoT analytics platform.
    *   [https://thingspeak.com/docs](https://thingspeak.com/docs)

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
*   **PortSwigger Web Security Academy**: Sumber belajar gratis untuk kerentanan web dan Burp Suite.
    *   [https://portswigger.net/web-security](https://portswigger.net/web-security)
*   **YouTube Channels**: Berbagai kanal yang menyediakan tutorial dan penjelasan tentang keamanan jaringan, pemrograman Python, dan IoT (misal: The Cyber Mentor, NetworkChuck, FreeCodeCamp).

### Tools dan Software Referensi
*   **Python**: [https://www.python.org/](https://www.python.org/)
*   **Docker**: [https://www.docker.com/](https://www.docker.com/)
*   **MikroTik RouterOS**: [https://mikrotik.com/](https://mikrotik.com/)
*   **VirtualBox**: [https://www.virtualbox.org/](https://www.virtualbox.org/)
*   **VMware Workstation Player**: [https://www.vmware.com/products/workstation-player.html](https://www.vmware.com/products/workstation-player.html)
*   **Burp Suite Community Edition**: [https://portswigger.net/burp/communitydownload](https://portswigger.net/burp/communitydownload)
*   **OWASP ZAP**: [https://www.zaproxy.org/](https://www.zaproxy.org/)
*   **DVWA (Damn Vulnerable Web Application)**: [https://dvwa.co.uk/](https://dvwa.co.uk/)
*   **Juice Shop**: [https://owasp.org/www-project-juice-shop/](https://owasp.org/www-project-juice-shop/)
*   **Trivy**: [https://aquasecurity.github.io/trivy/](https://aquasecurity.github.io/trivy/)
*   **Arduino IDE / PlatformIO**: Untuk pemrograman mikrokontroler.

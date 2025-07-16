# Sistem Parkir Otomatis

Sistem parkir otomatis berbasis Python dan Arduino yang terintegrasi dengan kamera untuk deteksi plat nomor kendaraan.

## Fitur

- Deteksi plat nomor kendaraan menggunakan kamera
- Pengendalian gate parkir otomatis
- Pencatatan transaksi parkir
- Antarmuka berbasis jaringan
- Integrasi dengan Arduino

## Persyaratan Sistem

### Server
- Python 3.7+
- OpenCV
- MySQL Server
- Kamera USB/Webcam

### Arduino
- Arduino Uno/Mega dengan Ethernet Shield
- Sensor IR/Ultrasonic (2x)
- Servo Motor
- LED (2x)
- Buzzer

## Instalasi

1. Clone repositori ini
2. Buat database MySQL:
   ```bash
   mysql -u root -p < database/schema.sql
   ```
3. Install dependensi Python:
   ```bash
   pip install -r requirements.txt
   ```
4. Upload kode Arduino ke board
5. Sesuaikan konfigurasi di `server/config.py`

## Cara Menjalankan

1. Jalankan server:
   ```bash
   cd server
   python -m main
   ```

2. Nyalakan Arduino

3. Gunakan aplikasi client untuk berinteraksi dengan sistem

## Struktur Folder

```
sistem_parkir/
├── server/           # Kode server Python
├── arduino/         # Kode Arduino
├── database/        # Skema database
└── README.md        # Dokumentasi
```

## Konfigurasi

### Server
Edit file `server/config.py` untuk mengatur:
- Alamat IP dan port server
- Kredensial database
- Konfigurasi kamera

### Arduino
Edit bagian berikut di `arduino/arduino_gate.ino`:
- Alamat IP Arduino
- Pin untuk sensor dan aktuator

## Penggunaan

1. Saat kendaraan mendekati pintu masuk:
   - Kamera akan mendeteksi plat nomor
   - Gate akan terbuka
   - Transaksi masuk dicatat

2. Saat kendaraan keluar:
   - Kamera mendeteksi plat nomor
   - Sistem menghitung biaya parkir
   - Gate terbuka setelah pembayaran
   - Transaksi keluar dicatat

## Troubleshooting

1. Jika kamera tidak terdeteksi:
   - Periksa koneksi kamera
   - Pastikan tidak ada aplikasi lain yang menggunakan kamera

2. Jika koneksi ke database gagal:
   - Periksa kredensial database
   - Pastikan MySQL server berjalan

3. Jika Arduino tidak merespons:
   - Periksa koneksi jaringan
   - Pastikan IP Arduino benar
   - Periksa kabel Ethernet

## Lisensi

MIT License

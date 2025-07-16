-- Buat database
CREATE DATABASE IF NOT EXISTS parkir_db;
USE parkir_db;

-- Tabel kendaraan
CREATE TABLE IF NOT EXISTS kendaraan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plat_nomor VARCHAR(20) UNIQUE NOT NULL,
    jenis_kendaraan VARCHAR(50),
    pemilik VARCHAR(100),
    dibuat_pada TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabel transaksi parkir
CREATE TABLE IF NOT EXISTS transaksi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plat_nomor VARCHAR(20) NOT NULL,
    waktu_masuk DATETIME NOT NULL,
    waktu_keluar DATETIME,
    durasi INT, -- dalam menit
    biaya DECIMAL(10,2),
    status ENUM('MASUK', 'KELUAR') DEFAULT 'MASUK',
    dibuat_pada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plat_nomor) REFERENCES kendaraan(plat_nomor)
);

-- Tambahkan index untuk pencarian yang lebih cepat
CREATE INDEX idx_plat_nomor ON transaksi(plat_nomor);
CREATE INDEX idx_waktu_masuk ON transaksi(waktu_masuk);
CREATE INDEX idx_status ON transaksi(status);

-- Data dummy untuk testing
INSERT IGNORE INTO kendaraan (plat_nomor, jenis_kendaraan, pemilik) VALUES
('B1234ABC', 'Mobil', 'John Doe'),
('B5678XYZ', 'Motor', 'Jane Smith'),
('B9999ZZZ', 'Mobil', 'Bob Wilson');

-- Trigger untuk menghapus data lama (opsional)
DELIMITER //
CREATE EVENT IF NOT EXISTS hapus_data_lama
ON SCHEDULE EVERY 1 MONTH
DO
BEGIN
    DELETE FROM transaksi 
    WHERE waktu_masuk < DATE_SUB(NOW(), INTERVAL 3 MONTH);
END //
DELIMITER ;

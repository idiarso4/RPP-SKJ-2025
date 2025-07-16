import mysql.connector
from datetime import datetime
from .config import DB_CONFIG

class Database:
    def __init__(self):
        self.connection = None
        self.connect()
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            print("Koneksi database berhasil")
        except mysql.connector.Error as err:
            print(f"Error koneksi database: {err}")
    
    def save_vehicle_entry(self, plat_nomor):
        try:
            cursor = self.connection.cursor()
            sql = """
                INSERT INTO transaksi (plat_nomor, waktu_masuk, status)
                VALUES (%s, %s, 'MASUK')
            """
            cursor.execute(sql, (plat_nomor, datetime.now()))
            self.connection.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error menyimpan data kendaraan: {err}")
            return None
    
    def save_vehicle_exit(self, plat_nomor):
        try:
            cursor = self.connection.cursor()
            # Hitung biaya parkir (contoh: Rp2000 per jam)
            sql = """
                UPDATE transaksi 
                SET waktu_keluar = %s,
                    durasi = TIMESTAMPDIFF(MINUTE, waktu_masuk, %s),
                    biaya = TIMESTAMPDIFF(HOUR, waktu_masuk, %s) * 2000,
                    status = 'KELUAR'
                WHERE plat_nomor = %s AND status = 'MASUK'
                ORDER BY waktu_masuk DESC LIMIT 1
            """
            now = datetime.now()
            cursor.execute(sql, (now, now, now, plat_nomor))
            self.connection.commit()
            
            # Ambil data transaksi terbaru
            cursor.execute("""
                SELECT * FROM transaksi 
                WHERE plat_nomor = %s 
                ORDER BY id DESC LIMIT 1
            """, (plat_nomor,))
            return cursor.fetchone()
            
        except mysql.connector.Error as err:
            print(f"Error update data kendaraan: {err}")
            return None
    
    def close(self):
        if self.connection:
            self.connection.close()
            print("Koneksi database ditutup")

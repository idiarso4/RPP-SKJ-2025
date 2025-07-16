import cv2
import numpy as np
from datetime import datetime
import os

class Camera:
    def __init__(self):
        from .config import CAMERA_CONFIG
        self.camera = cv2.VideoCapture(CAMERA_CONFIG['device_id'])
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_CONFIG['width'])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_CONFIG['height'])
        
        # Buat folder untuk menyimpan gambar
        self.save_dir = 'captures'
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    def capture_plate(self):
        """Ambil gambar plat nomor"""
        ret, frame = self.camera.read()
        if ret:
            # Simpan gambar
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.save_dir}/plate_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            
            # Proses gambar untuk deteksi plat (contoh sederhana)
            # Di sini bisa ditambahkan logika OCR yang lebih canggih
            plate_number = self.detect_plate_number(frame)
            
            return {
                'success': True,
                'plate_number': plate_number,
                'image_path': filename
            }
        return {'success': False, 'error': 'Gagal mengambil gambar'}
    
    def detect_plate_number(self, image):
        """Fungsi untuk mendeteksi plat nomor"""
        # Ini adalah contoh sederhana
        # Di implementasi nyata, gunakan library seperti OpenALPR atau EasyOCR
        try:
            # Konversi ke grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Thresholding
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
            
            # Simpan gambar hasil thresholding (untuk debugging)
            cv2.imwrite(f"{self.save_dir}/thresh.jpg", thresh)
            
            # Di sini seharusnya ada logika deteksi karakter OCR
            # Untuk saat ini kita kembalikan nilai dummy
            return "B1234ABC"
            
        except Exception as e:
            print(f"Error deteksi plat: {e}")
            return "UNKNOWN"
    
    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()

# 🔐 Praktikum: Implementasi Kriptografi Dasar

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan praktikum ini, peserta didik mampu:
1. Menggunakan OpenSSL untuk operasi kriptografi dasar
2. Menerapkan enkripsi simetris dan asimetris
3. Membuat dan memverifikasi tanda tangan digital
4. Bekerja dengan sertifikat digital
5. Menerapkan kriptografi dalam skrip sederhana

## 📋 Persiapan

### 1. Peralatan yang Diperlukan
- Komputer dengan sistem operasi Linux (disarankan Ubuntu/Kali Linux)
- Akses terminal dengan hak akses root/sudo
- Koneksi internet untuk mengunduh paket yang diperlukan
- Teks editor (nano, vim, atau VS Code)

### 2. Instalasi Paket
```bash
# Update package list
sudo apt update

# Install paket yang diperlukan
sudo apt install -y openssl gpg python3-pip

# Install library kriptografi Python
pip3 install cryptography pycryptodome
```

## 📝 Langkah Kerja

### 1. Enkripsi Simetris dengan OpenSSL

#### 1.1 Membuat File Teks
```bash
echo "Ini adalah pesan rahasia untuk praktikum kriptografi" > rahasia.txt
cat rahasia.txt
```

#### 1.2 Enkripsi dengan AES-256
```bash
# Enkripsi file
openssl enc -aes-256-cbc -salt -in rahasia.txt -out rahasia.enc

# Lihat isi file terenkripsi
hexdump -C rahasia.enc | head -n 5

# Dekripsi file
openssl enc -d -aes-256-cbc -in rahasia.enc -out hasil_dekripsi.txt

# Verifikasi isi file
diff rahasia.txt hasil_dekripsi.txt && echo "File identik"
```

### 2. Enkripsi Asimetris dengan OpenSSL

#### 2.1 Membuat Pasangan Kunci
```bash
# Buat private key RSA 2048-bit
openssl genpkey -algorithm RSA -out private_key.pem -aes256 -pkeyopt rsa_keygen_bits:2048

# Ekstrak public key
openssl rsa -pubout -in private_key.pem -out public_key.pem

# Lihat isi kunci
cat private_key.pem
cat public_key.pem
```

#### 2.2 Enkripsi dan Dekripsi
```bash
# Enkripsi dengan public key
echo "Pesan rahasia untuk enkripsi asimetris" > pesan.txt
openssl rsautl -encrypt -inkey public_key.pem -pubin -in pesan.txt -out pesan.enc

# Dekripsi dengan private key
openssl rsautl -decrypt -inkey private_key.pem -in pesan.enc -out pesan_dekripsi.txt

# Bandingkan isi file
cat pesan_dekripsi.txt
diff pesan.txt pesan_dekripsi.txt && echo "Pesan berhasil didekripsi"
```

### 3. Tanda Tangan Digital

#### 3.1 Membuat Hash dan Tanda Tangan
```bash
# Buat hash dari file
openssl dgst -sha256 -sign private_key.pem -out signature.bin pesan.txt

# Verifikasi tanda tangan
openssl dgst -sha256 -verify public_key.pem -signature signature.bin pesan.txt
```

### 4. Bekerja dengan Sertifikat Digital

#### 4.1 Membuat Sertifikat Self-Signed
```bash
# Buat private key
openssl genrsa -out server.key 2048

# Buat Certificate Signing Request (CSR)
openssl req -new -key server.key -out server.csr -subj "/C=ID/ST=Jawa Tengah/L=Banjarnegara/O=SMKN 1 Punggelan/CN=smkn1pgl.sch.id"

# Buat sertifikat self-signed (valid 365 hari)
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# Lihat detail sertifikat
openssl x509 -in server.crt -text -noout
```

### 5. Implementasi dengan Python

#### 5.1 Enkripsi Simetris dengan PyCryptodome
Buat file `enkripsi_simetris.py`:
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_aes(plaintext, key):
    # Generate random IV
    iv = get_random_bytes(16)
    
    # Create cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encrypt the data
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    
    # Combine IV and ciphertext
    return base64.b64encode(iv + ciphertext).decode()

def decrypt_aes(encrypted_data, key):
    # Decode from base64
    data = base64.b64decode(encrypted_data)
    
    # Extract IV and ciphertext
    iv = data[:16]
    ciphertext = data[16:]
    
    # Create cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the data
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return plaintext.decode()

# Contoh penggunaan
if __name__ == "__main__":
    # Kunci harus 16, 24, atau 32 bytes (AES-128, AES-192, atau AES-256)
    key = get_random_bytes(32)  # AES-256
    
    # Pesan yang akan dienkripsi
    message = "Ini adalah pesan rahasia untuk praktikum kriptografi"
    
    # Enkripsi
    encrypted = encrypt_aes(message, key)
    print(f"Encrypted: {encrypted}")
    
    # Dekripsi
    decrypted = decrypt_aes(encrypted, key)
    print(f"Decrypted: {decrypted}")
    
    # Verifikasi
    print(f"Pesan asli dan hasil dekripsi {'sama' if message == decrypted else 'berbeda'}")
```

#### 5.2 Menjalankan Program
```bash
python3 enkripsi_simetris.py
```

## 📋 Laporan Praktikum

### 1. Pendahuluan
Jelaskan tujuan dan latar belakang praktikum kriptografi ini.

### 2. Alat dan Bahan
Daftar semua peralatan dan perangkat lunak yang digunakan.

### 3. Langkah Kerja
Jelaskan langkah-langkah yang telah dilakukan selama praktikum.

### 4. Hasil Pengamatan
#### 4.1 Enkripsi Simetris
```
# Tempelkan output perintah OpenSSL untuk enkripsi/dekripsi
```

#### 4.2 Enkripsi Asimetris
```
# Tempelkan output pembuatan kunci dan proses enkripsi/dekripsi
```

#### 4.3 Tanda Tangan Digital
```
# Tempelkan hasil pembuatan dan verifikasi tanda tangan
```

#### 4.4 Implementasi Python
```
# Tempelkan output dari program Python yang dibuat
```

### 5. Analisis
1. Bandingkan kecepatan enkripsi simetris dan asimetris. Mengapa ada perbedaan?
2. Apa kelebihan dan kekurangan tanda tangan digital dibanding tanda tangan konvensional?
3. Mengapa penting untuk menggunakan salt dalam enkripsi?
4. Apa yang terjadi jika kunci private hilang dalam sistem enkripsi asimetris?

### 6. Kesimpulan
Berikan kesimpulan dari praktikum yang telah dilakukan.

## 📌 Tantangan Lanjutan
1. Coba implementasikan protokol pertukaran kunci Diffie-Hellman dengan Python
2. Buat program untuk mengenkripsi seluruh isi direktori
3. Implementasikan skema enkripsi hybrid (gabungan simetris dan asimetris)

## ⚠️ Keamanan dan Etika
1. Jangan pernah membagikan kunci private kepada siapapun
2. Selalu backup kunci dan sertifikat dengan aman
3. Gunakan panjang kunci yang memadai (minimal 2048-bit untuk RSA)
4. Selalu validasi sertifikat sebelum digunakan

## 📚 Referensi
1. OpenSSL Documentation: https://www.openssl.org/docs/
2. PyCryptodome Documentation: https://pycryptodome.readthedocs.io/
3. NIST Special Publication 800-175B: Guideline for Using Cryptographic Standards
4. RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3

---
<div align="center">
  <p>Lembar Kerja Praktikum - Implementasi Kriptografi Dasar</p>
  <p>© 2025 SMKN 1 Punggelan - Program Keahlian Teknik Komputer dan Jaringan</p>
</div>

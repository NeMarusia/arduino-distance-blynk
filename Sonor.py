import serial
import time
import requests
import re

PORT = 'COM4'
BAUD = 9600
BLYNK_AUTH_TOKEN = 'I7XkDimEb87J7ggY0qPLVxXSus5cJevC'
VIRTUAL_PIN = 'V0'

# Инициализация
ser = serial.Serial(PORT, BAUD, timeout=1)
print(f"[Serial] Подключено к {ser.name}")
time.sleep(2)

last_distance = None

try:
    while True:
        line = ser.readline().decode('utf-8').strip()

        if "Distance:" in line:
            print(f"[Serial] {line}")

            match = re.search(r'Distance:\s*(\d+)', line)
            if match:
                distance = int(match.group(1))
                print(f"[Parsed] {distance} cm")

                if distance != last_distance:
                    last_distance = distance
                    url = f'https://blynk.cloud/external/api/update?token={BLYNK_AUTH_TOKEN}&{VIRTUAL_PIN}={distance}'

                    try:
                        response = requests.get(url, timeout=3)
                        print(f"[Blynk] {response.status_code} → {response.text}")
                    except Exception as e:
                        print(f"[Error] Ошибка при запросе к Blynk: {e}")

        time.sleep(1.5)

except KeyboardInterrupt:
    print("\n[Exit] Завершение работы по Ctrl+C")
    ser.close()

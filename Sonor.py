import os
import re
import time

import requests
import serial

PORT = os.getenv("SERIAL_PORT", "COM4")
BAUD = int(os.getenv("SERIAL_BAUD", "9600"))
BLYNK_AUTH_TOKEN = os.getenv("BLYNK_AUTH_TOKEN")
VIRTUAL_PIN = os.getenv("BLYNK_VIRTUAL_PIN", "V0")

if not BLYNK_AUTH_TOKEN:
    raise RuntimeError("BLYNK_AUTH_TOKEN is not set. Export it before running the script.")

# Инициализация
ser = serial.Serial(PORT, BAUD, timeout=1)
print(f"[Serial] Подключено к {ser.name}")
time.sleep(2)

last_distance = None

try:
    while True:
        line = ser.readline().decode("utf-8").strip()

        if "Distance:" in line:
            print(f"[Serial] {line}")

            match = re.search(r"Distance:\s*(\d+)", line)
            if match:
                distance = int(match.group(1))
                print(f"[Parsed] {distance} cm")

                if distance != last_distance:
                    last_distance = distance
                    url = "https://blynk.cloud/external/api/update"
                    params = {"token": BLYNK_AUTH_TOKEN, VIRTUAL_PIN: distance}

                    try:
                        response = requests.get(url, params=params, timeout=3)
                        print(f"[Blynk] {response.status_code} → {response.text}")
                    except Exception as e:
                        print(f"[Error] Ошибка при запросе к Blynk: {e}")

        time.sleep(1.5)

except KeyboardInterrupt:
    print("\n[Exit] Завершение работы по Ctrl+C")
    ser.close()

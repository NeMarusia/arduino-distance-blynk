# Система дистанционного мониторинга расстояния на базе Arduino и Blynk

Прототип IoT-сенсора на Arduino Uno с ультразвуковым датчиком HC-SR04. Измеряет расстояние через Serial и передаёт данные в Blynk Cloud для визуализации.

## Стек

- Arduino C++
- Python 3
- Blynk IoT Cloud
- HC-SR04

## Файлы

- `sonor_api.ino` — прошивка Arduino Uno для чтения HC-SR04.
- `Sonor.py` — мост Serial → Blynk Cloud.
- `.env.example` — пример переменных окружения без секретов.
- `requirements.txt` — Python-зависимости.

## Быстрый старт

1. Подключите HC-SR04: VCC → 5V, GND → GND, TRIG → D9, ECHO → D10.
2. Загрузите `sonor_api.ino` на Arduino и закройте Serial Monitor в Arduino IDE.
3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Передайте токен Blynk через переменную окружения:

   ```bash
   export BLYNK_AUTH_TOKEN="your_token_here"
   export SERIAL_PORT="COM4"      # например /dev/ttyUSB0 на Linux
   export BLYNK_VIRTUAL_PIN="V0"
   python Sonor.py
   ```

## Безопасность

Blynk Auth Token не хранится в коде. Если токен уже попадал в публичный репозиторий, его нужно перевыпустить в Blynk Cloud.

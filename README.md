# Система дистанционного мониторинга расстояния на базе Arduino и Blynk

Прототип IoT-сенсора на Arduino Uno с ультразвуковым датчиком HC-SR04.  
Измеряет расстояние и передаёт данные в облачный сервис Blynk для визуализации.  
Разработан в рамках образовательной практики по направлению «Интернет вещей».

## Стек технологий

- Arduino C++
- Python 3
- Blynk IoT Cloud
- HC-SR04 (ультразвуковой датчик расстояния)

## Структура проекта

- `arduino/sonar_distance.ino` — прошивка для Arduino Uno
- `python/serial_to_blynk.py` — Python-скрипт для чтения данных с COM-порта и отправки их в Blynk
- `README.md` — описание проекта
- `.gitignore` — исключения для Arduino и Python сред
- `requirements.txt` — зависимости Python-части (pyserial, requests)

## Как использовать

### 1. Подготовка оборудования

- Подключите HC-SR04 к Arduino Uno:
  - VCC → 5V
  - GND → GND
  - TRIG → D9
  - ECHO → D10

### 2. Настройка Blynk

- Зарегистрируйтесь на [blynk.cloud](https://blynk.cloud)
- Создайте новый Template
- Добавьте Virtual Pin `V0` (тип: Integer, например от 0 до 400)
- Создайте устройство на основе шаблона
- Скопируйте **Auth Token** для использования в Python

### 3. Загрузка скетча

- Откройте `arduino/sonar_distance.ino` в Arduino IDE
- Загрузите на плату
- После загрузки **обязательно закройте монитор порта в Arduino IDE** — иначе Python не сможет подключиться

### 4. Запуск Python-скрипта

- Установите зависимости:

pip install -r requirements.txt


- Убедитесь, что в `serial_to_blynk.py` указан правильный COM-порт и Auth Token
- Запустите скрипт: python python/serial_to_blynk.py

  
### 5. Просмотр данных

- Откройте Web Dashboard в Blynk
- Добавьте виджет **Gauge**
- Привяжите к Virtual Pin `V0`
- Данные с датчика будут отображаться в реальном времени

## Возможности расширения

- Поддержка нескольких датчиков
- Telegram-уведомления через webhook
- Хранение данных в Google Sheets
- Переход на ESP-платы для автономной работы без ПК

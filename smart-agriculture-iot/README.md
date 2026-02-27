# Smart Agriculture through IoT 🌱

## Overview
This project demonstrates an IoT-based Smart Agriculture system designed to monitor soil and environmental conditions in real time. 
The system collects data such as soil moisture, humidity, and temperature using sensors connected to an Arduino and sends the data for monitoring and reporting.

## Features
- Soil moisture monitoring
- Temperature & humidity tracking
- Automated reporting (twice daily updates)
- Real-time data transmission
- Sustainable farming decision support

## Tech Stack
- Arduino (Sensor Integration)
- Python (Data Processing & Reporting)
- IoT Sensors (Soil Moisture, DHT11/DHT22)
- Serial Communication

## Project Structure
```
smart-agriculture-iot/
│
├── arduino/
│   └── smart_agri.ino
│
├── python/
│   └── data_receiver.py
│
├── requirements.txt
└── README.md
```

## Hardware Required
- Arduino Uno/Nano
- Soil Moisture Sensor
- DHT11/DHT22 Sensor
- USB Cable
- Jumper Wires

## Setup Instructions

### 1️⃣ Arduino Setup
Upload the Arduino code from `arduino/smart_agri.ino` using Arduino IDE.

### 2️⃣ Python Setup
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the receiver:
```bash
python python/data_receiver.py
```

## Example Output
```
Temperature: 28°C
Humidity: 65%
Soil Moisture: 520
Status: Soil is Moderately Wet
```

## Future Improvements
- Cloud dashboard integration
- Mobile notifications
- AI-based irrigation prediction

## Author
Ritik Raj

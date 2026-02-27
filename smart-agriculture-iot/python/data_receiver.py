import serial
from datetime import datetime

# Change COM port according to your system
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

def interpret_soil(value):
    if value > 700:
        return "Dry Soil"
    elif value > 400:
        return "Moderately Wet"
    else:
        return "Wet Soil"

def main():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print("Listening for sensor data...")

    while True:
        line = ser.readline().decode().strip()
        try:
            parts = dict(item.split(":") for item in line.split(","))
            temp = parts["TEMP"]
            hum = parts["HUM"]
            soil = int(parts["SOIL"])

            print(f"\n[{datetime.now()}]")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {hum}%")
            print(f"Soil Moisture: {soil}")
            print(f"Status: {interpret_soil(soil)}")
        except:
            pass

if __name__ == "__main__":
    main()

import serial
import requests

PORT = "/dev/ttyUSB0"

ser = serial.Serial(PORT, 9600)

while True:

    line = ser.readline().decode().strip()

    print("RAW:", line)

    try:
        value, status = line.split(",")

        payload = {
            "air_quality": int(value),
            "status": status
        }

        response = requests.post(
            "http://127.0.0.1:8000/api/sensor-data",
            json=payload
        )

        print("SENT:", response.json())

    except Exception as e:
        print("ERROR:", e)
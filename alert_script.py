import serial
import requests

# Arduino serial port configuration
serial_port = 'COM3'  # Update with the appropriate serial port for your system
baud_rate = 9600

# Telegram bot API credentials
bot_token = '6127138997:AAG3qmW5oIe2az7d_xmlVs-i23nmv45kVdM'
chat_id = '5776095914'

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Send a message to the Telegram bot
def send_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Message sent to Telegram: {message}")
    else:
        print("Failed to send message to Telegram")

# Read the Arduino messages and forward them to the Telegram bot
while True:
    message = ser.readline().strip().decode('utf-8')

    if message:
        print(f"Received message from Arduino: {message}")
        send_message(message)

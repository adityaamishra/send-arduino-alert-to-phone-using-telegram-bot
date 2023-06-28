import serial
import requests

# Arduino serial port configuration
serial_port = 'YOUR_SERIAL_PORT'  # Update with the appropriate serial port for your system...in my case it was 'COM3'
baud_rate = 9600

# Telegram bot API credentials...REPLACE THE VARIABLES
bot_token = 'your_bot_token'
chat_id = 'your_chat_id'

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

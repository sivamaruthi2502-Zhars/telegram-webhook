from flask import Flask, request
import requests

app = Flask(__name__)

# உன்னோட Telegram Bot Token மற்றும் Group Chat ID
BOT_TOKEN = "9183584864:AAGFB1mYSSlUcqZVlVDCKKN4zNJxqnhYtpM"
# உங்களுடைய பிரீமியம் குரூப் சாட் ஐடியை (-100xxxx 형식) இங்கே மாற்றிக் கொள்ளவும்
CHAT_ID = "YOUR_GROUP_CHAT_ID_HERE"


@app.route('/webhook', methods=['POST'])
def webhook():
  try:
    data = request.data.decode('utf-8')
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": data, "parse_mode": "HTML"}
    requests.post(telegram_url, json=payload)
    return "OK", 200
  except Exception as e:
    return str(e), 500


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

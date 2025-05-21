# sarvaksham-alert-system
Language: Python 3 | Build Command: pip install -r requirements.txt | Start Command: gunicorn app:app
from flask import Flask, request
import requests

app = Flask(_name_)

TELEGRAM_BOT_TOKEN = 'your_bot_token_here'
TELEGRAM_CHAT_ID = 'your_chat_id_here'

@app.route('/alert-receive', methods=['POST'])
def alert_receive():
    data = request.json
    message = f"""
📢 Chartink Alert Received 📉

🔹 Symbol: {data.get('symbol')}
🔹 Open: {data.get('open')}
🔹 High: {data.get('high')}
🔹 Low: {data.get('low')}
🔹 Close: {data.get('close')}
🔹 VWAP: {data.get('vwap')}
🔹 Volume: {data.get('volume')}
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)
    return 'Alert sent to Telegram', 200from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

# Replace with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = 'your_bot_token_here'
TELEGRAM_CHAT_ID = 'your_chat_id_here'

@app.route('/alert-receive', methods=['POST'])
def alert_receive():
    try:
        data = request.json

        # Build the message using data safely
        message = f"""
📢 Chartink Alert Received 📉

🔹 Symbol: {data.get('symbol', 'N/A')}
🔹 Open: {data.get('open', 'N/A')}
🔹 High: {data.get('high', 'N/A')}
🔹 Low: {data.get('low', 'N/A')}
🔹 Close: {data.get('close', 'N/A')}
🔹 VWAP: {data.get('vwap', 'N/A')}
🔹 Volume: {data.get('volume', 'N/A')}
        """

        # Telegram API endpoint
        url = f"https://api.telegram.org/bot{TELEGRA…

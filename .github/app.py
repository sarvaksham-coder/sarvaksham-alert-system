from flask import Flask, request
import requests

app = Flask(__name__)

# 🔑 Replace with your actual bot token & chat ID
TELEGRAM_BOT_TOKEN = '7269300718:AAHYByBEUEjE9ev_Wb8rVjAMAx6OMAFFiGc'
TELEGRAM_CHAT_ID = '-1002587354739'

@app.route('/alert-receive', methods=['POST'])
def alert_receive():
    data = request.json
    message = f"""
📢 *Chartink Alert Received*

🔹 *Symbol*: {data.get('symbol')}
🔹 *Open*: {data.get('open')}
🔹 *High*: {data.get('high')}
🔹 *Low*: {data.get('low')}
🔹 *Close*: {data.get('close')}
🔹 *VWAP*: {data.get('vwap')}
🔹 *Volume*: {data.get('volume')}
🔹 *Stop Loss*: {data.get('sl')}
🔹 *Target*: {data.get('target')}
"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)
    return '✅ Alert sent to Telegram', 200

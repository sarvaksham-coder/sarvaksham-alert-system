# 📡 Sarvaksham Alert System

This is a Flask-based webhook system to receive real-time alerts (like from Chartink) and forward them to a Telegram group/channel using a bot.

---

## 🔧 Setup

### 📁 Files Needed

- app.py → Main application code (see below)
- requirements.txt
- Procfile

---

### 🧠 Full app.py Code

```python
from flask import Flask, request
import requests

app = Flask(_name_)

TELEGRAM_BOT_TOKEN = '7269300718:AAHYByBEUEjE9ev_Wb8rVjAMAx6OMAFFiGc'
TELEGRAM_CHAT_ID = '-1002136945794'  # Your Telegram group/channel ID

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
    return 'Alert sent to Telegram', 200
git add requirements.txt
git commit -m "Added requirements.txt for Render deploy"
git push origin main

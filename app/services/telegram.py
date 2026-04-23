import requests
from app.config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "disable_web_page_preview": True
    }

    try:
        requests.post(url, data=payload, timeout=10)
    except requests.RequestException as exc:
        print(f"Telegram error: {exc}")

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID")

# Filter
MIN_POWER_HP = 190
MAX_MILEAGE_KM = 150000
MIN_YEAR = 2008
MAX_PRICE_PLN = 75000
BRANDS = ["BMW", "Audi"]

# Files
SEEN_FILE_PATH = "data/seen.json"

# Timing
SCRAPE_INTERVAL_SECONDS = 600

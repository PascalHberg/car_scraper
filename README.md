# car_scraper

Python-based scraper that monitors car listings (BMW, Audi) on Otomoto, filters them by predefined criteria, and sends new matches to Telegram. The scraper uses Selenium to open the website, extracts listings, filters them by horsepower, mileage, year, and price, and compares them with previously saved links in `seen.json`. Only new results are sent to Telegram. The process runs automatically every 10 minutes.

## Setup

Install Python 3.10 or higher and install dependencies:

pip install -r requirements.txt

Go to `.env` file in the project root and insert your Telegram credentials:

BOT_TOKEN=your_telegram_bot_token  
CHAT_ID=your_chat_id  

Replace the values with your actual bot token and chat ID.

Make sure Google Chrome is installed.

## Run

python -m app.main

Stop with CTRL + C.

## Notes

The scraper runs continuously and may need adjustments if the website structure changes.

## License

Apache License 2.0

Copyright 2026

import time
from datetime import datetime

from app.scraper.otomoto import scrape_otomoto
from app.services.storage import load_seen_links, save_seen_links
from app.services.telegram import send_message
from app.config.settings import SCRAPE_INTERVAL_SECONDS


def run():
    seen_links = load_seen_links()

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Start...")

        try:
            new_cars = scrape_otomoto(seen_links)
        except Exception as exc:
            print(f"[{timestamp}] Scraping error: {exc}")
            new_cars = []

        if new_cars:
            print(f"{len(new_cars)} neue Inserate")

            for car in new_cars:
                message = f"{car.title}\n{car.link}"
                print(message)

                send_message(message)
                seen_links.add(car.link)

            save_seen_links(seen_links)
        else:
            print("Keine neuen Inserate")

        time.sleep(SCRAPE_INTERVAL_SECONDS)


if __name__ == "__main__":
    run()

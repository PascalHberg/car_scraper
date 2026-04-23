from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

from app.config.settings import (
    MIN_YEAR, MIN_POWER_HP, MAX_MILEAGE_KM, MAX_PRICE_PLN
)
from app.models.car import Car


def build_url() -> str:
    return (
        f"https://www.otomoto.pl/osobowe/audi--bmw/od-{MIN_YEAR}?"
        f"search%5Bfilter_enum_gearbox%5D=automatic&"
        f"search%5Bfilter_float_engine_power%3Afrom%5D={MIN_POWER_HP}&"
        f"search%5Bfilter_float_mileage%3Ato%5D={MAX_MILEAGE_KM}&"
        f"search%5Bfilter_float_price%3Ato%5D={MAX_PRICE_PLN}&"
        f"search%5Border%5D=created_at_first%3Adesc"
    )


def create_driver():
    chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")

    return webdriver.Chrome(options=options)


def scrape_otomoto(seen_links: set) -> list[Car]:
    driver = create_driver()
    cars = []

    try:
        driver.get(build_url())

        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article")))

        listings = driver.find_elements(By.CSS_SELECTOR, "article")

        for item in listings:
            try:
                title = item.find_element(By.CSS_SELECTOR, "h1, h2, h3").text.strip()
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                if link and link not in seen_links:
                    cars.append(Car(title=title, link=link))

            except Exception:
                continue

    finally:
        driver.quit()

    return cars

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import time, sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 15)

print("Looking for language selection...")
try:
    language_button = wait.until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    language_button.click()
    print("English language selected")
except:
    print("Language selection not found")

cookie = wait.until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

upgrade_check_interval = 5
next_upgrade_check = time() + upgrade_check_interval

game_end_time = time() + 60 * 5 

while True:

    cookie.click()

    sleep(0.01)

    if time() > next_upgrade_check:

        try:
            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")

            best_product = None

            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_product = product
                    break

            if best_product:
                best_product.click()
                print(f"Bought: {best_product.get_attribute('id')}")

        except NoSuchElementException:
            print("Upgrade not found")

        next_upgrade_check = time() + upgrade_check_interval

    if time() > game_end_time:

        try:
            cookies = driver.find_element(By.ID, "cookies").text
            print(f"\nFinal Result: {cookies}")
        except NoSuchElementException:
            print("Could not fetch final score")

        break
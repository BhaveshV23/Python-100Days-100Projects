from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.get("https://www.tinder.com")

input("Login manually then press ENTER to start the bot...")

sleep(5)

try:
    allow_location = driver.find_element(By.XPATH, '//button[text()="Allow"]')
    allow_location.click()
except:
    pass

try:
    cookies = driver.find_element(By.XPATH, '//button[contains(text(),"I accept")]')
    cookies.click()
except:
    pass

body = driver.find_element(By.TAG_NAME, "body")

for _ in range(100):

    sleep(1)

    try:
        body.send_keys(Keys.ARROW_RIGHT)

    except ElementClickInterceptedException:

        try:
            match_popup = driver.find_element(By.XPATH, '//button[text()="Back to Tinder"]')
            match_popup.click()

        except:
            sleep(2)

driver.quit()
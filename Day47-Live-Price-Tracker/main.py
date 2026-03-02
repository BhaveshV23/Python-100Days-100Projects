import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=LIVE_URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
price_whole = soup.find(name="span", class_="a-price-whole")
price_decimal = soup.find(name="span", class_= "a-price-fraction")
total_price = price_whole.get_text()+price_decimal.get_text()
float_price = float(total_price.replace(',', ''))

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 7500
SMTP_ADDRESS=os.getenv("SMTP_ADDRESS")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

if float_price < BUY_PRICE:
    message = f"{title} is on sale for {float_price}!"

    with SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=RECEIVER_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{LIVE_URL}".encode("utf-8")
                            )
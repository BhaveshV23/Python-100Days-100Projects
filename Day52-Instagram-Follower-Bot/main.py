import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_NAME = "chefsteps"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class InstaFollowers:
    def __init__(self):
        """
        This Function creates Selenium Driver
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        username = self.driver.find_element(by=By.NAME, value="email")
        password = self.driver.find_element(by=By.NAME, value="pass")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)

        save_login_prompt = self.driver.find_element(by=By.XPATH,
                                                     value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div')
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)

        notifications_prompt = self.driver.find_element(by=By.XPATH,
                                                        value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        if notifications_prompt:
            notifications_prompt.click()

    def search_account(self):
        """
        This Function will search and open the Target Account
        """
        print(f"Searching for Account : {ACCOUNT_NAME}\n")
        try:
            search_button = self.driver.find_element(
                By.XPATH, "//a[.//span[text()='Search']]"
            )
            search_button.click()
        except Exception as e:
            print(f"Error : {e}")

        search_input = self.driver.find_element(
            By.CSS_SELECTOR, value="input[placeholder='Search']"
        )
        search_input.send_keys("Chefsteps", Keys.ENTER)

        print("Search Results are Available...\n")
        time.sleep(2)

        account = self.driver.find_element(
            By.XPATH, value=f"//a[.//span[text()='{ACCOUNT_NAME}']]"
        )
        if account:
            try:
                print(f"Account Found : {ACCOUNT_NAME}\n")
                account.click()
                time.sleep(2)
                print(f"Account Opened : {ACCOUNT_NAME}\n")
            except Exception as e:
                print(f"Account not Found : {e}\n")

    def find_followers(self):
        """
        This Function will open the Followers List
        """
        print("Searching the Followers List\n")

        followers = self.driver.find_element(
            By.XPATH, value='//a[@href="/chefsteps/followers/"]'
        )
        if followers:
            try:
                print("Followers List Found !!\n")
                followers.click()
                time.sleep(1)
                print("Followers List is Available now\n")
            except Exception as e:
                print(f"Followers List Not Found : {e}")

    def follow(self):
        """
        This Function will follow the Avaible 20 Accounts
        """
        followers_list = self.driver.find_elements(
            By.CLASS_NAME,
            value="x1qnrgzn.x1cek8b2.xb10e19.x19rwo8q.x1lliihq.x193iq5w.xh8yej3",
        )

        accounts_followed = 0

        if followers_list:
            try:
                print("Initializing the Account Following Process\n")

                for items in followers_list:
                    time.sleep(3)

                    button = items.find_element(By.TAG_NAME, "button")

                    if accounts_followed < 15:
                        try:
                            if button.text == "Follow":
                                accounts_followed += 1
                                button.click()
                                print(f"Accounts Followed: {accounts_followed}\n")

                        except Exception as e:
                            print(f"Task Interrupted due to Error : {e}")
                            print("\nDriver will be Exited in 10 Seconds...")
                            time.sleep(10)
                            self.driver.quit()
                    else:
                        print("Task Completed....\n")
                        time.sleep(5)
                        self.driver.quit()

            except Exception as e:
                print(f"Error : {e}")

instagram_bot = InstaFollowers()
login = instagram_bot.login()
time.sleep(5)
searching = instagram_bot.search_account()
time.sleep(5)
find_followers = instagram_bot.find_followers()
time.sleep(5)
following_task = instagram_bot.follow()
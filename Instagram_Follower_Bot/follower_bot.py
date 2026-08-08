SIMILAR_ACCOUNT="chefsteps"
USERNAME="ahmadfkwj@gmail.com"
PASSWORD="-b5KfZ5bGSMS-LI3"
LOGIN_URL="https://app.100daysofpython.dev/services/share-a-naan/login"
BASE_URL="https://app.100daysofpython.dev/services/share-a-naan"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

## Keep the Browser Open:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        ## Set up the Chrome Driver:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(LOGIN_URL)
        self.driver.fullscreen_window()


    def login(self):
        input_username = self.driver.find_element(By.ID , value="username")
        input_password = self.driver.find_element(By.ID, value="password")
        login_button = self.driver.find_element(By.CLASS_NAME , value="naan-btn-primary")

        input_username.send_keys(USERNAME)
        input_password.send_keys(PASSWORD)
        login_button.click()
        time.sleep(4)

        ## Dismiss "Save your login info?" → "Not now"
        save_info = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info:
            save_info[0].click()
        time.sleep(1)
        ## Dismiss "Turn on notifications" → "Not Now"
        notifications = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications[0].click()


    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)

        # ## The scrollable element inside the followers dialog. Inspect to confirm the class.
        # modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll _aano")

        # for _ in range(10):
        #     ## "scroll this element to the bottom" → loads the next batch of followers
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(1)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)

            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()


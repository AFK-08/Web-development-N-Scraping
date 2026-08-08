SIMILAR_ACCOUNT="chefsteps"
USERNAME="ahmadfkwj@gmail.com"
PASSWORD="-b5KfZ5bGSMS-LI3"
LOGIN_URL="https://app.100daysofpython.dev/services/share-a-naan/login"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

## Keep the Browser Open:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        ## Set up the Chrome Driver:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(LOGIN_URL)
        self.driver.fullscreen_window()
        self.wait = WebDriverWait(self.driver , 3)


    def login(self):
        input_username = self.driver.find_element(By.ID , value="username")
        input_password = self.driver.find_element(By.ID, value="password")
        login_button = self.driver.find_element(By.CLASS_NAME , value="naan-btn-primary")

        input_username.send_keys(USERNAME)
        input_password.send_keys(PASSWORD)
        login_button.click()

        ## Save Info Pop up Dismiss
        popup = self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"naan-popup-dismiss")))
        popup.click()
        popup.click()

    def find_followers(self):
        pass


    def follow(self):
        pass


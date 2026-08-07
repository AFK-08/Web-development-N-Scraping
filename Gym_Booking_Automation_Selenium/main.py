Account_Email = "yourname@test.com"
Account_Password = "Test@419"
Gym_URL = "https://appbrewery.github.io/gym/"

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

user_data_dir = os.path.join(os.getcwd(), "./Gym_Booking_Automation_Selenium/chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(Gym_URL)


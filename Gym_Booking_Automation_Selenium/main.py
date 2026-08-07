## Credentials:
Account_Email = "yourname@test.com"
Account_Password = "Test@419"
Gym_URL = "https://appbrewery.github.io/gym/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

user_data_dir = os.path.join(os.getcwd(), "./Gym_Booking_Automation_Selenium/chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

## Opening Webpage:
driver = webdriver.Chrome(options=chrome_options)
driver.get(Gym_URL)

## Creating a wait Object:
wait = WebDriverWait(driver , 2)

## Logging in:
login_button = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
login_button.click()

## Entering credentials:
email_input = wait.until(ec.presence_of_element_located((By.ID,"email-input")))

password_input = driver.find_element(By.ID , value="password-input")
submit_button = driver.find_element(By.ID , value="submit-button")

email_input.send_keys(Account_Email)
password_input.send_keys(Account_Password)
submit_button.click()

## Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))




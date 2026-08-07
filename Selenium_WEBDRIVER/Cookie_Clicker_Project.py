from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

## Set Time Seconds Clicking Cookie:
start_time = time.time()
duration = 120

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
driver.fullscreen_window()

## Waiting Screen to Load:
time.sleep(5)

## Removing the language pop-up:
try:
    language = driver.find_element(By.ID, value="changeLanguage")
    language.click()
    cancel = driver.find_element(By.ID , value="promptOption0")
    cancel.click()

except NoSuchElementException:
    print("Language Selection Not Found!")


time.sleep(3)

## Finding and Clicking Cookie Button:
cookie = driver.find_element(By.ID, value="bigCookie")

while time.time() < start_time + duration:
    cookie.click()

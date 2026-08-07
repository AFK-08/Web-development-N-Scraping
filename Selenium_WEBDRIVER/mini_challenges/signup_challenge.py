from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
driver.fullscreen_window()

first_name = driver.find_element(By.NAME , value="fName")
first_name.send_keys("Ahmad")

last_name = driver.find_element(By.NAME , value="lName")
last_name.send_keys("Farooq")

email = driver.find_element(By.NAME , value="email")
email.send_keys("ahmadfk@gmail.com",Keys.ENTER)



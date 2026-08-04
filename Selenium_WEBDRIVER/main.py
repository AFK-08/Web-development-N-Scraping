## Selenium Automates Browsers
from selenium import webdriver

## Keep browser open after program finishes:

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

## Closing Browser Methods:
## -- closes only active tab
driver.close()
## -- close whole browser
driver.quit()


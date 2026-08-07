from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.fullscreen_window()

## 1. Printing no of Articles:
# article_numbers = driver.find_element(By.ID,value="mwDw")
# print(article_numbers.text)


## 2. Finding and Clicking on Links:

# portals = driver.find_element(By.LINK_TEXT,value="Community portal")
# portals.click()

## 3. Searching through the page :

search_wiki = driver.find_element(By.NAME, value="search")
search_wiki.send_keys("Python", Keys.ENTER)








driver.quit()

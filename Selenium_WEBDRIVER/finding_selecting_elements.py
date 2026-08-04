from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1?crid=2HM5VKC468KG&dib=eyJ2IjoiMSJ9.y4LLAMvRXyF-GJBFF44Ypjru1JC4sFXkbqtPv_wdGE5E9Axl1MNpLrgsRhSUkjwZzMNiczvK-8m5tTtlJu6X8OLwWzH9fOPYRMvUzQJKMgsy-TXrqVS29Q0vHl9KFGqBroXaQ-Cm1LmHrv5rEafMkDQ_83Hy3YyKzfKdSfdERWYqoUuJ5EKBlGwDX4kXBEfvXYotXNGn3rQvICINx4gqU11GjypgG7rm2NbEzkf-zf4.aLtuckvNp2JygjUEVUf3EBoQ9AwaPSyBaHu7CPl99Po&dib_tag=se&keywords=instant%2Bpot&qid=1785857562&sprefix=ins%2Caps%2C506&sr=8-1&th=1")

price_whole = driver.find_element(By.CLASS_NAME,value="a-price-whole")

price_fraction = driver.find_element(By.CLASS_NAME,value="a-price-fraction")

print(f"The price of pot is {price_whole.text}.{price_fraction.text}")

driver.quit()


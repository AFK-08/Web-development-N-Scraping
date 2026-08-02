import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")

## Finding news article link in span tag with class titleline:

article_texts = []
article_links = []

articles = soup.find_all(name="span" , class_="titleline")

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes =[int(score.getText().split()[0]) for score in soup.select(selector=".score")] 

print(article_texts)
print(article_links)
print(article_upvotes)

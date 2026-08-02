from bs4 import BeautifulSoup
#import lxml

with open("./Beautiful_Soup-start/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.a)
print(soup.title.string)
print(soup.p)

## Find all Function for finding all elements

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

print("***************************************")

## Finding Text between anchor tags and also Links:
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

## Finding Elements by id name:

id_name = soup.find_all(id="name")
print(id_name)

## Using CSS Selectors to find Selected Element:

company_url = soup.select_one(selector="p a")
print(company_url)

## Acessing Class using Selectors:

headings = soup.select(".heading")
print(headings)

## Accessing Id using Selectors:

name = soup.select("#name")
print(name)

    
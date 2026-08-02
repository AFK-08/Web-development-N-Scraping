from bs4 import BeautifulSoup
#import lxml

with open("./Beautiful_Soup-start/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.a)
print(soup.title.string)
print(soup.p)

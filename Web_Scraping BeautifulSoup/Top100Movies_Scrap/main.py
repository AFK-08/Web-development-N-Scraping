import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

response.raise_for_status()

contents = response.text
soup = BeautifulSoup(contents, "html.parser")
movies = soup.find_all(name="h3" , class_="title")

movie_titles = [movie.getText() for movie in movies]
movie_titles = movie_titles[::-1]

with open("movies.txt", mode="w" , encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")




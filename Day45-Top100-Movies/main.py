from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("Day45-Top100-Movies/movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie + "\n")

print("Top 100 movies saved successfully!")
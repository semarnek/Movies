import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_list = []

movies = soup.find_all("h3", class_="title")

for movie in movies:
    movie_list.append(movie.getText())
    movie_list[-1] = movie_list[-1] + "\n"

movie_list.reverse()

with open("movies.txt", "w", encoding="utf-8") as moviefile:
    moviefile.writelines(movie_list)


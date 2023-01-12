from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
titles = soup.select('.article-title-description .title')

top_movies = []

for title in titles:
    top_movies.append(title.get_text())

top_movies.reverse()

with open('movies.txt', mode='w', encoding='utf8') as file:
    for movie in top_movies:
        file.write(f"{movie}\n")





from bs4 import BeautifulSoup
import requests

user_input = input("Please Enter the Playlist Date in YYYY-MM-DD Format: ")

url = f"https://www.billboard.com/charts/hot-100/{user_input}/"
response = requests.get(url)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

songs_title = soup.select('div .o-chart-results-list-row-container #title-of-a-story')

songs_list = []

for song in songs_title:
    if ":" not in song.get_text():
        songs_list.append(song.get_text().strip())

with open('top_10_songs.txt', mode='w', encoding='utf8') as file:
    for song in songs_list:
        file.write(f"{song}\n")











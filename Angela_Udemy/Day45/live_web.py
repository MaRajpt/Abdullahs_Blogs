from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
tags = soup.select(".titleline a")
score_tags = soup.select('span .score')

article_title = []
article_link = []
article_score = []

for tag in tags:
    if "https://" in tag.get('href'):
        article_link.append(tag.get('href'))
        article_title.append(tag.get_text())

for score_tag in score_tags:
    article_score.append(int((score_tag.get_text().split()[0])))


print(len(article_title))
print(len(article_link))
print(len(article_score))

print(article_title)
print(article_link)
print(article_score)


max_points = max(article_score)
max_index = article_score.index(max_points)
max_link = article_link[max_index]
max_title = article_title[max_index]


print(max_title)
print(max_link)
print(max_points)

# print(score_tag.get_text())

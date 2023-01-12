from bs4 import BeautifulSoup
from html import escape
import urllib
# import lxml is target web is  xml

file = open("website.html", encoding="utf8")
contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.name)
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())      # indents properly
# print(soup.a)  #  finds first anchor tags in finds e.g <a href="https://www.appbrewery.co/">The App Brewery</a>
# # print(soup.li)  #first li
# # print(soup.p)   #first paragraph it finds
#
# #--------------------------------------------------------------------------------------------------------#
# # FINDING ALL THE TAGS INSTEAD OF FIRST ONE AS SEEN ABOVE USING "find_all()" FUNCTION
#
all_anchor_tags = soup.find_all(name="a")  # returns a list
print(all_anchor_tags)  # ALL ANCHOR TAGS or p for paras

 # WHAT IF WE ONLY WANT TEXT IN ANCHOR TAGS INSTEAD OF EVERYTHING

for tag in all_anchor_tags:
    print(tag.get("href"))
    print(tag.get_text())

heading = soup.find(name="h1", id="name")       # NOT FIND ALL AS USED PREVIOUSLY ABOVE
print(heading, "yolo")

section_heading = soup.find(name="h3", class_="heading")  # notice class_  ( an underscaore)
print(section_heading)
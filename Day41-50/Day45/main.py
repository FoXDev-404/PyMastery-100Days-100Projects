# from bs4 import BeautifulSoup
# import lxml


# with open("website.html") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)

# all_anchor_tags = (soup.find_all(name="a"))
# print(all_anchor_tags)

# for tag in all_anchor_tags:
      # print(tag.getText())
#     print(tag.get("href"))


# print(soup.find_all(name="h1", id="name"))



# ===========Test in index.html website===============
# with open("./index.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")

# fruit = soup.select_one(selector="#fruits")
# print(fruit)
#
# veg = soup.select(".veg")
# print(veg)

# Parse table rows
# print("\nUser Table:")
# rows = soup.select("#user-table tbody tr")
# for row in rows:
#     cols = row.find_all("td")
#     name, email, age = [col.text for col in cols]
#     print(f"  - {name} ({email}) is {age} years old.")



# ===========Scraping a Live Website==============
from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.a["href"]
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])


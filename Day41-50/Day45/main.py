from bs4 import BeautifulSoup
# import lxml


with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)
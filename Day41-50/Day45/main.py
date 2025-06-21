from bs4 import BeautifulSoup
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
with open("./index.html") as file:
    content = file.read()
    
soup = BeautifulSoup(content, "html.parser")

# fruit = soup.select_one(selector="#fruits")
# print(fruit)
#
# veg = soup.select(".veg")
# print(veg)

# Parse table rows
print("\nUser Table:")
rows = soup.select("#user-table tbody tr")
for row in rows:
    cols = row.find_all("td")
    name, email, age = [col.text for col in cols]
    print(f"  - {name} ({email}) is {age} years old.")
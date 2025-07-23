# Automating Data Entry with Web Scraping
from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://appbrewery.github.io/Zillow-Clone")
soup = BeautifulSoup(response.content, 'html.parser')

property_price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
property_prices = []
for price in property_price:
    cleaned_price = price.get_text().strip()
    cleaned_price = re.sub(r'\+.*', '', cleaned_price)
    cleaned_price = re.sub(r'/.*', '', cleaned_price)
    cleaned_price = cleaned_price.strip()
    property_prices.append(cleaned_price)

property_address = soup.find_all('address', {'data-test': 'property-card-addr'})
property_addresses = []
for address in property_address:
    cleaned_address = address.get_text().strip()
    cleaned_address = re.sub(r'\n+', ' ', cleaned_address)
    cleaned_address = cleaned_address.replace('|', '')
    cleaned_address = re.sub(r'\s+', ' ', cleaned_address)
    property_addresses.append(cleaned_address.strip())

property_links = soup.find_all(name="a", class_="property-card-link")
property_urls = [link.get("href") for link in property_links]

print(property_urls)
print(property_prices)
print(property_addresses)

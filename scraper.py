import requests
import json
# import lxml.html
from bs4 import BeautifulSoup

countries = []
url = "https://www.womenonwaves.org/en/map/country"
r = requests.get(url)
# print(r)
# print(r.text)
# root = lxml.html.parse(r.text)
# print(tostring(root))
# for el in root.find_class("list-item-country"):
#   print(el)
soup = BeautifulSoup(r.text,   "html.parser")
# print(soup.prettify())
for country in soup.find_all("div", class_="list-item-country"):
  country_obj = {}
  link = country.find("a")
  country_obj['name'] = link.get_text().strip()
  country_obj['link'] = link.get("href")
  country_obj['color'] = link.get("style")
  countries.append(country_obj)

print(json.dumps(countries, indent=2))
# print(countries)

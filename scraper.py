import requests
import json
import csv
from bs4 import BeautifulSoup

countries = []
url = "https://www.womenonwaves.org/en/map/country"
r = requests.get(url)

soup = BeautifulSoup(r.text,   "html.parser")

for country in soup.find_all("div", class_="list-item-country"):
  country_obj = {}
  link = country.find("a")
  country_obj['name'] = link.get_text().strip()
  country_obj['link'] = link.get("href")
  country_obj['color'] = link.get("style")
  countries.append(country_obj)

count = 0
with open('countries.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file)
  for country in countries:
    if count == 0:
      csv_writer.writerow(country)
      count += 1
    csv_writer.writerow(country.values())
 
print(json.dumps(countries, indent=2))

import requests
import json
import csv
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

count = 0
with open('countries.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file)
  for country in countries:
    if count == 0:
      csv_writer.writerow(country)
 
        # Writing headers of CSV file
        # header = emp.keys()
        # csv_writer.writerow(header)
      count += 1
    csv_writer.writerow(country.values())
 
    # Writing data of CSV file

print(json.dumps(countries, indent=2))
# print(countries)

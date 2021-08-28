import os
import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"
countrys = []
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countrys.append(country)


def re_ask():
  try:
    choice = int(input("#: "))
    if choice > len(countrys):
      print("Choose a number from the list.")
      re_ask()
    else:
      country = countrys[choice]
      print(f"You chose {country['name']}")
      print("The currency code is BND")
  except ValueError:
    print("That wasn't a number.")
    re_ask()


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countrys):
  print(f"#{index} {country['name']}")

re_ask()

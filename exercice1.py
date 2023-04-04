import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for country in soup.find_all('div', class_='col-md-4 country'):
    
  pays = country.find('h3', class_='country-name').text
  pays_espace = pays.lstrip()

  capitale = country.find('span', class_='country-capital').text
  population = country.find('span', class_='country-population').text
  area = country.find('span', class_='country-area').text

  print(pays_espace)
  print(capitale)
  print(population)
  print(area)
  print("\n")


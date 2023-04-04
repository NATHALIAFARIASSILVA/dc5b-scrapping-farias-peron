import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for country in soup.find_all('div', class_='col-md-4 country'):
  print(country.find('h3', class_='country-name').text)
  print(country.find('span', class_='country-capital').text)
  print(country.find('span', class_='country-population').text)
  print(country.find('span', class_='country-area').text)
import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for country in soup.find_all('div', class_='col-md-4 country'):
  print(country.find('h3').text)

for capital in soup.find_all('div', class_='country-capital'):
  print(capital.find('span').text)

for population in soup.find_all('div', class_='country-population'):
  print(population.find('span').text)
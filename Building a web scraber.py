import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Asus'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific data from the webpage
data = soup.find('div', class_='Asus').text

print(data)

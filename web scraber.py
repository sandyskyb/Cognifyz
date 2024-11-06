import requests
from bs4 import BeautifulSoup

url = 'https://www.cognida.ai'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific data from the webpage
data = soup.find('div', class_='service').text

print(data)

import requests
from bs4 import BeautifulSoup

url = 'https://pixabay.com/pt/photos/'

payload = {'q': 'gatinhos felizes'}

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

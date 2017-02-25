import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Lista_de_estados_brasileiros_por_número_de_munic%C3%ADpios'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find_all('table', {'class': 'wikitable'})[-1]
for tr in (x for x in table.children if x != '\n'):
    for th in (x for x in tr.children if x != '\n'):
        if th.string:
            print(th.string)
        else:
            print(th.a.string)

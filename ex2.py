import shutil
import requests
from bs4 import BeautifulSoup

url = 'https://pixabay.com/pt/photos/'

payload = {'q': 'gatinhos felizes'}

r = requests.get(url, params=payload)
soup = BeautifulSoup(r.text, 'html.parser')

for i, div in enumerate(soup.find('div', {'id': 'photo_grid'}).children):
    img = div.a.img

    if img.get('data-lazy'):
        img_url = img.get('data-lazy')
    elif div.a.img.get('src'):
        img_url = img.get('src')

    response = requests.get(img_url, stream=True)
    with open('img/%d.png' % i, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

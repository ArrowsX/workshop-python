import requests

url = 'https://pixabay.com/pt/photos/'

payload = {'q': 'gatinhos felizes'}

r = requests.get(url, params=payload)
print(r.status_code)
print(r.url)

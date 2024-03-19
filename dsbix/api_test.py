import requests

url = 'https://dsbix-api.vercel.app/'
response = requests.get(url)

if response.status_code == 200:
    entries = response.json()
    print(entries)
else:
    print('Error:', response.status_code)

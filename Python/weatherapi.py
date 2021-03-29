import json
import requests

print('Please enter your zip code')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45011,us&appid=5f86f0842fa96b957fad23e8d81b72a4'%[zip])

data=r.json()
print(data['weather'][0]['description'])
import json
import requests

api = requests.get('http://localhost:3000')
data=api.json()


print(data[0]['name'],"is",data[0]['color'])
print(data[1]['name'],"is",data[1]['color'])
print(data[2]['name'],"is",data[2]['color'])
print(data[3]['name'],"is",data[3]['color'])
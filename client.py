import requests
import json

url = 'http://127.0.0.1:8000/Products/type/keyboard'
response = requests.get(url)

# jjjj = json.load(response.text)

# print((json.dumps(response.json()["1"], indent = 4)))
# print((json.dumps(response.json()["2"], indent = 4)))
print((json.dumps(response.json(), indent = 4)))
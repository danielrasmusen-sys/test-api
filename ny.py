import requests
import json
response = requests.get('http://127.0.0.1:5000/allwines/1')
print(response.json())
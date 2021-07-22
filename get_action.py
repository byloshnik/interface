import json
import requests
import time


while True:
    response = requests.get('http://127.0.0.1:5000/api')
    json_data = json.loads(response.text)
    print(f'json_data = {json_data}')
    time.sleep(0.5)
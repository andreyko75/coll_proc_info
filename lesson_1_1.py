import json
from pprint import pprint

import requests

url = 'https://api.github.com/users/Andreyko75/repos'
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36', 'Accept': '*/*'}

response = requests.get(url, headers=my_headers)
j_data = response.json()
pprint(j_data)
with open('data_1.json', 'w') as f:
    json.dump(j_data, f)

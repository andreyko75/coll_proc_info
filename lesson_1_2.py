# Sun and Moon
# Information about the sun and moon
# Weather variables:
# Sunrise and sunset time
# Moon rise and moon set time
# Moon phase angle and name
# Moon age
# Moon phase transit time

import json
from pprint import pprint

import requests

url = 'https://my.meteoblue.com/packages/sunmoon?apikey=N6EaJnArsD2liQPZ&lat=55.7592&lon=39.2055&asl=119&format=json' \
      '&tz=Europe%2FMoscow'
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36', 'Accept': '*/*'}

response = requests.get(url, headers=my_headers)
j_data = response.json()
pprint(j_data)
with open('data_2.json', 'w') as f:
    json.dump(j_data, f)

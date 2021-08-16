import io

import pandas as pd
import prettytable as pt
from bs4 import BeautifulSoup

with open('test.html') as input_file:
    text_html = input_file.read()
df = pd.DataFrame(columns=['vac_name', 'salary', 'emloyer'])
tree = {}
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36', 'Accept': '*/*'}
#vac_name_html = 'залог'
# url = 'https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=' + vac_name_html + '&page=1'
# response = requests.get(url, headers=my_headers).text
# pprint(response)
soup = BeautifulSoup(text_html, 'html.parser')
vac_name = soup.find_all('div', {'class': ['vacancy-serp-item']})
last_value = len(df) + 1 if len(df) > 0 else 0
for i, x in enumerate(vac_name):
    df.loc[last_value + i] = [x.findNext('a').contents[0],
                              x.findNext('span', {'data-qa': ['vacancy-serp__vacancy-compensation']}).contents[0]
                              if x.find('span', {'data-qa': ['vacancy-serp__vacancy-compensation']}) is not None
                              else None,
                              x.findNext('a', {'class': ['bloko-link bloko-link_secondary']}).contents[0]]
output = io.StringIO()
df.to_csv('hh.csv')
df.to_csv(output)
output.seek(0)
print(pt.from_csv(output))

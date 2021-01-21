"""
Скрипт парсит табличку на странице https://стопкоронавирус.рф/information/
за текущий день и сохраняет результаты в csv-файл
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import datetime

html = requests.get('https://xn--80aesfpebagmfblc0a.xn--p1ai/information/').text
# soup = BeautifulSoup(html, 'lxml')
soup = BeautifulSoup(html, 'html.parser')
data = soup.findAll('cv-spread-overview')[0][':spread-data']
data = json.loads(data) # содержит все данные по короновирусу на текущий день

# Название файла
today = datetime.datetime.now()
today = today.strftime("%Y-%m-%d")
file = f'statistics {today}.csv'

# Сохраняем результаты в csv
with open(file, 'w', newline='', encoding='utf-8') as csvfile:
	header = ['title', 'code', 'sick', 'sick_incr', 'healed', 'healed_incr', 'died', 'died_incr']
	writer = csv.writer(csvfile)
	writer.writerow(header)
	for region in data:
		line = [region[atr] for atr in header]
		writer.writerow(line)
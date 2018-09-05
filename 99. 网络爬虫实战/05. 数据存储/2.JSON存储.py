from pyquery import PyQuery as pq
import requests
import json

URL = 'http://www.rxshc.com/'
html = requests.get(URL).text
doc = pq(html)
items = doc('.postitem').items()

with open('test.json', 'w', encoding='utf-8') as file:
    data = []
    for item in items:
        data.append({
            'title': item.find('.title').text(),
            'views': item.find('.views').text(),
            'time': item.find('.time').text()
        })
    # indent 缩进
    # ensure_ascii 中文输出
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
from pyquery import PyQuery as pq
import requests

URL = 'http://www.rxshc.com/'
# 获取网页数据
html = requests.get(URL).text
# 格式文档
doc = pq(html)
# 获取文章数据
items = doc('.postitem').items()

# 打开文件，以 w+ 的形式写入文件
with open('test.txt', 'w+', encoding="utf-8") as file:
    # 遍历列表
    for item in items:
        title = item.find('.title').text()
        views = item.find('.views').text()
        time = item.find('.time').text()
        # 写入数据
        file.write('\n'.join([title, views, time]))
        file.write('\n' + '=' * 50 + '\n')
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import pymongo

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['test']
collection = db['weibos']

def get_page (page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page (json):
    if json:
        items = json['data']['cards']
        for item in items:
            newItem = item.get('mblog')
            weibo = {}
            weibo['id'] = newItem.get('id')
            weibo['text'] = pq(newItem.get('text')).text()
            weibo['attitudes'] = newItem.get('attitudes')
            weibo['comments'] = newItem.get('comments')
            weibo['reposts'] = newItem.get('reposts')
            yield weibo

def saveDB (json):
    result = collection.insert(json)
    print('保存数据', result)


if __name__== '__main__':
    for page in range(1, 14):
        json = get_page(page)
        res = parse_page(json)
        for item in res:
            print(item)
            saveDB(item)
import requests
import re
import json
import time

def get_one_page (url):
    # 添加投头部信息模拟用户浏览
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Host': 'maoyan.com',
        'Cookie': 'uuid=1A6E888B4A4B29B16FBA1299108DBE9C67458134A6769AC24B0BC49E8A814434; _lxsdk_cuid=164217b0cbdc8-051cb9e77b0495-336e7707-1aeaa0-164217b0cbdc8; _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9C67458134A6769AC24B0BC49E8A814434; _csrf=7cc34d313831de6d21c8bdd10f4b37b98e47350e217ae8ba8ef77c75e663ba26; __mta=213185067.1529570069713.1531198550947.1531202635609.3; _lxsdk_s=16482c9ffbc-e56-493-34e%7C%7C2'

    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        reg = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
            re.S
        )
        items = re.findall(reg, res.text)
        for item in items:
            yield {
                'index': item[0],
                'image': item[1],
                'title': item[2],
                'actor': item[3].strip()[3:],
                'time': item[4],
                'score': item[5]
            }
    return None

def main (offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for h in html:
        with open('maoyan.txt', 'ab') as f:
            print(json.dumps(h))
            f.write(json.dumps(h, ensure_ascii=False).encode('utf-8'))
            f.write('\n'.encode('utf-8'))


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
import requests
import os
from urllib.parse import urlencode
from hashlib import md5

class TouTiao:
    def __init__ (self):

        # 搜索关键字
        self.keyword = '街拍'
        params = {
            'offset': 1,
            'format': 'json',
            'keyword': self.keyword,
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
        }
        self.url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    # 获取页面
    def get_page (self):
        res = requests.get(self.url)
        return res.json()['data']
    # 获取图片
    def get_imgs (self):
        data = self.get_page()
        for item in data:
            if item.get('has_image'):
                title = item.get('title')
                images = item.get('image_list')
                for img in images:
                    yield {
                        'title': title,
                        'image': 'https:' + img.get('url')
                    }
    # 保存图片
    def save_imgs (self, item):
        if not os.path.exists(item.get('title')):
            os.mkdir(item.get('title'))
        try:
            print(item)
            res = requests.get(item.get('image'))
            if res.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(res.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(res.content)
                else:
                    print('重复下载', file_path)
        except requests.ConnectionError:
            print('保存图片错误')
    # 启动方法
    def start (self):
        img = self.get_imgs()
        for item in img:
            self.save_imgs(item)

if __name__ == '__main__':
    newTouTiao = TouTiao()
    img = newTouTiao.start()
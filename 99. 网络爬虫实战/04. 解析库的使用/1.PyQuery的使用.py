from pyquery import PyQuery as pq
import requests

# 抓取的URL
URL = 'http://www.rxshc.com/'

# 包装 pyquery 对象
doc = pq(requests.get(URL).text)

# 抓取到的标题
sTitle = doc('title').text()
# 抓取到的文章列表
sPostListDoc = doc('#postlist .postitem')
# 存储格式化后的文章列表
sPostListArr = []
# 遍历组装列表数据
for post in sPostListDoc:
    post = pq(post)
    sPostListArr.append({
        'title': post.find('.title a').text(),
        'href': post.find('.title a').attr('href'),
        'des': post.find('.format').html()
    })

print(sPostListArr)
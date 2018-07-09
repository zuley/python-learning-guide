from urllib.parse import urlparse

reust = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(reust), reust)
from urllib import request, parse

url = 'http://httpbin.org/post'
header = {
  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
  'Host': 'httpbin.org'
}
dict = {
  'name': 'test'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=header, method='POST')
res = request.urlopen(req)
print(res.read().decode('utf-8'))
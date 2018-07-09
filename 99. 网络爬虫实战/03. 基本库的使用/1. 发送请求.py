import urllib.request
import urllib.parse
import socket

data = bytes(urllib.parse.urlencode({'w': 'h'}), encoding='utf8')
try:
  response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=0.1)
except urllib.error.URLError as e:
  if isinstance(e.reason, socket.timeout):
    print('TIME OUT')

# print(response.read())
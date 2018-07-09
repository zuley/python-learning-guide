import urllib.request
import socket

try:
  response = urllib.request.urlopen('http://www.rxshc.com/', timeout=0.1)
except urllib.error.URLError as e:
  if isinstance(e.reason, socket.timeout):
    print('time out')
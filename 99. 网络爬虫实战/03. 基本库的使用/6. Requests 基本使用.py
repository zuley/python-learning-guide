import requests

data = {
    'name': '猪不乐意',
    'age': 22
}

r = requests.get('http://httpbin.org/get', params=data)

print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
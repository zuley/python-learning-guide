import requests

def send_message ():
  title = 'title'
  message = 'text'
  token = 'ajpxsb2fr88vigqow99niry9f7vny8'
  user = 'u6a8u7xbx3ody2u1owa1oqdu25dhhy'
  api = 'https://api.pushover.net/1/messages.json?'
  template = 'token={token}&user={user}&message={message}&title={title}&url={url}'
  query = template.format(
    title = title,
    token = token,
    user = user,
    message = message,
    url = 'http://www.rxshc.com'
  )
  return api + query

def push_it ():
  requests.post(send_message())

push_it()

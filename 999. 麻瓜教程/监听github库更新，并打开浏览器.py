import requests
from pyquery import PyQuery as pq
from time import sleep
import webbrowser

gitUrl = 'https://github.com/zuley/python-learning-guide/commits/master'
hitDate = '2018-09-09T06:09:00Z'

def getGithubUpdate () :
  try:
    doc = pq(requests.get(gitUrl).text)
    return doc('.commits-listing .table-list relative-time').eq(0).attr('datetime')
  except expression as identifier:
    print('获取内容失败', expression)

if __name__ == '__main__':
  while (True):
    print('进入循环，开始获取github仓库形象')
    curDate = getGithubUpdate()
    if curDate > hitDate:
      print('github 仓库已经更新，打开浏览器')
      webbrowser.open(gitUrl)
      hitDate = curDate
    else:
      print('github 仓库未更新，跳过继续下一个循环。')
    sleep(3)
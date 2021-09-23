'''
LastEditors: 杜康
LastEditTime: 2021-09-23 17:02:45
'''
from urllib.request import urlopen
# 处理404跟500
from urllib.error import HTTPError
# 处理URL错误
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle (url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h1
  except AttributeError as e:
    return None
  return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
  print('Title cound not be found')
else:
  print(title)
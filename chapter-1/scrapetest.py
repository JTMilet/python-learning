'''
LastEditors: 杜康
LastEditTime: 2021-09-23 16:57:43
'''
from urllib.request import urlopen
# 处理404跟500
from urllib.error import HTTPError
# 处理URL错误
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
  html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
  print(e)
except URLError as e:
  print('The server cound not be found')
else:
  print('It worked!')
bs = BeautifulSoup(html.read(), 'html.parser') # 将获取到的页面转成一个BS对象
# 通过对BS对象进行检查
try:
  badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
  print('Tag was not found')
else:
  if badContent == None:
    print('Tag was not found')
  else:
    print(badContent)
print(bs.h1)
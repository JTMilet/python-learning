'''
LastEditors: 杜康
LastEditTime: 2021-09-23 19:45:37
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find_all('a'):
# 在id为bodyContent中
# URL中不包含冒号:
# URL都以/wiki/开头
for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
  if 'href' in link.attrs:
    print(link.attrs['href'])

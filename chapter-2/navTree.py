'''
LastEditors: 杜康
LastEditTime: 2021-09-23 19:19:01
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# 查找所有的后代标签
# for child in bs.find('table', {'id': 'giftList'}).children:
#   print(child)

# 查找所有的兄弟标签
# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#   print(sibling)

# 查找父标签
# print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
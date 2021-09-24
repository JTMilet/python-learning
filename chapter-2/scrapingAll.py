'''
LastEditors: 杜康
LastEditTime: 2021-09-23 22:15:14
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all('span',
                       {'class': 'green'})  # 获取所有含有class =  green 的span 标签
nameList2 = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])
for name in nameList:
    print(name.get_text())  # get_text() 会清空通过bs对象获取到的所有的标签的标签，但是不会清掉文本
    # print(name)
# divide line
print('------------- divide line --------------')
for name in nameList2:
    print(name.get_text())
# divide line
print('------------- divide line --------------')
# 匹配所有的文本
nameList3 = bs.find_all(text='the prince')
for name in nameList3:
    print(name)
print('------------- divide line --------------')
# 匹配所有的文本
nameList4 = bs.find_all('span', {'class': ['green', 'red']})
for name in nameList4:
    print(name.get_text())

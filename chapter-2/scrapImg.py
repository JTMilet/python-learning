'''
LastEditors: 杜康
LastEditTime: 2021-09-23 22:15:15
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
# images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
# for img in images:
#   print(img['src'])

# lambda表达式
# tags = bs.find_all(lambda tag: len(tag.attrs) == 2)
# for tag in tags:
#   print(tag)

tags = bs.find_all(
    lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
for tag in tags:
    print(tag)

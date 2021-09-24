'''
LastEditors: 杜康
LastEditTime: 2021-09-23 22:14:49
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {
        'id': 'bodyContent'
    }).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

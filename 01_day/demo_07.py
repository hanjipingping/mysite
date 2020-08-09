# _*_coding:utf-8_*_
# @time :2020-06-27 09:12 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_07.py
# @software PyCharm
'''
BeautifulSoup   美味汤
soup.prettify   美化

'''

from bs4 import BeautifulSoup

import requests

url = requests.get('http://www.baidu.com')
demo = url.text

soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())
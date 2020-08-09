# _*_coding:utf-8_*_
# @time :2020-06-27 09:27 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_08.py
# @software PyCharm

'''
BeautifulSoup   美味汤

'''

from bs4 import BeautifulSoup
import requests

url = 'http://www.baidu.com'

r = requests.get(url)
r.encoding = r.apparent_encoding

demo = r.text

soup = BeautifulSoup(demo,'html.parser')
print(soup.name)
print(soup.tag)
print(soup.title)
print(soup.a.name)
print(soup.a.attrs)   #获取标签属性值
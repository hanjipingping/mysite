# _*_coding:utf-8_*_
# @time :2020-06-27 11:10 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_10.py
# @software PyCharm

'''
bs4库的html 内容的查抄方法
.find_all(name)
name:对标签名称的检索字符串
attrs：对标签属性值的检索字符串，可标注属性检索
recursive=False,在子节点检索需要的信息

'''

import requests

from bs4 import BeautifulSoup

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
demo1 = soup.find_all('a')
print(demo1)

for tag in soup.find_all(True):
    print(tag.name)


print(soup.find_all(id = 'link1'))
print(soup.find_all('a',recursive=False))




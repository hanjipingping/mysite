# _*_coding:utf-8_*_
# @time :2020-06-27 10:47 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_09.py
# @software PyCharm

'''
bs4库的基本元素：
tag、name、Attributes、NavigableSting、Comment
bs4的遍历功能：
.contents  获取子节点的信息，存储在列表中
.children
.descendants

获取父级节点：
.parent
.parents
平行遍历：








'''
import requests
from bs4 import BeautifulSoup
r = requests.get('http://python123.io/ws/demo.html')

demo = r.text

soup = BeautifulSoup(demo,'html.parser')

#
# print(soup.head)
# print(soup.head.contents)   #获取子节点标签，存储在列表中
# print(soup.body.contents)

for child in soup.body.children:
    print(child)

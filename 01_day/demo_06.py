# _*_coding:utf-8_*_
# @time :2020-06-25 20:50 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_06.py
# @software PyCharm
'''

爬却图片
、
'''
import requests
import os
url = 'http://images.jddmoto.com/forum/20200625/4784838_1593087494841.jpeg!forum?_2736_3648'

b = os.path.dirname(__file__)
c = os.path.dirname(os.path.dirname(os.path.dirname(b))) + '/Desktop'
print(c + '/a.jpg')


r = requests.get(url)

print(r.status_code)

with open(c + '/a.jpg','wb') as f :
    f.write(r.content)

    f.close()
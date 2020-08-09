# _*_coding:utf-8_*_
# @time :2020-06-24 22:41 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_03.py
# @software PyCharm

import requests

url = 'https://item.jd.com/67058419855.html'

r = requests.get(url)
print(r.status_code)
print(r.headers)








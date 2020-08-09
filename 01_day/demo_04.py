# _*_coding:utf-8_*_
# @time :2020-06-25 20:11 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_04.py
# @software PyCharm
'''
亚马逊

'''

import requests

try:
    url = 'https://www.amazon.cn/dp/B00IZ821LU?ref_=Oct_DLandingS_D_c85c7ee3_61&smid=A3CQWPW49OI3BQ'
    kv = {'uaser-agent':'mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding =r.apparent_encoding
    print(r.text)

except:
    print('errow')

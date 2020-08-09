# _*_coding:utf-8_*_
# @time :2020-06-25 20:24 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_05.py
# @software PyCharm

'''
获取百度关键字信息代码

'''
import requests
try:
    url = 'http://www.baidu.com/s'
    kv1 = {'user-agent':'moailla/5.0'}
    kv = {'wd':'python'}
    r = requests.get(url,params=kv,headers = kv1)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.headers)

    print(r.request.url)
    print(len(r.text))

except:
    print('errow')


try:
    url = 'http://wap.jddmoto.com/brand-detail?'
    kv1 =  {'userw-agent':'moailla/5.0'}
    kv = {'id':8,'name':'阿普利亚'}
    r = requests.get(url,params=kv, headers = kv1,)
    r.raise_for_status()
    r.encoding = r.raise_for_status()
    print(r.request.url)
    print(r.text)

except:
    print('errow')
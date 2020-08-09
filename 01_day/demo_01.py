# _*_coding:utf-8_*_
# @time :2020-06-24 13:53 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :demo_01.py
# @software PyCharm

import requests
#
# r = requests.get('http://www.baidu.com')
# r.encoding = r.apparent_encoding
# print(r.encoding)
# print(r.text)

def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)  #获取url信息，
        r.raise_for_status()    #状态码是否返回200
        r.encoding = r.apparent_encoding   #设置正确的编码格式
        return r.text
    except:
        return "Something Wrong!"


if __name__ == '__main__':

    print(getHtmlText('http://www.baidu.com'))






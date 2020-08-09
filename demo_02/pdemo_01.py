# _*_coding:utf-8_*_
# @time :2020-08-08 20:05 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :pdemo_01.py
# @software PyCharm
from urllib.error import HTTPError,URLError

from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    html = urlopen('http://www.baidu.com')
    bso = BeautifulSoup(html.read(),'html.parser')
except URLError as e:
    print(e)

except HTTPError as e:
    print(e)

else:
    print(bso.h1)
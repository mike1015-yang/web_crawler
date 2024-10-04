# parse: 將資料轉成網頁伺服器看得懂的樣子
from urllib import request, parse
from bs4 import BeautifulSoup

url = 'http://httpbin.org/post'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent':user_agent}

data = {'key1':'value1', 'key2':'value2'}
data = bytes(parse.urlencode(data), encoding = 'utf-8')

req = request.Request(url = url, data = data, headers = headers)
res = request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')

print(soup)


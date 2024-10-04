# parse: 將資料轉成網頁伺服器看得懂的樣子
import requests
from bs4 import BeautifulSoup

url = 'http://httpbin.org/post'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent':user_agent}

data = {'key1':'value1', 'key2':'value2'}

res = requests.post(url = url, data = data, headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify)


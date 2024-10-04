import requests
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent': user_agent,
           'Cookie':'over18=1'
          }

# urllib方法
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

# print(res.read().decode('utf-8'))

# requests方法
res = requests.get(url = url, headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())
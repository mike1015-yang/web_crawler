from urllib import request
from bs4 import BeautifulSoup as bs
url = 'https://www.ptt.cc/bbs/joke/index.html'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

soup = bs(res, 'html.parser')
print(soup)
# print(res.read().decode('utf8'))
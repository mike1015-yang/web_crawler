from urllib import request
from bs4 import BeautifulSoup as bs
url = 'https://www.ptt.cc/bbs/joke/index.html'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

soup = bs(res, 'html.parser')

# soup.findAll('div', id = 'action-bar-container') 兩種寫法
action_bar = soup.findAll('div', {'id':'action-bar-container'})

tmp_div = action_bar[0].find('div')
tmp_a = action_bar[0].find('a')
# print(f"other <div>: ")
# print(tmp_div)
# print(f"other <a>: ")
# print(tmp_a)

# tmp_a.string 和 tmp_a.text 功能一樣
tmp_text_in_a = tmp_a.string
print(tmp_text_in_a)

tmp_url = tmp_a['href']
print(f"https://www.ptt.cc{tmp_url}")
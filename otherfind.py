from urllib import request
from bs4 import BeautifulSoup as bs
url = 'https://www.ptt.cc/bbs/joke/index.html'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

soup = bs(res, 'html.parser')

# soup.select('div#action-bar-container') 兩種寫法
action_bar = soup.select('div[id="action-bar-container"]')
# print(action_bar)

# action_bar[0].select_one('div') 和下面結果一樣
tmp_div = action_bar[0].div
# print(f"other <div>: ")
# print(tmp_div)

# 可以繼續.div，但都只會找到第一個<div>
tmp_div = action_bar[0].div.div
# print(tmp_div)

# 如果<div>裡面有多個<div>
tmp_div = action_bar[0].div.div.next_sibling.next_sibling
# print(tmp_div)
for i in action_bar[0].div.div.next_siblings:
    print(i)


# 一次找多個<a>
for i  in action_bar[0].div.div.next_sibling.next_sibling.a.next_siblings:
    print(i)



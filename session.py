import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent':user_agent }
# 建立連線
ss = requests.session()

ss.cookies['over18'] = '1'

res = ss.get(url = url, headers = headers)

print(res.text)
# parse: 將資料轉成網頁伺服器看得懂的樣子
import requests
from bs4 import BeautifulSoup

url = 'https://organic.afa.gov.tw/InOrganic/QueryApplyList'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent':user_agent}

res = requests.post(url = url, headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')

for i in soup.select('input[type="hidden"]'):
    try:
        print(f"{i['name']}\t{i['value']}")
    # 有些 hidden data 沒有 value 所以可能會出錯
    except KeyError:
        pass


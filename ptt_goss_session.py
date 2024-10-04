import requests
from bs4 import BeautifulSoup
import os

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent':user_agent}

resource_path = './ptt_goss'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

# 詢問是否18的頁面
url_if18 = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2Fgossiping%2Findex.html'
# 存放把隱藏表單的資料送進去的網址
url_tmp = ''

url_goss = 'https://www.ptt.cc/bbs/gossiping/index.html'

post_data = {}

ss = requests.session()

res_url_if18 = ss.get(url = url_if18, headers = headers)

soup_if18 = BeautifulSoup(res_url_if18.text, 'html.parser')
# 製作post_data，隱藏表單的資料
button = soup_if18.select('button[class="btn-big"]')[0]

button_key = button['name']

button_value = button['value']

post_data[button_key] = button_value

hidden = soup_if18.select_one('input')

hidden_key = hidden['name']

hidden_value = hidden['value']

post_data[hidden_key] = hidden_value

url_tmp = f"https://www.ptt.cc{soup_if18.select_one('form')['action']}"
# 把表單資料送進去後，Cookie就自動設定好了
ss.post(url = url_tmp, headers = headers, data = post_data)

res_url_goss = ss.get(url = url_goss, headers = headers)

soup_url_goss = BeautifulSoup(res_url_goss.text, 'html.parser')

for each_title in soup_url_goss.select('div[class="r-ent"]'):
    title = each_title.select_one('div[class="title"]').a.text
    print(f"標題: {title}")
    article_url = f"https://www.ptt.cc{each_title.a['href']}"
    print(f"網址: {article_url}")

    score = each_title.select_one('div[class="nrec"]').text
    print("="*30)

    res_article_url = ss.get(url = article_url, headers = headers)
    soup_article_url = BeautifulSoup(res_article_url.text, 'html.parser')

    content = soup_article_url.select_one('div[id="main-content"]').text.split("--")[0]
    # print(content)

    # print("---split---")
    good = 0
    bad = 0
    for message in soup_article_url.select('div[id="main-content"] div[class="push"]'):
        try:
            if message.select_one('span').text.strip() == '推':
                good += 1
            elif message.select_one('span').text.strip() == '噓':
                bad += 1
        except IndexError:
            pass
    # print(f"推: {good}")
    # print(f"噓: {bad}")
    # print(f"分數: {score}")
    author = soup_article_url.select('div[class="article-metaline"] span[class="article-meta-value"]')[0].text
    topic = soup_article_url.select_one('div[class="article-metaline-right"]').text
    small_title = soup_article_url.select('div[class="article-metaline"] span[class="article-meta-value"]')[1].text
    time = soup_article_url.select('div[class="article-metaline"] span[class="article-meta-value"]')[2].text
    # print(f"作者: {author}\n標題: {small_title}\n時間: {time}")
    all_content = f"{content}\n---split---\n推: {good}\n噓: {bad}\n\
分數: {score}\n作者: {author}\n標題: {small_title}\n時間: {time}"
    new_title = title
    for iw in '[\/:*?"<>|]':
        new_title = new_title.replace(iw, '_')
    with open(r'%s/%s.txt' % (resource_path, new_title), 'w', encoding='utf-8') as w:
        w.write(all_content)
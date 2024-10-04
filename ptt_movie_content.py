import requests
from bs4 import BeautifulSoup
import os

headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

resource_path = './res'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

# 方法一: 每一頁網址有規律時
i = 0
while i < 1:
    url = f"https://www.ptt.cc/bbs/movie/index{10314-i}.html"

    res = requests.get(url = url, headers = headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_article in article_title_html:
        try:
            print(each_article.a.text)
            print(f"https://www.ptt.cc{each_article.a['href']}\n")

            article_url = f"https://www.ptt.cc{each_article.a['href']}"
            article_text = each_article.a.text

            article_res = requests.get(url = article_url, headers = headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')

            article_content = article_soup.select('div[id="main-content"]')[0].text.split('--')[0]
            
            with open(r'%s/%s.txt' % (resource_path, article_text), 'w', encoding='utf-8') as w:
                w.write(article_content)
            # print(article_content)
            # print("="*30)

        except AttributeError as e:
            print(each_article)
            print(e.args)
        except FileNotFoundError as fe:
            with open(r'%s/%s.txt' % (resource_path, article_text.replace('/',' ')), 'w', encoding='utf-8') as w:
                w.write(article_content)
    i += 1
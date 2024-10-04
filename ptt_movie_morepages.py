import requests
from bs4 import BeautifulSoup

headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
# 方法一: 每一頁網址有規律時
# i = 0
# while i < 2:
#     url = f"https://www.ptt.cc/bbs/movie/index{10314-i}.html"

#     res = requests.get(url = url, headers = headers)

#     soup = BeautifulSoup(res.text, 'html.parser')

#     article_title_html = soup.select('div[class="title"]')

#     for each_article in article_title_html:
#         try:
#             print(each_article.a.text)
#             print(f"https://www.ptt.cc{each_article.a['href']}\n")
#         except AttributeError as e:
#             print(each_article)
#             print(e.args)
#     i += 1

# 方法二:找到上一頁按鈕的標籤位置

url = f"https://www.ptt.cc/bbs/movie/index.html"
res = requests.get(url = url, headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 上一頁標籤的網址
last_page_url = soup.select('a[class="btn wide"]')[1]['href']
last_page_url = f"https://www.ptt.cc{last_page_url}"

i = 0
while i < 2:
    res = requests.get(url = url, headers = headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_article in article_title_html:
        try:
            print(each_article.a.text)
            print(f"https://www.ptt.cc{each_article.a['href']}\n")
        except AttributeError as e:
            print(each_article)
            print(e.args)
    i += 1
    url = last_page_url
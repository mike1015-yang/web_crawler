import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

res = requests.get(url = url, headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')

# .prettify(): 幫HTML排版
# print(soup.prettify())
article_title_html = soup.select('div[class="title"]')

# print(article_title_html)

for each_article in article_title_html:
    print(each_article.a.text)
    print(f"https://www.ptt.cc{each_article.a['href']}\n")
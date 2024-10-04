import requests
from bs4 import BeautifulSoup

url = 'https://organic.afa.gov.tw/InOrganic/QueryApplyList'

# 製作post data，在開發人員工具裡的element，找到表單input的地方，還有hidden data，就是post_data
post_data = {
    "TYPE": "1",
    "YEAR": "",
    "qNnify_NO": "",
    "qC_NAME": "",
    "qPaper_NO": "",
    "qProduct_NAME": "米".encode("big5"),
    "B": "查　　詢"
}

# 製作header 只需要User-Agent就好
headers_str = """User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"""

headers = {}
for row in headers_str.split('\n'):
    try:
        headers[row.split(": ")[0]] = row.split(': ')[1]
    except IndexError:
        pass

res = requests.post(url = url, data = post_data, headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')

content = soup.select('table table tr')

i = 0
while i < 10:
    title = content[7+i].select('td')[0].text
    phone = content[7+i].select('td')[1].text
    caseNo = content[7+i].select('td')[2].a.text
    print(f"廠商名稱: {title}")
    print(f"連絡電話: {phone}")
    print(f"案件編號: {caseNo}")
    print("="*15)
    i += 1



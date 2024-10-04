import requests
import json
from urllib import request
import os

url = 'https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6543212'

# 創建放圖片的目錄
res_path = './NOWnews_image'
if not os.path.exists(res_path):
    os.mkdir(res_path)

for i in range(2):
    res = requests.get(url = url)

    json_str = res.text

    # json_data是一個字典，最外層的key有'msg'、'code'、'data'
    json_data = json.loads(json_str)

    # 取得字典裡key='data'和他的value
    for key, value in json_data.items():
        if key == 'data':
            newList = value
        else:
            continue

    # newList也是字典，key='newList'，取得他的value
    for value in newList.values():
        newList_value = value

    for i in range(len(newList_value)):
        article_title = newList_value[i]['postTitle']
        article_url = newList_value[i]['postUrl']
        article_image_url = newList_value[i]['imageUrl']

        location = os.path.join(res_path + '/%s.jpg'%(article_title).replace('/', ''))
        request.urlretrieve(article_image_url, location)
        
        print(f"{article_title}")
        print(f"https://www.nownews.com/{article_url}")
    
    url = f"https://www.nownews.com/nn-client/api/v1/cat/column/?pid={newList_value[len(newList_value)-1]['id']}"

import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.newmobilelife.com/wp-json/csco/v1/more-posts'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

headers = {'User-Agent': user_agent}

for i in range(2):
    post_data = {'action': 'csco_ajax_load_more',
                'page': i + 1,
                'posts_per_page': 30}

    res = requests.post(url = url, headers = headers, data = post_data)

    json_res = json.loads(res.text)

    for value in json_res['data'].values(): 
        data_value = value

    soup = BeautifulSoup(data_value, 'html.parser')

    for each_title in soup.select('h2[class="cs-entry__title"]'):
        print(f"標題: {each_title.text}")
        print(f"網址: {each_title.a['href']}\n")
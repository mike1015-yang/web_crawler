import requests
import json

url = 'https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6543173'

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

# newList_value是一個list，取得裡面每個index的值
# for value in newList_value:
#     print(value)
#     print("="*30)

for key in newList_value[0].keys():
    print(key)

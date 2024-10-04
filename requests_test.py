import requests

url = 'http://httpbin.org/get'

res = requests.get(url)

print(res.text)
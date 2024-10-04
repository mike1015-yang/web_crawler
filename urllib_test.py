from urllib import request

url = 'http://httpbin.org/get'
# 對網頁提出請求
res = request.urlopen(url)

# print(f"res.read(): {res.read()}")
# print("-"*100)

# print(f"res.read(): {res.read().decode('utf8')}")
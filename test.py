import requests

print("你好GitHub!!!!！")

res = requests.get("https://baidu.com")
print(res.status_code)
print(res.text)

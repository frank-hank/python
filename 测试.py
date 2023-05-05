# import json
import requests

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Cookie": "mysession=MTY4MjI3Mzg0MHxOd3dBTkU5TU5GTk5URGRQU2twR05WUlFTRTVKVUVVMlVqSklVMHROVWtKSU5VZENVbGRaVGxkWlJWZE5WMGxaU2xoSFFrUTBSRUU9fNG7s8VXexJmv_3WnmdO6uWWZesJ1_bvKvYNhD1EbHf7",
#     "Host": "127.0.0.1",
#     "sec-ch-ua": "Chromium;v=112, Microsoft Edge;v=112, Not:A-Brand;v=99",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58",
# }
res = requests.get("https://www.baidu.com")
# res = requests.post("http://127.0.0.1", json={"name": "迭代", "age": "8"})
print(res.status_code)

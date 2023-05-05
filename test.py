import requests

print("你好GitHub!!!!！")
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "tieba.baidu.com",
    "Referer": "https://tieba.baidu.com/",
    "sec-ch-ua": "Not A;Brand;v=99, Chromium;v=102",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}
res = requests.get("https://baidu.com", headers=headers)
print(res.status_code)

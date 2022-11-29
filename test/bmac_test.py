__author__ = 'duhongming'

import requests
from easyocr import easyocr

verify_url = 'https://www.bmac.com.cn/index/verify.html'
headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'referer': 'https://www.bmac.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
resp = requests.get(verify_url, headers=headers, verify=False)
with open('verify.png', 'wb+') as verify:
    verify.write(resp.content)

reader = easyocr.Reader(['en'], model_storage_directory='../model/')
result = reader.readtext('verify.png')
captcha = "".join(result[0][1].split(" "))
print(captcha)

url = "https://www.bmac.com.cn/userserver/cardRecord"

payload = f'id=10007515114549481946&captcha={captcha}'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://www.bmac.com.cn',
    'Referer': 'https://www.bmac.com.cn/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)

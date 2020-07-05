import requests
import random

url = 'http://icanhazip.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36icanhazip.com	favicon.ico	'}


proxiesLs = ['52.179.231.206:80','101.200.127.149:3129',"101.37.118.54:8888"]  # 存放代理 ip

for i in range(len(proxiesLs)):

    proxy = proxiesLs[i]
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    try:
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies)
        print(i)
        print(response.text)
    except:
        pass

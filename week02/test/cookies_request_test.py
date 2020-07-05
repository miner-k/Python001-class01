
import requests
from fake_useragent import UserAgent

url = 'https://shimo.im/welcome'


us = UserAgent(verify_ssl=False)
# print(us.random)
user_agent = us.random

headers = {
    'user-agent': user_agent,
    # 'referer': 'https://shimo.im/login?from=home',
    'origin': 'https://shimo.im'
}

data = {
    "email": "543156149@qq.com",
    "mobile": "+86undefined",
    "password": "543156149qq",
}

r = requests.session()

response = r.get(url=url,headers=headers)
# print(headers)
# print(response.text)
print(response.headers)
print(response.status_code)

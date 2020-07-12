import requests
from fake_useragent import UserAgent

print()

headers = {
    'User-Agent': UserAgent(verify_ssl=False).random
}


url = 'https://ip.jiangxianli.com/api/proxy_ips'
response = requests.get(url=url,headers=headers)

jsonObj = response.json()
# print(jsonObj)
if jsonObj['msg'] == '成功' :
    for ipinfo in jsonObj['data']['data']:
        print('地址:{} 代理地址{}'.format(ipinfo['ip_address'],ipinfo['protocol'] +'://'+ ipinfo['ip'] +":"+ ipinfo['port']))
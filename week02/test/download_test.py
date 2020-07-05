

import requests

# 小文件下载
# response = requests.get('https://assets.smcdn.cn/static/lizard-service-homepage/assets/service_solutions_logos.6e8e9103.png')
#
# with open('a.png','wb') as f:
#     f.write(response.content)

# 大文件下载
# 如果大文件下载的时候，需要先件下载的内容存放到内存里面，内存还是比较大的内存压力
# 所以为了防止内存不够用的现象，我们把文件分段下载
url = "https://cdn.npm.taobao.org/dist/chromedriver/81.0.4044.20/chromedriver_win32.zip"
response = requests.get(url=url,stream=True)

with open('a.zip','wb') as f:
    for  chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)


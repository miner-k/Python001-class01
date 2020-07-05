
import requests
import lxml.etree

url = "https://book.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
print(response.status_code)

# xml 化处理
selector = lxml.etree.HTML(response.text)

# bookname = selector.xpath('//div[@class="pl2"]/a/text()')
# bookname = selector.xpath('//div[@class="pl2"]/a/@title')
bookname1 = selector.xpath('//*[@id="content"]/div/div[1]/div/table[3]/tbody/tr/td[2]/div[1]/a')
print(bookname1)


'''
需求：安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。


思路：
1.导入requests、bs4
2.通过requests.get请求访问“ https://maoyan.com/films?showType=3”
3.通过BeautifulSoup提取电影的数名词、类型、上映时间
4.保存文件为csv格式的文件
'''


import  requests
from bs4 import BeautifulSoup
from pandas import DataFrame,Series


def getBookInfo():
    url = "https://book.douban.com/top250"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }

    response = requests.get(url=url,headers=headers)
    print(response.status_code)
    # print(response.text)
    context = BeautifulSoup(response.text,'html.parser')
    book_list = []
    for book in context.find_all('tr',class_="item"):

        if len(book_list) > 10 :
            return book_list
        book_name = book.find('div',class_="pl2").find('a')['title']
        book_info = book.find('p',class_="pl").text.split("/")
        book_price = book_info[-1]
        book_publisher = book_info[-3]
        book_list.append([book_name,book_publisher,book_price])

bookname = []
bookpublish = []
bookprice = []
for item in getBookInfo():
    bookname.append(item[0])
    bookpublish.append(item[1])
    bookprice.append(item[2])


data = {
    "书名": Series(data=bookname),
    "出版社": Series(data=bookpublish),
    "价格": Series(data=bookprice)
}

df = DataFrame(data)
df.to_csv(path_or_buf='./movies.csv',index=False,encoding='utf_8_sig')



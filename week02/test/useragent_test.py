

from fake_useragent import UserAgent

# 取消 ssl验证
ua = UserAgent(verify_ssl=False)

# 模拟不同的浏览器
print(ua.chrome)
print(ua.safari)
print(ua.ie)

# 随机返回头部信息，推荐使用
print(ua.random)


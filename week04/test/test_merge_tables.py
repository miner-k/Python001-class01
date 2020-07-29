
import pandas as pd
import numpy as np

group = ['x','y','z']
data1 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

data2 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

data3 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })

print(data1)

print("#"*30)
print(data2)
print("#"*30)
print(data3)

# # 一对一
# print(pd.merge(data1, data2))
#
# # 多对一
# print(pd.merge(data3, data2, on='group'))
# print(pd.merge(data3, data2))
#
# # 多对多
# print(pd.merge(data3, data2))
#
# # 连接键类型，解决没有公共列问题
print(pd.merge(data3, data2, left_on= 'age', right_on='salary'))
#
# 连接方式
# 内连接，不指明连接方式，默认都是内连接
pd.merge(data3, data2, on= 'group', how='inner')
# 左连接 left
# 右连接 right
# 外连接 outer

# 纵向拼接
pd.concat([data1, data2])
#

import pandas as pd
import numpy as np

# x = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
# # 检验序列中是否存在缺失值
# print(x.hasnans)
#
#
# print(x)
# # 将缺失值填充为平均值
# x1 = x.fillna(value=x.mean())
# print(x1)
# 前向填充缺失值

df3 = pd.DataFrame({"A": [5, 3, None, 4,4],
                    "B": [None, 2, 4, 3,3],
                    "C": [4, 3, 8, 5,5],
                    "D": [5, 4, 2, None,None],
                    "e": [5, 4, 2, None,None]})

print(df3)
# print(df3.isnull())
# print(df3.isnull().sum())  # 查看缺失值汇总

# df4 = df3.ffill()  # 用上一行填充

# df4 = df3.ffill(axis=1)  # 用前一列填充
#
# # 缺失值删除
# df3.info()
# df4 = df3.dropna()
#
# # 填充缺失值
# df4 = df3.fillna('无')
#
# # 重复值处理
df4 = df3.drop_duplicates()

print(df4)

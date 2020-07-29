

'''









'''


import pandas as pd

data = pd.DataFrame({
    'id' : [91,1002,500,None,1000,600,10],
    'name' : ['Jim','Tom','lucy','lucky','Don','Donr','tt'],
    'age':[21,22,20,32,21,40,50]
})

data2 = pd.DataFrame({
    'user_id' : [1,102,50,None,100,60,1],
    'name' : ['Jim','Tm','lcy','luky','Dn','Dnr','t'],
    'age':[21,22,20,32,21,40,50]
})

data3 = pd.DataFrame({
    'id' : [91,1002,500,None,1000,600,10],
    'name' : ['Jim','Tom','lucy','lucky','Don','Donr','tt'],
    'age':[21,22,20,32,21,40,50]
})
# # 1. SELECT * FROM data;
#
# print(data)
#
# # 2. SELECT * FROM data LIMIT 10;
#
# print(data.head(2))
#
# # 3. SELECT id FROM data;  //id 是 data 表的特定一列
#
# print(data['id'])
#
# # 4. SELECT COUNT(id) FROM data;
# print(data.count(axis=0)['id'])

# # 5. SELECT * FROM data WHERE id<1000 AND age>30;
#
# print(data[(data['id']< 1000) & (data['age'] > 30 )] )

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

# print(data.groupby('id').count())

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

print( data.merge(data2, left_on='id', right_on='user_id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([data,data3]))

# 9. DELETE FROM table1 WHERE id=10;
print(data.drop(data [data['id'] == 10].index))
# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(data.drop('name',axis=1))

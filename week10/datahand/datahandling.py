import pandas as pd
from sqlalchemy import create_engine
from snownlp import SnowNLP
import time



# # 查询语句
# qury_comment_tables = '''
#       show tables like "comment%%";
#       '''
# # read_sql_query的两个参数: sql语句， 数据库连接
# tables_pd = pd.read_sql_query(qury_comment_tables, engine)



def comment_analyze(table_name,engine):
    '''
    输入爬虫收集数据表，输出当天前十个商品的评价分析，存储到新表中，表名是产品id，表结构是表id，评价，情感分析
    :param table_name:
    :return:
    '''

    # table_name = tables_pd['Tables_in_week10 (comment%)'][0]

    sql = "select * from " + table_name + ";"
    qury_comment_pd = pd.read_sql(sql,engine)
    product_id_list = []
    for num in range(0,11):
        coment = qury_comment_pd.iloc[num]['comment_text'].strip('[').strip(']').split("',")
        emotional_value = []
        for line in coment:
            line = line.strip("'").strip(' ')
            emotional_value.append(SnowNLP(line).sentiments)

        product_pd = pd.DataFrame(data={'comment_text' : pd.Series(data=coment),'emotional_value': pd.Series(data=emotional_value)})
        product_pd['product_id'] = qury_comment_pd.iloc[num]['product_id']
        product_pd.to_sql(name=str(qury_comment_pd.iloc[num]['product_id']),con=engine,if_exists='replace',index=False)

        product_id_list.append(qury_comment_pd.iloc[num]['product_id'])
    comment_analyze_his = pd.DataFrame({"product_id": pd.Series(data=product_id_list)})
    comment_analyze_his['soucre_table'] = table_name
    # print(comment_analyze_his)
    comment_analyze_his.to_sql(name="comment_analyze_his", con=engine,if_exists='append')


if __name__ == '__main__':
    # print("#")
    # print("#" * 20)
    engine = create_engine('mysql+pymysql://root:1234@192.168.47.100:3306/week10')
    now_day = time.strftime("%Y_%m_%d", time.localtime())
    table_name = 'comment_' + now_day
    # table_name = 'comment_' + "2020_09_03"

    comment_analyze(table_name,engine)
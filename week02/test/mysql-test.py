
import pymysql


dataInfo = {
    'host': '192.168.47.158',
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'db': 'test'
}

sqls = ['show databases;']

result = []

class ConnDB():

    def __init__(self,dataInfo):
        self.host = dataInfo['host']
        self.port = dataInfo['port']
        self.user = dataInfo['user']
        self.password = dataInfo['password']
        self.db = dataInfo['db']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.db)

        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()

        try:
            for command in self.sqls:
                cur.execute(command)
                # result.append(cur.fetchone())  # 将游标执行的结果存储到列表中
                result.append(cur.fetchall())  # 将游标执行的结果存储到列表中
            # 关闭游标
            cur.close()
            conn.commit()  # 输入事务执行成功，直接提交
        except:
            conn.rollback()
        conn.close()

if __name__ == "__main__":
       con =  ConnDB(dataInfo)
       con.run()
       print(result)
# 导包
import pymysql
# 创建连接
conn=pymysql.connect('localhost','root','root','books', autocommit=True)
# 创建游标
cursor=conn.cursor()
# 执行语句
cursor.execute("update t_book set `read`=`read`+1  where title='三字经';")

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

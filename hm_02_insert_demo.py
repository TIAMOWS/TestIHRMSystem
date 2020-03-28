
# 1导包
import pymysql
# 创建连接
conn=pymysql.connect('localhost','root','root','books', autocommit=True)
# 获取游标
cursor=conn.cursor()
# 执行sql语句:
sql='insert into t_book(id,title,pub_date) value(4,"三字经","2020_03_20")'
cursor.execute(sql)
# 查看执行结果
# cursor.execute('select* from t_book')
print('插入后的结果:',cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
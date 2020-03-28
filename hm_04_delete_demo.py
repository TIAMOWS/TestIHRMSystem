# 导包
import pymysql
# 创建连接
conn=pymysql.connect('localhost','root','root','books', autocommit=True)
# 创建游标
cursor=conn.cursor()
cursor.execute('select* from t_book;')
print('删除前数据:',cursor.fetchall())
# 执行删除语句
cursor.execute("delete from t_book where title='三字经';")
cursor.execute('select* from t_book;')
print('删除后数据:',cursor.fetchall())

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

# 导包
import pymysql
# 创建连接
conn=pymysql.connect('localhost','root','root','books')
# 创建游标
cursor=conn.cursor()
# 执行sql语句:查询全部的图书数据
cursor.execute('select id,title,`read`,`comment` from t_book')
# 获取查询结果的记录数
print('rowcount:',cursor.rowcount)

# 获取下一条数据
print('下移条数据:',cursor.fetchone())
print('*'* 20)
print('下移条数据:',cursor.fetchone())

# 获取所有行数据
cursor.execute('select id,title,`read`,`comment` from t_book')
book_list=cursor.fetchall()
print('所有数据:',book_list)
for i in book_list:
    print(i[1])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


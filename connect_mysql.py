
# 1.导包
import pymysql
# 2.建立连接
conn=pymysql.connect("localhost", "root", "root", "books")
# 3.创建游标对象
cursor = conn.cursor()
# 4.执行操作：查询数据库版本信息
cursor.execute("select version()")
#5. 获取查询结果
result = cursor.fetchone()
print("result=", result)
# 6.关闭游标对象
cursor.close()
# 7.关闭数据库连接
conn.close()



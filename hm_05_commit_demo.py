# 导包
import pymysql
conn, cursor = None, None
try:
    # 创建数据库连接，不开启自动提交事务
    conn = pymysql.connect("localhost", "root", "root", "books", autocommit=False)
    # 获取游标对象
    cursor = conn.cursor()
    # 新增一条图书数据
    cursor.execute("insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01 ')")

    # 抛出一个异常
    raise Exception("故意抛出了一个异常")
    # 新增一条英雄人物数据
    cursor.execute("insert into t_hero(description,`name`,gender,book_id) values('金箍棒','孙悟空',1,4)")
    # 提交事务
    conn.commit()
except Exception as e:
    print("error:", e)
    # 回滚事务
    conn.rollback()
finally:
    # 关闭游标对象
    if cursor:
        cursor.close()
    # 关闭数据库连接
    if conn:
        conn.close()

import pymysql


class Select:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def select_list(self):
        self.cursor.execute('select* from t_book')
        data = self.cursor.fetchall()
        print(f'查询的数据为:{data}')

with Select('localhost', 'root', 'root', 'books') as a:
    a.select_list()

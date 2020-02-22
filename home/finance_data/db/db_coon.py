import pymysql


class DB():
    def __init__(self):
        self.coon = pymysql.connect(host="localhost", port=3306, user="root", password="haosuozhong", db="haosuozhong",
                                    charset="utf8")
        self.cur = self.coon.cursor()

    # 析构函数
    def __del__(self):
        self.coon.close()
        self.cur.close()

    # 查询函数
    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    # 修改函数
    def change_db(self, sql):
        try:
            self.cur.execute(sql)
            self.coon.commit()
        except Exception as e:
            self.coon.rollback()
            print(str(e))

    def check_user(self, name):
        result = self.query(sql="select * from haosuozhong when name = '{}'".format(name))
        return True if result else False

    def del_user(self, name):
        self.change_db(sql="delete from haosuozhong where name ='{}'".format(name))

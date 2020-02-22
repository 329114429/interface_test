import pymysql

coon = pymysql.connect(host="localhost", port=3306, user="root", password="haosuozhong", db="haosuozhong",
                       charset="utf8")
cur = coon.cursor()
result = cur.execute("select * from haosuozhong where name='hao'")
print(result)

coon.close()
cur.close()

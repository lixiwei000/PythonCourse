import mysql.connector


def show(cursor):
    print("===============查询数据===============")
    cursor.execute("select * from tb_user")
    for user in cursor.fetchall():
        print(user)

def show2(cursor):
    print("===============cursor操作===============")
    cursor.execute("select * from tb_user")
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    cursor.scroll(-1,mode='relative')
if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(user="root",password="lxw1993822",database="dmes")
        cursor = conn.cursor()
        # show(cursor)
        print("===============插入数据===============")
        sql = "insert into tb_user(name,age) values(%s,%s)"
        params = ('张宇',68)
        cursor.execute(sql,params)
        # show(cursor)
        # print("===============删除数据===============")
        # sql = "delete from tb_user where id = %s"
        # params = (11,)
        # cursor.execute(sql,params)
        # print("===============修改数据===============")
        # sql = "update tb_user set name = %s where id = %s"
        # params = ('李熙伟',30)
        # cursor.execute(sql,params)
        # print("===============批量添加===============")
        # sql = "insert into tb_user(name,age) values(%s,%s)"
        # params = [
        #     ('Niko',20),
        #     ('Tom',18),
        #     ('Helen',40)
        # ]
        # cursor.executemany(sql,params)

        show(cursor)
        print(cursor.lastrowid)

        # conn.commit()
        # show(cursor)
    except Exception as e:
        print("数据库操作异常")
        print(e)
    finally:
        # cursor.close()
        conn.close()
import pymysql

from Config.Config import SX_API_URl,SX_DB_HOST,SX_DB_PASS,SX_DB_USER

# username: sunxing_ccs
# password: DPNLRMaZPZdX3WHk
# jdbc:mysql://47.102.193.100:3306
# conn = pymysql.connect(host="47.102.193.100",
#                        user="sunxing_ccs",
#                        password="DPNLRMaZPZdX3WHk",
#                        database="sunxing_ccs", charset="utf8")


class DB_mysql():
    # 更新操作根据返回的状态码来判断有没有更新成功
    def update_db(self,db,data):
        global systen
        conn= pymysql.connect(host=SX_DB_HOST,user=SX_DB_USER,password=SX_DB_PASS,database=db,encoding="utf8")
        cursor=conn.cursor()
        try:
            cursor.execute(data),
            cursor.close()
            systen=1
        except Exception as f:
            print(f)
            systen=0
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        return systen

    # 查询操作根据执行sql查询对应数据 有就返回 没有就返回none
    def select_db(self,db,data):
        global b
        conn=pymysql.connect(host=SX_DB_HOST,user=SX_DB_USER,password=SX_DB_PASS,database=db,charset="utf8")
        cursor=conn.cursor()
        cursor.execute(data)
        cursor.rowcount
        if cursor.rowcount > 0:
            b=cursor.fetchall()
        else:
            None
        cursor.close()
        conn.close()
        return b



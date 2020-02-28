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
    # 查询操作
    def select_db(self,db,data):
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




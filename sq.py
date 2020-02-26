import pymysql

from Config.Config import SX_API_URl,SX_DB_HOST,SX_DB_PASS,SX_DB_USER

# username: sunxing_ccs
# password: DPNLRMaZPZdX3WHk
# jdbc:mysql://47.102.193.100:3306
# conn = pymysql.connect(host="47.102.193.100",
#                        user="sunxing_ccs",
#                        password="DPNLRMaZPZdX3WHk",
#                        database="sunxing_ccs", charset="utf8")

conn = pymysql.connect(host=SX_DB_HOST,
                       user=SX_DB_USER,
                       password=SX_DB_PASS,
                       database="sunxing_ccs", charset="utf8")
cursor=conn.cursor()

sql = """
select `merchant_name`
from `ccs_merchant`
where `merchant_name`= "liu"

"""

cursor.execute(sql)
liu=cursor.fetchall()
print(liu)
cursor.close()
conn.close()
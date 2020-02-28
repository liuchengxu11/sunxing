import pytest
from utils.db_sq import DB_mysql
from TestSuite import conftest
from utils.common import Common
from Config.Config import login_headers


class Test_merchant():
    def setup_class(self):
        self.database = "sunxing_ccs"
        self.db = DB_mysql()

    def test_select_db(self, merchantName_name=None, merchantName_id=None):
        if merchantName_name:
            sqlstring = '''
                        select `id`,
                        `is_delete`
                        from {}.`ccs_merchant`
                        where `merchant_name`= "{}"
                        '''.format(self.database, merchantName_name)
        else:
            sqlstring = '''
                        select `id`,
                        `is_delete`
                        from {}.`ccs_merchant`
                        where `merchant_name`= "{}"
                        '''.format(self.database, merchantName_id)
        a=self.db.select_db(self.database, merchantName_id)
        if a:
            return a[0]
        else:
            None

    def test_update_mer_addorupdate(self,Conftest,merchantName_name):
        with open('./Config/config_token', 'r', encoding='utf-8') as f:
            token = f.read()
        uri="/api/merchant/addOrUpdate"
        data1 = {
            "merchantName": merchantName_name,
            "address": "刘程旭",
            "amountReceived": "string",
            "brandName": "string",
            "commissionRatio": "string",
            "contact": "test2",
            "contactAmount": "string",
            "contactDeadline": "string",
            "contactLink": "string",
            "contactPhone": "13671618736",
            "contactUuid": "string",
            "cooperationStatus": 0,
            "cityAddress": [{
                "areaCode": "310000",
                "areaName": "上海市",
                "level": 1
            }, {
                "areaCode": "310100",
                "areaName": "上海市",
                "level": 2
            }, {
                "areaCode": "310110",
                "areaName": "虹口区",
                "level": 3}],
            "isElmOnline": 0,  # 饿了么是否上线(0.未上线 1.已上线)
            "elmMonthlySales": "",  # 饿了么月销量
            "isMtOnline": 0,  # 美团是否上线(0.未上线 1.已上线)
            "mtMonthlySales": "",
            "intentionality": 2  # 意向度 0不满意 1一般 2满意 3非常满意
        }
        headers1=login_headers
        common=Common()
        status=common.post(uri,data1,headers1)
        if status:
            return merchantName_name
        else:
            return None
    def test_get_mer_addorupdate(self,merchantName_id):
        uri="/api/merchant/getMerchant/{}".format(merchantName_id)
        data={"id":merchantName_id}
        comm=Common()
        comm.post(uri,merchantName_id)



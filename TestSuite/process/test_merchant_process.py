import pytest
from utils.db_sq import DB_mysql
from TestSuite import conftest
from utils.common import Common
from Config.Config import login_headers
import allure
import json
from utils.random_tools import random_merchantName
from Config.Config import SX_API_URl


class Test_merchant():
    def setup_class(self):
        self.database = "sunxing_ccs"
        self.db = DB_mysql()

    @allure.epic("隼骑士小程序")
    @allure.feature("验证商户的基本功能 - 新增> 查询> 删除")
    @pytest.mark.test
    # 验证商户基本功能 - 新增> 查询> 删除
    def test_process(self, Conftest):
        merchantName_name = str(random_merchantName())
    # 新增
        self.test_update_mer_addorupdate(
            Conftest=Conftest, merchantName_name=merchantName_name)
    # 查询  merchantName_id
        merchantName_id, is_delete = self.test_select_db(
            merchantName_name=merchantName_name)
        add = "merchantName_id=" + \
            str(merchantName_id) + "is_delete=" + str(is_delete)
        allure.attach(
            json.dumps(
                merchantName_name,
                ensure_ascii=False,
                indent=4),
            '商户查询接口查询对应的名字-{}'.format(merchantName_name),
            allure.attachment_type.TEXT)
        allure.attach(
            json.dumps(
                add,
                ensure_ascii=False,
                indent=4),
            '商户查询接口查询对应的id和删除id-{}'.format(add),
            allure.attachment_type.TEXT)
        self.test_select_db(merchantName_id)
    # 删除
        self.test_del_met_addorupdate(merchantName_id)
    # 验证数据库
        merchantName_id, is_delete = self.test_select_db(
            merchantName_id=merchantName_id)
        add1 = "merchantName_id=" + \
            str(merchantName_id) + "is_delete=" + str(is_delete)
        allure.attach(
            json.dumps(
                add1,
                ensure_ascii=False,
                indent=4),
            '再次查询商户id所获得的merchantName_id 和is_delete ',
            allure.attachment_type.TEXT)

    # 调用这个查询方法有名字就查询名字 没有就查询ID 有数据就返回然后取第一个id

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
                        where `id`= "{}"
                        '''.format(self.database, merchantName_id)
        a = self.db.select_db(self.database, sqlstring)
        if a:
            return a[0]
        else:
            None
    # 新增商户接口 根据名字增加商户

    def test_update_mer_addorupdate(self, Conftest, merchantName_name):
        uri = "/api/merchant/addOrUpdate"
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
        headers1 = login_headers
        common = Common()
        status = common.post(uri, data1, headers1)
        allure.attach(
            json.dumps(
                status.json(),
                ensure_ascii=False,
                indent=4),
            '新增商户接口新增的名字{},返回的数据'.format(merchantName_name),
            allure.attachment_type.TEXT)
        if status:
            return merchantName_name
        else:
            return None
     # 商户查询接口根据ID来查询

    def test_get_mer_addorupdate(self, merchantName_id):
        uri = "/api/merchant/getMerchant/{}".format(merchantName_id)
        data = {"id": merchantName_id}
        headers1 = login_headers
        comm = Common()
        status = comm.get(uri, data, headers1)
        if status:
            merchantName_id, is_delete = self.test_select_db(
                merchantName_id=merchantName_id)
            print("商户的id能够正常的显示，id为{}".format(merchantName_id))
        else:
            print("商户的id")

    # 商户查询接口——删除
    def test_del_met_addorupdate(self, merchantName_id):
        if merchantName_id:
            headers1 = login_headers
            uri = "/api/merchant/delete"
            req_Body = {"id": merchantName_id}
            status = Common().post(uri, req_Body, headers1)
            allure.attach(
                json.dumps(
                    status.json(),
                    ensure_ascii=False,
                    indent=4),
                '调用删除接口所返回的数据',
                allure.attachment_type.TEXT)
            if status:
                target_Merchant_Id, is_Deleted = self.test_select_db(
                    merchantName_id=merchantName_id)
                allure.attach(
                    json.dumps(
                        is_Deleted,
                        ensure_ascii=False,
                        indent=4),
                    '根据merchantName_id 去查询数据库得到is_Deleted  1就是删除成功 0 就是没删除',
                    allure.attachment_type.TEXT)
                if int(is_Deleted) == 1:
                    print('实现逻辑删除')
                else:
                    print('删除失败，商家还是能被查到')
            else:
                print("接口删除这个接口调用失败")

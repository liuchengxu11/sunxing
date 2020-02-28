import pytest
from utils.common import Common
import time
import allure
from utils.random_tools import random_merchantName
import json
from Config.Config import SX_API_URl
from TestSuite.conftest import Conftest

@allure.epic("隼骑士小程序")
@allure.feature("小程序登陆")
@allure.story("addorupdate_新增修改")
class Test_config():
    merchantName = str(random_merchantName())
    prams = [(merchantName, "王琦"),
             (merchantName, "刘程旭"), (merchantName, "")]

    @pytest.mark.parametrize("test1,test2", prams)
    def test_config(self, Conftest, test1, test2):
        """
        /api/merchant/addOrUpdate 接口的公共配置
        """
        with open('./Config/config_token', 'r', encoding='utf-8') as f:
            token = f.read()
        uri1 = "/api/merchant/addOrUpdate"
        allure.attach(SX_API_URl + uri1, '地址', allure.attachment_type.TEXT)
        data1 = {
            "merchantName": test1,
            "address": "刘程旭",
            "amountReceived": "string",
            "brandName": "string",
            "commissionRatio": "string",
            "contact": test2,
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
        headers1 = {
            'content-type': 'application/json',
            'token': token
        }
        allure.attach(
            json.dumps(
                data1,
                ensure_ascii=False,
                indent=4),
            '请求',
            allure.attachment_type.TEXT)
        allure.attach(
            json.dumps(
                headers1,
                ensure_ascii=False,
                indent=4),
            '请求头',
            allure.attachment_type.TEXT)
        comm1 = Common()
        response1 = comm1.post(uri1, params=data1, headers=headers1)
        allure.attach(
            json.dumps(
                response1.json(),
                ensure_ascii=False,
                indent=4),
            '响应',
            allure.attachment_type.TEXT)
        print(response1.text)
        code = int(response1.status_code)
        code1 = json.loads(response1.text)['code']
        msg = json.loads(response1.text)['msg']
        print(code)
        if code == 200 and code1 == 0:
            print("------------------------")
            print("/api/merchant/addOrUpdate_________接口调用成功")
        elif code == 200 and code1 == 500 and msg == "联系人参数缺失":
            print("------------------------")
            print("/api/merchant/addOrUpdate_________接口调用500_联系人参数缺失")
        elif code == 200 and code1 == 500 and msg == "该商户名称已存在":
            print("------------------------")
            print("/api/merchant/addOrUpdate_________接口调用500_该商户名称已存在")
        else:
            print("------------------------")
            print("/api/merchant/addOrUpdate_________接口调用失败建议查看")

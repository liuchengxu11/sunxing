import pytest
import allure
from Config.Config import User_password, User_account
from utils.common import Common
import json
from Config.Config import SX_API_URl


@pytest.fixture()
def Conftest():
    uri = "/api/user/login"
    allure.attach(SX_API_URl+uri, '地址', allure.attachment_type.TEXT)
    data = {
        "account": User_account,
        "password": User_password
    }
    headers = {
        'content-type': 'application/json'
    }
    allure.attach(json.dumps(data, ensure_ascii=False, indent=4), '请求', allure.attachment_type.TEXT)
    allure.attach(json.dumps(headers, ensure_ascii=False, indent=4), '请求头', allure.attachment_type.TEXT)
    comm = Common()
    response = comm.post(uri, params=data, headers=headers)
    allure.attach(json.dumps(response.json(), ensure_ascii=False, indent=4), '响应', allure.attachment_type.TEXT)
    print("__________________________")
    print(response.text)
    code=int(response.status_code)
    print(code)
    code1 = json.loads(response.text)['code']
    if  code == 200 and code1==0:
        msg = response.json().get('msg')
        with open('./Config/config_token', 'w', encoding='utf-8') as f:
            f.write(msg)
        print("Conftest——成功")
    else:
        print("Conftest——失败")






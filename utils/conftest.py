import pytest
import allure
from Config.Config import User_password,User_account
from utils.common import Common

@allure.epic("隼骑士小程序")
@allure.feature("小程序登陆")

@pytest.fixture()
def login():
    uri = "/api/user/login"

    data = {
        "account": User_account,
        "password": User_password
    }
    headers = {
        'content-type': 'application/json'
    }
    comm = Common()
    response = comm.post(uri, params=data, headers=headers)
    print(response.text)
    return (response.json().get('msg'))
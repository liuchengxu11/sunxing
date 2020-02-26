import allure
import pytest


def test_merchat_delete(Conftest):
    with open("./Config/config_token", "r", encoding="utf8") as f:
        token = f.read()
    uri = "/api/merchant/delete"
    data = {
        "delReason": "string",
        "id": 0
    }
    headers={
        "content-type":"application/json",
        "token":token
    }

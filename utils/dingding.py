import json
import requests




def dingding(Presentation):
    # 1、构建url
    # 测试组
    # url = "https://oapi.dingtalk.com/robot/send?access_token=abfda9e6be39b0c55d35d39f8978ced2237bc50d4aa68b74ecc104b6dd59ae20"   #url为机器人的webhook
    # IM组
    # url = "https://oapi.dingtalk.com/robot/send?access_token=2525a98a9bab6183029939c58a1a4c27a32eada6de0121f5f8ea1ad673132456"

    # 我自己
    url = "https://oapi.dingtalk.com/robot/send?access_token=61db9cca40abcca3ec2c4cd9d9535a7967a51aa9977470687ca0c5b1eb27cdd2"
    # 2、构建一下请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 3、构建请求数据
    data = {
        "msgtype": "text",
        "text": {
            "content": "测试报告%s"%Presentation
        },
        "at": {
            "atMobiles": [
                "17317937115"

            ],
            "isAtAll": False
        }
    }

    # 4、对请求的数据进行json封装
    sendData = json.dumps(data)  # 将字典类型数据转化为json格式
    sendData = sendData.encode("utf-8")  # python3的Request要求data为byte类型

    # 5、发送请求
    request = requests.post(url=url, data=sendData, headers=header)

    # 6、将请求发回的数据构建成为文件格式

    print(request.text)


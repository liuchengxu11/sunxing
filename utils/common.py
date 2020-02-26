import requests
import json
from Config.Config import SX_API_URl


class Common(object):
    def __init__(self):
        self.url = SX_API_URl
        # self.headers = {
        #     'content-type': 'application/json'
        # }

    # def get(self, uri, params=""):
    #     url = self.url + uri + params
    #     res = requests.get(url, headers=self.headers)
    #     return res
    #
    # def post(self, uri, params=""):
    #     url = self.url + uri
    #     if len(params) > 0:
    #         res = requests.post(url, data=params, headers=self.headers)
    #     else:
    #         res = requests.post(url, headers=self.headers)
    #     return res

    def get(self, uri, params="",headers=""):
        url = self.url + uri + params
        res = requests.get(url, headers=headers)
        return res

    def post(self, uri, params="",headers=""):
        url = self.url + uri
        if len(params) > 0:
            res = requests.post(url, data=json.dumps(params), headers=headers)
        else:
            res = requests.post(url, headers=headers)
        return res

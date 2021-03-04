"""
实现登录接口的验证码获取
"""

# 导入requests包
import requests
import json
from parameterized import parameterized
from tools.read_json import ReadJson
from config.logincode_setting import SettingLoginCode


class ApiLoginCode(object):
    # 登录接口的验证码获取类

    def __init__(self, url, phone):
        self.url = url
        self.phone = phone
        self.headers = SettingLoginCode().get_headers()

    def api_loginCode(self):
        params = {"params": {"phone": self.phone}}
        body = SettingLoginCode().get_body(params)

        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict

    def get_api_ticket(self):
        response_dict = self.api_loginCode()
        api_ticket = response_dict.get("data")
        value = api_ticket.values()
        return value


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=auth/loginCode"
    phone = 13437675841

    a = ApiLoginCode(url, phone).get_api_ticket()
    print(a)

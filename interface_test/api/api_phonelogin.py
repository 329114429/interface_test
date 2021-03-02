"""
实现登录接口验证
"""

# 导入requests包
import requests
import json

from interface_test.config.logincode_setting import SettingLoginCode
from interface_test.api.api_loginCode import ApiLoginCode


class ApiPhoneLogin():
    # 登录接口手机登录类
    def __init__(self, url, phone):
        self.url = url
        self.phone = phone
        self.headers = SettingLoginCode().get_headers()

    def login_api_ticket(self):
        self.api_ticket = ApiLoginCode(self.url, self.phone).get_api_ticket()
        return self.api_ticket

    def api_phonelogin(self, code):
        params = {"params": {"phone": self.phone, "api_ticket": self.api_ticket, "code": code}}
        body = SettingLoginCode().get_body(params)

        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=auth/loginCode"
    phone = 13437675841

    phonelogin = ApiPhoneLogin(url, phone)
    api_ticket = phonelogin.login_api_ticket()

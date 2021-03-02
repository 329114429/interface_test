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
    def __init__(self, url, phone, code):
        self.url = url
        self.phone = phone
        self.code = code
        self.headers = SettingLoginCode().get_headers()

    def api_phonelogin(self):
        api_ticket = ApiLoginCode(self.url, self.phone).get_api_ticket()
        params = {"params": {"phone": self.phone, "api_ticket": api_ticket, "code": self.code}}
        body = SettingLoginCode().get_body(params)

        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=auth/loginCode"
    phone = 13437675841
    code = 1
    a = ApiPhoneLogin(url, phone, code).api_phonelogin()
    print(a)

"""
实现登录接口验证
"""

# 导入requests包
import requests
import json

from interface_test.config.logincode_setting import SettingLoginCode


class ApiPhoneLogin():
    # 登录接口手机登录类
    def __init__(self, url, phone, code, api_ticket):
        self.url = url
        self.phone = phone
        self.code = code
        self.api_ticket = api_ticket
        self.headers = SettingLoginCode().get_headers()

    def api_phonelogin(self):
        params = {"params": {"phone": self.phone, "api_ticket": self.api_ticket, "code": self.code}}
        body = SettingLoginCode().get_body(params)

        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=auth/loginCode"
    phone = 13437675841


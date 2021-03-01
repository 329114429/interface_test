"""
实现登录接口的验证码获取
"""

# 导入requests包
import requests
import json
from parameterized import parameterized
from interface_test.tools.read_json import ReadJson


class ApiLoginCode(object):
    # 登录接口的验证码获取类

    def __init__(self, url, phone):
        self.url = url
        self.phone = phone
        self.headers = {
            "host": "www.xiziquan.com",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip",
            "user-agent": "quan/5.1.2 (iPhone; iOS 14.4; Scale/2.00)",
        }

    def api_loginCode(self):
        params = {"params": {"phone": self.phone}}
        params = json.dumps(params)

        body = {
            "app_id": 1,
            "data": {params
                     },
            "device": "iPhone11 ,8",
            "device_code": "3E530EC9-E0E5-4B10-907E-6D4A8ABDD0D8",
            "device_token": "0a9b6ad9a1979d16e9c730f722c44a3cad51f946a9a00329c5f4d32cb33414fe",
            "isdev": 1,
            "random": "e9d67a3093196fa1c84835bec4a6c155",
            "system_type": 1,
            "timestamp": 1614308784,
            "version": "5.1.2",
            "xzkey": "fd10dbf7ea7fec6230a2df7713865e76"
        }

        response = requests.post(self.url, headers=self.headers, data=body)
        response_dict = json.loads(response.text)
        return response_dict


if __name__ == '__main__':
    url = "https://www.xiziquan.com/index.php?r=auth/loginCode"
    phone = 13437675841

    a = ApiLoginCode(url, phone).api_loginCode()
    print(a)

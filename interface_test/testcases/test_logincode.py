"""
    目标：完成登录验证码获取的实现
"""

# 导入unittest Api_LoginCode

import json

import unittest
from api.api_loginCode import ApiLoginCode

from parameterized import parameterized
from tools.read_json import ReadJson


# 读取数据函数
def get_data():
    data = ReadJson("logincode.json").read_json()
    arrs_list = []

    arrs_list.append((data.get("url"), data.get("body"), data.get("ret"), data.get("text")))

    return arrs_list


# 新建测试类
class TestLoginCode(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_loginCode(self, url, body, ret, text):
        # 调用登录验证码获取方法
        response = ApiLoginCode().api_loginCode(url, body)

        # 断言响应信息
        self.assertEqual(500, response)

        # 断言响应状态码
        # self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()

"""
    目标：完成登录验证码获取的实现
"""

# 导入unittest Api_LoginCode

import json

import unittest
from interface_test.api.api_loginCode import ApiLoginCode

from parameterized import parameterized
from interface_test.tools.read_json import ReadJson


# 读取数据函数
def get_data():
    data = ReadJson("logincode.json").read_json()
    arrs_list = []

    arrs_list.append((data.get("url"), data.get("phone"), data.get("ret"), data.get("text")))

    return arrs_list


# 新建测试类
class TestLoginCode(unittest.TestCase):

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    @parameterized.expand(get_data())
    def test_loginCode(self, url, phone, ret, text):
        # 调用登录验证码获取方法

        response = ApiLoginCode(url, phone).api_loginCode()

        # 断言响应状态码
        self.assertEqual(ret, response["ret"])

        # 响应信息
        self.assertEqual(text, response["text"])


if __name__ == '__main__':
    unittest.main()

"""
验证发帖接口
"""

import unittest
from api.api_thread_post import ThreadPost

from parameterized import parameterized
from tools.read_json import ReadJson


class TestThreadPost(unittest.TestCase):
    # 新建发帖测试类

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def test_thread_post(self, url, fid, mode, phonetype, title, content, ret, text):
        # 调用发帖方法
        response = ThreadPost(url, fid, mode, phonetype, title, content).thread_post()


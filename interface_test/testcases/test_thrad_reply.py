"""
验证回帖接口
"""

import unittest

from parameterized import parameterized
from api.api_thread_reply import ApiThreadReply
from tools.read_json import ReadJson


def get_thread_reply_data():
    # 回帖函数的读取
    data = ReadJson("threadreply.json").read_json()
    arrs_list = []
    arrs_list.append(
        (data.get("url"),
         data.get("phonetype"),
         data.get("quoteusername"),
         data.get("tid"),
         data.get("content"),
         data.get("ret"),
         data.get("text"))
    )
    return arrs_list


class TestThreadReply(unittest.TestCase):
    # 新建回帖测试类
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    @parameterized.expand(get_thread_reply_data())
    def test_thread_reply(self, url, phonetype, quoteusername, tid, content, ret, text):
        # 调用回帖方法
        response = ApiThreadReply(url, phonetype, quoteusername, tid, content).thread_reply()

        self.assertEqual(ret, response["ret"])
        self.assertEqual(text, response["text"])


if __name__ == '__main__':
    unittest.main()

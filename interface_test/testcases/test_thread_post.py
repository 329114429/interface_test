"""
验证发帖接口
"""

import unittest
from api.api_thread_post import ThreadPost

from parameterized import parameterized
from tools.read_json import ReadJson


# 发帖读取数据函数
def get_thread_post_data():
    data = ReadJson("threadpost.json").read_json()
    arrs_list = []
    arrs_list.append(
        (data.get("url"),
         data.get("fid"),
         data.get("mode"),
         data.get("phonetype"),
         data.get("title"),
         data.get("content"),
         data.get("ret"),
         data.get("text"))
    )
    return arrs_list


def get_morethread_post_data():
    # 发帖多个用例参数读取
    data = ReadJson("threadpost_more.json").read_json()
    arrs_list = []
    for key, value in data.items():
        arrs_list.append(
            (
                value.get("url"),
                value.get("fid"),
                value.get("mode"),
                value.get("phonetype"),
                value.get("title"),
                value.get("content"),
                value.get("ret"),
                value.get("text")
            )
        )
    return arrs_list


class TestThreadPost(unittest.TestCase):
    # 新建发帖测试类

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    @parameterized.expand(get_thread_post_data())
    def test_thread_post(self, url, fid, mode, phonetype, title, content, ret, text):
        # 调用发帖方法
        response = ThreadPost(url, fid, mode, phonetype, title, content).thread_post()

        self.assertEqual(ret, response["ret"])
        self.assertEqual(text, response["text"])

    @parameterized.expand(get_morethread_post_data())
    def test_morethread_post(self, url, fid, mode, phonetype, title, content, ret, text):
        # 调用多个测试用例
        response = ThreadPost(url, fid, mode, phonetype, title, content).thread_post()

        self.assertEqual(ret, response["ret"])
        self.assertEqual(text, response["text"])


if __name__ == '__main__':
    unittest.main()

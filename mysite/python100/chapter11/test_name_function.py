import unittest
from python100.chapter11.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试 get_formatted_name"""

    def test_first_last_name(self):
        """能否够处理Janis Joplin"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """处理wolfgang amdeus mozart"""
        formatted_name = get_formatted_name("hao", "suo", "zhong")
        self.assertEqual(formatted_name, "Hao Suo Zhong")


unittest.main()

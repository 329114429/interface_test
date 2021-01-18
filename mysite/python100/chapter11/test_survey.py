import unittest
from python100.chapter11.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """AnonymousSurvey测试类"""

    def setUp(self):
        """创建一个调查对象"""
        question = "your first language"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['hao', 'suo', 'zhong']

    def test_store_single_response(self):
        """测试单个答案是否被妥善保存"""
        self.my_survey.store_response(self.responses[0])

        # 测试 english 是否在 答案列表里
        self.assertIn('hao', self.my_survey.responses)

    def test_store_three_response(self):
        """测试多个"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()

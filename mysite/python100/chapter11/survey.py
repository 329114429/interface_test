class AnonymousSurvey():
    """收集匿名调查问卷的的答案"""

    def __init__(self, question):
        """存储一个问题"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存单份问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示搜集到的答案"""
        print("survey results")
        for response in self.responses:
            print('-' + response)

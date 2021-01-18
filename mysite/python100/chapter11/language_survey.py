from python100.chapter11.survey import AnonymousSurvey

# 定义一个问题，并创建一个标识调查AnonymousSurvey
question = "what language did you first learn to speak"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("enter q to quit.\n")
while True:
    response = input("language : ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print(" survey")
my_survey.show_results()

from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("hao suo zhong")


def detail(request, question_id):
    response = "you are looking at question %s "
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = "you are looking at results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s" % question_id)




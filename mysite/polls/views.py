# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

        # return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/results.html',
                      {'question': question,
                       'error_message': "You did't select a choice."})
    else:
        select_choice.votes += 1
        select_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

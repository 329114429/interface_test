from django.shortcuts import render, HttpResponse

from .models import Card


# Create your views here.


def index(request):
    # 首页
    cards = Card.objects.all()
    context = {
        "cards": cards
    }
    return render(request, template_name="card/index.html", context=context)

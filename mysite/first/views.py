from random import sample

from django.shortcuts import render


# Create your views here.

def show_index(request):
    fruits = [
        'apple', 'orange', 'pitaya', 'durian', 'waxbery', 'buleberry',
    ]

    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})

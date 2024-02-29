from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from project.services import *


# @login_required
def index(request):
    text = 'Главная страница'
    title = 'test'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'project/index.html', context)

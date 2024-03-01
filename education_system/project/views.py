from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .service import list_lesson, list_produkt


# @login_required
def index(request):
    text = 'Главная страница'
    title = 'INFO'
    produkl_lst = list_produkt()

    context = {
        'produkl_lst': produkl_lst,
        'title': title,
        'text': text,
    }
    return render(request, 'project/index.html', context)

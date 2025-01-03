from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Главная',
        'content': 'О нас',
        'text_field': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)

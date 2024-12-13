from django.shortcuts import render


def index(request):
    context = []
    return render(request, 'main/index.html', context)


def about(request):
    return render()

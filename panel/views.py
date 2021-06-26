from django.shortcuts import render

# Create your views here.


def index(response):
    return render(response, "panel/index.html")


def login(request):
    return render(request, 'panel/login.html')


def banner(request):
    return render(request, 'panel/pages/banner/banner-list.html')


def add(request):
    return render(request, 'panel/pages/moviecenter/add-movies.html')

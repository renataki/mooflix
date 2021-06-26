from django.shortcuts import render

# Create your views here.


def index(response):
    return render(response, "panel/index.html")


def login(request):
    return render(request, 'panel/login.html')


def indexBanner(request):
    return render(request, 'panel/pages/banner/index.html')


def addBanner(request):
    return render(request, 'panel/pages/banner/add.html')


def indexMovies(request):
    return render(request, 'panel/pages/moviecenter/index.html')


def addMovies(request):
    return render(request, 'panel/pages/moviecenter/add.html')


def indexStaff(request):
    return render(request, 'panel/pages/staff/index.html')


def addStaff(request):
    return render(request, 'panel/pages/staff/add.html')

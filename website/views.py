from django.shortcuts import render

# Create your views here.


def index(response):
    return render(response, "website/index.html")


def viewMovie(request):
    return render(request, 'website/movie-detail.html')


def viewSeries(request):
    return render(request, 'website/series-detail.html')

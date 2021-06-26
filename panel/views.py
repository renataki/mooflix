from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response, "panel/index.html")

#def index(response, id):
    #return HttpResponse("<h1>Hello World</h1>")

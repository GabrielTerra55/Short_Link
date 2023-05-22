from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1> Receitas teste </h1>')
    return render(request, 'index.html')

def link(request):

    if request.POST:
        long_link = request.POST['link']
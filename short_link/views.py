from django.shortcuts import render
from short_link.models import ShortLink

from short_link.validators import *

def index(request):
    return render(request, 'index.html')

def link(request):
    if request.POST:
        long_link = request.POST['link']

        if not validate_url(long_link):
            print('invalido')
            return render(request, 'link.html', {})
        
        if not exist_url_in_database(long_link):
            new_short_link = ShortLink.objects.create(token=generate_token(), link=long_link)
            new_short_link.save()
            short_link_token = new_short_link.token
            token = {"token": short_link_token}
            return render(request, 'link.html', short_link)

        short_link = ShortLink.objects.get(link=long_link)
        short_link_token = short_link.token
        token = {"token": short_link_token}
        return render(request, 'link.html', token)
    
def token(request):
    if request.GET:
        token = request.GET['link']
        
            

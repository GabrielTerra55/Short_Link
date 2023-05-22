from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from short_link.models import ShortLink
from short_link.validators import *

def index(request):
    return render(request, 'index.html')

def link(request):
    if request.method == 'POST':
        long_link = request.POST['link']

        if not validate_url(long_link):
            print('invalido')
            return render(request, 'link.html', {})
        
        if not exist_url_in_database(long_link):
            new_short_link = ShortLink.objects.create(token=generate_token(), link=long_link)
            new_short_link.save()
            short_link_token = new_short_link.token
            token = {"token": detect_url(request, short_link_token)}  # da pra enchugar
            return render(request, 'link.html', token)

        short_link = ShortLink.objects.get(link=long_link)
        short_link_token = short_link.token
        token = {"token": detect_url(request, short_link_token)} # da pra enchugar
        return render(request, 'link.html', token)
    
def token(request, token):
    if token:
        token = token
        if not token:
            return redirect(index)
        
        if not token_exist_in_database(token):
            return redirect(index)
        
        short_link = ShortLink.objects.get(token=token)
        print('indo mandar')
        return HttpResponseRedirect(short_link.link)

    return redirect(index)

def detect_url(request,token):
    "host url detect"
    host = request.get_host()
    url = f"http://{host}/token/{token}"
    return url
        
            

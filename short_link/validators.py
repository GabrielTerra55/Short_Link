import random
import string
import requests

from short_link.models import ShortLink


def validate_url(url):
    """Verification addres"""
    url = url
    response = requests.get(url)
    return response.status_code == 200
    
def exist_url_in_database(url):
    """Verification if exist the url in database"""
    url = url
    return ShortLink.objects.filter(link=url).exists() 
        


def generate_token(size=5, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    """token generation and verification if token exist in database"""
    while True:
        token = ''.join(random.choice(chars) for _ in range(size))
        print('vapo')
        if not ShortLink.objects.filter(token=token).exists():
            break
    return token

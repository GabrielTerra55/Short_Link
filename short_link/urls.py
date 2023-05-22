from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link', views.link, name='link'),
    path('token/<str:token>/', views.token, name='token'), # essa foi a rota indicada pelo chat
]

# não esta reconhecendo a rota ne o token
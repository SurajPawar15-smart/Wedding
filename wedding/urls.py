from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
]

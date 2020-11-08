from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('about', views.about, name ='about-us')

]

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Main page of website', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

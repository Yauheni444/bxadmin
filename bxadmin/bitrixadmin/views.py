from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'bitrixadmin/index.html', {'title': 'Admin'})

def bxadmin(request):
    return HttpResponse("Страница приложения admin")

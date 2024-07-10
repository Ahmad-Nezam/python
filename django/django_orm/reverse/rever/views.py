from django.shortcuts import render, HttpResponse
from .import models
from .models import Author , book
def index(request):
    context = {
        'authors' :  Author.objects.all(),
        'books' : book.objects.all()
    }
    return render(request , 'index.html' , context )
    
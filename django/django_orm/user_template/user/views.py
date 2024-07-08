from django.shortcuts import render, HttpResponse ,redirect
from .import models
from .models import users
def index(request):
    models.get_user_info(id = 1)
    context = {
    "all_the_movies": users.objects.all()
    }
     
    return render(request , 'index.html' , context  ) 

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        users.objects.create(name=name, email=email , age=age)
    return redirect('')
   
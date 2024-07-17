from django.shortcuts import render ,redirect 
from .import models
from . models import tv_show

def show(request):
    user = models.read_show_all()
    return render(request , 'show.html' ,{'user' : user} )

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        show = models.create_show(title , network , release_date , desc )
    return render(request , 'create.html') 

def read(request , id):
    user = models.read_show(id = id)
    return render(request , 'read.html' , {'user' : user })


def update_show(request,id):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        models.update(id , title , network , release_date , desc)
    return render(request , 'update.html' ,{'id' : id } ) 


def read_update(request,id):
    user = models.read_show(id=id)
    return render(request,'read.html',{'user' : user })

def delete_show(request,id):
    models.delete_show(id = id)
    return redirect('/' ) 
    



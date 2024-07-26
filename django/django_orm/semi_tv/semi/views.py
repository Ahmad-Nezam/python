from django.shortcuts import render ,redirect 
from .import models 
from django.contrib import messages 
from .models import tv_show

def show(request):
    user = models.read_show_all()
    return render(request , 'show.html' ,{'user' : user} )

def create(request ):
    if request.method == 'POST':
        errors = models.tv_show.objects.show_val(request.POST)
        if len(errors) > 0:
                for key , value in errors.items():
                 messages.error(request , value)
                return redirect('/new')
        if tv_show.objects.filter(title = request.POST['title']):
                messages.error(request , 'title not exsist')
                return redirect('/new')
        else : 
         
            title = request.POST['title']
            network = request.POST['network']
            desc = request.POST['desc']
            release_date = request.POST['release_date']
            models.create_show(title , network , desc , release_date)
            messages.success(request , 'the show user successfuly created !!')
    return render(request , 'create.html' ) 

def read(request , id):
    user = models.read_show(id = id)
    return render(request , 'read.html' , {'user' : user })

def update_show(request ,id ):
    if request.method == 'POST':
        errors = models.tv_show.objects.show_val(request.POST)
        if len(errors) > 0:
                for key , value in errors.items():
                  messages.error(request , value)
                return render(request , 'update.html' , {'id':id} )
        else : 
            
            title = request.POST['title']
            network = request.POST['network']
            desc = request.POST['desc']
            release_date = request.POST['release_date']
            models.update( id=id,title = title , network = network, desc = desc , release_date =release_date)
            messages.success(request , 'the show user successfuly created !!')
    return render(request , 'update.html' , {'id' : id} )  


def read_update(request,id):
    user = models.read_show(id=id)
    return render(request,'read.html',{'user' : user })


def delete_show(request,id):
    models.delete_show(id = id)
    return redirect('/' ) 
    



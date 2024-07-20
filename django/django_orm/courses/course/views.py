from django.shortcuts import render, HttpResponse ,redirect
from .import models 
from .models import course
from django.contrib import messages 

def create(request):
    courses = models.read_courses()
    if request.method == 'POST':
        errors = models.course.objects.show_val(request.POST)
        if len(errors) > 0:
                for key , value in errors.items():
                 messages.error(request , value)
                return redirect('/')
        else :
            name =request.POST['name']
            desc = request.POST['desc']
            models.create_course(name , desc)
            messages.success(request , 'the show user successfuly created !!')
    return render(request , 'main.html' , {'courses' : courses} )

def remove(request , id):
    courses = models.course.objects.get(id=id)
    if request.method == 'POST': 
        models.delete_course(id)
        return redirect('/')
    return render(request ,'delete.html' , {'courses':courses} )

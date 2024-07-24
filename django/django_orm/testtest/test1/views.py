from django.shortcuts import render , redirect
from .import models 
from django.contrib import messages 
def login(request):
    return render(request , 'login.html')
    
def register(request):
    if request.method == 'POST':
        errors = models.course.objects.show_val(request.POST)
        if len(errors) > 0:
                for key , value in errors.items():
                 messages.error(request , value)
                return redirect('/')
        else :  
            name = request.POST['name']
            password =request.POST['password']
            models.register_user(name , password)
            messages.success(request , 'the show user successfuly created !!')
    return render(request , 'register.html')
        
        
        

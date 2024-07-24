from django.shortcuts import render ,redirect
from . import models
from .models import user
from django.contrib import messages 
import bcrypt

def register(request):
    if request.method == 'POST':
        errors = models.user.objects.val(request.POST)
        if len(errors) > 0:
                for key , value in errors.items():
                  messages.error(request , value)
                return redirect('/')
        else:
            users = models.create_user(request.POST)
            messages.success(request , 'the show user successfuly created !!')
            request.session['user_id'] = users.id
            request.session['First_name'] = users.First_name
            request.session['Last_name'] = users.Last_name 
            return redirect('/')
    return render(request , 'login_register.html')




def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']        
        users =  user.objects.filter(email = email , password = password).first()
        if users:
            request.session['user_id'] = users.id
            request.session['First_name'] = users.First_name
            request.session['Last_name'] = users.Last_name   
            return redirect('/success')
        else:
            return render(request,'login_register.html')


def success(requset):
    First_name = requset.session['First_name']
    Last_name = requset.session['Last_name']
    return render(requset , 'success.html' ,{'First_name' : First_name , 'Last_name' :Last_name})   

def clear(request):
    request.session.clear()
    return redirect('/')
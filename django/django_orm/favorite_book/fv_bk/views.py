from django.shortcuts import render ,redirect
from . import models
from .models import user , book
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
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(pw_hash) 
            users = models.create_user(request.POST , pw_hash = pw_hash ) 
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
        users =  user.objects.filter(email = email).first()
        if users and bcrypt.checkpw(request.POST['password'].encode(), users.password.encode()):
            request.session['user_id'] = users.id  
            request.session['First_name'] = users.First_name
            request.session['Last_name'] = users.Last_name   
            return redirect('/add_book')
        else:   
            return render(request,'login_register.html')


def books(request): 
    First_name = request.session['First_name']
    Last_name = request.session['Last_name']
    user_id = request.session.get('user_id')  
    loged_user = user.objects.get(id=user_id)  
    books = book.objects.all()  
    if request.method == 'POST': 
            errors = models.user.objects.val_2(request.POST)
            if len(errors) > 0:
                    for key , value in errors.items():
                     messages.error(request , value)
                    return redirect('/add_book') 
            if book.objects.filter(title = request.POST['title']):
                messages.error(request , 'title is exsist')
                return redirect('/add_book')
            else : 
                title = request.POST['title'] 
                desc = request.POST['desc']   
                models.create_book(title , desc , loged_user )  
    return render(request,'ad_bk.html' , {'books' : books ,'First_name' : First_name , 'Last_name' :Last_name } )      


def show_bk(request , id):
    First_name = request.session['First_name']
    Last_name = request.session['Last_name'] 
    user_id = request.session.get('user_id')   
    loged_user = user.objects.get(id=user_id)  
    books = models.get_book(id)  
    return render(request,'show_bk.html' , {'books' : books ,'First_name' : First_name , 'Last_name' :Last_name } )


def delete(request , id):
    if request.method == 'POST': 
     id = request.POST['id']
    models.delete_book(id = id)
    return redirect('/add_book')


def update_book(request , id):
    First_name = request.session['First_name']
    Last_name = request.session['Last_name'] 
    user_id = request.session.get('user_id') 
    loged_user = user.objects.get(id=user_id)  
    books = models.get_book(id)
    if request.method == 'POST':
        if 'title' in request.POST:
            title =request.POST['title'] 
            models.update_book(id , title)
            desc = request.POST['desc'] 
            models.update_book(id = id , desc = desc , title = None)  
    return render(request , 'show_bk.html', {'books' : books ,'First_name' : First_name , 'Last_name' :Last_name } )


def clear(request):
    request.session.clear()
    return redirect('/')

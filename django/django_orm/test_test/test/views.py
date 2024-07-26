from django.shortcuts import render ,redirect
from . import models
from .models import user , Pie
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
            return redirect('/add_pie')
        else:   
            return render(request,'add_pie.html')


def add_pie(request ):
    show = models.get_all_pie()
    First_name = request.session['First_name']
    Last_name = request.session['Last_name']
    if request.method == 'POST':
        name = request.POST['name'] 
        crust = request.POST['crust']
        filling = request.POST['filling'] 
        if not name or not crust or not filling : 
            messages.error(request , "include the filling")
            return redirect('/add_pie')
        else :
            models.add_pie(request.POST) 
    return render(request , 'add_pie.html' , {'show' : show , 'First_name':First_name , 'Last_name' :Last_name}) 


def edit_pie(request , id):
    First_name = request.session['First_name']
    Last_name = request.session['Last_name']
    shows = models.read_pie(id = id) 
    if request.method == 'POST':
        name = request.POST['name'] 
        crust = request.POST['crust']
        filling = request.POST['filling'] 
        if not name or not crust or not filling : 
            messages.error(request , "include the filling")
        else : 
            name = request.POST['name']
            crust = request.POST['crust']
            filling = request.POST['filling']
            models.edit_pie(id = id , name = name , crust=crust , filling=filling)
    return render(request , 'update_pie.html' , { 'shows':shows  , 'First_name':First_name , 'Last_name' :Last_name} )


def delete_pie(request,id):
    models.delete_pie(id = id)
    return redirect('/add_pie') 


def all_pies(request , id): 
    First_name = request.session['First_name'] 
    shows = models.read_pie(id=id)
    return render(request, 'all_pies.html' , { 'shows' : shows,'First_name':First_name }) 

def view(request,id):
    First_name = request.session['First_name'] 
    shows = models.read_pie(id=id)
    return render(request ,'view.html' , {'shows' : shows ,'First_name':First_name })

def logout(request):
    request.session.clear()
    return redirect('/')

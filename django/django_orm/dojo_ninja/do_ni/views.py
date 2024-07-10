from django.shortcuts import render, HttpResponse
from .import models
from .models import dojos , ninjas

def index(request):
    # create 3 dojos
    # models.create_user('ahmad' , 'Ram' , 'Palestine')
    # models.create_user('Amir' , 'Nablus' , 'Palestine')
    # models.create_user('Obada' , 'Khalil' , 'Palestine')

    # delete 3 dojos
    # models.delete_user(id=1)
    # models.delete_user(id=2)
    # models.delete_user(id=3)


    # create 3 more dojos
    # models.create_user('Abdullah' , 'Ramallah' , 'Palestine')
    # models.create_user('Sami' , 'Jenin' , 'Palestine')
    # models.create_user('Ali' , 'Nablus' , 'Palestine')

    # create 3 ninjas that belong to the first dojo
    # models.create_ninja()
    

    # retreive all the ninjas from the first dojo

    user=models.get_user(id)
    context = {
        'users' : user
    }

    # retreive all the ninjas from the last dojo
    # user=models.get_last(id)
    # context = {
    #     'users' : user
    # }

    # retreive all the ninjas from the last dojo

    # user=models.get_ninja(id)
    # context = {
    #     'users' : user
    # }

    return render(request , 'index.html',context )

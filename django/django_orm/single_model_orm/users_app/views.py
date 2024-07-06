from django.shortcuts import render, HttpResponse
from . import models
def index(request):
    # creating 3 users
    # models.create_user('ahmad','aamer','ahmad@gmail.com','22')
    # models.create_user('salah','aamer','salah@gmail.com','20')
    # models.create_user('moe','aamer','moe@gmail.com','15')

    # Retrieve all the users
    # user = models.get_user_info(id)
    # context = {
    #     'users' : user
    # }
   
   # getting the last user 
   # user = models.get_last(id)
   # context ={
   #      'users' : user
   #     }

    #getting the first user
    # user = models.get_first(id)
    # context = {
    #     'users' :user
    # }

    # updating the lastuser
    # models.updating_user(id=3)

    # deleting a user 
    # models.delete_user(id = 2)

    # veiwing the users sorted by the first name

    # user = models.veiw_names(id )
    # context = {
    #      'users' : user
    #  }

    # veiwing the users sorted descending order by the first name

    user = models.veiw_names_desc(id )
    context = {
          'users' : user
      }



    return render(request , 'index.html'  ,context ) 
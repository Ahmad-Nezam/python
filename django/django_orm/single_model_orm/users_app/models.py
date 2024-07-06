from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_adress = models.CharField(max_length=30)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user(fst_name , lst_name , email , age ):
    User.objects.create(first_name = fst_name , last_name = lst_name , email_adress = email , age = age)

def get_user_info(id):
    user = User.objects.all().values()    
    return user

def get_last(id):
    user = User.objects.last()
    return user 

def get_first(id):
    user = User.objects.first()
    return user

def updating_user(id):
    user =User.objects.get(id = id)
    user.last_name = 'pancake'
    user.save()

def delete_user(id):
    user = User.objects.get(id = id)
    user.delete()

def veiw_names(id):
  user = User.objects.all().order_by('first_name')    
  return user

def veiw_names_desc(id):
  user = User.objects.all().order_by('-first_name')    
  return user
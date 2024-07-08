from django.db import models

class users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.IntegerField()    

def create_user(fst , email , age ):
    users.objects.create(name = fst , email = email , age = age )

def get_user_info(id):
    user = users.objects.get(id = id)   
    return user
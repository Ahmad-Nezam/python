from django.db import models

class val_register(models.Manager):
    def val(self , postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'name should be at least 5 charcters'
        if len(postData['password']) < 10:
            errors['password'] = 'password should be at least 15 charcters'    
        return errors  

class user(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    objects = val_register()

def register_user(name ,password):
    return user.objects.create(name = name , password = password)

def read_user(id):
    return user.objects.all()


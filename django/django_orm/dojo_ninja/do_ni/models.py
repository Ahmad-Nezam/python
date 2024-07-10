from django.db import models

class dojos(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

class ninjas(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dojo = models.ForeignKey(dojos ,related_name="ninjas", on_delete=models.CASCADE)


def create_user(name , city , state ):
    dojo = dojos.objects.create(name = name , city = city , state = state)
    return dojo

def delete_user(id):
    dojo = dojos.objects.get(id = id)
    dojo.delete()


def create_ninja():
    dojo1 = dojos.objects.get(id = 1)
    ninja1 = ninjas.objects.create(first_name = "ninja1" , last_name = 'ninja1' ,dojo = dojo1)    
    return ninja1 

def get_user(id):
    dojo1 = dojos.objects.first()
    return dojo1

def get_last(id):
    dojo1 = dojos.objects.last()
    return dojo1

def get_ninja(id):
    ninja = ninjas.objects.first()
    return ninja


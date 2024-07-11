from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

class Ninja(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)


def create_dojo(name, city, state):
    new_dojo = Dojo.objects.create(name=name, city=city, state=state)
    return new_dojo


def create_ninja(first_name, last_name, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    new_ninja = Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return new_ninja

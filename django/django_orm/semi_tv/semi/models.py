from django.db import models
from django.shortcuts import get_object_or_404

class tv_show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    desc = models.TextField()

def __str__(self):
    return self.title    

def create_show(title , network , release_date , desc ):
    show = tv_show.objects.create(title = title , network = network , release_date =release_date , desc =desc  )
    return show

def read_show_all():
    return tv_show.objects.all()

def read_show(id):
     return tv_show.objects.get(id=id)
   
def delete_show(id):
    show = tv_show.objects.get(id=id)
    show.delete()

def update(id,title,network,release_date,desc):
    my_id = tv_show.objects.get(id=id)
    my_id.title = title
    my_id.network = network
    my_id.release_date = release_date
    my_id.desc = desc
    my_id.save()
    return my_id

    





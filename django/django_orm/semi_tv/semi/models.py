from django.db import models


class show_manager(models.Manager):
    def show_val(self , postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'title should be at least 2 charcters'
        if len(postData['network']) < 3:
            errors['network'] = 'network should be at least 2 charcters'
        if len(postData['desc']) < 10:
            errors['desc'] = 'desc should be at least 10 charcters'    

        return errors        

class tv_show(models.Model):
    title = models.CharField(max_length=45 )
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    objects = show_manager()

def __str__(self):
    return self.title    

def create_show(title , network , release_date , desc ):
   return tv_show.objects.create(title = title , network = network , release_date =release_date , desc =desc  )
   

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

    





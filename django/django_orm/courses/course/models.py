from django.db import models


class show_manager(models.Manager):
    def show_val(self , postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'name should be at least 5 charcters'
        if len(postData['desc']) < 15:
            errors['desc'] = 'desc should be at least 15 charcters'    
        return errors   

class course(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    objects = show_manager()

def create_course(name , desc):
    return course.objects.create(name = name , desc = desc)


def delete_course(id):
    delete =  course.objects.get(id=id)
    delete.delete()

def read_courses():
    return course.objects.all()
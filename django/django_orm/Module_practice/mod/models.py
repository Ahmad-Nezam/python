from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date= models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
# this function for creating a user 

def create_user(username , password , email):
    User.objects.create(username = username , password = password , email = email)

# this function for deleting a user 

def remove_user(id):
    a = User.objects.get(id = id)
    a.delete()
    
# this function for updating

def update_user(id):
    user = User.objects.get(id = id)
    user.email = 'abd@gmail.com'
    user.username = 'abd_alrahman'
    user.save()

# this function for reading a coulmn
def get_username(id):
    user = User.objects.get(id = 3)
    return user

# this function to get all the records
def get_all(id):
    user = User.objects.all()
    return user
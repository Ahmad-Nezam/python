from django.db import models
import re	
import bcrypt

class UserManager(models.Manager):
    def val(self , postData ):
        errors = {}
        if len(postData['First_name']) < 2:
            errors['First_name'] = 'First_name should be at least 2 charcters'

        if len(postData['Last_name']) < 2:
            errors['password'] = 'Last_name should be at least 2 charcters'  

        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 charcters'   

        if len(postData['conf_password']) < 8:
            errors['conf_password'] = 'conf_password should be at least 8 charcters'      

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if len(postData['password']) != len(postData['conf_password']):
            errors['conf_password'] = "passwords do not match"
            
        if user.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email already exists."

        return errors 

    def val_2(self , postData):
        errors = {}
        if len(postData['title']) < 2:
           errors['title'] = 'title should be at least 2 charcters'

        if len(postData['desc']) < 10:
           errors['desc'] = 'desc should be at least 10 charcters' 
        return errors 


class user(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.CharField(max_length= 30)
    password = models.CharField(max_length=30)
    conf_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    uploaded_by = models.ForeignKey(user , on_delete=models.CASCADE , related_name = 'book_uploaded' )
    users_who_like = models.ManyToManyField(user , related_name = 'liked_books' ) 


def create_user(request , pw_hash):
    First_name = request['First_name']
    Last_name = request['Last_name']
    email = request['email']
    password = request['password']
    conf_password = request['conf_password']
    return user.objects.create(First_name = First_name , Last_name = Last_name , email = email ,  conf_password = pw_hash , password = pw_hash)


def create_book(title , desc , user ): 
    books = book.objects.create(title = title , desc = desc , uploaded_by = user) 
    books.users_who_like.add(user)
    return books

def get_book(id):
    return book.objects.get(id=id)
   

def update_book(id , desc ):
    my_id = book.objects.get(id=id)
    my_id.desc = desc 
    my_id.save()
    return my_id

def delete_book(id):
    bk = book.objects.get(id = id)
    bk.delete() 
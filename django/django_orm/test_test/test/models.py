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

        if len(postData['password']) !=  len(postData['conf_password']):
            errors['conf_password'] = "passwords do not match"
            
        if user.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email already exists."

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

class Pie(models.Model):
    name = models.CharField(max_length=30)
    filling = models.CharField(max_length=30)
    crust = models.CharField(max_length=30)
    bakery = models.ForeignKey(user , on_delete=models.CASCADE , related_name = 'bk')

def create_user(request , pw_hash):
    First_name = request['First_name']
    Last_name = request['Last_name']
    email = request['email']
    password = request['password']
    conf_password = request['conf_password']
    return user.objects.create(First_name = First_name , Last_name = Last_name , email = email ,  conf_password = pw_hash , password = pw_hash)

def add_pie(request):
    name = request['name']
    filling = request['filling'] 
    crust = request['crust'] 
    return Pie.objects.create(name = name , filling = filling , crust = crust)

def get_all_pie():
    return Pie.objects.all()

def edit_pie(id , name ,crust , filling):
    my_id = Pie.objects.get(id = id)
    my_id.name = name
    my_id.crust = crust
    my_id.filling =filling
    my_id.save()
    return my_id

def delete_pie(id):
    shows = Pie.objects.get(id=id)
    shows.delete()
    
def read_pie(id):
    return Pie.objects.get(id=id)  
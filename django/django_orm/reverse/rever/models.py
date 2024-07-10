from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author,related_name='books' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_user(id):
   my_book = book.objects.create(title = 'little women' , author = Author.objects.get(id = id)) 
   return my_book
     

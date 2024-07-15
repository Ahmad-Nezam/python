from django.db import models

class book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(book,related_name='booking')

def add_books(id):
    this_book= book.objects.get(id=id)
    this_author = author.objects.get(id=id)
    au=this_author.books.add(this_book)
    return au

def get_book(id):
      return book.objects.get(id=id)

def get_author(id):
    return author.objects.get(id=id)

def create(first_name,last_name,notes):
    bb = author.objects.create(first_name = first_name ,last_name =last_name, notes=notes )
    return bb
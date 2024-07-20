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
    books = models.ManyToManyField(book,related_name='authors')

def add_books(author,book):
    author.books.add(book)
    return author

def add_author(author , book):
    book.authors.add(author)
    return book

def get_book(id):
      return book.objects.get(id=id)

def get_author(id):
    return author.objects.get(id=id)

def create_book(title , desc):
    bk = book.objects.create(title = title , desc = desc)
    return bk

def create_author(first_name ,last_name ,notes ):
    au = author.objects.create(first_name = first_name , last_name =last_name , notes =notes)
    return au

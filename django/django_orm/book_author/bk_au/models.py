from django.db import models

class book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(book,related_name='booking')


def create_book(title):
    this_book = book.objects.create(title=title)
    return this_book
    
def create_author(first_name,last_name):
    this_author = author.objects.create(first_name = first_name ,last_name = last_name )
    return this_author

def rename_bk():
    bk = book.objects.get(title = 'c sharp')
    bk.title='C#'
    bk.save()
 
def rename_au():
    au = author.objects.get(first_name = 'William')
    au.first_name = 'Bill'
    au.save()

def ass_fst():
    fst_au = author.objects.get(id=4)
    first_two_books = book.objects.get(id=1)
    fst_au.books.add(first_two_books)

def ass_scnd():
    fst_au = author.objects.get(id=4)
    first_two_books = book.objects.get(id=5)
    fst_au.books.add(first_two_books)

def get_auth():
    fst_au = author.objects.get(id=1)
    ge=fst_au.books.all() 
    return ge
def add():
    fst = author.objects.get(id=5)
    scnd = book.objects.get(id=2)
    fst.books.add(scnd)

def rmv():
    fst = author.objects.get(id=1)
    scnd = book.objects.get(id=3)
    fst.books.remove(scnd)

def find():
    fst = author.objects.get(id=3)
    ge=fst.books.all()
    return ge

def find_2():
    fst = author.objects.all()
    ge = fst.books.get(id=5)
    return ge 

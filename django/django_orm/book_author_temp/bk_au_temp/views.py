from django.shortcuts import render, HttpResponse ,redirect
from .import models
from .models import book , author
# for the main page
def index(request):
    context = {
        'bk' : book.objects.all()
    }
  
    return render(request,'index.html',context)

# to show the info of the author 

def index2(request , bk_id):
    if request.method == 'POST':
     bk_id = request.POST['bk']
     books = book.objects.get(id = bk_id)
     author.objects.create(books = books)
     authors = author.objects.all()
     books = models.get_author(bk_id)
    return render(request , 'info.html' , {'authors':authors , 'books' : books })



def index3(request):
    context = {
        'au' : author.objects.all()
    }
    return render(request , 'author.html' , context)

def index4(request):
    context = {
        'au' : author.objects.all(),
        'bk' : book.objects.all()
     } 
    return redirect('add',context)

def index5(request,au_id):
    if request.method == 'POST':
      au_id = request.POST['auth']
      books = book.objects.get(id = au_id)
      author.objects.create(books = books)
    authors = author.objects.all()
    author = models.get_author(au_id)
    return render(request , 'info_au.html' , {'authors':authors , 'book' : books })


def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        add_book= book.objects.create(title = title , desc = desc)
    return render(request,'index.html',{'add_book':add_book})



def create_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        author.objects.create(first_name = first_name , last_name = last_name , notes = notes )
    return redirect('/au')


from django.shortcuts import render, HttpResponse ,redirect
from .import models
from .models import book , author

# to show the info of the author 

def create_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        author = models.create_author(first_name , last_name ,notes)
        return redirect('add_author') 
    else:
        au = author.objects.all()
        return render(request , 'author.html' , {'authors' : au})
    


def author_info(request,au_id):
    au = models.get_author(au_id)
    if request.method == 'POST':
      bk_id = request.POST['book']
      bks = models.get_book(bk_id)
      models.add_author(bks , au )
      return redirect('info_au',au_id = au_id)
    bk = book.objects.all() 
    return render(request , 'info_au.html' , {'authors':au , 'book' : bk })


def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        books = models.create_book(title , desc)
        return redirect('add_book')
    else:
        bks = book.objects.all()
        return render(request,'index.html',{'bks':bks})



def book_info(request, book_id):
    book = models.get_book(book_id)
    if request.method == 'POST':
        author_id = request.POST['bk']
        au = models.get_author(author_id)
        models.add_books(au , book)
        return redirect('book_info',book_id = book_id)
    au = author.objects.all()
    return render(request,'info.html',{'book':book , 'authors' : au})


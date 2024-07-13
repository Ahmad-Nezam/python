from django.shortcuts import render, HttpResponse
from .import models
from .models import book 
def index(request):
    # create 5 books
    # models.create_book('ruby','java','python','php','ruby')

    # create 5 authors
    # models.create_author('jane','austen')
    # models.create_author('Emily','Dickinsion')
    # models.create_author('Fyodor','Dostoevsky')
    # models.create_author('William','Shakespeare')
    # models.create_author('Lau','Tzu')

    # rename c sharp to c# in book
    # models.rename_bk()

    # rename in author
    # models.rename_au()

    # assign the first author to the books
    # models.ass_fst()

    # assign the 4 author to all the books
    # models.ass_scnd()

    # retreive the author from the book 
    # get = models.get_auth()
    # context = {
    #     'gets' : get
    # }

    # remove the first author from the third book
    # models.rmv()

    # add the fifth to the second
    # models.add()

    # get = models.find()
    # context = {
    #      'gets' : get
    #  }

    # find all the authors that contributed to the 5th book
    # get = models.find_2()
    # context = {
    #     'get' : get
    # }
    return render(request,'index.html' )


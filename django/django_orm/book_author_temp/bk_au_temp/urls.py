from django.urls import path     
from . import views
urlpatterns = [
    
    
     path('', views.create_book, name='add_book'),

     path('books/<book_id>', views.book_info ,name='book_info'),

     path('add_author/', views.create_author,  name='add_author'),

     path('author/<au_id>', views.author_info ,name='author_info')

       ]


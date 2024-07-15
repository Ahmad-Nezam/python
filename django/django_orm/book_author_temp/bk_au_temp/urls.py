from django.urls import path     
from . import views
urlpatterns = [
    
    
     path('add_book/', views.create_book, name='add_book'),
     path('add_bk/<int:bk_id>', views.index2 ,name='add_bk'),

     path('add_author/', views.create_author,  name='add_author'),

     path('add_au/<int:au_id>', views.index2 ,name='add_au')

       ]


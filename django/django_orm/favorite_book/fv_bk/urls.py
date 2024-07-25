from django.urls import path     
from . import views
urlpatterns = [
    path('', views.register , name = 'register'),
    path('login', views.login , name = 'login'),
    path('add_book', views.books , name = 'add_book'),
    path('update/<int:id>', views.show_bk , name = 'update'),
    path('del' , views.clear  ),
    path('delete/<int:id>' , views.delete ,name = 'delete' ),
    path('updated/<int:id>' , views.update_book , name='updated')  
       
          ]

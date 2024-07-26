from django.urls import path     
from . import views

urlpatterns = [
    path('', views.register , name = 'register'),
    path('login', views.login , name = 'login'),
    path('add_pie' ,views.add_pie , name='add_pie') ,
    path('edit/<int:id>',views.edit_pie , name='edit_pie'),
    path('delete/<int:id>',views.delete_pie , name='delete_pie'),
    path('all_pies/<int:id>' , views.all_pies  ,name='all_pies'),
    path('view/<int:id>' ,views.view , name='show_pie'),
    path('logout' ,views.logout , name='logout' )
            
        ]

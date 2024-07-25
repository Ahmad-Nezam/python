from django.urls import path     
from . import views
urlpatterns = [
    path('', views.show),
    path('new', views.create),
    path('shows/<int:id>', views.read , name='show_detail'),
    path('shows/update/<int:id>',views.update_show , name='update_detail'),
    path('shows/update/goshow/<int:id>',views.read_update , name='read_up' ),
    path('clear/<int:id>',views.delete_show,name='delete_detail')
    
           ]



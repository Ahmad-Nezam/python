from django.urls import path     
from . import views 
urlpatterns = [
    
     path('blog/', views.root),
     path('blogs/', views.index),
     path('blogs/new', views.new),
     path('blogs/create', views.create),
     path('blogs/<int:number>', views.show),
     path('blogs/<int:number>/edit', views.edit),
     path('blogs/delete', views.destroy),
     path ('blogs/json',views.redirect_json )

           ]

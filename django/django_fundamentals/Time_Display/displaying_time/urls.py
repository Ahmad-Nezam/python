from django.urls import path     
from . import views
urlpatterns = [ 
    path('show/', views.index),
    path('show/', views.time),   
          ]

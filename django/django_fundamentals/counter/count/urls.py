from django.urls import path     
from . import views
urlpatterns = [
     path('', views.count1),
     path('res/',views.count2),
     path('res/',views.count3),
     path('delete/',views.destroy),
           ]


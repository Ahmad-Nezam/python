from django.urls import path     
from . import views
urlpatterns = [
  
    path('',views.create ),
    path('<int:id>' , views.remove , name='delete_course')

      ]

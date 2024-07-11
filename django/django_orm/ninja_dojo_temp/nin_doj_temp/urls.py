from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_dojo/', views.create_doj, name='add_dojo'),
    path('add_ninja/', views.create_nin, name='add_ninja'),
    path('clr' ,views.clear)
]

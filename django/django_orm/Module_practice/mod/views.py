from django.shortcuts import render, HttpResponse
from . import models

def index(request):
    
	user = models.get_all(id = 3)
	context = {
		'users' : user.get(id=3)
	}
	return render(request, 'index.html' , context)

    		

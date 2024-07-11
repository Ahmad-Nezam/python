from django.shortcuts import render, redirect
from .models import Ninja, Dojo

def index(request):
    context = {
        'doj': Dojo.objects.all(),
        'nin': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def create_doj(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/')

def create_nin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo_id = request.POST['dojo']
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')

def clear(request):
    request.session.clear()
    return render('/')
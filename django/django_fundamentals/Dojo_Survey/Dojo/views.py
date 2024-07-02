from django.shortcuts import render, HttpResponse , redirect

def index(request):
   
    return render(request,"index.html")

def create_user(request):
    name_doj = request.POST['name']
    loc_doj = request.POST['location']
    lan_doj = request.POST['language']
    comm_doj = request.POST['comment']
    context={
        'name' :  name_doj,
        'loc' : loc_doj,
        'lan' : lan_doj,
        'comm' :comm_doj
    }
    return render(request,"show.html",context)

def success(request):
    return render(request,"show.html")

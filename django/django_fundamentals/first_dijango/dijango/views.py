from django.shortcuts import render, HttpResponse ,redirect 
from django.http import JsonResponse

def root(request):
    return redirect ("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")

def show(request,number):
    return HttpResponse(f"placeholder to display the blog number : {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit the blog  {number}")

def destroy(request):
    return redirect ("/blogs")


def redirect_json(request):
    return JsonResponse({"tittle" : " My First Blog" , "content" : "Lorem ,ipsm dolor sit amet consectetur "})


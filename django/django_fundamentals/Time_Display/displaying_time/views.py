from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from datetime import datetime
def index(request ):
    context = {
        "Time" : "The Current Time and Date : " , 
        "time" : strftime("%Y-%m-%d %H:%M %p",gmtime())
    } 
    return render(request , "index.html" , context)


def time(request):
    
    current_datetime = datetime.now()
    print(current_datetime)

    return render(request , "index.html" , current_datetime)
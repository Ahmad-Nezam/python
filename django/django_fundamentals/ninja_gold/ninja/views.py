import random
from django.shortcuts import render, HttpResponse , redirect 
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activites'] = []
    ninja_dictionary = {
        'gold' : request.session['gold'],
        'activites' : request.session['activites'] 
     }
    return render(request,'index.html', ninja_dictionary)

def process_money(request):
    if request.method == 'POST':
     building= request.POST.get('building') 
     request.session['building'] = building

    if building == 'farm':
      earn_gold = random.randint(10,20)
    elif building == 'quest':
       earn_gold = random.randint(-50,50)
    time = datetime.now().strftime('%d%y - %H%M')
    
    if earn_gold > 0:
       activity = f' Earned {earn_gold} from {building} on {time}' 
    else: 
       activity = f' Lost {earn_gold} from {building} on {time}'   

    request.session['activites'].insert(0,activity)
    request.session['gold'] += earn_gold

    return redirect('/')    

def delete(request):
    request.session.clear()
    return redirect('/')
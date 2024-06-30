from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['message'] = ''

    if request.method == 'POST':
        guess = int(request.POST['guess'])
        if guess == 55:
            request.session['message'] = '55 was the number!!'
        elif 49 < request.session['number']:
            request.session['message'] = 'Too low!'
        elif 50 > request.session['number']:
            request.session['message'] = 'Too high!'
        else:
            # request.session['message'] = f'Correct! The number was {request.session["number"]}. Play again?'
            request.session.pop('number')
    
    return render(request, 'great_num.html', {'message': request.session.get('message', '')})

def reset(request):
    request.session.pop('number', None)
    request.session['message'] = ''
    return redirect('index')

from django.shortcuts import render, redirect
import random
def home(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1,100)
        request.session['message'] = ''
        print(request.session['number'])
    return render(request,'great_num.html')


def index(request):
    # if request.method == 'POST':
        guess = int(request.POST['guess'])
        num = request.session['number']
        if guess < num:
            request.session['message'] = 'Too low!'
        elif guess > num:
            request.session['message'] = 'Too high!'
        elif guess == num:
            request.session['message'] = ' correct  number!!'    
            request.session['number'] = random.randint(1,100)
        return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

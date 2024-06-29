from django.shortcuts import render, HttpResponse , redirect
    
def count1(request):
   if "count" not in request.session:
        request.session['count'] = 1
   else:
        request.session['count'] +=1
   return render(request,'index.html')

def count2(request):
        if request.POST.get('alterr') == 'add':
            request.session['count'] += 1
        elif request.POST.get('alter') == 'reset':
            request.session['count'] = 0
            return redirect('/')


def destroy(request):
    request.session.clear()
    return redirect("/")        
        

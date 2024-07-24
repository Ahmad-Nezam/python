from django.shortcuts import render ,redirect
from .models import Order, Product
from . import models
def index(request):
    context = {
        "all_products": Product.objects.all()
    }
   
    return render(request, "store/index.html", context)

def checkout(request):
    
    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["price"])
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

        request.session['total_charge'] = total_charge
        request.session['total_quantity'] = quantity_from_form
        request.session['price'] = price_from_form

        return redirect('/check')
    return render(request, "store/checkout.html" )
    # context = {
    #     'total_charge' : total_charge ,
    #     'total_quantity' : quantity_from_form , 
    #     'price' : price_from_form 
    # }
    
def check(request):
    # get_id = models.get(id=id)
    if request.method == "POST":
        total_charge = request.session.get('total_charge')
        total_quantity = request.session.get('total_quantity')
        price = request.session.get('price')

        context = {
            'total_charge': total_charge,
            'total_quantity': total_quantity,
            'price': price
        }  

        return redirect('check')
    return render(request, "store/check.html" )

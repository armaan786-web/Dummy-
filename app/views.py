from multiprocessing import context
import re
from django.shortcuts import render
from app.models import AllProduct,Price

# Create your views here.

def home(request):
    product = AllProduct.objects.all()
   

    if request.method == "POST":
        product = request.POST.get('product_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        price_details=Price(product=product,amount=price, category=category)
        price_details.save()
  
    return render(request,'index.html',{'product':product})



    

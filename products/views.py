from django.shortcuts import render
from .models import Product



def vk_trading(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products': products})

# Create your views here.

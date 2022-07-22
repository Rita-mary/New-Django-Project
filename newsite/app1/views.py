from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(request , 'app1/index.html', context)
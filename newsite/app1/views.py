from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def products(request):
    products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(request , 'app1/index.html', context)
def product_details(request , id):
    product = Product.objects.get(id = id)
    context = {
        'product' : product
    }
    return render(request , 'app1/product_details.html', context)
@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['upload']
        product = Product(name = name, price = price, description = description, image = image) 
        product.save()
        return redirect('/app1/index')
    return render(request , 'app1/add_products.html')

@login_required
def update_product(request , id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/app1/index')
    context = {'product': product}
    return render(request , 'app1/update_products.html', context)

@login_required
def delete_product(request , id):
    product = Product.objects.get(id = id)
    if request.method =='POST':
        product.delete()
        return redirect('/app1/index')
    context =  {'product': product}
    return render(request , 'app1/delete_product.html' , context)
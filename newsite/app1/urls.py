from pathlib import Path
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'app1'
urlpatterns = [
    path('index/', views.products , name= 'index'),
    path('index/<int:id>/', views.product_details, name='product_details'),
    path('index/add_product/', views.add_product, name='add_product'),
    path('index/update_product/<int:id>', views.update_product, name='update_product'),
    path('index/delete_product/<int:id>', views.delete_product, name='delete_product')
]
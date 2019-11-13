from django.shortcuts import render
from app.models import *
from app.forms import *

def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})

def dog_product_detail(request, id):
    dog_product = DogProduct.objects.get(id=id)
    return render(request, "home.html", {"dog_product": dog_product})

def purchase_dog_product(request, id):
    pass

def purchase_detail(request, id):
    pass

def new_dog_tag(request):
    pass

def dog_tag_list(request):
    pass

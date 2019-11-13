from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
from datetime import datetime 
from django.contrib import messages


def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, dog_product_id):
    id = dog_product_id
    dog_product = DogProduct.objects.get(id=id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_dog_product(request, dog_product_id):
    id = dog_product_id
    dog_product = DogProduct.objects.get(id=id)
    if dog_product.quantity > 0:
        dog_product.quantity -= 1
        purchase_id = Purchase.objects.create(dog_product=dog_product, purchased_at=datetime.now())
        messages.success(request, f"Purchased {dog_product.name}")
        return redirect("purchase_detail", purchase_id)
    elif dog_product.quantity :
        messages.error(f"{dog_product.name} is out of stock")
        return redirect(request, "home")


def purchase_detail(request, id):
    print("hi")


def new_dog_tag(request):
    pass


def dog_tag_list(request):
    pass

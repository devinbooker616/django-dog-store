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
    dogs = DogProduct.objects.get(id=id)
    if dogs.quantity > 0:
        dogs.quantity -= 1
        dogs.save()
        purchase = dogs.purchase_set.create(purchased_at=datetime.now())
        messages.success(request, f"Purchased {dogs.name}")
        return redirect("purchase_detail", purchase.id)
    elif dogs.quantity <= 0:
        messages.error(request, f"{dogs.name} is out of stock")
        return redirect("dog_product_detail", dogs.id)


def purchase_detail(request, purchase_id):
    id = purchase_id
    purchase = Purchase.objects.get(id=id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def new_dog_tag(request):
    if request.method == "GET":
        return render(request, "new_dog_tag.html")
    elif request.method == "POST":
        form = NewDogTagForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            dog_name = form.cleaned_data["dog_name"]
            dog_birthday = form.cleaned_data["dog_birthday"]
            dogtag = DogTag.objects.create(owner_name=owner_name, dog_name=dog_name, dog_birthday=dog_birthday)
            return redirect("dog_tag_list")
        else:
            form = NewDogTagForm(request.GET)
            return render("new_dog_tag.html", {"form": form})


def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dog_tags})

from django.shortcuts import render
from .models import Item, Animal, Revenue

# Create your views here.
def showitems(request):
    items = Item.objects.all() #fetch all items in db
    return render(request, "index.html", {"items_key": items})

def showanimals(request):
    animals = Animal.objects.all() #fetch all animals in db
    return render(request, "index.html", {"animals_key": animals})

def showrevenue(request):
    revenue = Revenue.objects.all() #fetch all revenue in db
    return render(request, "index.html", {"revenue_key": revenue})
from django.shortcuts import render
from .models import Item, Animal, Revenue
# Create your views here.
def showitems(request):
    items = Item.objects.all() #fetch all items in db
    return render(request, "index.html", {"items_key": items})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .models import Animal

# Create your views here.S
def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'item': item})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item)
    return render(request, 'inventory/item_detail.html', {'item': item}) 
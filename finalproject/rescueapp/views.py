from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView
from .models import Item, Animal, Revenue
from .forms import ItemForm

# Create your views here.
class Index(TemplateView):
    template_name = 'rescueapp/index.html'
    
# class showitems(ListView):
#     model = Item
#     template_name = 'rescueapp/item_list.html'
#     context_object_name = 'items'

# class showanimals(ListView):
#     model = Animal
#     template_name = 'rescueapp/animal_list.html'
#     context_object_name = 'animals'

# class showrevenue(ListView):
#     model = Revenue
#     template_name = 'rescueapp/revenue_list.html'
#     context_object_name = 'revenue'

def showitems(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'rescueapp/item_list.html', context)

def showanimals(request):
    animals = Animal.objects.all() #fetch all animals in db
    context = {"animals": animals}
    return render(request, "rescueapp/animal_list.html", context)

def showrevenue(request):
    revenue = Revenue.objects.all() #fetch all revenue in db
    context = {"revenue": revenue}
    return render(request, "rescueapp/revenue_list.html", context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list.html')
    else:
        form = ItemForm()
    return render(request, 'rescueapp/item_form.html', {'form': form})
from django import forms
from .models import Item, Animal, Revenue

#form models go here
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'description']

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'breed', 'species', 'gender', 'color', 'age']

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['week', 'profit', 'expense']
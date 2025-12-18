from django.contrib import admin
from .models import Item, Animal, Revenue

# Register your models here.
admin.site.register(Item)
admin.site.register(Animal)
admin.site.register(Revenue)
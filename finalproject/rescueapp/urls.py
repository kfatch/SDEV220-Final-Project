from django.contrib import admin
from django.urls import path
from rescueapp.views import Index, showitems, showanimals, showrevenue, add_item

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('items/', showitems, name="items"),
    path('animals/', showanimals, name="animals"),
    path('revenue/', showrevenue, name="revenue"),
    path('add_item/', add_item, name='add_item')
]

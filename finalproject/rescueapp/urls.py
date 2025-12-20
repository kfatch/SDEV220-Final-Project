from django.contrib import admin
from django.urls import path
from rescueapp import views
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('items/', views.showitems, name="items"),
    path('animals/', views.showanimals, name="animals"),
    path('revenue/', views.showrevenue, name="revenue"),
]

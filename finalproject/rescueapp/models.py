from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.quantity} left"

class Animal(models.Model):
    name = models.TextField(max_length=50)
    breed = models.TextField(max_length=50)
    species = models.TextField(max_length=50)
    gender = models.TextField(max_length=1)
    color = models.TextField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}, {self.gender}, {self.color} {self.breed}, {self.age}"
    
class Revenue(models.Model):
    week = models.PositiveIntegerField()
    income = models.PositiveIntegerField()
    expense = models.PositiveIntegerField()

    def __str__(self):
        return f"Week: {self.week} - Income: {self.income} - Expense: {self.expense}"
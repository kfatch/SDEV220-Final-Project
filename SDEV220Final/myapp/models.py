from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.TextField(max_length=50)
    breed = models.TextField(max_length=50)
    species = models.TextField(max_length=50)
    gender = models.TextField(max_length=1)
    color = models.TextField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name, self.breed, self.species, self.gender, self.color, self.age
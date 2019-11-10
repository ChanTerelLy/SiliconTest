from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ManyToManyField(Category)
    count = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
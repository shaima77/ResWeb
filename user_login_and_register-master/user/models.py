from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField


class Recipe(models.Model):
    author = models.CharField(max_length=24, unique=False, default='Main dishes')
    fullname = models.CharField(max_length=20)
    Time = models.IntegerField()
    choices = [
        ('Easy', 'Easy'),
        ('Normal', "Normal"),
        ('Hard', "Hard")
    ]
    categories = [
        ('Starters', 'Starters'),
        ('Salads', "Salads"),
        ('Main dishes', "Main dishes"),
        ('Desserts', "Desserts"),
    ]
    Difficulty = models.CharField(max_length=24, choices=choices, default='Easy', unique=False)
    categoriesss = models.CharField(max_length=24, choices=categories, default='Main dishes')

    ResText = models.TextField()
    Ingredients = models.TextField()
    upload = models.ImageField(upload_to='media/uploads', null=False, blank=False)















class Review(models.Model):
    name = models.CharField(max_length=24, unique=False, default='Name')
    date = models.CharField(max_length=24)
    Text = models.TextField()

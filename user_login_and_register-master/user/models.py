from django.db import models
from jsonfield import JSONField


class Recipe(models.Model):
    fullname = models.CharField(max_length=20)
    Time = models.IntegerField()
    choices = [
        ('Easy', 'Easy'),
        ('Noraml', "Normal"),
        ('Hard', "Hard")
    ]
    categories = [
        ('Starters', 'Starters'),
        ('Salads', "Salads"),
        ('Main dishes', "Main dishes"),
        ('Desserts', "Desserts"),
    ]
    Difficulty = models.CharField(max_length=24, choices=choices, default='Easy')
    categoriesss = models.CharField(max_length=24, choices=categories, default='Main dishes')

    ResText = models.TextField()
    Ingredients = models.TextField()
    upload = models.ImageField(upload_to='media/uploads', null=True, blank=True)

    # namee = models.CharField(max_length=20)
    # numberr = models.IntegerField()

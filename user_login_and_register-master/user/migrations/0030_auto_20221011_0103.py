# Generated by Django 2.2.13 on 2022-10-10 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_recipe_categoriesss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Ingredients',
            field=models.TextField(),
        ),
    ]

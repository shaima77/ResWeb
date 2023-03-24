# Generated by Django 2.2.13 on 2022-11-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard')], default='Easy', max_length=24),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.CharField(max_length=24),
        ),
    ]

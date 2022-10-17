# Generated by Django 2.2.13 on 2022-10-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_geeksmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('mobile_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
    ]
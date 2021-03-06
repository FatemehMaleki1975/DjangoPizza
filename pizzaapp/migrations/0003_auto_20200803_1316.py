# Generated by Django 3.0.8 on 2020-08-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0002_pizzamodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminmodel',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='adminmodel',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pizzamodel',
            name='pizzaName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pizzamodel',
            name='pizzaPrice',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

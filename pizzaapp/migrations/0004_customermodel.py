# Generated by Django 3.0.8 on 2020-08-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_auto_20200803_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
    ]

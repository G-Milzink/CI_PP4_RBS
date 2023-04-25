# Generated by Django 3.2.18 on 2023-04-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50, unique=True)),
                ('item_description', models.CharField(max_length=250, unique=True)),
                ('item_price', models.FloatField()),
                ('item_category', models.IntegerField(choices=[(0, 'Starters'), (1, 'Mains'), (2, 'Desserts'), (3, 'New')], default=0)),
                ('item_available', models.BooleanField(default=False)),
            ],
        ),
    ]
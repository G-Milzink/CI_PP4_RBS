from django.db import models


FOOD_CATEGORY = ((0, 'New'), (1, 'Starters'), (2, 'Mains'), (3, 'Desserts'))  # noqa
DRINKS_CATEGORY = ((0, 'New'), (1, 'Beers'), (2, 'Wines'), (3, 'Non-Alchocolic'))  # noqa


class FoodItem(models.Model):

    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, unique=True)
    item_description = models.CharField(max_length=250, unique=True)
    item_price = models.FloatField()
    item_category = models.IntegerField(choices=FOOD_CATEGORY, default=0)
    item_available = models.BooleanField(default=False)

    class meta:
        ordering = ['-item_category']

    def __str__(self):
        return self.item_name


class DrinkItem(models.Model):

    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, unique=True)
    item_description = models.CharField(max_length=250, unique=True)
    item_price = models.FloatField()
    item_category = models.IntegerField(choices=DRINKS_CATEGORY, default=0)
    item_available = models.BooleanField(default=False)

    class meta:
        ordering = ['-item_category']

    def __str__(self):
        return self.item_name

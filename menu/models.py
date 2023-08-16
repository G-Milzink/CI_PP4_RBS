# Third party imports:
from django.db import models


# Categories for food, drink and bites items.
# items in the "new" category are not visible on the website.
FOOD_CATEGORY = ((0, 'New'),
                 (1, 'Starters'),
                 (2, 'Mains'),
                 (3, 'Desserts'))
DRINKS_CATEGORY = ((0, 'New'),
                   (1, 'Beers'),
                   (2, 'Wines'),
                   (3, 'Non-Alchocolic'))
BITES_CATEGORY = ((0, "New"),
                  (1, 'Assorted'),
                  (2, 'Vegetarian'))


class FoodItem(models.Model):
    """
    class for the FoodItem database model
    """
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
    """
    class for the DrinkItem database model
    """
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


class BitesItem(models.Model):
    """
    class for the BitesItem database model
    """
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, unique=True)
    item_description = models.CharField(max_length=250, unique=True)
    item_price = models.FloatField()
    item_category = models.IntegerField(choices=BITES_CATEGORY, default=0)
    item_available = models.BooleanField(default=False)

    class meta:
        ordering = ['-item_category']

    def __str__(self):
        return self.item_name

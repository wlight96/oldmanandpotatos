from django.db import models

# Create your models here.
class Banchan(models.Model):
    banchan_code = models.CharField(primary_key=True, max_length=10)
    category = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'banchan'

class Ingredients(models.Model):
    ingredients_code = models.CharField(primary_key=True, max_length=10)
    ingredients_name = models.CharField(max_length=20)
    ingredients_from = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'
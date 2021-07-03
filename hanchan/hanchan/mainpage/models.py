from django.db import models
# Create your models here.

class Ingredients(models.Model):
    ingredients_code = models.CharField(primary_key=True, max_length=10)
    ingredients_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ingredients'

class Banchan(models.Model):
    banchan_code = models.CharField(primary_key=True, max_length=10)
    category = models.CharField(max_length=20)
    banchan_name = models.CharField(max_length=30)
    store = models.ForeignKey('account.Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'banchan'
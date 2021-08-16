from django.db import models
# Create your models here.

class Ingredients(models.Model):
    ingredients_code = models.CharField(primary_key=True, max_length=10)
    ingredients_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ingredients'

class Banchan(models.Model):
    banchan_code = models.CharField(primary_key=True, max_length=10, db_collation='utf8mb4_0900_ai_ci')
    banchan_name = models.CharField(max_length=20, db_collation='utf8mb4_0900_ai_ci')
    cost = models.IntegerField()
    category = models.CharField(max_length=20, db_collation='utf8mb4_0900_ai_ci')
    saleflag = models.IntegerField()
    discount = models.IntegerField()
    banchan_img = models.TextField(blank=True, null=True)
    s = models.ForeignKey('account.Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'banchan'

class BanchanIngredients(models.Model):
    b_code = models.OneToOneField(Banchan, models.DO_NOTHING, db_column='b_code', primary_key=True)
    i_code = models.ForeignKey('Ingredients', models.DO_NOTHING, db_column='i_code')
    i_name = models.CharField(max_length=20, db_collation='utf8mb4_0900_ai_ci')

    class Meta:
        managed = False
        db_table = 'banchan_ingredients'
        unique_together = (('b_code', 'i_code'),)
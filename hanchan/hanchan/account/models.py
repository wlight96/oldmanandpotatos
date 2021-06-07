from django.db import models

# Create your models here.
class Userpage(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    useremail = models.CharField(max_length=45)
    name = models.CharField(max_length=20)
    b_date = models.DateField()
    user_phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Userpage'

class Store(models.Model):
    store_id = models.CharField(max_length=20)
    store_code = models.CharField(primary_key=True, max_length=20)
    store_name = models.CharField(max_length=45)
    store_phone = models.IntegerField()
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    adress = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'store'
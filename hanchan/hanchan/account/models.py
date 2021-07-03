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
    store_id = models.CharField(primary_key=True, max_length=20)
    store_name = models.CharField(max_length=45)
    store_phone = models.IntegerField()
    extra_address = models.CharField(max_length=50, blank=True, null=True)
    address_detail = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.IntegerField()
    adress = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'store'


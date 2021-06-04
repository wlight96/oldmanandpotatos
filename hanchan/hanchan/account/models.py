from django.db import models

# Create your models here.
class Userpage(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=20)  # Field name made lowercase.
    useremail = models.CharField(max_length=45)
    name = models.CharField(max_length=30)
    b_date = models.DateField()
    user_phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userpage'
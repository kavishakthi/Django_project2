from django.db import models

# Create your models here.

class dbform(models.Model):

    name = models.CharField(max_length=100)
    reg_no = models.IntegerField(null=True)
    email = models.EmailField()
    phone = models.BigIntegerField(default=None)
    address = models.TextField(max_length = 100, default =None)
    dob = models.DateField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    sign = models.ImageField(upload_to='signs/', default=None, null=True)

    class Meta:
        db_table = "usertable"

from unicodedata import category
from django.db import models
from numpy import maximum, product
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        ('1', 'HOD'),
        ('2', 'STAFF'),
        ('3 ', 'STUDENT'),

    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')
    code = str(uuid.uuid4()).replace("-", "")[:6]
    user_id=models.CharField(max_length=50, default=code)
 

    
class HOD(models.Model):
    
    
    # id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    rank = models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class AllProduct(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.product_name
    class Meta:
        db_table = "product"

class Price(models.Model):
    product = models.CharField(max_length=50)        
    amount = models.IntegerField()
    category = models.CharField(max_length=50, null=True,blank=True)

    

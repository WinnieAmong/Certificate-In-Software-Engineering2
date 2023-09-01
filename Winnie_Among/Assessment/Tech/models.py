from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomerDetail(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

     
    def __self__(self):
        return self.name
           
           

class Bio_data(models.Model):
    Customer = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE,null=False, blank=False)
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50,null=False,blank=False)
    date_of_birth = models.DateField()
    Genda =models.CharField(max_length=50,null=False,blank=False)
    Country=models.CharField(max_length=50,null=False,blank=False)
    Town=models.CharField(max_length=50,null=False,blank=False)
    District=models.CharField(max_length=50,null=False,blank=False)
    Phone_Number1=models.IntegerField(max_length=50,null=False,blank=False)
    Phone_Number2=models.IntegerField(max_length=50,null=False,blank=False)
    Email=models.EmailField()




    def __str__(self):
        return self.first_name
    
# class Location(models.Model):
#     country = models.CharField()
#     town =
#     district=
#     zip_code=
        




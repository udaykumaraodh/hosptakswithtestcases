from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.

User=get_user_model()
class Sales(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phote=models.ImageField(upload_to='sales_profile/')
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    mobile=models.BigIntegerField(unique=True)
    emailId=models.EmailField(max_length=150)
    qualificaton=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

    def __str__(self):
        return  self.name








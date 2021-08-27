from django.db import models
from sales.models import Sales

# Create your models here.

class PreRegHos(models.Model):
    hospital_name=models.CharField(max_length=80)
    h_address=models.CharField(max_length=150)
    mobile=models.BigIntegerField(unique=True)
    allocate_to=models.ForeignKey(Sales,on_delete=models.CASCADE)

    def __str__(self):
        return self.hospital_name



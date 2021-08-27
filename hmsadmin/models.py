from django.db import models

from sales.models import Sales
from hospital.models import PreRegHos
from django.contrib.auth.models import User

#Create your models here.
class Sales2Admin(models.Model):

    #
    salesperson=models.ForeignKey(Sales,on_delete=models.CASCADE)
    hopital=models.OneToOneField(PreRegHos,on_delete=models.CASCADE)
    mob2 = models.BigIntegerField()
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    def __str__(self):
        return self.salesperson.name

    # sp=Sales()
    # print(sp.pk)
    # print('===================')
    #
    #
    # prg=PreRegHos.objects.get(allocate_to=sp.pk)
    # h_name=prg.hospital_name
    # # salesperson = models.OneToOneField(user, on_delete=models.CASCADE)
    # # hopital=models.OneToOneField(h_name,on_delete=models.CASCADE)


from django.shortcuts import render
from hmsadmin.serializers import AdminSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sales2Admin
from sales.models import Sales
from hospital.models import PreRegHos
from rest_framework import viewsets
# Create your views here.

@api_view(['GET','POST'])
def hmsAdmin(request):
    if request.method == 'GET':
        hid = request.data.get('hospital_id')
        salesid = request.data.get('salesperson_id')
        so = Sales.objects.get(pk=salesid)
        #ho = PreRegHos.objects.get(pk=hid)

        print(so.pk)
        #print(so.user)
        #print(ho.pk)
        sa=Sales2Admin.objects.filter(salesperson_id=salesid)
        print(sa.values())
        adminserial=AdminSerializer(data=sa,many=True)

        adminserial.is_valid( )
        print(adminserial.data)

        return Response(data=adminserial.data)






    if request.method =='POST':
        data=request.data
        sa=AdminSerializer(data=data)
        if sa.is_valid():
            sa.save()
            message="Data is created successfully"

        else:

            message=sa.errors

        return Response({'message':message})


# class Hmviewset(viewsets.ModelViewSet):
#     queryset = Sales2Admin.objects.all()
#     serializer_class = AdminSerializer

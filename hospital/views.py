from django.shortcuts import render
from hospital.models import PreRegHos
from hospital.serializers import PreRegSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def preRegHos(request):


    if request.method=='GET':
        id = request.data.get('id')
        if id is not None:
            preg = PreRegHos.objects.get(pk=id)
            pres = PreRegSerializer(data=preg)
            return Response(pres.data)

        preg=PreRegHos.objects.all()

        pres=PreRegSerializer(data=preg,many=True)
        pres.is_valid()
        return Response(data=pres.data)

    if request.method== 'POST':
        data=request.data
        serializer=PreRegSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created successfully'})
        return Response(serializer.errors)

    if request.method== 'PUT':
        id = request.data.get('id')
        preg=PreRegHos.objects.get(pk=id)
        pres=PreRegSerializer(preg,data=request.data)
        if pres.is_valid():
            pres.save()
            return Response({"msg":"Data is updated"})
        return Response(pres.errors)

    if request.method== "DELETE":
        id=request.data.get('id')
        preg=PreRegHos.objects.get(pk=id)
        preg.delete()
        return Response({'msg':"Data Deleted"})












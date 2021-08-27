from django.shortcuts import render
from .models import Sales
from sales.serializers import SalesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets




@api_view(['POST','PUT','DELETE'])
def salesApi(request):
    if request.method== 'POST':
        data=request.data
        serializer=SalesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created successfully'})
        return Response(serializer.errors)

    if request.method== 'PUT':
        id = request.data.get('id')
        sm=Sales.objects.get(pk=id)
        serializer=SalesSerializer(sm,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data is updated"})
        return Response(serializer.errors)

    if request.method== "DELETE":
        id=request.data.get('id')
        sm=Sales.objects.get(pk=id)
        SalesSerializer.delete()
        return Response({'msg':"Data Deleted"})





@api_view(['GET'])
def salesViewall(request):
    if request.method == 'GET':

        # id = request.data.get('id')
        #
        # if id is not None:
        #     sm = Sales.objects.get(pk=id)
        #     serializer= SalesSerializer(data=sm)
        #     return Response(serializer.data)

        sm=Sales.objects.all()
        print(sm)
        ss=SalesSerializer(data=sm,many=True)
        ss.is_valid()
        print(ss.data,'salesmana')
        return Response(data=ss.data)
        #return JsonResponse(ss.data,safe=False,content_type='application/json')



# class MyviewSet(viewsets.ModelViewSet):
#     queryset = Sales.objects.all()
#     serializer_class = SalesSerializer
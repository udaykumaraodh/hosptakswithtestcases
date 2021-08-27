from rest_framework import serializers
from  sales.models import Sales
from hospital.models import PreRegHos

Choice=Sales.name
print(Choice)
class PreRegSerializer(serializers.ModelSerializer):

    #allocate_to=serializers.ChoiceField(choices=Choice)
    class Meta:
        model=PreRegHos
        fields="__all__"


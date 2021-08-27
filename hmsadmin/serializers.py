from hmsadmin.models import Sales2Admin
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model=Sales2Admin
        fields="__all__"
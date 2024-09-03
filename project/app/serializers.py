from rest_framework import serializers
from .models import*

class sample(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()

class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=std
        fields='__all__'
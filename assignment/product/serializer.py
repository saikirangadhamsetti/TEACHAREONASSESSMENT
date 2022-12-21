from rest_framework import serializers
from .models import productMainModel
class productserializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields="__all__"
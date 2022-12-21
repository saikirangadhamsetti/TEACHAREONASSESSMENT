from django.shortcuts import render
from rest_framework.views import APIView
from .models import productMainModel
from .serializer import productserializer
from rest_framework.response import Response
class Productlist(APIView):
    def get(self,request):
        products=productMainModel.objects.all()
        serialize=productserializer(products,many=True)
        return Response(serialize.data)
class particularproduct(APIView):
    def get(self,request,id):
        try:
            m=productMainModel.objects.get(id=id)
        except:
            return Response(FileNotFoundError)
        serialize=productserializer(m)
        return Response(serialize.data)
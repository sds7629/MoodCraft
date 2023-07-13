from django.shortcuts import render
from .models import Visiter
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

from .serializer import VisiterSerializer

# Create your views here.


class AllVisiters(APIView):

    def get(self, request):
        visiter = Visiter.objects.all()
        serializer = VisiterSerializer(visiter, many = True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = VisiterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("success") 

# class Counts(APIView):

#     def get(self, request):
#         counts = Count.objects.all()
#         counts.update_counter()
#         counts.save()
#         serializer = CountSerializer(counts)
#         return Response(serializer.data)

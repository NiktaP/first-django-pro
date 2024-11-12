from random import random

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
# Create your views here.

class RegisterView(APIView):

    def post(self,request):

         email=request.data.get('email')
         if not email:
             return Response(status=status.HTTP_400_BAD_REQUEST)

         try:
             user = CustomUser.objects.get(email=email)
         except CustomUser.DoesNotExist:
             CustomUser.objects.creat_user(email)

         code = random.randint(10000, 99999)

         return Response({'code' : code})


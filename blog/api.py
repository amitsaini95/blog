
from asyncio import FastChildWatcher
from functools import partial
import imp
import re
from sys import api_version
from urllib import request, response
from .serializers import userSerializers,postSerializers,categorySerializers,tagSerializers,commentSerializers

from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .models import Category, Post, Tag, User,Category,Comment
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog import serializers

class userlist(viewsets.ModelViewSet):
   
       queryset=User.objects.all()
       serializer_class=userSerializers
class postlist(viewsets.ModelViewSet):
       queryset=Post.objects.all()
       serializer_class=postSerializers
class categorylist(viewsets.ModelViewSet):
      queryset=Category.objects.all()
      serializer_class=categorySerializers
class taglist(viewsets.ModelViewSet):
      queryset=Tag.objects.all()
      serializer_class=tagSerializers
class commentlist(viewsets.ModelViewSet):
      queryset=Comment.objects.all()
      serializer_class=commentSerializers
    
       

        


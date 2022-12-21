from .serializers import userSerializers,postSerializers,loginSerializers,signupSerializers,tagSerializers,categroySerializers,commentSerializers
from .models import Category, Post, Tag, User,Category,Comment
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
class userlist(viewsets.ModelViewSet):
       queryset=User.objects.all()
       serializer_class=userSerializers
       http_method_names=['get','put','patch']
       
class postlist(viewsets.ModelViewSet):
       queryset=Post.objects.all()
       serializer_class=postSerializers
        
class categorylist(viewsets.ModelViewSet):
      queryset=Category.objects.all()
      serializer_class=categroySerializers
    
class taglist(viewsets.ModelViewSet):
      queryset=Tag.objects.all()
      serializer_class=tagSerializers

class signuplist(viewsets.ModelViewSet):
      queryset=User.objects.all()
      serializer_class=signupSerializers
      http_method_names=['post','get']
      
class loginlist(viewsets.ModelViewSet):
      queryset = User.objects.all()
      serializer_class=loginSerializers
      http_method_names=['post']
      permission_classes=((AllowAny,))
      
class commentlist(viewsets.ModelViewSet):
      queryset=Comment.objects.all()
      serializer_class=commentSerializers
      



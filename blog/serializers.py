from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from rest_framework import serializers

from .models import *



from blog.models import User,Post,Category,Comment
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('id','username','first_name','last_name','password','email','company','state','gender','profileimage',) 
class postSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields= ('id','author','title','text','timage','featureimage','category','tag')
class categorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('category_name', 'slug')
class tagSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=('tag_name', 'slug')
class commentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('name', 'email', 'post', 'created',)
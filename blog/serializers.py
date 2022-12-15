from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('id','username','first_name','password','last_name','email','company','state','gender','profileimage',) 
    	
    def get_token(self, obj):
            token = Token.objects.get_or_create(user=obj)
            return token.key
        
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
class signupSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email','company','state','gender','profileimage')
        
    def to_representation(self, instance):
            serializer = userSerializers(instance=instance)
            return serializer.data

    def create(self, validated_data):
            user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'],email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],company=validated_data['company'],gender=validated_data['gender'],profileimage=validated_data['profileimage'],state=validated_data['state'])
            return user
        
class loginSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password',)
        extra_kwargs = {
			'username': {'required': True, 'validators': []},
			'password': {'required': True, 'style': {'input_type': 'password'}},
		}
    def to_representation(self, instance):
            serializer = userSerializers(instance=instance)
            return serializer.data

    def create(self, validated_data):
            user = authenticate(username=validated_data['username'], password=validated_data['password'],)
            if user is not None:
                return user
            raise serializers.ValidationError({"detail":'Invalid username or password.'})

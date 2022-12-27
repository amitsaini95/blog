from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token 
      
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
        
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('id','username','first_name','password','last_name','email','company','state','gender','profileimage',) 
    	
    def get_token(self, obj):
            token = Token.objects.get_or_create(user=obj)
            return token.key
        

class commentSerializers(serializers.ModelSerializer):

    class Meta:
        model=Comment
        fields=('id','name','email','body','created','updated','active','post','parent') 
    
    def to_representation(self, obj):
        rep = super(commentSerializers, self).to_representation(obj)
        cat=Comment.objects.filter(parent=obj.id)
        catlists=[]
        for i in cat:
         catlists.append({'id':i.id,'name':i.name,'email':i.email,'body':i.body,'created':i.created,'updated':i.updated,'post':i.post_id,'parent':i.parent_id})
        rep['replies']=catlists
        return rep
        
class categroySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class tagSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'     
           
class postSerializers(serializers.ModelSerializer): 
    class Meta:
        
        model=Post
        fields =('__all__')
        
    def to_representation(self, instance):
        rep = super(postSerializers, self).to_representation(instance)
        cat=categroySerializers(Category.objects.get(id=instance.category.id))
        rep['category']=cat.data
        tagList = []
        for i in instance.tag.all():
            tagList.append({'id':i.id,'tag':i.tag_name,'slug':i.slug,'created_date':i.created_date, 'published_date':i.published_date})
        rep['tag'] = tagList
        commentList = []
        for i in instance.comments.all():
            commentList.append({'id':i.id,'name':i.name, 'email':i.email, 'body':i.body,'created':i.created,'updated':i.updated,'active':i.active,'parent':i.parent_id,'post':i.post_id})
        rep['comment'] = commentList
        rep['author'] = instance.author.first_name
        return rep
  
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
     
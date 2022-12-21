from dataclasses import fields
from re import I
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django.contrib.auth import get_user_model
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','timage','featureimage','category','tag',)
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=('id','category_name','slug','created_date','published_date')

class TagForm(forms.ModelForm):
    class Meta:
        model =Tag
        fields = ('__all__')

class UserRegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','company','state','gender','profileimage')
        
class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    company =models.CharField(max_length=50)
    state = models.CharField(max_length= 40)
    gender = models.CharField(max_length=20)
    profileimage = models.ImageField(upload_to='images/',default='/images/job.png')  

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','company','state','gender','profileimage')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body' )
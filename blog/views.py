

from asyncore import write
from cgitb import reset
import email
import imp
import json
from pydoc import resolve
from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.http import HttpResponse
from django import views
import csv

from rest_framework.renderers import JSONRenderer
# from django.views.generic import CreateView
# from django.utils.text import slugify
# from django.contrib.auth.models import User


from django.contrib.auth  import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UsernameField

from .forms import UserRegistraionForm,LoginForm,CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)
    return render(request, 'blog/post_list.html',{'posts':posts})
    
    
def post_edit(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/',slug=slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
          
            post.save()
            
            return redirect('/',slug=post.slug)
         
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request,slug):
    posts=get_object_or_404(Post,slug=slug)
 
    
    comments = posts.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
       
            try:
           
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
            
                if parent_obj:
                
                    replay_comment = comment_form.save(commit=False)
                   
                    replay_comment.parent = parent_obj
    
            new_comment = comment_form.save(commit=False)
        
            new_comment.post = posts
         
            new_comment.save()
            return redirect('blog:post_detail',slug=slug)
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post_detail.html',
                  {'posts': posts,
                   'comments': comments,
                   'comment_form': comment_form})



def category_list(request):
    category= Category.objects.filter(published_date__lte=timezone.now())
   
    return render(request, 'blog/category_list.html', {'categories': category})
    
def category_detail(request,slug):
    categorydetails= get_object_or_404(Category,slug=slug)
    post=Post.objects.filter(category=categorydetails)
 
    return render(request, 'blog/category_detail.html',{'cat':post})

def user_signup(request): 
    if request.method == "POST": 
     form=UserRegistraionForm(request.POST,request.FILES)
     if form.is_valid():
       
        messages.success(request,"you have become an author")
        form.save()
        return redirect('/')
    else:
        form=UserRegistraionForm()
    return render(request,'blog/user_signup.html',{'form':form})


def user_login(request):
    if request.method == "POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
          
            uname = form.cleaned_data['username']
              
            upass = form.cleaned_data['password']
            
            user = authenticate(username=uname,password=upass)
             
            if user is  not None:
                 
                login(request,user)
                messages.success(request,"logged in successfully ||")
                return HttpResponseRedirect('/')
    else:   
        form=LoginForm()
    return  render(request,'blog/login.html',{'form':form})



def user_profile(request):
     return render(request,'blog/profile.html',{})
def user_logout(request):
    logout(request)
    return redirect('/')

def profileupdate(request):

    if request.method == "POST":
        form = UpdateProfile(request.POST,request.FILES,instance=request.user)
        update=form.save(commit=False)
        update.user=request.user
        update.save()
        return redirect('/profile/')
        
    else:
        form = UpdateProfile(instance=request.user)

    return render(request, 'blog/profileupdate.html', {'form':form})

def tag_list(request):
    tag= Tag.objects.filter(published_date__lte=timezone.now())
   
    return render(request, 'blog/tag_list.html', {'tags': tag})
    
    
def tag_detail(request,slug):
    tagdetails= get_object_or_404(Tag,slug=slug)
    post=Post.objects.filter(tag=tagdetails)
 
    return render(request, 'blog/tag_detail.html',{'cat':post})






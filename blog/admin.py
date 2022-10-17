from pyexpat import model
from urllib import response
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from blog import views


# Register your models here.
from .forms import *
from .models import *
import csv


class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','text','timage','featureimage')
    list_filter = ('author', 'title', 'text','timage','featureimage')
    search_fields = ('title',)
  


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
    search_fields=('category_name','slug')
    list_filter=('category_name','slug')

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag_name',)}
    list_display = ('tag_name', 'slug')
    search_fields=('tag_name','slug')
    list_filter=('tag_name','slug')

class UserAdmin(admin.ModelAdmin):
    
  
    list_display= ('username','profileimage','email','company','state','gender','first_name','last_name')
    search_fields=('username','profileimage','email','company','state','gender','first_name','last_name')
    list_filter=('username','profileimage','email','company','state','gender','first_name','last_name')
    actions=['export_to_csv']
    def export_to_csv(self,request,queryset):
        
        response=HttpResponse(content_type='text/csv')
        response['Content-Despostion']='attachment;filename=user_export.csv'
        writer=csv.writer(response)
        writer.writerow(['username','password','profileimage','email','company','state','gender','first_name','last_name'])
        queryset=queryset.values_list('username','password','profileimage','email','company','state','gender','first_name','last_name')
        for obj in queryset:
            writer.writerow(obj)
        return response
       
       
    export_to_csv.short_description='Export as csv'


    
from django.urls import reverse


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
   
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)




admin.site.register(User,UserAdmin)
admin.site.register(Comment,CommentAdmin)



from argparse import Namespace
from email.mime import base
from django.urls import path,include
from . import api
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('user',api.userlist,basename="userlist")
router.register('post',api.postlist,basename="postlist")
router.register('category',api.categorylist,basename="categorylist")
router.register('tag',api.taglist,basename="taglist")
router.register('comment',api.commentlist,basename="comemntlist")


urlpatterns = [
 
  path('',include(router.urls)),
 
  ]
from django.urls import path,include
from . import api
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('users',api.userlist,basename="userlist")
router.register('posts',api.postlist,basename="postlist")
router.register('category',api.categorylist,basename="categorylist")
router.register('tag',api.taglist,basename="taglist")
router.register('signup',api.signuplist,basename="signuplist")
router.register('login',api.loginlist,basename="loginlist")
router.register('comment',api.commentlist,basename="commentlist")
urlpatterns = [
  path('',include(router.urls)),
  ]
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('category/<slug:slug>/',views.category_detail,name='category_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('tag/<slug:slug>/',views.tag_detail,name='tag_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('profile-update/',views.profileupdate,name="profileupdate"),
    path('category/', views.category_list,name='category_list'),
    path('signup/',views.user_signup,name="user_signup"),
    path('login/',views.user_login,name="user_login"), 
    path('profile/',views.user_profile,name="user_profile"),
    path('logout/',views.user_logout,name="logout"),
    path('tag/', views.tag_list,name='tag_list'),
    path('', views.post_list, name='post_list'), 
]   
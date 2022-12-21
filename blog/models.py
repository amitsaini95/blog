from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    email =models.EmailField(max_length=50)
    company =models.CharField(max_length=50)
    state = models.CharField(max_length= 40)
    gender = models.CharField(max_length=20)
    profileimage = models.ImageField(upload_to='images')  
 
class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=250,allow_unicode=True , null=True, blank=True, unique=True)
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tag_name
        
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField( null=True, blank=True)
    slug = models.SlugField(max_length=250,allow_unicode=True ,unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.category_name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    timage=models.ImageField(upload_to='images1')
    published_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts",blank=True)
    featureimage=models.ImageField(upload_to='images')
    tag = models.ManyToManyField(Tag,related_name="posts",blank=True)
    slug = models.SlugField(max_length=250,allow_unicode=True,null=True, blank=True, unique=True)
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
   
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
    def __str__(self):
        return 'Comment by {}'.format(self.name)
    

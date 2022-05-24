from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class PublishedManager(models.Manager):
   def get_queryset(self):
      return super(PublishedManager, self).get_queryset().filter

      
class Post(models.Model):
        title = models.CharField(max_length=200, unique=True)
        slug = models.SlugField(max_length=200, unique=True)
        author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
        body = models.TextField()    
        created_on = models.DateTimeField(auto_now_add=True)
        published= models.BooleanField(default=False)
        published_on = models.DateTimeField(auto_now_add=True)
        updated_on = models.DateTimeField(auto_now= True)
        status = models.IntegerField(choices=STATUS, default=0)
        #model managers
        objects = models.Manager() #custom manager
        published = PublishedManager()  #our manager


class Comment(models.Model):
       post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
       name = models.CharField(max_length=80)
       email = models.EmailField()
       body = models.TextField()
       created_on = models.DateTimeField(auto_now_add=True)
       active = models.BooleanField(default=False)




class Meta:
    ordering = ['-published_on']

def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)
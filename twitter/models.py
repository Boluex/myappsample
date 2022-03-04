from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class posts(models.Model):
    author = models .ForeignKey(User,on_delete=models.CASCADE,related_name='yo')
    content= models.TextField()
    tagline=models.CharField(max_length=20000)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='blah')
    date_posted=models.DateTimeField(default=timezone.now)


like_choices = (
    ('like','like'),
    ('unlike','unlike')
)

choice = (
    ('follow','follow',),
    ('unfollow','unfollow')
)




class likebutton(models.Model):
    value = models.CharField(choices=like_choices,max_length=12,default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(posts,on_delete=models.CASCADE)

class comment(models.Model):
    post = models.ForeignKey(posts,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content =models.CharField(max_length=120000)
    date_posted=models.TimeField(auto_now_add=True)



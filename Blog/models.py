from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=20)
    content = models.TextField()
    img = models.ImageField(null=True,blank=True,default="default.jpg") 
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title + ' by- '+ self.author

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
from django.db import models
from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    msg = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Message from ' + self.name + ' - '+ self.email
    

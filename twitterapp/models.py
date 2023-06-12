from django.db import models
from django.contrib.postgres.fields import ArrayField,JSONField
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class profile(models.Model):
    followers= ArrayField(models.CharField(max_length=255,null=True, default=list))
    following= ArrayField(models.CharField(max_length=255,null=True,default=list))
    tweet=ArrayField(models.TextField(),default=list)
    tweet_time=ArrayField(models.DateTimeField(datetime.now,blank=True),default=list)
    followingtweet=models.JSONField(default=dict)
    userinfo=models.OneToOneField(User,on_delete=models.CASCADE)

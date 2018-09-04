from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class information(models.Model):
    login=models.CharField(max_length=100,)
    idd=models.CharField(max_length=100,)
    avatar_url=models.CharField(max_length=100,default='nll',null=True)
    gravatar_id=models.CharField(max_length=100,default='nll',null=True)
    url=models.CharField(max_length=100, default='nll',null=True)
    html_url=models.CharField(max_length=100,default='nll',null=True)
    followers_url=models.CharField(max_length=100,default='nll',null=True)
    following_url=models.CharField(max_length=100,default='nll',null=True)
    gists_url=models.CharField(max_length=100,default='nll',null=True)
    starred_url=models.CharField(max_length=100,default='nll',null=True)
    subscriptions_url=models.CharField(max_length=100,default='nll',null=True)
    organizations_url=models.CharField(max_length=100,default='nll',null=True)
    repos_url=models.CharField(max_length=100,default='nll',null=True)
    events_url=models.CharField(max_length=100,default='nll',null=True)
    received_events_url=models.CharField(max_length=100,default='nll',null=True)
    typ=models.CharField(max_length=100,default='nll',null=True)
    site_admin=models.CharField(max_length=100,default='nll',null=True)
    name=models.CharField(max_length=100,default='nll',null=True)
    company=models.CharField(max_length=100,default='nll',null=True)
    blog=models.CharField(max_length=100,default='nll',null=True)
    location=models.CharField(max_length=100,default='nll',null=True)
    email=models.CharField(max_length=100,default='nll',null=True)
    hireable=models.CharField(max_length=100,default='nll',null=True)
    bio=models.CharField(max_length=100,default='nll',null=True)
    public_repos=models.CharField(max_length=100,default='nll',null=True)
    public_gists=models.CharField(max_length=100,default='nll',null=True)
    followers=models.CharField(max_length=100,default='nll',null=True)
    following=models.CharField(max_length=100,default='nll',null=True)
    created_at=models.CharField(max_length=100,default='nll',null=True)
    updated_at=models.CharField(max_length=100,default='nll',null=True)
    dat = models.DateField()
class sapi(models.Model):
        dat = models.DateField()

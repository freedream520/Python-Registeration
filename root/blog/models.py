from django.db import models

# Create your models here.
from taggit.managers import TaggableManager
from django import template
from django import forms
from time import time

# this func will retrieve and find the file name where the img saved for post class
def get_upload_file_name(instance, filename):
    return 'uploaded_files/%s_%s' % (str(time()).replace('.', '-'), filename)

class Post(models.Model):
    title     = models.CharField(max_length=64)
    body      = models.TextField()
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateField(auto_now=True)
    published = models.BooleanField(default=True)
    likes     = models.IntegerField(default=0)
    tags      = TaggableManager()
    
    def __unicode__(self):
        return u'%s - %s' % (self.title, self.created)

class Tag(models.Model):
    tags = models.ForeignKey(Post)


class Contact(models.Model):
    name    = models.CharField(max_length=64)
    email   = models.EmailField(max_length=72)
    message = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    title   = models.CharField(max_length=100)
    text    = models.TextField()
    images  = models.ImageField(upload_to='about/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s - %s' % (self.title, self.created)

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='gallery/')

    def __unicode__(self):
        return self.title

class Slidshow(models.Model):
    title = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='slidshow/')

    def __unicode__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Nobel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Poem(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    type = models.TextField()


    def __str__(self):
        return self.title
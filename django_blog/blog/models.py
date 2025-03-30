# blog/models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Add TaggableManager instead of ManyToMany field
    tags = TaggableManager(blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])
    

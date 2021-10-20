from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100, default='AutoCategorise')

    def __str__(self):
        return self.title + ' | ' +  str(self.author)

    def get_absolute_url(self):
        return reverse('home') 

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    
    Text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title
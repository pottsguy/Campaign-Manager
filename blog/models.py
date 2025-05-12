from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
    
class Campaign(models.Model):
    name = models.CharField(max_length = 50)
    system = models.CharField(max_length=50)
    premise = models.TextField()
    key = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name='campaigns')

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    session = models.SmallIntegerField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("Individual Post", kwargs={'pk': self.pk})
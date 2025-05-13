from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random, string
    
def generate_random_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class Campaign(models.Model):
    name = models.CharField(max_length = 50)
    system = models.CharField(max_length=50)
    premise = models.TextField()
    key = models.CharField(max_length=50, default=generate_random_key, unique=True)
    users = models.ManyToManyField(User, related_name='campaigns')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_campaigns')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Individual Campaign", kwargs={'pk': self.pk})
    
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
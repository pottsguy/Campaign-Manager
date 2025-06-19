from django.db import models
import random, string
from django.contrib.auth.models import User
from django.urls import reverse

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
    class Meta:
        db_table = 'blog_campaign'
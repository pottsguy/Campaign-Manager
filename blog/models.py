from django.db import models
from django.urls import reverse
from accounts.models import Campaign
    
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
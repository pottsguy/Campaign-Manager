from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    campaign = models.CharField(max_length=200)
    session = models.SmallIntegerField()
    system = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("Individual Post", kwargs={'pk': self.pk})
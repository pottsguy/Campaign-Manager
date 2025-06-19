from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User
from accounts.models import Campaign
from django.urls import reverse

class Charsheet(models.Model):
    name = models.CharField(max_length=50)
    player = ForeignKey(User, on_delete=models.CASCADE)
    campaign = ForeignKey(Campaign, on_delete=models.CASCADE)
    basic_info = models.TextField(blank=True)
    primary_stats = models.TextField(blank=True)
    combat_stats = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    special_abilities = models.TextField(blank=True)
    inventory_main = models.TextField(blank=True)
    inventory_extra = models.TextField(blank=True)
    backstory = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Character Sheets")
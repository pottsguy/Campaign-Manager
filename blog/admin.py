from django.contrib import admin
from .models import Post, Campaign

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "campaign",
    )

admin.site.register(Post, PostAdmin)

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'premise')  # Specify the fields you want to display in the list view
    filter_horizontal = ('users',)  # This makes the user selection more user-friendly

admin.site.register(Campaign, CampaignAdmin)
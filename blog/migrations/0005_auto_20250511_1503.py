from django.db import migrations

def convert_campaign_to_foreign_key(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Campaign = apps.get_model('blog', 'Campaign')

    for post in Post.objects.all():
        campaign_name = post.campaign
        # Use an underscore to indicate that we're ignoring the second return value
        campaign, _ = Campaign.objects.get_or_create(name=campaign_name)
        post.campaign = campaign
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_campaign'),  # Replace with the name of the previous migration
    ]

    operations = [
        migrations.RunPython(convert_campaign_to_foreign_key),
    ]
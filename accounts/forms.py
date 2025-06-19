from django import forms
from blog.models import Campaign

class NewCampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'system', 'premise', 'key']

class JoinCampaignForm(forms.Form):
    name = forms.CharField(max_length=50, label="Campaign Name")
    key = forms.CharField(max_length=50, label="Campaign Key")

class EditCampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'system', 'premise', 'key']

class LeaveCampaignForm(forms.Form):
    confirm = forms.BooleanField(label="leave", required=False)
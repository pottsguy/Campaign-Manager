from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from blog.models import Campaign

class SignUpView(CreateView) :
    form_class = UserCreationForm
    success_url = reverse_lazy('Home Page')
    template_name = "registration/sign_up.html"

def CampaignsView(request) :
    campaign_list = Campaign.objects.filter(users=request.user)
    return render(request, 'campaigns.html', {'campaign_list':campaign_list})
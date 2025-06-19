from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic import DetailView
from .models import Campaign
from .forms import NewCampaignForm, JoinCampaignForm, EditCampaignForm, LeaveCampaignForm
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q

class SignUpView(CreateView) :
    form_class = UserCreationForm
    success_url = reverse_lazy('Home Page')
    template_name = "sign_up.html"

def accounts_page_view(request):
    return render(request, "login.html")

def campaigns_view(request):
    campaign_list = Campaign.objects.filter(Q(users=request.user) | Q(host=request.user))
    return render(request, 'campaigns.html', {'campaign_list': campaign_list})

class CreateCampaignView(CreateView):
    model = Campaign
    form_class = NewCampaignForm
    template_name = 'new_campaign.html'
    success_url = reverse_lazy('Campaigns')
    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)
    
class JoinCampaignView(FormView):
    form_class = JoinCampaignForm
    template_name = 'join_campaign.html'
    success_url = reverse_lazy('Campaigns')
    def form_valid(self, form):
        campaign_name = form.cleaned_data.get('name')
        campaign_key = form.cleaned_data.get('key')
        try:
            campaign = Campaign.objects.get(name=campaign_name, key=campaign_key)
        except Campaign.DoesNotExist:
            raise Http404("Campaign not found or invalid key")
        campaign.users.add(self.request.user)
        return redirect(self.success_url)

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = "campaign_detail.html"

class EditCampaignView(UpdateView):
    model = Campaign
    form_class = EditCampaignForm
    template_name = 'edit_campaign.html'
    success_url = reverse_lazy('Campaigns')
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.host != self.request.user:
            raise Http404("You are not the host of this campaign.")
        return obj
    def form_valid(self, form):
        form.instance.host = self.get_object().host
        return super().form_valid(form)

class LeaveCampaignView(FormView):
    template_name = "leave_campaign.html"
    form_class = LeaveCampaignForm
    success_url = reverse_lazy('Campaigns')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = get_object_or_404(Campaign, pk=self.kwargs['pk'])
        return context
    def form_valid(self, form):
        campaign = get_object_or_404(Campaign, pk=self.kwargs['pk'])
        if self.request.user in campaign.users.all():
            campaign.users.remove(self.request.user)
        return HttpResponseRedirect(self.success_url)

class DeleteCampaignView(DeleteView):
    model = Campaign
    template_name = "delete_campaign.html"
    success_url = reverse_lazy("Campaigns")
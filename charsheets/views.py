from .models import Charsheet#, Campaign
from accounts.models import Campaign
from django.db import models
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy

class CharsheetsView(ListView):
    model = Charsheet
    template_name = "charsheets.html"
    def get_queryset(self):
            queryset = super().get_queryset().filter(player=self.request.user)
            campaign_id = self.request.GET.get('campaign')
            if campaign_id:
                queryset = queryset.filter(campaign__id=campaign_id)
            return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.filter(
            Q(users=self.request.user) | Q(host=self.request.user)
        ).distinct()
        context['selected_campaign'] = self.request.GET.get('campaign', '')
        return context

class NewCharacterView(LoginRequiredMixin,CreateView):
    model = Charsheet
    template_name = "new_character.html"
    fields = ['name', 'campaign', 'basic_info', 'primary_stats', 'combat_stats', 'skills', 'special_abilities', 'inventory_main', 'inventory_extra', 'backstory', 'notes']
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Only show campaigns where the user is a participant or the host
        form.fields['campaign'].queryset = Campaign.objects.filter(
            models.Q(users=self.request.user) | models.Q(host=self.request.user)
        ).distinct()
        return form
    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

class IndividualSheetView(UpdateView):
    model = Charsheet
    template_name = "individual_charsheet.html"
    fields = ['name', 'basic_info', 'primary_stats', 'combat_stats', 'skills', 'special_abilities', 'inventory_main', 'inventory_extra', 'backstory', 'notes']
    def get_success_url(self):
        return reverse('Character Sheet', kwargs={'pk': self.object.pk})
    
class DeleteSheetView(DeleteView):
    model = Charsheet
    template_name = "delete_charsheet.html"
    success_url = reverse_lazy("Character Sheets")
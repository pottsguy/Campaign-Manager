from django.shortcuts import render
from .models import Charsheet, Campaign
from django.db import models
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

def charsheets(request):
    charsheets = Charsheet.objects.filter(player=request.user)
    return render(request, 'charsheets.html', {'charsheets': charsheets})

class NewCharacterView(LoginRequiredMixin,CreateView):
    model = Charsheet
    template_name = "new_character.html"
    fields = ['name', 'campaign', 'basic_info', 'primary_stats', 'combat_stats', 'skills', 'special_abilities', 'inventory_main', 'inventory_extra', 'backstory', 'notes']
    # def form_valid(self, form):
    #     form.instance.player = self.request.user
    #     return super().form_valid(form)
    
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
    
# class IndividualSheetView(DetailView):
#     model = Charsheet
#     template_name = "individual_charsheet.html"

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
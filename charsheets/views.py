from django.shortcuts import render
from .models import Charsheet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

def charsheets(request):
    charsheets = Charsheet.objects.filter(player=request.user)
    return render(request, 'charsheets.html', {'charsheets': charsheets})

class NewCharacterView(LoginRequiredMixin,CreateView):
    model = Charsheet
    template_name = "new_character.html"
    fields = ['name', 'campaign', 'basic_info', 'primary_stats', 'combat_stats', 'skills', 'special_abilities', 'inventory_main', 'inventory_extra', 'backstory', 'notes']
    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)
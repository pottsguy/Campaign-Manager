from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def home_page_view(request):
    return render(request, "home.html")

def dice_roller_view(request):
    return render(request, "dice/dice_roller.html")
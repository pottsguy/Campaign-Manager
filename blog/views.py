from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def home_page_view(request):
    return render(request, "home.html")

def campaign_diary_view(request):
    return render(request, "blog/campaign_diary.html")
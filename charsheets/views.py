from django.shortcuts import render
from .models import Charsheet

def charsheets(request):
    charsheets = Charsheet.objects.all()
    return render(request, 'charsheets.html', {'charsheets': charsheets})
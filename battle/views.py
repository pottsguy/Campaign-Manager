from django.shortcuts import render
from django.http import HttpResponse

def battle_view(request) :
    return render(request, 'battle.html')
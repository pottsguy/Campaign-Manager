from django.shortcuts import render

def battle_view(request) :
    return render(request, 'battle.html')
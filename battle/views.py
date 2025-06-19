from django.shortcuts import render

def home_page_view(request):
    return render(request, "home.html")

def battle_view(request) :
    return render(request, 'battle.html')
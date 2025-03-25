from django.shortcuts import render
from django.http import HttpResponse
from random import randrange

def home_page_view(request):
    return HttpResponse(
        "<h1>Welcome to Guy's Website</h1>"
        "<button>Dice Roller</button>"
        )

def dice_roller_view(request):
    context = {
        "d4" : randrange(4)+1, 
        "d6" : randrange(6)+1,
        "d8" : randrange(8)+1, 
        "d10" : randrange(10)+1, 
        "d12" : randrange(12)+1, 
        "d20" : randrange(20)+1, 
        "d100" : randrange(100)+1
        }
    return render(request, "dice/dice_roller.html", context)
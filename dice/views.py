from django.shortcuts import render

# def home_page_view(request):
#     return render(request, "home.html")

def dice_roller_view(request):
    return render(request, "dice_roller.html")
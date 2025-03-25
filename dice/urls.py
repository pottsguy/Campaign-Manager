from django.urls import path
from .views import home_page_view, dice_roller_view

urlpatterns = [
    path('', home_page_view),
    path('dice', dice_roller_view)
]
from django.urls import path
from .views import battle_view, home_page_view

urlpatterns = [
    path('', home_page_view, name='Home Page'),
    path('battle', battle_view, name='Battle'),
]
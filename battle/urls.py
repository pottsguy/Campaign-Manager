from django.urls import path
from .views import battle_view

urlpatterns = [
    path('', battle_view, name='Battle'),
]
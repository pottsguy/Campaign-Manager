from django.urls import path
from .views import charsheets

urlpatterns = [
    path('charsheets/', charsheets, name='Character Sheets'),
]
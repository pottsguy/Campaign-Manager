from django.urls import path
from .views import charsheets, NewCharacterView

urlpatterns = [
    path('', charsheets, name='Character Sheets'),
    path('new/', NewCharacterView.as_view(), name="Create New Character"),
]
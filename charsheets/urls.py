from django.urls import path
from .views import NewCharacterView, IndividualSheetView, DeleteSheetView, CharsheetsView

urlpatterns = [
    path('', CharsheetsView.as_view(), name='Character Sheets'),
    path('new/', NewCharacterView.as_view(), name="Create New Character"),
    path("<int:pk>/", IndividualSheetView.as_view(), name='Character Sheet'),
    path("<int:pk>/delete/", DeleteSheetView.as_view(), name="Delete Character"),
]
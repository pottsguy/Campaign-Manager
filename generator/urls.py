from django.urls import path
from .views import generator_view

urlpatterns = [
    path('', generator_view, name='Generators')
]
from django.urls import path
from .views import SignUpView, CampaignsView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='Sign Up'),
    path('campaigns/', CampaignsView, name='Campaigns')
]
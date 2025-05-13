from django.urls import path
from .views import SignUpView, CampaignsView, CreateCampaignView, DeleteCampaignView, JoinCampaignView, LeaveCampaignView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='Sign Up'),
    path('campaigns/', CampaignsView, name='Campaigns'),
    path('new_campaign/', CreateCampaignView.as_view(), name='New Campaign'),
    path('campaigns/<int:pk>/delete/', DeleteCampaignView.as_view(), name='Delete Campaign'),
    path('campaigns/join/', JoinCampaignView.as_view(), name='Join Campaign'),
    path('campaigns/<int:pk>/leave/', LeaveCampaignView.as_view(), name='Leave Campaign'),
]
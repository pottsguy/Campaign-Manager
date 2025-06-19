from django.urls import path
from .views import SignUpView, campaigns_view, CreateCampaignView, DeleteCampaignView, JoinCampaignView, LeaveCampaignView, EditCampaignView, CampaignDetailView, accounts_page_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='Sign Up'),
    path('login/', accounts_page_view, name='Account'),
    path('campaigns/', campaigns_view, name='Campaigns'),
    path('new_campaign/', CreateCampaignView.as_view(), name='New Campaign'),
    path('<int:pk>/delete/', DeleteCampaignView.as_view(), name='Delete Campaign'),
    path('join/', JoinCampaignView.as_view(), name='Join Campaign'),
    path('<int:pk>/leave/', LeaveCampaignView.as_view(), name='Leave Campaign'),
    path('<int:pk>/edit/', EditCampaignView.as_view(), name='Edit Campaign'),
    path("<int:pk>/", CampaignDetailView.as_view(), name='Campaign Detail'),
]
from django.urls import path
from .views import CampaignDiaryView, IndividualPostView, UploadReportView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", CampaignDiaryView.as_view(), name="Campaign Diary"),
    path("post/<int:pk>/", IndividualPostView.as_view(), name='Individual Post'),
    path("new/", UploadReportView.as_view(), name="Upload Session Report"),
    path("<int:pk>/edit/", UpdatePostView.as_view(), name='Edit Post'),
    path("<int:pk>/delete/", DeletePostView.as_view(), name="Delete Post"),
]
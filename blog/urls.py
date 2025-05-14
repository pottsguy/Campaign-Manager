from django.urls import path
from .views import home_page_view, CampaignDiaryView, IndividualPostView, UploadReportView, UpdatePostView, DeletePostView#, accounts_page_view

urlpatterns = [
    # path('', home_page_view, name='Home Page'),
    # path('account/login/', accounts_page_view, name='Account'),
    path("", CampaignDiaryView.as_view(), name="Campaign Diary"),
    # path('blog/', campaign_diary_view, name='Campaign Diary'),
    path("post/<int:pk>/", IndividualPostView.as_view(), name='Individual Post'),
    # path('blog/post/<int:pk>', individual_post_view, name='Individual Post')
    path("new/", UploadReportView.as_view(), name="Upload Session Report"),
    path("<int:pk>/edit/", UpdatePostView.as_view(), name='Edit Post'),
    path("<int:pk>/delete/", DeletePostView.as_view(), name="Delete Post"),
]
from django.urls import path
from .views import home_page_view, accounts_page_view, CampaignDiaryView, IndividualPostView, UploadReportView #campaign_diary_view, individual_post_view

urlpatterns = [
    path('', home_page_view, name='Home Page'),
    path('account/login/', accounts_page_view, name='Account'),
    path("blog/", CampaignDiaryView.as_view(), name="Campaign Diary"),
    # path('blog/', campaign_diary_view, name='Campaign Diary'),
    path("blog/post/<int:pk>/", IndividualPostView.as_view(), name='Individual Post'),
    # path('blog/post/<int:pk>', individual_post_view, name='Individual Post')
    path("blog/new/", UploadReportView.as_view(), name="Upload Session Report")
]
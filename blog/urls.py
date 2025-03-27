from django.urls import path
from .views import home_page_view, campaign_diary_view, individual_post_view

urlpatterns = [
    path('', home_page_view, name='Home Page'),
    path('blog/', campaign_diary_view, name='Campaign Diary'),
    path('blog/post/<int:pk>', individual_post_view, name='Individual Post')
]
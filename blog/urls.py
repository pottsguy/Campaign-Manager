from django.urls import path
from .views import home_page_view, campaign_diary_view

urlpatterns = [
    path('', home_page_view, name='Home Page'),
    path('blog/', campaign_diary_view, name='Campaign Diary')
]
from django.urls import path
from .views import UserStatsView, SiteDashboardView

urlpatterns = [
    path('user-stats/', UserStatsView.as_view(), name='user-stats'),
    path('site-dashboard/', SiteDashboardView.as_view(), name='site-dashboard'),
]

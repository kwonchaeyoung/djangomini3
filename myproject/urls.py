"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from analytics.views import UserStatsView, SiteDashboardView
from foods.views import FoodListView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='main_page.html'), name='main_page'),  # 루트 경로 추가
    path("admin/", admin.site.urls),
    path('main/', TemplateView.as_view(template_name='main_page.html'), name='main_page'),
    path('main/', FoodListView.as_view(), name='main_page'),
    path('accounts/', include('accounts.urls')),
    path('foods/', include('foods.urls')),
    path('user-stats/', UserStatsView.as_view(), name='user_stats'),
    path('analytics/', include('analytics.urls')),
    path('analytics/site-dashboard/', SiteDashboardView.as_view(), name='site_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
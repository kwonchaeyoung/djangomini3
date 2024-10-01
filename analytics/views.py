from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from foods.models import Food
from django.db.models import Count

class UserStatsView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/user_stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # 개별 사용자의 게시글 수
        context['post_count'] = Food.objects.filter(user=user).count()
        # 개별 사용자의 리뷰 수 (리뷰 모델이 활성화되면 주석을 해제)
        # context['review_count'] = Review.objects.filter(user=user).count()
        # 개별 사용자가 게시한 게시물의 업종별 수
        context['cuisine_counts'] = Food.objects.filter(user=user).values('cuisine').annotate(count=Count('id'))
        return context

class SiteDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/site_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 사이트 전체의 총 게시글 수
        context['total_posts'] = Food.objects.count()
        # 사이트 전체의 업종별 게시글 수
        context['posts_by_cuisine'] = Food.objects.values('cuisine').annotate(count=Count('id'))
        # 사이트 전체의 위치별 게시글 수
        context['posts_by_region'] = Food.objects.values('location').annotate(count=Count('id'))
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from foods.models import Food, Comment
from django.db.models import Count, DateField
from django.db.models.functions import TruncDate
import json


class UserStatsView(LoginRequiredMixin, TemplateView):
    template_name = 'user_stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # 개별 사용자의 게시글과 댓글
        context['posts'] = Food.objects.filter(user=user)
        context['comments'] = Comment.objects.filter(user=user)
        # 개별 사용자의 게시글 수
        context['post_count'] = Food.objects.filter(user=user).count()
        # 개별 사용자가 게시한 게시물의 업종별 수
        context['cuisine_counts'] = Food.objects.filter(user=user).values('cuisine').annotate(count=Count('id'))
        return context


class SiteDashboardView(TemplateView):
    template_name = 'site_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 게시글 작성일별 게시글 수를 리스트로 변환
        posts_by_day = Food.objects.annotate(day=TruncDate('created_at', output_field=DateField())) \
            .values('day') \
            .annotate(count=Count('id')) \
            .order_by('day')

        # 업종별 게시글 수를 리스트로 변환
        posts_by_cuisine = Food.objects.values('cuisine') \
            .annotate(count=Count('id')) \
            .order_by('cuisine')

        # 위도와 경도 데이터를 가지고 있는 게시글
        posts_with_location = Food.objects.exclude(location_lat__isnull=True, location_lng__isnull=True)

        # 데이터를 JSON 형태로 변환
        context['posts_by_day'] = json.dumps(list(posts_by_day), default=str)
        context['posts_by_cuisine'] = json.dumps(list(posts_by_cuisine), default=str)
        context['posts_with_location'] = posts_with_location
        return context
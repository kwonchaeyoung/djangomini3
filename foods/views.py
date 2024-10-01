from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Food

class FoodListView(ListView):
    model = Food
    template_name = 'main_page.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        region_filter = self.request.GET.get('region', '')
        category_filter = self.request.GET.get('category', '')
        rating_filter = self.request.GET.get('rating', '')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(user__username__icontains=search_query)
        if region_filter:
            queryset = queryset.filter(location__icontains=region_filter)
        if category_filter:
            queryset = queryset.filter(cuisine=category_filter)
        if rating_filter:
            queryset = queryset.filter(rating__gte=rating_filter)

        return queryset

class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name = 'food_detail.html'

class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['title', 'content', 'location', 'call', 'photo', 'rating', 'cuisine', 'parking_available', 'reservation_available']
    template_name = 'food_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # 작성자를 현재 로그인한 사용자로 설정
        return super().form_valid(form)

    def get_success_url(self):
        # 작성된 게시글의 상세 페이지로 이동
        return reverse('foods:food_detail', kwargs={'pk': self.object.pk})

class FoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Food
    fields = ['title', 'content', 'location', 'call', 'photo', 'rating', 'cuisine', 'parking_available', 'reservation_available']
    template_name = 'food_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        food = self.get_object()
        return food.user == self.request.user  # 현재 사용자가 해당 게시글의 작성자인지 확인


class FoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('foods:food_list')

    # 권한 검사 함수
    def test_func(self):
        food = self.get_object()
        return food.user == self.request.user  # 현재 로그인한 사용자가 작성자인지 확인

    def handle_no_permission(self):
        # 권한이 없으면 403 에러 발생
        return self.response_class(
            request=self.request,
            template='403.html',
            status=403
        )

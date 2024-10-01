from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Food

class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name = 'food_list.html'

class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name = 'food_detail.html'

class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['title', 'content', 'location', 'call', 'photo', 'rating', 'cuisine', 'parking_available', 'reservation_available']
    template_name = 'food_create.html'
    success_url = reverse_lazy('main_page')  # 메인 페이지로 리디렉션

    def form_valid(self, form):
        form.instance.user = self.request.user  # 작성자를 현재 로그인한 사용자로 설정
        return super().form_valid(form)

class FoodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Food
    fields = ['title', 'content', 'location', 'call', 'photo', 'rating', 'cuisine', 'parking_available', 'reservation_available']
    template_name = 'food_update.html'
    success_url = reverse_lazy('foods:food_list')
    permission_required = 'foods.change_food'

    def has_permission(self):
        food = self.get_object()
        return super().has_permission() and food.user == self.request.user

class FoodDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('foods:food_list')
    permission_required = 'foods.delete_food'

    def has_permission(self):
        food = self.get_object()
        return super().has_permission() and food.user == self.request.user

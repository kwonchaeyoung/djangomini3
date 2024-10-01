from django.urls import path
from .views import FoodListView, FoodDetailView, FoodCreateView, FoodUpdateView, FoodDeleteView

app_name = 'foods'

urlpatterns = [
    path('', FoodListView.as_view(), name='food_list'),  # 게시글 목록
    path('<int:pk>/', FoodDetailView.as_view(), name='food_detail'),  # 게시글 상세 보기
    path('create/', FoodCreateView.as_view(), name='food_create'),  # 게시글 작성
    path('<int:pk>/update/', FoodUpdateView.as_view(), name='food_update'),  # 게시글 수정
    path('<int:pk>/delete/', FoodDeleteView.as_view(), name='food_delete'),  # 게시글 삭제
]

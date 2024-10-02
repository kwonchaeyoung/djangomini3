from django.db import models
from django.conf import settings
import datetime
from django.utils.timezone import now # Django의 now 함수를 사용
from django.contrib.auth.models import User
from django.urls import reverse

class Food(models.Model):
    CUISINE_CHOICES = [
        ('KR', '한식'), ('WE', '양식'), ('JP', '일식'), ('CN', '중식')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    location = models.CharField(max_length=255)
    call = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='foods_photos/')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    cuisine = models.CharField(max_length=2, choices=CUISINE_CHOICES)
    parking_available = models.BooleanField(default=False)
    reservation_available = models.BooleanField(default=False)
    # created_at = models.DateTimeField(default=now) -> 두 옵션 동시가 안되서 마이그레이션 진행 후 아래 행 추가해서 다시 진행
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add로 변경
    location_lat = models.FloatField(null=True, blank=True)  # 위도
    location_lng = models.FloatField(null=True, blank=True)  # 경도

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('foods:food_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Food, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

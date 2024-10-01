from django.db import models
from django.conf import settings

class Food(models.Model):
    CUISINE_CHOICES = [
        ('KR', '한식'), ('JP', '일식'), ('CN', '중식'), ('WE', '양식')
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

    def __str__(self):
        return self.title

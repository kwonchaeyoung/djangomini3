from django.contrib import admin
from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'location', 'rating', 'cuisine', 'parking_available', 'reservation_available']
    search_fields = ['title', 'location', 'user__username']

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # UserCreationForm 또는 UserChangeForm을 사용해서
    # email 필드를 추가하거나 기본 필드를 변경할 수 있습니다.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

# 기본 User 모델의 Admin을 커스터마이징한 Admin으로 등록
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

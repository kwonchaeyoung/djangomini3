from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # 필드 라벨 제거 및 placeholder 설정
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs.update({
            'placeholder': '아이디',
            'class': 'form-control',
        })

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update({
            'placeholder': '이메일',
            'class': 'form-control',
        })

        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].widget.attrs.update({
            'placeholder': '비밀번호',
            'class': 'form-control',
        })

        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs.update({
            'placeholder': '비밀번호 확인',
            'class': 'form-control',
        })


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
        labels = {
            'username': '아이디',
            'password': '비밀번호',
        }

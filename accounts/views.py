from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, FormView

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_page')

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('login')

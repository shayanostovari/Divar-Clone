from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from user.forms import SignupForm, LoginForm


class SignupFormView(FormView):
    form_class = SignupForm
    template_name = 'user/signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)

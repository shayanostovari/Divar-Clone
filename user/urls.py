#urls
from django.urls import path

from user.views import SignupFormView, LoginFormView

urlpatterns = [
    path('signup/', SignupFormView.as_view(), name='signup-form'),
    path('login/', LoginFormView.as_view(), name='login-form'),
]

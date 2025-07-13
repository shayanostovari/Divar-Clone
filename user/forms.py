#forms
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField()
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        if User.objects.filter(phone_number=self.cleaned_data['phone_number']).exists():
            raise forms.ValidationError(_('phone_number already exists'))

        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(_('email already exists'))

        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'], email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'], password=self.cleaned_data['password']
        )
        return user


class LoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data['phone_number']
        password = cleaned_data['password']

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)

            if user is None:
                raise forms.ValidationError('invalid fields')

            cleaned_data['user'] = user
        return cleaned_data

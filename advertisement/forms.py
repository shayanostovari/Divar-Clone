#forms
import random

from django import forms
from django.contrib.auth import get_user_model

from advertisement.models import Advertisement, Category, AdvertisementImage


class AdvertisementCreateForm(forms.ModelForm):
    image = forms.ImageField(label='advertisement image')
    
    class Meta:
        model = Advertisement
        fields = ['title', 'city', 'description', 'price', 'category']

    def save(self, commit=True):
        advertisement = super().save(commit=commit)
        image = self.cleaned_data.get('image')
        if image:
            advertisement_image = AdvertisementImage(advertisement=advertisement, image=image)
            advertisement_image.save()
        return advertisement


class AdvertisementUpdateForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['title', 'city', 'description', 'price', 'category']

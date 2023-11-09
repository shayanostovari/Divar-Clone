from django.contrib import admin
from django.contrib.admin import register

from advertisement.models import Advertisement, Category, City, AdvertisementImage


class AdvertisementImageInline(admin.TabularInline):
    model = AdvertisementImage


@register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'upc', 'user', 'city',
        'description', 'category', 'status',
    ]
    inlines = [AdvertisementImageInline]


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['title']

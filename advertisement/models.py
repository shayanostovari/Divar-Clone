#models
import random

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from lib.base_model import BaseModel

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=48, verbose_name=_('title'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class City(BaseModel):
    title = models.CharField(max_length=64, verbose_name=_('title'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.title


class Advertisement(BaseModel):
    ACCEPTED = 1
    DENIED = 2
    WAITING = 3

    STATUS = (
        (ACCEPTED, _('accepted')),
        (DENIED, _('denied')),
        (WAITING, _('waiting')),
    )

    title = models.CharField(max_length=64, verbose_name=_('title'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='advertisements', verbose_name=_('user'))
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, related_name='advertisements', verbose_name=_('city'), null=True
    )
    description = models.TextField(null=True, verbose_name=_('description'))
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='advertisements', verbose_name=_('category')
    )
    upc = models.BigIntegerField(unique=True, verbose_name=_('upc'), default=random.randint(100, 1000))
    status = models.SmallIntegerField(choices=STATUS, default=WAITING)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _('Advertisement')
        verbose_name_plural = _('Advertisements')

    # def __str__(self):
    #   return self.title, self.upc


class AdvertisementImage(BaseModel):
    image = models.ImageField(upload_to='advertisements/')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='images', null=True)

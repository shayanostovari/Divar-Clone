from advertisement.models import Advertisement
from django import template

register = template.Library()


@register.simple_tag
def get_advertisement():
    return Advertisement.objects.all()

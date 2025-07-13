#urls
from django.urls import path

from advertisement.views import AdvertisementCreateView, AdvertisementDetailView, AdvertisementListView, \
    AdvertisementUpdateView

urlpatterns = [
    path('list/', AdvertisementListView.as_view(), name='adv-list'),
    path('detail/<str:upc>', AdvertisementDetailView.as_view(), name='adv-detail'),
    path('update/<str:upc>/', AdvertisementUpdateView.as_view(), name='adv-update'),
    path('create/', AdvertisementCreateView.as_view(), name='adv-create'),
]

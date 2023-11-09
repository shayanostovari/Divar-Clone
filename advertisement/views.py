import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from django.views.generic import CreateView, FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from advertisement.forms import AdvertisementCreateForm, AdvertisementUpdateForm
from advertisement.models import Advertisement, City


@method_decorator(require_GET, name='dispatch')
class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/adv_list.html'
    context_object_name = 'advertisement'

    def get_queryset(self):
        queryset = super().get_queryset()
        city = self.request.GET.get('city')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        queryset = queryset.filter(status=1)

        if city != 'all':
            queryset = queryset.filter(city__title=city)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['cities'] = City.objects.all()
        return context


@method_decorator(require_GET, name='dispatch')
class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement/adv_detail.html'
    context_object_name = 'advertisement'

    def get_object(self, queryset=None):
        upc = self.kwargs.get('upc')
        return self.model.objects.get(upc=upc)


@method_decorator(login_required, name='dispatch')
class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    form_class = AdvertisementUpdateForm
    template_name = 'advertisement/adv_update.html'
    context_object_name = 'advertisement'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return render(request, 'advertisement/404.html')

        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class AdvertisementCreateView(CreateView):
    model = Advertisement
    template_name = 'advertisement/adv_create.html'
    form_class = AdvertisementCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

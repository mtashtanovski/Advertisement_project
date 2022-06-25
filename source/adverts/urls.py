from django.urls import path

from adverts.views import (
    AdvertsListView,
    AdvertsCreateView,
)

app_name = 'adverts'

urlpatterns = [
    path('', AdvertsListView.as_view(), name="index"),
    path('adverts/create/', AdvertsCreateView.as_view(), name="adverts_create"),
]

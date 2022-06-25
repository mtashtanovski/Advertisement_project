from django.urls import path

from adverts.views import (
    AdvertsListView,
)

app_name = 'adverts'

urlpatterns = [
    path('', AdvertsListView.as_view(), name="index"),
]

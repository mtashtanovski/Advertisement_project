from django.urls import path

from adverts.views import (
    AdvertsListView,
    AdvertsCreateView,
    ModeratedAdvertsDetailView,
)

app_name = 'adverts'

urlpatterns = [
    path('', AdvertsListView.as_view(), name="index"),
    path('adverts/create/', AdvertsCreateView.as_view(), name="adverts_create"),
    path('adverts/moderated/<int:pk>/', ModeratedAdvertsDetailView.as_view(), name="moderated_adverts")
]

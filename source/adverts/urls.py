from django.urls import path

from adverts.views import (
    AdvertsListView,
    AdvertsCreateView,
    AdvertsDetailView,
    AdvertsEditView,
    AdvertsDeleteView,
)

app_name = 'adverts'

urlpatterns = [
    path('', AdvertsListView.as_view(), name="index"),
    path('adverts/create/', AdvertsCreateView.as_view(), name="adverts_create"),
    path('adverts/<int:pk>/', AdvertsEditView.as_view(), name="adverts_edit"),
    path('adverts/<int:pk>/', AdvertsDetailView.as_view(), name="adverts_detail"),
    path('adverts/<int:pk>/', AdvertsDeleteView.as_view(), name="adverts_delete"),

]

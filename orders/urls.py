from django.urls import path
from .views import buy_crop

urlpatterns = [
    path('buy/<int:crop_id>/', buy_crop, name='buy_crop'),
]

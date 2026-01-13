from django.urls import path
from .views import buy_crop, buyer_orders

urlpatterns = [
    path('buy/<int:crop_id>/', buy_crop, name='buy_crop'),
      path('my-orders/', buyer_orders, name='buyer_orders'),
]

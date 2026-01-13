from django.urls import path
from .views import buy_crop, buyer_orders, add_to_cart, view_cart, checkout

urlpatterns = [
    path('add-to-cart/<int:crop_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('buy/<int:crop_id>/', buy_crop, name='buy_crop'),
    path('my-orders/', buyer_orders, name='buyer_orders'),
]

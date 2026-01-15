from django.urls import path
from .views import farmer_dashboard, add_crop, delete_crop

urlpatterns = [
    path('farmer/', farmer_dashboard, name='farmer_dashboard'),
    path('farmer/add/', add_crop, name='add_crop'),
    path('farmer/delete/<int:crop_id>/', delete_crop, name='delete_crop'),

]

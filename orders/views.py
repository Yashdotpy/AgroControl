from django.shortcuts import redirect
from .models import Order
from marketplace.models import Crop
from django.contrib.auth.decorators import login_required

@login_required
def buy_crop(request, crop_id):
    crop = Crop.objects.get(id=crop_id)

    Order.objects.create(
        buyer=request.user,
        crop=crop,
        quantity=1
    )

    return redirect('home')

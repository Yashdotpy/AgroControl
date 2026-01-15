from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Crop
from accounts.models import Profile

def home(request):
    crops = Crop.objects.all()

    search_query = request.GET.get('search')
    max_price = request.GET.get('max_price')

    if search_query:
        crops = crops.filter(name__icontains=search_query)

    if max_price:
        crops = crops.filter(price__lte=max_price)

    return render(request, 'home.html', {'crops': crops})
@login_required
def farmer_dashboard(request):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'farmer':
        return redirect('home')

    crops = Crop.objects.filter(farmer=request.user)
    return render(request, 'farmer_dashboard.html', {'crops': crops})


@login_required
def add_crop(request):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'farmer':
        return redirect('home')

    if request.method == 'POST':
        Crop.objects.create(
            farmer=request.user,
            name=request.POST['name'],
            price=request.POST['price'],
            unit=request.POST['unit'],
            quantity=request.POST['quantity'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('farmer_dashboard')

    return render(request, 'add_crop.html')

@login_required
def delete_crop(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)

    # ensure only the farmer who owns the crop can delete it
    if crop.farmer != request.user:
        return redirect('home')

    crop.delete()
    return redirect('farmer_dashboard')

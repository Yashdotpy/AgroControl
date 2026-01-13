from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Crop
from accounts.models import Profile

def home(request):
    crops = Crop.objects.all()
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
            quantity=request.POST['quantity'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('farmer_dashboard')

    return render(request, 'add_crop.html')

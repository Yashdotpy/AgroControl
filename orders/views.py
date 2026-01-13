from django.shortcuts import redirect, render, get_object_or_404
from .models import Order, Cart, CartItem
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

@login_required
def buyer_orders(request):
    orders = Order.objects.filter(buyer=request.user)
    return render(request, 'buyer_orders.html', {'orders': orders})

@login_required
def add_to_cart(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        crop=crop
    )

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(item.total_price() for item in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)

    for item in items:
        Order.objects.create(
            buyer=request.user,
            crop=item.crop,
            quantity=item.quantity
        )

    items.delete()  # clear cart after checkout
    return redirect('buyer_orders')

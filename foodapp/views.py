from django.shortcuts import render,redirect, get_object_or_404
from foodapp.models import Restaurant, FoodItem,Cart
from .import views

# Create your views here.
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    return render(request,'restaurant_Listing.html', {
    'restaurants': restaurants
})




def menu_page(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    foods = FoodItem.objects.filter(restaurant=restaurant)

    return render(request, 'restaurant_menu.html', {
        'restaurant': restaurant,
        'foods': foods
    })


def add_to_cart(request, food_id):

    food = get_object_or_404(FoodItem, id=food_id)

    cart_item = Cart.objects.filter(food_item=food).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(
            food_item=food,
            quantity=1
        )

    return redirect('cart')




from .models import Cart

def cart_page(request):
    cart_items = Cart.objects.all()

    total = 0

    for item in cart_items:
        total += item.food_item.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

from .models import Order, Cart
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .models import Cart, Order

def checkout(request):

    if request.method == "POST":

        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        cart_items = Cart.objects.all()

        total = 0
        for item in cart_items:
            total += item.food_item.price * item.quantity

        Order.objects.create(
            customer_name=customer_name,
            email=email,
            phone=phone,
            address=address,
            payment_method=payment_method,
            total_amount=total
        )

        # Cart Empty
        cart_items.delete()

        return redirect('success')

    return render(request, 'checkout.html')


def ordersuccess(request):
    return render(request, 'order_success.html')


from django.shortcuts import get_object_or_404, redirect
from .models import Cart

def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()

    return redirect('cart')

from django.shortcuts import get_object_or_404, redirect

def increase_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def decrease_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def order_history(request):
    orders = Order.objects.all().order_by('-created_at')

    return render(request, 'order_history.html', {
        'orders': orders
    })
       
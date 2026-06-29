from django.shortcuts import render,redirect, get_object_or_404
from foodapp.models import Restaurant, FoodItem,Cart,Order,OrderItem,Review
from .import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestaurantSerializer,FoodItemSerializer,CartSerializer,OrderSerializer,OrderItemSerializer,ReviewSerializer
from rest_framework import generics

# Create your views here.
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    print("Restaurant Count =", restaurants.count())

    return render(request,'restaurant_Listing.html', {
        'restaurants': restaurants
    })



def menu_page(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    foods = FoodItem.objects.filter(
        restaurant=restaurant
    )

    reviews = Review.objects.all()

    for food in foods:
        avg_rating = Review.objects.filter(
            food_item=food
        ).aggregate(
            Avg('rating')
        )['rating__avg']

        food.avg_rating = round(avg_rating, 1) if avg_rating else 0

        food.review_count = Review.objects.filter(
            food_item=food
        ).count()

    return render(
        request,
        'restaurant_menu.html',
        {
            'restaurant': restaurant,
            'foods': foods,
            'reviews': reviews
        }
    )
@login_required(login_url='login')
def add_to_cart(request, food_id):

    food = get_object_or_404(FoodItem, id=food_id)

    cart_item = Cart.objects.filter(
    user=request.user,
    food_item=food
).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
       Cart.objects.create(
    user=request.user,
    food_item=food,
    quantity=1
)

    return redirect('cart')


@login_required(login_url='login')
def cart_page(request):
    cart_items = Cart.objects.filter(
    user=request.user
)

    total = 0

    for item in cart_items:
        total += item.food_item.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required(login_url='login')
def checkout(request):

    if request.method == "POST":

        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        cart_items = Cart.objects.filter(user=request.user)

        print("Cart Count =", cart_items.count())

        total = 0
        for item in cart_items:
            total += item.food_item.price * item.quantity

        order = Order.objects.create(
            user=request.user,
            customer_name=customer_name,
            email=email,
            phone=phone,
            address=address,
            payment_method=payment_method,
            total_amount=total
        )

        for item in cart_items:
            print("Food:", item.food_item.name)

            OrderItem.objects.create(
                order=order,
                food_item=item.food_item,
                quantity=item.quantity,
                price=item.food_item.price
            )

        print("Order Items Created")

        # Empty Cart
        cart_items.delete()

        return redirect('success')

    return render(request, 'checkout.html')
def ordersuccess(request):
    return render(request, 'order_success.html')


@login_required(login_url='login')
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart_item.delete()

    return redirect('cart')

from django.shortcuts import get_object_or_404, redirect
@login_required(login_url='login')
def increase_quantity(request, cart_id):
    cart_item = get_object_or_404(
    Cart,
    id=cart_id,
    user=request.user
)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def decrease_quantity(request, cart_id):
    cart_item = get_object_or_404(
    Cart,
    id=cart_id,
    user=request.user
)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

@login_required(login_url='login')
def order_history(request):
    orders = Order.objects.filter(
    user=request.user
).order_by('-created_at')

    return render(request, 'order_history.html', {
        'orders': orders
    })


def search_food(request):

    search = request.GET.get('search')

    food_items = FoodItem.objects.all()

    if search:
        food_items = FoodItem.objects.filter(
            name__icontains=search
        )

    return render(request, 'search_result.html', {
        'food_items': food_items,
        'search': search
    })    



from django.contrib.auth.models import User


def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(
                request,
                'register.html',
                {'error': 'Passwords do not match'}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import FoodItem, Review

@login_required(login_url='login')
def add_review(request, food_id):

    food = get_object_or_404(
        FoodItem,
        id=food_id
    )

    if request.method == "POST":

        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        review = Review.objects.filter(
            user=request.user,
            food_item=food
        ).first()

        if review:
            review.rating = rating
            review.comment = comment
            review.save()
        else:
            Review.objects.create(
                user=request.user,
                food_item=food,
                rating=rating,
                comment=comment
            )

    return redirect(
        'menu',
        restaurant_id=food.restaurant.id
    )

from rest_framework import viewsets
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class FoodItemViewset(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class =  FoodItemSerializer  

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  

class OrderItemViewset(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class  = OrderItemSerializer   

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer   
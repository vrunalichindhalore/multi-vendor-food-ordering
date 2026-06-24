from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('menu/<int:restaurant_id>/', views.menu_page, name='menu'),
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('ordersuccess/', views.ordersuccess, name='success'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase-quantity/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('orders/', views.order_history, name='order_history'),
    

    
]
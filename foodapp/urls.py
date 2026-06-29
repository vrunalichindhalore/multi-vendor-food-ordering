from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet,FoodItemViewset,CartViewset,OrderViewset,OrderItemViewset,ReviewViewset

router = DefaultRouter()
router.register('restaurants',RestaurantViewSet,basename='restaurant'),
router.register('fooditems',FoodItemViewset, basename='fooditem'),
router.register('carts',CartViewset, basename='cart'),
router.register('orders',OrderViewset,basename='order'),
router.register('orderitems',OrderItemViewset,basename='orderitem')
router.register('reviews',ReviewViewset,basename='review')



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
    path('search/', views.search_food, name='search_food'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('review/<int:food_id>/',views.add_review,name='add_review'),
    path('api/',include(router.urls)),
    
    
]
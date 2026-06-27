from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

#def register(request):
    return render(request,'register.html')

def restaurant_register(request):
    return render(request,'restaurant_register.html')

def menu(request):
    return render(request,'restaurant_menu.html')

def RestaurantList(request):
    return render(request,'Restaurant_Listing.html')

def cart(request):
    return render(request,'cart.html')

def check(request):
    return render(request,'checkout.html')

def ordersuccess(request):
    return render(request,'order_success.html')




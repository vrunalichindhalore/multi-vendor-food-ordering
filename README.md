# Multi-Vendor Food Ordering System

## Project Overview

A full-stack Food Ordering System built using Django and Django REST Framework. Users can browse restaurants, view food menus, add items to cart, place orders, make online payments using Razorpay, and submit reviews and ratings.

## Features

### User Features

* User Registration and Login
* Restaurant Listing
* Food Menu Display
* Search Food Items
* Add to Cart
* Update Cart Quantity
* Remove Items from Cart
* Checkout System
* Order History
* Reviews and Ratings

### Payment Integration

* Razorpay Payment Gateway Integration
* Secure Online Payments
* Payment Tracking

### REST API Features

* Restaurant API
* Food Item API
* Cart API
* Order API
* Order Item API
* Review API

## Technologies Used

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite

### Frontend

* HTML
* CSS
* JavaScript

### Payment Gateway

* Razorpay

### Version Control

* Git
* GitHub

## Project Structure

foodOnline/

├── foodapp/

├── foodOnline_main/

├── templates/

├── static/

├── media/

├── manage.py

├── requirements.txt

└── build.sh

## Installation

1. Clone the repository

git clone <repository-url>

2. Create virtual environment

python -m venv env

3. Activate virtual environment

Windows:

env\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Run migrations

python manage.py migrate

6. Start server

python manage.py runserver

## API Endpoints

* /api/restaurants/
* /api/fooditems/
* /api/carts/
* /api/orders/
* /api/orderitems/
* /api/reviews/

## Future Enhancements

* Vendor Dashboard
* Order Tracking
* Email Notifications
* Advanced Search and Filters
* Deployment with PostgreSQL

## Author

Vrunali Chindhalore

B.Tech Computer Science Engineering

Python Developer | Django Developer




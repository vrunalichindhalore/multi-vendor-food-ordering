from rest_framework import serializers
from . models import Restaurant,FoodItem,Cart,Order,OrderItem,Review


class FoodItemSerializer(serializers.ModelSerializer):

    restaurant_name = serializers.CharField(source='restaurant.name',read_only=True)

    class Meta:
        model = FoodItem
        fields = '__all__'      

class ReviewSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username',read_only=True)
    food_name = serializers.CharField(source='food_item.name',read_only=True)

    class Meta:
        model = Review
        fields = '__all__'   

class OrderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    food_name = serializers.CharField(source='food_item.name',read_only=True)

    restaurant_name = serializers.CharField(source='food_item.restaurant.name',read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'     

class CartSerializer(serializers.ModelSerializer):

    food_name = serializers.CharField(source='food_item.name',read_only=True)

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.food_item.price * obj.quantity           

class RestaurantSerializer(serializers.ModelSerializer):

    foods = FoodItemSerializer(many=True,read_only=True,source='fooditem_set')

    class Meta:
        model = Restaurant
        fields = '__all__'
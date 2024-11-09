from rest_framework import serializers
from .models import User, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, attrs):
        order_instance = Order(**attrs)
        order_instance.clean()
        return attrs
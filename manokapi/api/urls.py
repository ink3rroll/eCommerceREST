from django.urls import path
from .views import get_users, create_user, user_detail
from .views import get_orders, create_order, order_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),
    path('orders/', get_orders, name='get_orders'),
    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:pk>', order_detail, name='order_detail'),
]
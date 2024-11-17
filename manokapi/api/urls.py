from django.urls import path
from .views import get_users, create_user, user_detail
from .views import get_orders, create_order, order_detail, checkout_order
from .views import get_cartitems, create_cartitem, cartitem_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<uuid:pk>', user_detail, name='user_detail'),
    path('orders/', get_orders, name='get_orders'),
    path('orders/create/', create_order, name='create_order'),
    path('orders/<uuid:pk>', order_detail, name='order_detail'),
    path('orders/<uuid:pk>/checkout/', checkout_order, name='checkout_order'),
    path('cartitems/', get_cartitems, name='get_cartitems'),
    path('cartitems/create/', create_cartitem, name='create_cartitem'),
    path('cartitems/<uuid:pk>', cartitem_detail, name='cartitem_detail'),
]
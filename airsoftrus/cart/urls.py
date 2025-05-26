from django.urls import path
from .views import cart_add, cart_remove, cart_detail, order_create

app_name = 'cart'  # Добавьте эту строку

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('create/', order_create, name='order_create'),
]
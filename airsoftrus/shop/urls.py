from django.urls import path
from .views import (
    ProductListView, 
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = 'shop'  # Добавьте эту строку

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Переместить выше
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:id>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('', ProductListView.as_view(), name='product_list'),
]
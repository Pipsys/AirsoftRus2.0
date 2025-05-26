from django.urls import path
from .views import ProfileView, profile_edit

app_name = 'accounts'  # Добавьте эту строку

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]
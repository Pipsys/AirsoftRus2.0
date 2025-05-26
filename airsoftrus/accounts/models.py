from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        # username обязателен для AbstractUser
        if not extra_fields.get('username'):
            extra_fields['username'] = email
        return super().create_superuser(email=email, password=password, **extra_fields)

class CustomUser(AbstractUser):  # Было: User
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)  # вернуть username, но сделать необязательным
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)  # Было: addres

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # используем кастомный менеджер

    def __str__(self):
        return self.email
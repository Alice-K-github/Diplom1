from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='Email', blank=False)
    avatar = models.ImageField(verbose_name="Аватар", upload_to='pictures/', blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15, blank=True, help_text='Введите номер телефона (необязательно)')
    country = models.CharField(verbose_name='Страна', max_length=30, blank=True, help_text="Введите страну (необязательно)")
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

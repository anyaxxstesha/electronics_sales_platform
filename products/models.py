from django.db import models

from network.models import NetworkElement

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название', help_text='Укажите название')
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Укажите email')
    model = models.CharField(max_length=100, verbose_name='Модель продукта', help_text='Укажите модель продукта',
                             **NULLABLE)
    seller = models.ForeignKey(NetworkElement, on_delete=models.SET_NULL, related_name='product',
                               verbose_name='Продавец', help_text='Укажите продавца', **NULLABLE)
    released_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода продукта на рынок',
                                       help_text='Укажите дату выхода продукта на рынок')

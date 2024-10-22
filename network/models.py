from django.db import models

NULLABLE = {'blank': True, 'null': True}


class NetworkElement(models.Model):
    TYPE_NAME_CHOICES = (
        ('FT', 'Завод'),
        ('RT', 'Розничная сеть'),
        ('IE', 'Индивидуальный предприниматель'),
    )
    type_name = models.CharField(max_length=2, choices=TYPE_NAME_CHOICES, verbose_name='Тип звена',
                                 help_text='Выберите тип звена')
    title = models.CharField(max_length=128, verbose_name='Название', help_text='Укажите название')

    email = models.EmailField(unique=True, verbose_name='Email', help_text='Укажите email')
    country = models.CharField(max_length=50, verbose_name='Страна', help_text='Укажите страну', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Укажите город', **NULLABLE)
    street = models.CharField(max_length=50, verbose_name='Улица', help_text='Укажите улицу', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text='Укажите номер дома',
                                    **NULLABLE)

    supplier = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, verbose_name='Поставщик',
                                 help_text='Укажите поставщика', **NULLABLE)
    debt = models.DecimalField(decimal_places=2, max_digits=20, default=0,
                               verbose_name='Задолженность перед поставщиком',
                               help_text='Укажите задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания карточки звена',
                                      help_text='Дата создания добавляется автоматически')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'

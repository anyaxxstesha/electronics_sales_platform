# Generated by Django 5.1.2 on 2024-10-22 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('FT', 'Завод'), ('RT', 'Розничная сеть'), ('IE', 'Индивидуальный предприниматель')], help_text='Выберите тип звена', max_length=2, verbose_name='Тип звена')),
                ('title', models.CharField(help_text='Укажите название', max_length=128, verbose_name='Название')),
                ('email', models.EmailField(help_text='Укажите email', max_length=254, unique=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, help_text='Укажите страну', max_length=50, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, help_text='Укажите город', max_length=50, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, help_text='Укажите улицу', max_length=50, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, help_text='Укажите номер дома', max_length=10, null=True, verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0, help_text='Укажите задолженность перед поставщиком', max_digits=20, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания добавляется автоматически', verbose_name='Дата создания карточки звена')),
                ('supplier', models.ForeignKey(blank=True, default=None, help_text='Укажите поставщика', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='network.networkelement', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Элемент сети',
                'verbose_name_plural': 'Элементы сети',
            },
        ),
    ]
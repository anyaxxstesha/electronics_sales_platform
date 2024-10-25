from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'seller', 'released_at')
    list_filter = ('title', 'seller')
    search_fields = ('title',)

from django.contrib import admin

from network.models import NetworkElement


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'email', 'country', 'city', 'debt', 'created_at')
    list_filter = ('title', 'country',)
    search_fields = ('country',)

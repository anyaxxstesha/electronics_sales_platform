from django.contrib import admin, messages
from django.utils.translation import ngettext

from network.models import NetworkElement


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type_name', 'title', 'level', 'email', 'country', 'city', 'debt', 'supplier', 'created_at')
    list_filter = ('city',)
    search_fields = ('city',)

    actions = ['set_debt_to_null']

    @admin.action(description="Clear the debt of selected network elements")
    def set_debt_to_null(self, request, queryset):
        updated = queryset.update(debt=0)
        self.message_user(
            request,
            ngettext(
                'The debt of %d network element was successfully written off.',
                'Debts of %d network elements were successfully written off.',
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

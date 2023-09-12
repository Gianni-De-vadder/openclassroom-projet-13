from django.contrib import admin
from .models import Letting, Address


class AddressAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Address model.
    """
    list_display = ['number', 'street', 'city', 'state', 'zip_code', 'country_iso_code']
    search_fields = ['number', 'street', 'city', 'state', 'zip_code', 'country_iso_code']
    list_filter = ['country_iso_code']


admin.site.register(Address, AddressAdmin)
admin.site.register(Letting)

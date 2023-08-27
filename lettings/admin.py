from django.contrib import admin
from .models import Letting, Address

class AddressAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Address model.
    """
    list_display = ['number', 'street', 'city', 'state', 'zip_code', 'country_iso_code']
    search_fields = ['number', 'street', 'city', 'state', 'zip_code', 'country_iso_code']
    list_filter = ['country_iso_code']

# Change the plural name for Address model in admin interface
Address._meta.verbose_name_plural = "Addresses"

# Register the Address model with the custom admin options
admin.site.register(Address, AddressAdmin)

# Register the Letting model without any custom admin options
admin.site.register(Letting)

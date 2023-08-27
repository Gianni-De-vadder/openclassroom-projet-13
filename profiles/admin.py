from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class for Profile model.
    """
    list_display = ['user', 'favorite_city']
    search_fields = ['user__username', 'favorite_city']
    list_filter = ['favorite_city']

    def user_username(self, obj):
        """
        Display the username of the related user.
        """
        return obj.user.username

    user_username.short_description = 'Username'  # Column header

    # You can add more customizations and methods as needed.

admin.site.register(Profile, ProfileAdmin)

from django.db import models
from django.contrib.auth.models import User
import logging

profiles_logger = logging.getLogger('profiles')

class Profile(models.Model):
    """
    Model representing user profiles.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.
        """
        return self.user.username

    def save(self, *args, **kwargs):
        """
        Override the save method to add a log when a profile is saved.
        """
        profiles_logger.info(f'Profile saved for user: {self.user.username}')
        super().save(*args, **kwargs)

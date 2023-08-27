from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
import logging
models_logger = logging.getLogger('models')

class Address(models.Model):
    """
    Model to represent an address.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def save(self, *args, **kwargs):
       models_logger.info('Address saved: %s', self)
       super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model to represent a letting property.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        models_logger.info('Letting saved: %s', self)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the letting property.
        """
        return self.title

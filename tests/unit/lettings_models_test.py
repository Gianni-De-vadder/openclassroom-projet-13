from django.test import TestCase
from lettings.models import Address, Letting

class AddressModelTest(TestCase):
    def test_str_representation(self):
        address = Address(number=123, street="Main St", city="City", state="ST", zip_code=12345, country_iso_code="US")
        self.assertEqual(str(address), "123 Main St")

class LettingModelTest(TestCase):
    def test_str_representation(self):
        letting = Letting(title="Test Letting")
        self.assertEqual(str(letting), "Test Letting")

from django.test import TestCase, RequestFactory
from django.urls import reverse
from lettings.models import Letting, Address
from lettings.views import index, letting

class LettingsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.address = Address.objects.create(number=123, street="Main St", city="City", state="ST", zip_code=12345, country_iso_code="US")
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_index_view(self):
        request = self.factory.get(reverse("lettings:index"))
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    def test_letting_view(self):
        request = self.factory.get(reverse("lettings:letting", args=[self.letting.id]))
        response = letting(request, self.letting.id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
